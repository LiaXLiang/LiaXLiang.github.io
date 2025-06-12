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


## Java Type
### 1. What is a "Type", and why do variables need it?

A variable's type tells the compiler:
- what **values** it can take,
- what **operations** you can perform on it,
- what **type-checking rules** the compiler applies (how variables with the *same name* are resolved)

Without knowing the type, the compiler can't do its job. That’s why Java is **a statically typed language**: **every variable must have a type known at compile time**.

### 2. Java has two main categories of types
#### I. Primitive Types (also called value types)

Primitive Data Types are the most fundamental building blocks a program uses to represent values. 

Java defines 8 built-in













e.g.
```java
String name = "Alice";
Animal cat = new Cat();
```
- *name* has type `String`
- *cat* has type `Animal` (even though the object is of class `Cat`)

This distinction between **type (what the variable is declared as)** and **class (what object is actually stored)** will turn out to be crucial.


