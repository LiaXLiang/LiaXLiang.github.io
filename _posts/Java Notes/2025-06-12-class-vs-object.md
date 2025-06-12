---
title: What is Object-Oriented Programming?
date: 2025-06-12
categories: [Java_Notes]
---

### Analogy: Animals in the Zoo
Let's say we visit a zoo. We see a *cat*, a *dog*, and a *rabbit*. These are actural animals we can touch - they are **objects**. But when we describe what we saw, we might just say:" I saw some *animals*." The word "*animal*" is abstract - it refers to the concept or type, not a specific instance that we can point to. In Java, that abstract idea is represented by a **class**.

### Defining a Class
A Class defines:
- **State** —— **Fields**
  - the properties an object holds (e.g., name, age)
- **Behaviour** —— **Methods**
  - the actions the object can perform (e.g., eat, sleep, hunt)
- **Construction** —— **Constructor**
  - how an object is created (via *Constructors*)    

```java
public class Animal {
    private String name;
    private int age;

    // Default constructor
    public Animal() {}

    private void eat() {}
    
    private void sleep() {}
    
    private void hunt() {}
    
}
```
- **Fields**
  -  *name* and *age* represent the **state** of an animal. These are also called **member variables** or **instance variables.** They do **NOT** occupy memory at compile time. Only when we instantiate the class (i.e., create an actual animal object), memory is allocated.
- **Methods**
  - `eat()`, `sleep()`, and `hunt()` define the **behavious** of the animal.
- **Constructor **  