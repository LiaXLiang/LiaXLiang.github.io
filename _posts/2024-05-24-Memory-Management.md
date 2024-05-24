## 1. Where do addresses come from?
Addresses can be generated at different stages of program execution, involving both the compiler and the OS:

- **Compile Time**: The compiler assigns *exact physical addresses* in memory, starting from a predetermined position 𝑘. The OS does not alter these addresses.
- **Load Time**: Although the compiler generates addresses, the OS determines the *actual starting position* in memory at the time the process is loaded. Once the process finishes loading, the process’s memory location remains unchanged.

- **Execution Time**: The compiler produces relocatable addresses, allowing the OS to shift them to any required position in memory during the process’s runtime.


## 2. Memory Management - Direct Physical Mapping
### I. Uniprogramming
Until the early 1980s, there was no memory abstraction: programs directly used physical memory, i.e., memory is managed directly by the user program(s) and not by the OS. Computer manufacturers/OS developers may provide guidelines to users to avoid programs touching kernel memory.  <br> &nbsp; Due to its simplicity and low hardware requirements, direct physical mapping was naturally suited for early Uniprogramming technique. 


#### (1) Uniprogramming is characterized by the following attributes:
- OS gets a fixed part of memory (highest memory in DOS)
- Only one process is executed at a time.
- Process is always loaded starting at address 0.
- Process executes in a contiguous section of memory.
- Compiler can generate physical addresses.
- Maximum address = Memory Size - OS Size
- OS is protected from process by checking addresses used by
process.

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/2.1.Uniprogramming.png?raw=true" alt="Uniprogramming">
</figure>

#### (2) Limitation
It is simple, but does not allow for overlap of I/O and computation.

### II.  Multiprocessing by Swapping Memory
#### (1) Definition
Swapping is a technique that consists in moving memory between *RAM* and *storage device*s. Moving (usually unused) memory from memory to storage is called *swapping out*, while moving memory back from disk into memory when it is needed is called *swapping in*.

#### (2) Naive Approach Intuition  
Copy user memory to/from a storage device, e.g., hard drive.

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/2.2Swapping.png?raw=true" alt="Uniprogramming">
</figure>
e.g. If we want to context switch between processes A and B:

- Move the currently running process (A)’s memory to storage.
  - A’s memory: RAM $\rightarrow$ storage
- Move the newly scheduled process (B)’s memory into RAM 
  - B’s memory: storage $\rightarrow$ RAM

#### (3) Limitations
- Copying to/from storage is very costly 
- Not suitable for multi-core systems



## 3. Memory Management - Dynamic Relocation / 动态重定位
### I. The Address Space Abstraction 
#### (1) To efficiently and safely manipulate memory, three criteria are essential:
 - ① Transparency
   - Multiple processes should coexist in memory 
   - Processes should be unaware of the shared nature of memory and indifferent to the specific physical memory segments assigned to them.
 - ② Safety
   - Processes must be prevented from interfering with or corrupting each other.
   - It is crucial that processes cannot corrupt the OS.
 - ③ Efficiency
   - The performance of both the CPU and memory should not suffersignificantly due to sharing. 

#### (2) To provide these properties, OS designers came up with an abstraction - **address spaces**
- The addresses manipulated by programs are **virtual addresses**.
- An **address space** is an *abstract view* of the memory seen by a *process*. 
- The range of virtual addresses (from 0 to size of the process) that is available to a process is known as the process's (virtual) address space. 
- They are independent from each other and may be mapped to any physical address in memory. e.g., address 1000 of two different address spaces can be mapped to different physical addresses. Manipulating address spaces can be done in various ways, with different hardware supports.


#### (3) Address Space Size
- **Fixed-size** address space: <br> Whenever a process is created or swapped in, a contiguous chunk of memory of the size of the process’ address space is allocated. Note that *eviction/驱逐* or *compaction/压缩* may happen to make this possible.
- **Variable-size** address space: Depending on the memory layout of address spaces, they could grow in different directions.

   | Classic UNIX layout    | Fixed-stack layout |
   | --------- | ----------- |
   | Stack and heap grow towards each other    | Stack has a fixed maximum size, and heap grows towards the limit       |
    When Stack and Heap touch each other, the process is Out-of-Memory (OoM): it can be killed or grow. | When the stack reaches the limit, the process is OoM        |
   |   Growing requires to: <br> ① Move the *limit* register to increase the size of the address space<br> ②  Move the *stack* up to the limit to allow stack and heap to grow again    |       Growing requires to move the *limit* register      |

