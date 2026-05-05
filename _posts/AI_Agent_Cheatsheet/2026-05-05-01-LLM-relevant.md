---
title: Must-know about LLMs
layout: post
---

## 1. What is the fundamental task of a Language Model (LM)?
A language model calculates the probability of a word sequence (i.e., a sentence) appearing. A good language model can tell us what kind of sentences are fluent and natural.

### 1.1 Language Model: N-gram models
- Time: before the rise of deep learning
- statistical method (at the time the mainstream of language models)
- Core Idea: the probability of a sentence appearing equals the product of **conditional probabilities** of each word in the sentence. The formula is called **the chain rule of probability**
- Problem: calculating the conditional probability is almost impossible, since like $P(w_m∣w_1, ..., w_{m-1})$ are too difficult to estimate from a corpus, 
, as the word sequence $w_1, ..., w_{m-1}$ may have never appeared in the training data.


To solve this problem, researchers introduced the **Markov Assumption**.

#### Core Idea of Markov Assumption
We can approximately assume that a word's probability of appearing is only related to the limited **n-1 **words before it. Language models built on this assumption are called N-gram models. 
- "N" := context window size we consider
  - e.g., N = 2: Bigram. i.e., a word's appearance is only related to the one word before it. $P(w_i∣w_1, ..., w_{i-1})$ roughly equals $P(w_i∣w_{i-1})$
  - e.g., N = 3: Trigra. i.e.,  we assume a word's appearance is only related to the two words before it. 

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

