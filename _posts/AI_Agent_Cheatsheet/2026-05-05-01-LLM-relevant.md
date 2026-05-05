---
title: Must-know about LLMs
layout: post
---
## 1. What is the fundamental task of a Language Model?

A language model estimates the probability of a sequence of words. Given a sentence consisting of words $(w_1, w_2, ..., w_m)$, the model estimates:

$$
P(w_1, w_2, ..., w_m)
$$

Intuitively, a good language model assigns higher probability to fluent and natural sentences, and lower probability to unnatural word sequences.

For example, it should assign a higher probability to:

> The cat sits on the mat.

than to:

> Mat the on sits cat the.

Therefore, the fundamental task of a language model is to **model the probability distribution of word sequences**.

---

## 1.1 Traditional Language Models: N-gram Models

Before deep learning became dominant, language models were mainly based on statistical methods. A classic example is the **N-gram language model**.

The probability of a sentence can be decomposed using the **chain rule of probability**:

$$
P(w_1, w_2, ..., w_m)
=
\prod_{i=1}^{m} P(w_i \mid w_1, ..., w_{i-1})
$$

This means that the probability of a sentence is the product of the **conditional probabilities** of each word, given all previous words.

However, this is difficult to estimate in practice because of **data sparsity**. For example:

$$
P(w_m \mid w_1, ..., w_{m-1})
$$

requires the full context $(w_1, ..., w_{m-1})$ to appear frequently enough in the training corpus. In real-world data, many long word sequences rarely or never appear, making the estimation unreliable.

---

## 1.2 Markov Assumption

To make language modeling practical, N-gram models use the **Markov assumption**.

The core idea is:

> The probability of the current word depends only on a limited number of previous words, rather than the entire history.

Formally, an N-gram model approximates:

$$
P(w_i \mid w_1, ..., w_{i-1})
$$

with:

$$
P(w_i \mid w_{i-n+1}, ..., w_{i-1})
$$

Here, $n$ is the size of the context window.

### Bigram Model

When $n = 2$, the model is called a **bigram model**. It only considers the previous word:

$$
P(w_i \mid w_1, ..., w_{i-1})
\approx
P(w_i \mid w_{i-1})
$$

### Trigram Model

When $n = 3$, the model is called a **trigram model**. It considers the previous two words:

$$
P(w_i \mid w_1, ..., w_{i-1})
\approx
P(w_i \mid w_{i-2}, w_{i-1})
$$

In general, an N-gram model uses the previous $n-1$ words to predict the next word.

---

## 1.3 Estimating N-gram Probabilities with MLE

N-gram probabilities are usually estimated using **Maximum Likelihood Estimation (MLE)**.

The idea is simple:

> If something appears more often in the training corpus, the model considers it more likely.

For a bigram model, we estimate the probability of word $w_i$ appearing after word $w_{i-1}$ as:

$$
P(w_i \mid w_{i-1})
=
\frac{Count(w_{i-1}, w_i)}{Count(w_{i-1})}
$$

where:

- $Count(w_{i-1}, w_i)$ is the number of times the word pair $(w_{i-1}, w_i)$ appears consecutively.
- $Count(w_{i-1})$ is the number of times the word $w_{i-1}$ appears.

In other words:

> Among all occurrences of $w_{i-1}$, how often is it followed by $w_i$?

Example:

If `"deep"` appears 100 times, and `"deep learning"` appears 60 times, then:

$$
P(\text{learning} \mid \text{deep})
=
\frac{Count(\text{deep}, \text{learning})}{Count(\text{deep})}
=
\frac{60}{100}
=
0.6
$$

So the estimated probability of `"learning"` appearing after `"deep"` is 0.6.

---

## 1.4 Limitations of N-gram Models

N-gram models are simple and interpretable, but they have three major limitations.

### 1. Data Sparsity
Imagine you are learning English only by memorizing exact sentences from a textbook. If you see a new sentence that is grammatically correct but never appeared in the textbook, you may mistakenly think it is invalid.