- Note that this is from the address space perspective. The OS may still need to move/evict/compact memory to find a free chunk large enough.

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/3.AddressSpace.png?raw=true" alt="Address Space">
</figure>


### II.Dynamic Relocation Procedure
#### (1) Each process is mapped in physical memory and assigned two registers
  - **Base Register**: contains the base address where the process’s address space is mapped
  - **Limit Register**: contains the size of the process’ address space

    When the process accesses a memory address X, the CPU automatically:
    - ① Adds the value of the base register: &nbsp;  *addr* = X + base
    - ② Checks that the result is contained in the address space: base $\leq$ *addr* $<$ base + limit <br> Addresses that exceed this limit trigger an address trap, leading the processor to disregard the invalid physical address.
<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/2.3DynamicRelocation.png?raw=true" alt="Relocation">
</figure>

#### (2) Pros and Cons
- (+) OS can allow a process address spaces to grow over time.
  <br>(-) They can grow, but they are still a single piece of contiguous memory.

- (+) OS can easily move a process during execution
<br> (-) Swapping is still extremely costly. Address spaces must be copied entirely to/from storage devices.

- (-) Slows down hardware due to the add on every memory reference.
- (-) Can't share memory (such as program text) between processes.
- (-) Process is still limited to physical memory size. Address spaces cannot be larger than physical memory. <br> $\Rightarrow$ Degree of multiprogramming is very limited since all memory of all active processes must fit in memory.
- (-) Fragmentation cannot be avoided, only mitigated. Compaction is also costly as entire address spaces must be moved in memory.

## 4. Memory Allocation Policies
### I. Fragmentation
| |External Fragmentation | Internal Fragmentation
------------ |------------ | -------------|
|Description |External fragmentation occurs when there is *enough* total memory to satisfy a request but the available memory is not contiguous.  | Internal fragmentation occurs when memory allocated to a process is slightly larger than what the process actually requested. |
|Cause|Frequent loading and unloading of programs can cause the free memory space to become fragmented into smaller, non-contiguous pieces.|  e.g., if a process requires 8846 bytes but the system allocates a block of 8848 bytes, the extra 2 bytes represent wasted space.|
Desired Policy | We want an allocation policy that minimizes wasted sapce | It is often more efficient to allocate a slightly larger block of memory rather than creating and managing smaller partitions. |

### II. Free Memory Mangement
Note that thesse techniques to track free memory also applies to storage systems. The memory of the following example is split into small 8-bytes chunks. 
#### (1) Technique1: Bitmaps / 位图
Each bit in the bitmap represents the state of one chunk:
  - Bit 0: chunk 0, 
  - Bit 1: chunk 1, etc.

The state of a chunk can have two values:
  - 0 means that the chunk is free
  - 1 means that the chunk is in use

When the OS needs to allocate memory, it will iterate over the bitmap until it finds a large enough contiguous free space, i.e., enough consecutive 0s.

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/4.1Bitmaps.png?raw=true" alt="Bitmaps">
</figure>

Design issues:
Smaller chunks mean finer granularity, there will be less waste but also results in a larger bitmap. Larger bitmaps mean long search times
  
#### (2) Technique2: Free lists
The OS maintains a sorted list of allocations and free memory chunks.

Each element of the list contains:
  - State: U(used) or F(free)
  - Address: the starting address of the chunk
  - Size: the size of the chunk

When the OS needs to allocate memory, it iterates on this list searching for a large enough free chunk according to an allocation strategy. <br> When an allocated chunk is freed, the list is updated to merge the adjacent elements (if they are free)

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/4.2FreeLists.png?raw=true" alt="reeLists">
</figure>

### III. Memory Allocation Policies
- **First fit**:
<br> &nbsp;The allocator returns the first free chunk where the allocation fits. <br> &nbsp; The free chunk is split into two smaller chunks: the newly allocated one, and a free one with the remaining bytes of the chosen free chunk.

- **Next fit**:
<br> &nbsp; Same as *first fit*, except that the search starts from where the last search stopped (instead of from the beginning).
<br> &nbsp; This is supposed to avoid iterating over a lot of allocated chunks in the beginning of the list (they should statistically be more present there).

- Best fit: <br> &nbsp; Search for the *smallest* free chunk where the allocation fits.
<br> &nbsp; The rationale is to avoid breaking up large free chunks for small allocations, thus avoiding waste. <br> &nbsp; In practice, this creates more internal fragmentation. It is also slow since it requires iterating over the whole list.

