---
title: What is Object-Oriented Programming?
date: 2025-06-12
categories: [Java_Notes]
---


To understand **Object-Oriented Programming (OOP)**, we must first grasp the concept of an **object**. But to fully appreciate the evolution and purpose of objects in programming, it's helpful to contrast them with their *predecessor*: **Procedure-Oriented Programming (POP)**

### A Simple Analogy
Imagine we're hungry and want to have some *Seafood Spaghetti* for dinner. We have two choices:
- Option A: Go to the supermarket, buy ingredients like spaghetti, tomato, onion and seafood, and cook the dish yourself.
- Option B: Go to a restaurant and order a plate of Seafood Spaghetti. 
  
Option A represents *Procedure-Oriented Programming*.

Option B represents *Object-Oriented Programming*.

### Understanding POP
Cooking at home requires us to know and perform every individual step in the recipe: preparing ingredients, following the cooking process, and cleaning up. 

Similarly, in POP, the program is structred as a sequence of steps (procedures) tha, written in a top-down manner. 

#### Limitations of POP
- **Low Reusability**
  - If we’ve written a program that "makes Seafood Spaghetti", and now we want to prepare ***Pizza***, we can’t reuse much of your existing code. We must start a new procedure from scratch - buying different ingredients, following a new set of steps, and writting new code for each part.
- **High Maintenance Effort**
  - Suppose we still want Spaghetti, but a ***vegetarian*** version instead of seafood, this requires going back to the recipe, identifying and removing all seafood-related logic, adjusting cooking steps, and carefully ensuring nothing breaks.
- **Poor Scalability**
  - As the program grows, managing procedures and shared data becomes more difficult and error-prone.   

### Understanding OOP
We simply order a dish in the restaurant. We don't need to know how the chef prepares it, which ingredients are used, or how the kitchen is structured. We just interact with the restaurant via a well-defined interface: the waitor.

Similarly, in OOP, object expose **public methods (interface)** and hide internal implementation details (**encapsulation**)

#### Advantages of OOP
- **Modularity and Encapsulation**
  - There is a pasta chef, and a pizza chef. Each one knows their task, does it well, and doesn't need to understand the others' recipe to contribute. 
- **Reusability** 
  - Once the *Pizza* class is defined, we could reuse it anywhere in our program.
- **Flexibility and Scalability**
  - It's easier to extend or modify programs without affecting other parts of the program.   
  
### Is OOP fancier as POP?
Yes and No.

At the **machine level**, all programs ultimately execute instructions procedurally - the CPU processes one instruction at a time. OOP doesn't change this underlying behaviour.

However,at the **language and abstraction level**, OOP is a powerful *design paradigm*. By encapsulating data and behaviour into classes and objects, developers can build larger, more maintainable systems that mirror real-world entities and interactions more naturally. 

In other words: OOP is a higher-level abstraction built on top of *procedural* execution, enabling modularity, code reuse, and scalable architecture. OOP is a different way of thinking about problem-solving: While procedural programming focuses on ***how*** things are done, OOP focuses on ***who*** is responsible for doing them.

