---
title: The Three Characteristics of Java - 01. Encapsulation
layout: post
---

## Intuition: The Human Analogy
Just as deep learning models are inspired by the human brain, object-oriented design patterns reflect how we interact in real life.

In human society, we don’t expose our private details indiscriminately. Instead, we share information selectively—through controlled conversations and deliberate actions. Similarly, encapsulation in Java ensures that an object’s internal state is hidden from the outside world and accessed only through controlled interfaces.

This design philosophy:
- Prevents unintended misuse and safeguards data integrity.
- Promotes modularity and maintainability (like well-defined social roles and boundaries).


## What is Encapsulation? 
Encapsulation is a fundamental object-oriented concept that involves：
- bundling **data (fields)** and **behaviour (methods)** into **a single unit (a class)** 
- restricting direct access to internal state, forcing external code to interact through a controlled interface.

## Why Encapsulation? 
Condider this naïve implementation:
```java
public class Person {
    String name;
    int age;
    Boolean married;
}
```

#### Problem 1: Unrestricted Access Leads to Invalid States
In this version, fields are publicly accessible. Any external class can directly assign values—even absurd or logically invalid ones:

```java
Person alice = new Person();
alice.age = 1000;  // No error, but logically absurd.
```

#### Solution: Controlled Modification via Setters
Make fields private and provide validated *setters* to enforce invariants:

```java
public class Person {
    private String name;
    private int age;
    private Boolean married;

    // Name control
    public void setName(String name) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Name cannot be empty");
        }
        if (name.length() > 100) {
            throw new IllegalArgumentException("Name too long");
        }
        this.name = name;
    }

    // Age control
    public void setAge(int age) {
        if (age < 18 || age > 70) { 
            throw new IllegalArgumentException("Age must be 1–100");
        }
        this.age = age;
    }
}
```


#### Problem 2: Inappropriate Information Exposure
In hiring scenarios, recruiters should not have unrestricted access to sensitive personal details such as a candidate’s exact age. Instead, they should interact only with the information relevant to their decision-making — for example, whether the candidate is legally an adult.

Moreover, storing *age* as a field introduces data staleness: the value becomes outdated as time progresses, unless actively updated. A better design is to replace *age* with *birthDate*, and expose only the necessary behavior through a well-defined interface — such as `isAdult()`.

External code should rely on what the object can do, not what data it holds.

```java
import java.time.LocalDate;
import java.time.Period;

public class Person {

    private String name;
    private LocalDate birthDate;     // Replaces 'age' with 'birthDate'
    private boolean married;


    // Name control

    /**
     * Determines whether the person is legally an adult (18+ years).
     * This abstracts away birth date logic and avoids exposing raw data.
     */
    public boolean isAdult() {
        return Period.between(birthDate, LocalDate.now()).getYears() >= 18;
    }
}
```    

#### Problem 3: Lack of Modularity and Maintainability
Without proper encapsulation, a class exposes its internal structure to the outside world, **tightening** the coupling between modules. As a result, any internal change risks breaking dependent code, reducing flexibility and maintainability.

Assume that earlier implementations stored *age* directly and all external access relied on the `getAge()` method:

```java
public class Person {
    private int age;

    // ...

    public int getAge() {
        return age;
    }
}
```
When we later swap *age* for *birthDate*, we must update every occurrence. But with encapsulation, we can only change the body of `getAge()`:

```java
public class Person {
    private LocalDate birthDate;

    // ...

    public int getAge() {
        return Period.between(birthDate, LocalDate.now()).getYears();
    }
}
```
Encapsulation isolates change. 