- Worst fit: <br> &nbsp; Exact opposite of best fit: always allocate in the *largest* available hole. <br> &nbsp; The idea is to avoid the internal fragmentation of best fit. <br> &nbsp;In practice, it doesn’t really work well either.

<br> All strategies can be improved with various optimizations:
- Keeping a separate list for free chunks speeds up search but makes list updates costly / 保持一个单独的空闲块列表
 - Sorting the list to avoid long searches, at the cost of expensive insertions / 对列表进行排序以避免长时间搜索
 - Storing the free list directly in the free chunks themselves / 每个空闲块可以通过内部指针指向下一个空闲块，形成链表


## 5. Memory Management - The Virtual Memory Abstraction
### Problem encountered till now and solution intuition
  - Fragmentation (Frequent compaction needed); 
  - Contiguous allocation (Difficult to grow or shrink process memory)
  - Requirement that process resides entirely in memory (Swapping helps but not perfect)
 
## 5.1 The Virtual Memory Abstraction - Paging
#### Solution motivation: 
Processes typically spend 90% of their time accessing only 10% of their memory space. Therefore, it is efficient to keep only the *actively used portions of a process* in memory.

#### Solution Core Idea:
- We divide address spaces into small chunks called *pages*.
- Each page itself is a contiguous range of memory addresses. However, pages themselves need not be allocated contiguously in physical memory, This means that pages can be mapped anywhere in *physical memory*, and only the pages currently in use need to be in memory, while others can be swapped out to storage.
- When a process attempts to use a virtual address that is not currently mapped to physical memory, the OS swaps in the necessary data allowing the process to continue execution seamlessly.
- Paging is a form of dynamic relocation, where each virtual address is bound by the paging hardware to a physical address. We can think of the *page table* as a set of *Relocation Registers*, one for each frame. Base registers tell where the entire process begins, whereas relocation registers tell the mapped location of every single page in physical memory. 

### I. Definitions
Most systems implement virtual memory with paging. 
- A **page** is a fixed-size unit of virtual memory.

- A **page frame / 页框** is a fixed-size unit of physical memory. 
  
- Pages are mapped by the OS into a page frame of the same size. Note that the mapping is invisible to the process. The OS maintains the mapping and the hardware does the translation. 

- The p**age table** needs ***one*** entry per page. **Page table entries (PTE / 分页表项)** are architecture-dependent, but usually contain the following information:

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/5.0PTE.png?raw=true" alt="PTE">
</figure>

   |     | Definition |
   | --------- | ----------- |
   | Page frame number    | the page frame corresponding to this page, i.e., the actual translation  |
   | Protection bits | the access permissions of this page (read/write/execute). <br> Can be 1 bit (read/write or read-only) or 3 bits (read, write, execute).  |
   | Modified/dirty bit |  set to 1 if the page has been modified after being swapped in. <br> This is needed when the OS swaps out a page: if the page is not dirty, the OS does not need to copy it into storage. |
   | Referenced bit | set to 1 when the page is read from/written to. <br> This is used for page reclamation algorithms to choose which page to evict. |
   | Supervisor bit    | set to 1 if the page is only accessible in supervisor mode, i.e., by the kernel. <br> A user process accessing a page with this bit set will trigger a fault.|
   | Present bit | set to 1 if the page is mapped onto a page frame, 0 if it is only on storage. <br> Accessing a page with this bit set to 0 will trigger a page fault to allow the OS to swap the page in.  |
   | Uncached bit    | set to 1 if the page must not be cached in the CPU caches and always be accessed from/to memory. <br> Used for pages mapping physical devices to avoid using outdated cached values.     |

- The **Memory Management Unit (MMU / 内存管理单元)** is a hardware component that transparently performs address translations.
  - MMU sits between the CPU and the bus to translate virtual addresses into physical addresses, i.e., page $\rightarrow$ page frame.
  - It contains a table with the translations from virtual addresses to physical ones: the **page table / 分页表**.
    <figure>
        <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/5.1MMU.png?raw=true" alt="MMU">
    </figure>


### II. Example of paging  
<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/5.2Paging_Example.png?raw=true" alt="Paging Example">
</figure>

Note that we need to keep track of which pages are absent from physical memory to swap them in when needed.

### III. Example of MMU and Unmapped Pages
#### Setting: 
- 64 KiB address spaces (virtual addresses are 16 bits long);
- 32 KiB physical memory (physical addresses are 15 bits long)  
- 4 KiB pages