N-gram models rely on exact word sequence counts. If a valid phrase never appears in the corpus, the model may assign it zero probability.

For example, if `"neural language model"` never appears in the training data, a trigram model may fail to estimate its probability correctly.

This is known as the **zero-probability problem**.

### 2. Limited Context
Imagine reading a long story but only being allowed to remember the last one or two words. You may understand local phrases, but you will easily miss the larger meaning of the sentence.


N-gram models only use a fixed-size context window.

A bigram model only considers one previous word, and a trigram model only considers two previous words. Therefore, they struggle to capture long-range dependencies.

For example:

> The book that I borrowed from the library yesterday was very interesting.

To understand that `"was"` refers to `"book"`, the model needs information from much earlier in the sentence. Traditional N-gram models are not good at handling this.

### 3. Weak Semantic Representation

N-gram models treat words as discrete symbols. They rely on surface-level co-occurrence statistics and do not learn deep semantic relationships.

For example, they cannot naturally understand that `"car"` and `"automobile"` are semantically similar unless this relation is reflected in the corpus statistics.

---

## 1.5 Interview Summary

The fundamental task of a language model is to estimate the probability of word sequences.

Traditional N-gram models use the chain rule of probability, but directly estimating long-context conditional probabilities is impractical because of data sparsity.

To address this, N-gram models apply the Markov assumption: the current word depends only on the previous $n-1$ words.

N-gram probabilities are commonly estimated using Maximum Likelihood Estimation:

$$
P(w_i \mid w_{i-1})
=
\frac{Count(w_{i-1}, w_i)}{Count(w_{i-1})}
$$

However, N-gram models suffer from data sparsity, limited context, and weak semantic representation. These limitations motivated the development of neural language models and, later, large language models.



## A Simple Analogy

## Understanding POP
Cooking at home requires us to know and perform every individual step in the recipe: preparing ingredients, following the cooking process, and cleaning up. 

Similarly, in POP, the program is structred as a sequence of steps (procedures) tha, written in a top-down manner. 

### Limitations of POP
- **Low Reusability**
  - If we’ve written a program that "makes Seafood Spaghetti", and now we want to prepare ***Pizza***, we can’t reuse much of your existing code. We must start a new procedure from scratch - buying different ingredients, following a new set of steps, and writting new code for each part.
- **High Maintenance Effort**
  - Suppose we still want Spaghetti, but a ***vegetarian*** version instead of seafood, this requires going back to the recipe, identifying and removing all seafood-related logic, adjusting cooking steps, and carefully ensuring nothing breaks.
- **Poor Scalability**
  - As the program grows, managing procedures and shared data becomes more difficult and error-prone.   

## Understanding OOP
We simply order a dish in the restaurant. We don't need to know how the chef prepares it, which ingredients are used, or how the kitchen is structured. We just interact with the restaurant via a well-defined interface: the waitor.

Similarly, in OOP, object expose **public methods (interface)** and hide internal implementation details (**encapsulation**)

### Advantages of OOP
- **Modularity and Encapsulation**
  - There is a pasta chef, and a pizza chef. Each one knows their task, does it well, and doesn't need to understand the others' recipe to contribute. 
- **Reusability** 
  - Once the *Pizza* class is defined, we could reuse it anywhere in our program.
- **Flexibility and Scalability**
  - It's easier to extend or modify programs without affecting other parts of the program.   
  
## Is OOP fancier as POP?
Yes and No.

At the **machine level**, all programs ultimately execute instructions procedurally - the CPU processes one instruction at a time. OOP doesn't change this underlying behaviour.

However,at the **language and abstraction level**, OOP is a powerful *design paradigm*. By encapsulating data and behaviour into classes and objects, developers can build larger, more maintainable systems that mirror real-world entities and interactions more naturally. 

In other words: OOP is a higher-level abstraction built on top of *procedural* execution, enabling modularity, code reuse, and scalable architecture. OOP is a different way of thinking about problem-solving: While procedural programming focuses on ***how*** things are done, OOP focuses on ***who*** is responsible for doing them.

