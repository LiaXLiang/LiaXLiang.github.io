from __future__ import print_function
import oldp_client
from oldp_client.rest import ApiException
import json
import glob
from bs4 import BeautifulSoup
import os,html,re
from typing import List, Dict, Any
from tqdm import tqdm

import chromadb
from chromadb.config import Settings
from langchain_chroma import Chroma
from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer

#==================================================
# config
#==================================================
API_KEY = '0b84d4cd16c99031f2625727c5a11f444281fc25'

RAW_DIR = "./raw_json_file"  
INPUT_DIR = "./processed_json_file" 

CHROMA_DIR = "./chroma_cases" 
LOOKUP_PATH = os.path.join(CHROMA_DIR, "case_lookup_index.json")

COLLECTION_NAME = "cases_database"
MODEL_NAME = "intfloat/multilingual-e5-large-instruct"
BATCH_ADD = 256     
# #=======================================================================
# # I. Data Collection


# # Configure API key authorization: api_key
# cfg = oldp_client.Configuration()
# cfg.api_key['Authorization'] = API_KEY
# client = oldp_client.ApiClient(cfg)


# # create an instance of the caseAPI class
# cases_api = oldp_client.CasesApi(client)

# def save_page(page, page_size=100):
#     resp = cases_api.cases_list(page=page, page_size=page_size)
#     data = resp.to_dict()
#     with open(f"cases_page_{page}.json", "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2, default=str)


# try:
#     # take the previous 200 pages
#     for p in range(1, 201):
#         save_page(p)
#         print(f"page {p} done!")
# except ApiException as e:
#     print("API error:", e)









#=======================================================================
# II. Preprocess the data

def html_to_clean_text(content_html: str) -> str:
    if not content_html:
        return ""
    # 1) Parse HTML using BeautifulSoup
    soup = BeautifulSoup(content_html or "", "html.parser")

    # 2) Remove irrelevant tags that don't contain meaningful text
    for tag in soup(["script", "style"]):
        tag.decompose()

    # 3) Remove line numbers/layout classes
    for sp in soup.select("span.absatzRechts, span.absatzLinks"):
        sp.decompose()

    # 4) Convert <br> to newlines (implicit in get_text with separator
    # 4) Add bullet points for list items
    for li in soup.find_all("li"):
        li.insert_before("• ")

    # 5)Extract text while preserving paragraph breaks
    text = soup.get_text(separator="\n")

    # 6) Unescape HTML entities (&nbsp; → normal space)
    text = html.unescape(text)


    lines = [ln.strip() for ln in text.splitlines()]
    lines = [ln for ln in lines if ln]
    text = "\n".join(lines)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text


def preprocess_file(in_path: str, out_path: str):
    with open(in_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict) and "results" in data:
        for it in data["results"]:
            it["content"] = html_to_clean_text(it.get("content") or "")
    elif isinstance(data, list):
        for it in data:
            it["content"] = html_to_clean_text(it.get("content") or "")

    with open(out_path, "w", encoding="utf-8") as out:
        json.dump(data, out, ensure_ascii=False, indent=2, default=str)


# def run_batch():
#     files = [f for f in os.listdir(RAW_DIR) if f.endswith(".json")]
#     files.sort(key=lambda x: int(re.findall(r"(\d+)", x)[-1]))
#     for fn in files:
#         in_path = os.path.join(RAW_DIR, fn)
#         out_path = os.path.join(OUT_DIR, fn)
#         preprocess_file(in_path, out_path)
#         print(f"Processed: {fn}")

# if __name__ == "__main__":
#     run_batch()



# =======================================================================
# III. Vector Store Creation

class E5Embeddings(HuggingFaceEmbeddings):
    def __init__(self, **kwargs):
        kwargs.setdefault("model_name", MODEL_NAME)
        kwargs.setdefault("encode_kwargs", {"normalize_embeddings": True})
        super().__init__(**kwargs)
        self._tok = AutoTokenizer.from_pretrained(MODEL_NAME)
        self._max_len = 512

    def _truncate(self, text: str) -> str:
        enc = self._tok(text, add_special_tokens=False, truncation=True, max_length=self._max_len)
        ids = enc["input_ids"]
        if isinstance(ids, list) and ids and isinstance(ids[0], list):
            ids = ids[0]
        return self._tok.decode(ids, skip_special_tokens=True)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        processed = []
        for t in texts:
            t2 = t if t.strip().lower().startswith("passage:") else ("passage: " + t)
            processed.append(self._truncate(t2))
        return super().embed_documents(processed)

    def embed_query(self, text: str) -> List[float]:
        q = text if text.strip().lower().startswith("query:") else ("query: " + text)
        return super().embed_query(self._truncate(q))




client = chromadb.PersistentClient(path=CHROMA_DIR, settings=Settings(allow_reset=False))
embeddings = E5Embeddings()

vectorstore = Chroma(
    client=client,
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
    is_separator_regex=False,
)


def iter_cases_from_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for i, case in enumerate(data.get("results", [])):
        yield i, case

def ingest_folder():
    json_files = sorted(glob.glob(os.path.join(INPUT_DIR, "cases_page_*.json")))
    if not json_files:
        raise FileNotFoundError(f"No files found under {INPUT_DIR}/cases_page_*.json")

    buffer: List[Document] = []

    for file_path in tqdm(json_files, desc="Ingesting pages"):
        page_tag = os.path.splitext(os.path.basename(file_path))[0]  # e.g., cases_page_98

        for result_idx, case in iter_cases_from_file(file_path):
            case_id = str(case.get("id") or f"{page_tag}-{result_idx}")
            content = case.get("content", "") or ""
            if not content.strip():
                continue

           
            chunks = text_splitter.split_text(content)
            total = len(chunks)
            if total == 0:
                continue

            
            base_meta: Dict[str, Any] = {
                "case_id": case_id,
                "page": page_tag,
                "source_path": file_path,
                "result_idx": result_idx,
                "slug": case.get("slug"),
                "file_number": case.get("file_number"),
                "date": case.get("_date"),
                "type": case.get("type"),
                "ecli": case.get("ecli"),
                "court_name": (case.get("court") or {}).get("name"),
                "court_slug": (case.get("court") or {}).get("slug"),
            }

            for idx, ch in enumerate(chunks):
                meta = dict(base_meta)
                meta.update({"chunk_index": idx, "chunk_count": total})
                buffer.append(Document(page_content=ch, metadata=meta))

                if len(buffer) >= BATCH_ADD:
                    vectorstore.add_documents(buffer)
                    buffer = []

    if buffer:
        vectorstore.add_documents(buffer)


if __name__ == "__main__":
    print("CWD      =", os.getcwd())
    print("Looking  =", os.path.join(INPUT_DIR, "cases_page_*.json"))
    ingest_folder()

    hits = vectorstore.similarity_search_with_score("Kostenübernahme für Liposuktion bei Lipödem", k=3)
    for i, (doc, score) in enumerate(hits, 1):
        m = doc.metadata
        print(f"{i}. case_id={m['case_id']} chunk={m['chunk_index']+1}/{m['chunk_count']} "
              f"court={m.get('court_name')} date={m.get('date')} score={score:.4f}")





collections = client.list_collections()
print("Collections available in the Chroma database:")
for collection in collections:
    print(f"- {collection.name}")






