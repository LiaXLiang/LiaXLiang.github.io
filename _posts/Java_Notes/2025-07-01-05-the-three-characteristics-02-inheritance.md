---
title: The Three Characteristics of Java - 02. Inheritance
layout: post
---
## Intuition: The Human Analogy
Every person is descended from someone else. 

We *inherit* certain characteristics from our parents and *extend* them with traits of our own. Inheritance lets us quickly classify living organisms—species, genera, families, and so on—without restating the same biological facts for every single creature.

Object-oriented programming borrows this idea. A `Student` or an `OfficeWorker` can inherit from a common `Person` class (*name*, *age*, etc.), while a `Dog` or a `Cat` can inherit from an `Animal` class (*breathe*, *hunt*, …). Each subclass adds behaviour that is specific to its role — `students` *attend lectures*, `office workers` *receive salaries* — without rewriting the fundamentals of “being alive” or “being human.”

## Single Inheritance
### 1. Class-Level Inheritance (Compile-Time Perspective)
- (1) Single inheritance rule 
    
     In Java every class (except `java.lang.Object`) has exactly ONE direct superclass.

     ```java
     class Child extends Parent { … }   // only one name allowed after extends
     ```

- (2) *is-a* relationship
  
  A **subclass instance** is a specialised instance of its superclass; therefore it automatically acquires the superclass’s **non-private** state (fields) and behaviour (methods). The subclass may define additional state or behaviour, but it never loses what it inherited.

- (3) Usage 
    
    After compilation there is no syntactic difference between invoking an inherited method and a method declared locally in the subclass; both are called in exactly the same way.


### 2.  Object-Level Inheritance (Run-Time Perspective)
- (1) Construction Order

    When an object is instantiated in Java, the constructor chain is executed in a strict **top-down** order along the inheritance hierarchy. The process ensures that all superclass state is fully initialized before subclass-specific logic is executed.

    - The JVM starts with the root class Object
    - It then traverses the inheritance chain downward, one class at a time
    - At each level, the corresponding constructor is invoked (either **explicitly** via `super(...)` or **implicitly**)


        ```java
        Object   →  Animal   →  Cat              
        // executed top-to-bottom
        ```

- (2) Up-casting ( “pretending to be a parent” )
  
  Because every `Cat` is-a `Animal`, a reference of type `Animal` can safely point to a `Cat`. No cast is required:

    ```java
    class Main{
        public static void main(String[] args){
        
            // Usage is syntactically identical
            new Cat().sleep();   // Inherited
            new Cat().meow();  // Declared


            Animal oreo = new Cat();  // implicit up-cast
            oreo.sleep();  // Output: zzzzzzz
        }
    }

    class Animal{
        public void sleep() {
            System.out.println("zzzzzzz");
        }
    } 

    class Cat extends Animal{
        public void meow() { 
            System.out.println("Meow"); 
        }
    }
    ```
    The reference type (`Animal`) dictates which members are visible at compile time, even though the underlying object is still a `Cat`.

- (3) Constructors Are Not Inherited
    
    Constructors are **excluded** from inheritance because their names must match the class they construct.
    
     Nonetheless, every subclass **constructor—explicit** or **compiler-generated**—must invoke a superclass constructor (`super(...)`) as its very first action, establishing the object chain. 
     
     If NO call to `super(...)` is written **explicitly**, the compiler **automatically** inserts a call to the **no-argument constructor of the superclass**.

    ```java
    class Main{
        public static void main(String[] args){
            Animal oreo = new Cat();
        }
    }

    class Animal{
        Animal(String name) {
            System.out.println("Animal constructor: " + name);
        }
    } 

    class Cat extends Animal{
        Cat() {
            super("Cat"); // must explicitly call a superclass constructor
            System.out.println("Cat constructor");
        }
    }
    ```

    ```
    Output:
    Animal constructor: Cat
    Cat constructor
    ```



## Complementary Mechanisms for Code Reuse
Although we cannot extend two classes at once, Java provides three complementary techniques that together cover most use-cases sometimes labelled “multiple inheritance.”

### 1. Achieving Multiple Inheritance Effect via Inner Classes
```

      +-----------+           +-----------+
      |  Class B  |           |  Class C  |
      +-----------+           +-----------+
           ▲                       ▲
           │                       │
  +----------------------------------------+
  |        │       Class A         │       |
  |--------│-----------------------│-------|
  |  Inner Class B1|     |  Inner Class C1 |
  |  (extends B)   |     |   (extends C)   |
  +----------------------------------------+
```
  - `Class A` is the outer class that contains two inner classes: `InnerB1` and `InnerC1`
  - `InnerB1` extends `Class B`
  - `InnerC1` extends `Class C`
  - This allows `Class A` to *modularly* leverage multiple inheritance indirectly, even though Java does not allow multiple inheritance for outer classes.


### 2. Achieving Multiple Inheritance Effect via Multilevel Inheritance
```

       +-----------+
       |  Class A  |
       +-----------+
             ▲
             │
       +-----------+
       |  Class B  |
       +-----------+
             ▲
             │
       +-----------+
       |  Class C  |
       +-----------+

```
Each level adds or overrides behaviour, and the deepest descendant inherits the combined API of the whole chain. Because every link obeys single inheritance, Java’s rules stay simple.

### 3. Achieving Multiple Inheritance Effect via Interfaces
A class may implements **many** *interfaces* (and an *interface* may itself extends multiple *interfaces*) using the `implements` keyword.

#### What is an Interface? 
An interface in Java is a pure **abstract** type—a blueprint of a class—that specifies method signatures without providing implementations. It defines a set of expected behaviors that any implementing class must fulfill.