<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/5.3MMU_Example.png?raw=true" alt="Paging Example">
</figure>

#### e.g. (1)  
 - (i) The CPU issues a memory access to a *virtual address*, 41772, bin(41772) = 1010 001100101100 <br> &nbsp; 当前正在执行的程序包含一条指令，该指令需要CPU访问虚拟地址41772处的数据

 - (ii)The virtual address goes through the MMU that splits it into two parts: <br> &nbsp; 分页机制下，MMU处理虚拟地址。虚拟地址包括两部分:
   - ① Page number / 页号: 
     - The page number is used as an index in the page table to find the associated page frame number.  The page frame number will become the most significant bits of the physical address. <br> 页号用作页表的索引，找到对应的页框号。页框号将成为物理地址的最高有效位
     - we have 16 pages = $2^4$, so the 4 most significant bits identify the page. This will be used for the translation. 64 / 4 = 16个页面（= $2^4$），所以4个最高有效位用于标识页面。这部分将用于地址转换。
   - ② Page Offset / 页内偏移: 
     - The offset is propagated as is in the physical address. 偏移量在物理地址中保持不变
     - The remaining 16 - 4 = 12 bits identify the memory location in the page. This will be kept as is in the physical address. <br>剩下的12个低有效位标识页面内的内存位置。这部分在物理地址中将保持不变。
 - (iii) The physical address, 13 100, is used to issue the memory access in memory through the bus.

#### e.g. (2)  If the page is not present in physical memory   
a slightly modified page table：
<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/5.4PageFault.png?raw=true" alt="Page Fault">
</figure>

 - (i) The CPU wants to access the virtual address 41772, which has the page number 10.
 - (ii) Page 10 is not mapped in memory, thus triggering a page fault. The OS must map page 10 into a page frame. 查找页表并发现页码10没有映射到物理内存，触发页面错误
 - (iii) The OS decides to evict page 11 (swap out) to make space in physical memory. OS决定驱逐页码11以腾出空间，i.e.,页码11的页框被释放。
 - (iv) The OS then allocates page 10 in the newly freed page frame.
The page fault is now resolved. 页码10被映射到新释放的页框
 - (v) Translation continues normally by concatenating the page frame number and the offset into the physical address 13 100.


### IV. Paging with multiple address spaces  
<figure>
    <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/5.5Page&Multiple.png?raw=true" alt="Page with Multiple Processes">
</figure>

- Virtual address spaces are spread into physical page frames, they don’t need to be fully contiguous. External fragmentation is not a problem anymore. But paging does NOT eliminate internal fragmentation. 
  
- Paging is a form of dynamic relocation, virtual address spaces can be swapped in and out at page granularity, transparently and on-demand. Swapping now becomes much more efficient. 
  
- Kernel memory is shared for ALL address spaces, so it is usually mapped in ALL of them at the same place, with the supervisor bit set to 1 in the PTEs. <br> &nbsp; 
  - If the kernel had its own page table, each system call would require saving the user's page table context, loading the kernel's page table to access the kernel address space, and then switching back to the user's page table and restoring its context after the system call completes. By sharing kernel memory—mapping the kernel address space identically in all user processes' page tables—frequent page table switches are avoided. Thus, system calls only need to switch the CPU mode, not the page tables, thereby improving efficiency.
  - / 如果内核有自己的页表，每次系统调用都需要先保存用户页表的上下文，然后加载内核页表以访问内核地址空间，系统调用完成后再切换回用户页表，恢复用户页表的上下文。通过共享内核内存，即内核地址空间在所有用户进程的页表中都有相同的映射，减少了频繁的页表切换，系统调用只需要切换运行模式，而不需要切换页表，这样便提高了效率。

### V. Optimizing Paging Motivation
#### we may face some major problems:
- The address space can be very large as it does not depend on the size of the physical memory. <br> Take 32 bit address spaces (4 GiB) with 4 KiB pages as an example:
  - Address space size: AS = $2^{32}$ Bytes = 4GiB
  <br> &nbsp; Each process can grow its address spaces up to 4GiB
  <br> &nbsp; And this is replicated for each address space, i.e., for **each** process.
  - Page Size: P = 4 KiB = $2^{12}$ Bytes
  - Page Table Size: E =  32 Mib = 4 MiB (for **each** process)
    - The Page Table stores one Page Table Entry per page, each PTE stores:
      - Page Frame Number: assuming machines with 4 GiB of physical memory, this would be 20 bits
      - Metadata, e.g., present, dirty, etc.: 12 bits on x86 

  <br> For each process, we can have as much as 4 GiB / 4 KiB = 1Mi pages, and 4 MiB to store Page Tables. 
