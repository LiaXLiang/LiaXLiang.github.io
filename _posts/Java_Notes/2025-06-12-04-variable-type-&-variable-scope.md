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

***

## Type
### 1. What is a "Type", and why do variables need it?

In Java, a variable acts like a named memory *container* that stores values during program execution. When a variable is **declared**, its associated data type must be specified. 
 
A variable's type tells the compiler:
- what **values** it can take,
- what **operations / type-checking** it can / should perform on it

Without knowing the type, the compiler can't do its job. That’s why Java is **`a statically typed language`**: **every variable must have a type known at compile time**.

### 2. Java has two main categories of types
#### I. Primitive Types (also called Value Types)

Primitive Data Types are atomic in the sense of not being composed of smaller parts. <font color = red>They are stored directly in stack memory</font> and are NOT instances of any class.

Java defines 8 built-in primitive types, each representing a specific kind of raw value:

| Category        | Types                        |
|:----------------|:-----------------------------|
| Integer         | byte, short, int, long       |
| Floating point  | float, double                |
| Character       | char                         |
| Boolean         | boolean                      |

Precision Ordering of Integer Types:
- **byte** (**8** bit signed integer) < **short** (**16**-bit signed integer) 
  
  < **int** (**32**-bit signed integer) < **long** (**64**-bit signed integer) 
  
  < **float** (32-bit floating point) < **double** (64-bit floating point)
- Note that just because *byte* or *short* uses less memory doesn't mean it's faster. On most systems, operations on *int* are more efficient, and smaller types might even be promoted to *int* during computation.

#### II. Reference Types (also called Object Types)
 <font color = red>Reference types store a memory address (reference) pointing to an object stored in heap memory.</font>

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


### 4. Understanding Object References in Java 
In Java, variables of class <font color = red>types</font> do NOT store the object itself, but rather a reference (pointer)** to the object in memory. 

#### (1) Declare Two Animal Variables
```java
Animal a, b;
```
We've declared two variables *a* and *b*. These are reference variables, but they do not yet point to any object — their value is null.
```
a ---> null
b ---> null
```

#### (2)  Instantiate an Animal Object
```java
a = new Animal();
```
- This creates a new Animal object on the heap.
- Variable *a* now holds a reference to the new Animal object.
- All fields are initialized to their default values (*0*, *null*, etc.).
```

a ---> [ species: null, name: null, age: 0 ]
b ---> null
```

#### (3) Assign Field Values
```java
a.species = "Cat";
a.name = "Oreo";
a.age = 4;
```
Now, the object referenced by *a* has updated fields.
```
a ---> [ species: "Cat", name: "Oreo", age: 4 ]
b ---> null
```

#### (4) Assign ```b = a```
```java
b = a;
```
Now, *b* also refers to the same object in memory that *a* points to. This is not a copy of the object — both *a* and *b* point to the same instance.
```
a ---> [ species: "Cat", name: "Oreo", age: 4 ]
        ^
        |
b ------
```

#### (5) Modify Through *b* 
```java
b.age = 5;
```
Since both *a* and *b* point to the same object, modifying the object through *b* also affects *a*.
```
a ---> [ species: "Cat", name: "Oreo", age: 5 ]
        ^
        |
b ------
```





*** 

## Scope
Understanding a variable's type is not sufficient to understand how it behaves in real programs.

Let's say we declare two variables with the same name - one inside a method, and one as a field in the class. Or, we declare a field in a subclass that has the same name as one in its superclass. Which variable does Java access? This is where the concpet of **scope** comes in.

A Variable's scope defines:
- **where** a variable is accessible
- **when** it is created and destroyed
- **which** variable gets used when multiple variables with the same name exist


By scope, Java variables fall into three main categories:
- Local Variables
- Instance (Member) Variables
- Static (Class) Variables

### 1. Local Variables
A local variable is declared <font color = red>WITHIN a method, constructor, or block (such as loops or if statements)</font>. Its scope is strictly confined to the enclosing block where it is declared, meaning it can only be accessed from the point of declaration until the end of that block.

| Aspect             | Description                                                                                                                                                         |
|:------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lifetime**       | Created when execution enters its defining block. <br>Automatically destroyed when control exits the block.                                                         |
| **Accessibility**  | Accessible only within its declared scope. <br>Not visible outside the block.                                                                                       |
| **Modifier**       | Cannot be declared with access modifiers (`public`, `private`, `protected`), as local variables are not part of the class-level API. <br>Can be declared `final` to prevent reassignment after initialization.              |
| **Storage**        | Stored in the **call stack** of the executing thread(as opposed to the heap for instance variables). <br>Each thread maintains its own copy; not shared across instances or threads.       |
| **Initialization** | **Must** be explicitly initialized before its first use. <br>**No default value** is assigned automatically (unlike instance or static variables).                      |


