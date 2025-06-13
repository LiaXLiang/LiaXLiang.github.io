---
title: Variable Hiding v.s. Variable Shadowing
layout: post
---

## Variables Are Everywhere

In almost every programming language, variables serve as the basic units to solve problems. 

A variable is not just a name.

Take this simple line of code:
```java
int score = 100;
```
Here, `score` is a variable — but Java doesn't just see a name and a value. It also sees a <font color = red>type</font>.


## Type
### 1. What is a "Type", and why do variables need it?

In Java, a variable acts like a named memory *container* that stores values during program execution. When a variable is **declared**, its associated data type must be specified. 
 
A variable's type tells the compiler:
- what **values** it can take,
- what **operations / type-checking** you can / should perform on it
- how to **resolve variable naming conflicts**

Without knowing the type, the compiler can't do its job. That’s why Java is **`a statically typed language`**: **every variable must have a type known at compile time**.

### 2. Java has two main categories of types
#### I. Primitive Types (also called Value Types)

Primitive Data Types are atomic in the sense of not being composed of smaller parts. <font color = sky-blue>They are **stored directly in stack memory**</font> and are NOT instances of any class.

Java defines 8 built-in primitive types, each representing a specific kind of raw value:
| Category        | Types                        |
|:----------------|:-----------------------------|
| Integer         | byte, short, int, long       |
| Floating point  | float, double                |
| Character       | char                         |
| Boolean         | boolean                      |

Precision Ordering of Integer Types:
- **byte** (8 bit signed integer) < **short** (16-bit signed integer) 
  
  < **int** (32-bit signed integer) < **long** (64-bit signed integer) 
  
  < **float** (32-bit floating point) < **double** (64-bit floating point)
- Note that just because *byte* or *short* uses less memory doesn't mean it's faster. On most systems, operations on *int* are more efficient, and smaller types might even be promoted to *int* during computation.

#### II. Reference Types (also called Object Types)
 <font color = sky-blue>Reference types **store a memory address (reference)** pointing to an object stored in heap memory.</font>

| Reference Type | Description                        | Example         |
|:---------------|:-----------------------------------|:----------------|
| Class          | User-defined or library class      | `String name;`  |
| Interface      | A contract implemented by classes  | `Runnable r;`   |
| Array          | Collection of elements             | `int[] nums;`   |
| Enum           | Constant group of named values     | `Day day;`      |

### 3.  Type v.s. Class: What's the Difference?
| Aspect              | Type                                                                 | Class                                                   |
|:--------------------|:----------------------------------------------------------------------|:---------------------------------------------------------|
| What it is          | A **compiler-level concept** that tells what kind of data a **variable** holds and how it behaves | A **programmer-defined** blueprint for creating **objects**      |
| Role                | Used to declare **variables**, check compatibility, and enforce compile-time safety | Used to define the structure and behavior of **objects**     |
| Examples            | `int`, `String`, `Animal`, `List<String>`                            | `Animal`, `String`, `ArrayList`, etc.                    |
| Not all types are…  | Not all types are classes (e.g., `int`)                              | Every class can be used as a type                        |


Every class can be used as a type, but not every type is a class.
- e.g. 
    ```java
    Animal a = new Animal(); 
    ```
    - `new Animal()` creates a new **object** whose **runtime class** is `Animal`, and stores a **reference** to it in variable `a`.
    - The variable `a` has a **decalred type** `Animal`, and its **actual object** is also of type `Animal`.


## Scope
Understanding a variable's type is only part of the story.

In real-world scenarios, multiple variables with the same name can exist in different locations - a method, a class, a subclass, or even a loop. This is where the concpet of **scope** comes in.

While *type* answers the question "**what is this variable?**, *scope* answers "**where is this variable accessible?**" and "**which one is picked if there are multiple with the same name?**".