<br> $\Rightarrow$ We need an efficient way of storing page tables.


- Every memory access triggers a translation from virtual to physical address. This means that for every memory access, we need to look up the page frame number corresponding to the accessed page and build the physical address before actually performing the access.
<br> $\Rightarrow$  We need mechanisms to make translation fast

#### (1) Solution for an efficient way of storing page tables: Multilevel page tables
  <figure>
      <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/5.6MultilevelPageTable.png?raw=true" alt="Multilevel PageTables">
  </figure>

  e.g. Two-Level Page Table  
  <figure>
      <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/5.7TwoLevelPageTable.png?raw=true" alt="2-level PageTables">
  </figure>
  &nbsp; Assume this process using only 12 MiB of address space (3 second level page tables = 3x 4 MiB). 
  <br> &nbsp; Note that we only need 4 pages (16 KiB) for page tables.

  -  When an virtual address *vaddr* = 0x4041FB is used by the CPU, it goes through the MMU like previously
  - The MMU splits the virtual address int three parts:

    |    | PT1 | PT2 | Offset |
    | --- | ----------- | ----------- | ----------- |
    | Usage |  PT1 is used as an index in the first level page table to find the address of the corresponding second level page table: the Page Table Address (PTA) |  PT2 is used as an index in the second level page table to find the *page frame number* | The physical address *paddr* is built by concatenating the page frame number with the offset. |
    | Example | 10 bits for the index in the first level page table |10 bits for the index in the level 2 page table |12 bits for the offset in the page <br> 4 kiB = $2^{12}$ Bytes, thus last 12 bits for offset|

    This lookup process is called a *page walk*. Whenever a virtual address needs to be translated into a physical address (potentially multiple times per instruction), the MMU must perform a page walk to recover the page frame number.
  
 #### (2) Solution for mechanisms to make translation fast - Translation Lookaside Buffer(TLB / 页表缓存)
 ##### (a.) Observation: Most programs frequently reference the same addresses.
$\Rightarrow$ the obvious solution to our translation speed problem is to use *caching*.

 ##### (b.) The MMU usually contains a small associative cache called the Translation Lookaside Buffer. 
It stores for each entry:
- The mapping from a virtual page number to the corresponding physical page frame number 
- Valid bit: set to 1 if the entry in the TLB is valid
- Metadata from the page table entry:
  - *Protection* bits from the page table entry (read/write/execute) 
  - *Modified* bit from the page table

  <figure>
      <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/5.8TLB.png?raw=true?raw=true" alt="TLB">
  </figure>

 ##### (c). When a virtual address *vaddr* goes through the MMU, it follows this path:

  <figure>
      <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/5.9TLBWorkflow.png?raw=true" alt="TLB Workflow">
  </figure>

 ##### (d). Costs of using the TLB
 Let *ma* be the memory access cost per unit time.
  - If the page table is in memory, the effective memory access (*ema*) cost would be:
    - Search for the corresponding page table entry in the page table: 1 memory access.
    - Use this page table entry to convert the virtual address to a physical address and then access this physical address: this is the 2nd memory access.
    - In total: *2ma*
  - If the page table entry is in the TLB: 
    - Case 1 **TLB Hit**: Search for the corresponding page table entry in the TLB. If found, directly convert the address and access the physical address. This requires 1 memory access and 1 TLB access.
    - Case 2 **TLB Miss**: If not found in the TLB, search for the entry in the page table in memory, load this entry into the TLB, then convert the address and access the physical memory.
    - The total effective memory access cost is given by:
    <br> ema = p(ma + TLB access) + (1-p)(2ma + TLB access), where *p* is the TLB hit ratio. 

 ##### (e).TLB Management
Most of the TLB management is performed by the MMU:
- When a TLB entry is loaded from the page table, the necessary metadata are copied into the TLB entry.
- If the TLB is full when a new entry must be saved, the MMU will evict an entry
-  When a TLB entry is evicted, the MMU writes back the metadata in the TLB into the page table entry

<br> Some operations must still be triggered by the OS:
- When a context switch occurs, the TLB must be flushed to avoid wrong translations,
<br> e.g., processes A and B might both use virtual page , but they point to different page frames.
- When updating a page table entry, the OS needs to invalidate the related TLB entries to force a synchronization with the page table in memory,
<br> e.g., page 61 is swapped out, making the translation in the TLB invalid.

