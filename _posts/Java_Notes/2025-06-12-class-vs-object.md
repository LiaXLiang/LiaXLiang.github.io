
### I. Analogy: Animals in the Zoo
Let's say we visit a zoo. We see a *cat*, a *dog*, and a *rabbit*. These are actural animals we can touch - they are **objects**. But when we describe what we saw, we might just say: "I saw some *animals*." The word "*animal*" is abstract - it refers to the concept or type, not a specific instance that we can point to. In Java, that abstract idea is represented by a **class**. **`A class is a blueprint to create an object.`**

### II. Viewing Classes from the Perspective of Data Types
From the perspective of *data types*, **`a class in Java can be seen as a user-defined composite data type`**. It achieves this by encapsulating other data types (both *primitive* and *class* <font color = red>types</font>) as its own fields, thereby defining a new, more complex data structure.

***

### Defining a Class
A Class defines:
- **State** —— **Fields**
  - the properties an object holds (e.g., name, age, species)
- **Behaviour** —— **Methods**
  - the actions the object can perform (e.g., eat, sleep, hunt)
- **Construction** —— **Constructor**
  - how an object is created (via *Constructors*)    

```java
public class Animal {
    private String species;
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
  -  *species*, *name* and *age* represent the **state** of an animal. These are also called **member variables** or **instance variables.** They do **NOT** occupy memory at compile time. Only when we instantiate the class (i.e., create an actual animal object), memory is allocated.
- **Methods**
  - `eat()`, `sleep()`, and `hunt()` define the **behavious** of the animal.
- **Constructor**  
  - `Animal()` is a **default constructor**, automatically provided by the Java compiler if not explicitly written.

### Instantiating Objects 
Standard way: via a parameterized constructor

e.g.
```java
public class Animal {
    private String species;
    private String name;
    private int age;

    public Animal(String species, String name, int age) {
        this.species = species;
        this.name = name;
        this.age = age;
    }
}

Animal animal = new Animal("Cat","Oreo", 4);
```


***
### Understanding Object References in Java 
In Java, **variables of class <font color = red>types</font>) do NOT store the object itself, but rather a reference (pointer)** to the object in memory. 

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