### 2. Instance (Member) Variables
An instance variable is declared <font color = red>WITHIN a class but OUTSIDE any method/constructor/block</font>. They define the **state** of an individual **object** and persist as long as the object exists in memory.

| Aspect             | Description                                                                                                                                                         |
|:------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lifetime**       | Created when an object is instantiated (i.e., via `new`) and exists as long as the object exists. <br>Destroyed when the object is garbage collected.              |
| **Accessibility**  | Depends on its access modifier — can be `public`, `private`, `protected`, or package-private (default).                                                            |
| **Modifier**       | Can be declared with access modifiers (`public`, `private`, `protected`). <br>Can also be declared `final` to ensure it is assigned only once.                     |
| **Storage**        | Stored in the **heap memory** as part of the object. <br>Each instance of the class has its own copy of the variable.                                               |
| **Initialization** | Automatically initialized with a **default value** if not explicitly assigned (e.g., `0` for `int`, `null` for reference types, `false` for `boolean`).            |


e.g.
```java
public class Test {

    int instanceVar; 

    public void demo() {
        int localVar; 

        // ✅ OK — instanceVar has a default value of 0
        System.out.println(instanceVar); 

        // ❌ Compile-time error — localVar must be explicitly initialized
        System.out.println(localVar);    
    }
}
```

- `instanceVar`
  - Instance variable (field), implicitly initialized to 0
  - Visible **throughout the entire class** (`Test`), as long as accessed through an object
- `localVar`
  - Local variable, not initialized by default
  - Only visible **within the method block** `demo()`


### 3. Static (Class) Variables
A static variable is declared <font color = red>with the `static` keyword</font>. It belongs to the class rather than any instance. It is shared across all objects of the class.

| Aspect             | Description                                                                                                                                                                         |
|:------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Lifetime**       | Created when the class is **loaded by the JVM** (typically on first reference). <br>Destroyed when the class is unloaded or when the JVM shuts down.                              |
| **Accessibility**  | Controlled by access modifiers: `public`, `private`, `protected`, or package-private (default). <br>**Best practice**: declare `private` and expose via static getter/setter.     |
| **Modifier**       | Must be declared with the `static` keyword. <br>Often combined with `final` for constants, e.g., `public static final double PI = 3.14`.                                            |
| **Storage**        | Stored in the **method area** (JVM metaspace). <br>Only **ONE copy exists per class**, shared across all instances and threads.              |
| **Initialization** | Automatically initialized with **default values** (e.g., `0`, `false`, `null`). <br>Explicit initialization is recommended for clarity and control.                                |


*** 
## Variable Shadowing v.s. Variable Hiding
### 1. Variable Shadowing
Shadowing occurs when <font color = red>a local variable</font>(declared within a method/constructor/block) or <font color = red>a method parameter</font> shares the same name as <font color = red>an instance or static field</font> in the same class.

<font color = red>In that local scope, the instance/static variable is shadowed</font> - its name is hidden in name resolution and can only be accessed explicitly: 
  - Use `this.fieldName` to access the shadowed instance field.
  - Use `ClassName.fieldName` to access the shadowed static field.

e.g. 
```java
public class VariableShadowingDemo {
    public static void main(String[] args) {
        Triangle triangle1 = new Triangle();
        Triangle.setSides(triangle1, 3, 4, 5);
        int result1 = triangle1.compute();
        System.out.println("Computed sum (triangle1) = " + result1);

        Triangle triangle2 = new Triangle();
        Triangle.setSides(triangle2, 6, 8, 10);
        int result2 = triangle2.compute();
        System.out.println("Computed sum (triangle2) = " + result2);

        // Access static field
        System.out.println("Total Triangle objects created: " + Triangle.unitCount);
    }
}


class Triangle {
    int a, b, c; // Instance variables
    static int unitCount = 0; // Static variable shared across all Triangle instances

    /**
     * Sets the sides of the given triangle.
     * Demonstrates how method parameters can shadow instance variables.
     * Also shows how a local variable can shadow a static field.
     */
    static void setSides(Triangle t, int a, int b, int c) {
        // Method parameters 'a', 'b', 'c' shadow the instance fields 't.a', 't.b', 't.c'
        t.a = a;
        t.b = b;
        t.c = c;

        // Example of shadowing a static variable (⚠️ not recommended)
        int unitCount = 7; // This local variable shadows the static field 'Triangle.unitCount'

        // To increment the static field, we must qualify it using the class name
        Triangle.unitCount++;
    }

    /**
     * Computes the sum of the three sides.
     * Demonstrates shadowing of an instance field by a local variable.
     */
    int compute() {
        int b = this.b + 1; // Local variable 'b' shadows the instance variable 'this.b'
        return a + b + c;   // Uses instance 'a' and 'c', and local 'b'
    }
}
```
```
Output:
Computed sum (triangle1) = 13
Computed sum (triangle2) = 25
Total Triangle objects created: 2
```