### VI. Page Replacement
#### (1) Page Fault
When a page is not mapped into a page frame, a *page fault* is triggered.
<br> The page faults triggers the OS to bring the requested page into memory:
- If there is no *page frame* available, evict a page from memory, i.e., a page is swapped out.
  - If the page has been modified, it must be written back to disk
  - The page is unmapped in the page table
- Map the requested page into an available page frame, i.e., the page is swapped in.
  - Update the page table of the process
  - Copy the content of the page into the page frame
  
#### (2) How does the operating system choose which page to evict from memory? <br>—— Page Replacement Algorithms

Page replacement algorithms usually try to evict pages that will not be used in the near future to avoid frequent swapping in/out. Whatever algorithm is used, the OS needs to measure the use of ALL pages to determine which one to evict.
##### (a)  First-In First-Out /FIFO

-  When a page is mapped in memory, it is added into a list
-   When a page must be evicted, the last (oldest) page of the list is evicted
  <figure>
      <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/510.FIFO.png?raw=true?raw=true" alt="FIFO">
  </figure>
‼️ The FIFO page replacement algorithm decides which page to evict based solely on the order in which pages were loaded into memory, without considering how often or recently they have been accessed.

##### (b) Clock Algorithm
The clock algorithm is an updated version of FIFO that gives a second chance to pages if they have been recently accessed, using the *Referenced bit* (R) from the page table entry, set to 1 by the MMU at each access.

- Imagine that all our physical page frames are arranged around a clock. We have a clock hand that points to *the next page for eviction* 
- Each time a page is accessed, the hardware sets its reference bit to 1. The OS is not involved in this step.
- When a page that is not currently mapped into memory needs to be loaded, the OS takes control of the page replacement process. The OS examines the page under the clock hand:
  - If its reference bit = 1, the OS sets it to 0 and moves the hand to the next page. This step is repeated until a page with a reference bit of 0 is found;
  - If its reference bit = 0, the OS evicts this page and loads the needed page into its place. 

##### (c) Least Recently Used (LRU)
LRU evicts the page that hasn’t been used for the longest time.
To implement it precisely, there are two possibilities:
- Implement a FIFO list and, whenever a memory access happens, move the corresponding page to the head of the list. <br> $\Rightarrow$ This must be done by the OS in software, which is too costly.

- Add a field in the PTE that logs the timestamp of the last access, updated by the MMU, and look for the oldest timestamp for eviction <br> $\Rightarrow$  This needs hardware support and the lookup is costly with a large number of pages.

In practice, most systems implement **approximations of LRU with aging**.
- Each page has a small counter associated to it, e.g., 8 bits
- At every clock tick, the counter of every page is shifted once to the right, and the Referenced bit is added as the leftmost bit
- When a page fault occurs and eviction is required, the page with the smallest counter is evicted

## 5.2 The Virtual Memory Abstraction - Segmentation
 &nbsp;Instead of providing a ***single*** virtual address space per process, segmentation offers ***many*** independent virtual address spaces called *segments*.
<br> &nbsp; Segments take the user's view of the program and gives it to the OS. 
<br> &nbsp; Each segment starts at address 0 and has a length that can change over time.
<br> &nbsp; The OS maintains a segment table for each process that stores segment descriptors:
 - Base address: the physical address where the segment is located 
 - Length: the length of the segment
 - Metadata (non-exhaustive list)
    - Present bit: is the segment mapped in memory?
    - Supervisor bit: is the segment only accessible in supervisor mode? 
    - Protection bits: is the segment read-only, read-write, executable?
  <figure>
      <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/6.1Segment.png?raw=true" alt="Segment">
  </figure>

Programs can split their memory into segments as they wish. For example, one could use four segments as follows:
  <figure>
      <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/6.2SegmentExample.png?raw=true" alt="Segment Example">
  </figure>

  - A text segment of size 4 KiB;
  - A stack segment of size 4 KiB 
  - A data segment of size 16 KiB 
  - A heap segment of size 8 KiB
<br> This is usually done transparently by the *compiler*, not explicitly by the programmer. Most languages assume a flat address space, i.e., a single address space per process.

## Summary
Comparison of Virtual Memory Mechanisms
  <figure>
      <img src="https://github.com/LiaXLiang/LiaXLiang.github.io/blob/master/assets/img/OS_Lectures/Chap4/7.Summary.png?raw=true" alt="Summary">
  </figure>

## 6. Memory Allocators / 内存分配器