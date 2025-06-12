
### Analogy: Animals in the Zoo
Let's say we visit a zoo. We see a *cat*, a *dog*, and a *rabbit*. These are actural animals we can touch - they are **objects**. But when we describe what we saw, we might just say:" I saw some *animals*." The word "*animal*" is abstract - it refers to the concept or type, not a specific instance that we can point to. In Java, that abstract idea is represented by a **class**. A class is a blueprint to create an object.

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
- **Constructor**  
  - `Animal()` is a **default constructor**, automatically provided by the Java compiler if not explicitly written.

### Instantiating Objects 
Standard way: via a parameterized constructor

e.g.
```java
public class Animal {
    private String name;
    private int age;

    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

Animal animal = new Animal("Oreo", 4);
```

### Viewing Classes from the Perspective of Data Types
From the perspective of *data types*, a **class** in Java can be seen as a **user-defined composite data type**. It achieves this by encapsulating other data types (both *primitive* and *class* types) as its own fields, thereby defining a new, more complex data structure.