### 2. Variable Hiding 
Hiding occurs when <font color = red>a subclass</font> declares a field with the same name as one in its <font color = red>superclass</font>. 

Unlike methods, fields in Java are NOT polymorphic — <font color = red>the superclass field is not overridden, but rather hidden</font>. 

Which field is accessed **depends on the declared reference type**, NOT the runtime object. i.e., if we try to access the variable from the parent's reference by holding the child's object, it will be accessed from the parent class.

  - To access the hidden superclass field: use `super.fieldName`.
  - To access the subclass field: cast the reference to the subclass type if necessary.

e.g.
```java
class Animal {
    String name;
    boolean isDomestic;
}

class Cat extends Animal {
    String name;         // hides Animal.name
    String isDomestic;   // hides Animal.isDomestic
}


public class Main {
    public static void main(String[] args) {
        Cat cat = new Cat();
        Animal animal= cat;

        // Scenario 1
        cat.name = "Kitty";
        System.out.println(cat.name);       // Cat's field
        System.out.println(animal.name); // Animal's field

        // Scenario 2
        animal.name = "Whiskers";
        System.out.println(cat.name);       // Cat's field remains unchanged
        System.out.println(animal.name); // Animal's field changed

        // Scenario 3
        cat.isDomestic = "yes";
        animal.isDomestic = true;

        System.out.println(cat.isDomestic);      // Cat's field (String)
        System.out.println(animal.isDomestic); // Animal's field (boolean)
    }
}
```

```
Output:
Kitty
null

Kitty
Whiskers

yes
true
```

```java
Cat cat = new Cat();
Animal animal = cat;
```

```
References:

  cat        ─────┐
  animal     ─────┘ ——>  both point to the same Cat object

╔═══════════════════════════════════════╗
║                 Object: Cat           ║
║────────────────────────────────────── ║
║               |  name      isDomestic ║
║ Animal part   |  null      false      ║
║ Cat part      |  null      null       ║
╚═══════════════════════════════════════╝
```

```java
// Scenario 1
cat.name = "Kitty";
System.out.println(cat.name);       // "Kitty"
System.out.println(animal.name);   // null
```
```

References:
  cat        ─────┐
  animal     ─────┘ ——>  both point to the same Cat object

╔═══════════════════════════════════════╗
║                 Object: Cat           ║
║───────────────────────────────────────║
║               |  name      isDomestic ║
║ Animal part   |  null      false      ║
║ Cat part      |  "Kitty"   null       ║
╚═══════════════════════════════════════╝
```

```java
// Scenario 2
animal.name = "Whiskers";
System.out.println(cat.name);       // "Kitty"
System.out.println(animal.name); // "Whiskers"
```
```
References:
  cat        ─────┐
  animal     ─────┘ ——>  both point to the same Cat object

╔═════════════════════════════════════════╗
║                 Object: Cat             ║
║─────────────────────────────────────────║
║               |  name        isDomestic ║
║ Animal part   |  "Whiskers"  false      ║
║ Cat part      |  "Kitty"     null       ║
╚═════════════════════════════════════════╝
```
```java
// Scenario 3
cat.isDomestic = "yes";
animal.isDomestic = true;

System.out.println(cat.isDomestic);      // "yes"
System.out.println(animalRef.isDomestic); // true
```

```
References:
  cat        ─────┐
  animal     ─────┘ ——>  both point to the same Cat object

╔═════════════════════════════════════════╗
║                 Object: Cat             ║
║─────────────────────────────────────────║
║               |  name        isDomestic ║
║ Animal part   |  "Whiskers"  true       ║
║ Cat part      |  "Kitty"     "yes"      ║
╚═════════════════════════════════════════╝
```

In all scenarios, both `animal` and `cat` refer to the **same runtime object**, an instance of the `Cat` class. However, **field access in Java is statically bound** - the compiler resolves which field to access based on the **declared type of the reference**, **NOT the actual type of the object**.

As a result:
- `animal.name` accesses the name field defined in the `Animal` class
- `cat.name` accesses the name field declared in the `Cat` subclass