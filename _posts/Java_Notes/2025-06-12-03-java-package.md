### Intro
In collaborative software development, it's common for different developers to create classes with the same name. For example:
- Developer Alice writes a class `Cat`
- Developer Bob also writes a class `Cat`
- Developer Charlie wants to use both versions of class `Cat`

Or consider this case:
- Developer David creates a custom `Collections` class.
- However, Java already provides a built-in `Collections` class in the `java.util` package.

Java uses **packages** to resolve these naming conflicts to eliminate ambiguity.

### I. What Is a Package?
A **package** in Java is a **namespace** that organizes a set of related *classes* and *interfaces*. Every class belongs to a package. While class names like `Cat` or `Dog` may be common, the **fully qualified class name** includes the **package path**, making it unique. 

e.g.
| Developer | Class Name  | Package Path    | Fully Qualified Class Name     |
|-----------|-------------|-----------------|--------------------------------|
| Alice     | Cat         | dev.alice       | dev.alice.Cat                  |
| Bob       | Cat         | dev.bob         | dev.bob.Cat                    |
| David     | Collections | custom.tools    | custom.tools.Collections       |
| JDK       | Collections | java.util       | java.util.Collections          |

### II. Declaring Packages in Java
To assign a *class* to a *package*, declare the *package* at the top of the file.

```Cat.java``` by Developer Alice:
```java
package dev.alice;

public class Cat {
    public void meow() {
        System.out.println("Meow");
    }
}
```

```Cat.java``` by Developer Bob:
```java
package dev.bob;

public class Cat {
    public void meow() {
        System.out.println("Meow");
    }
}
```

```Collections.java``` by Developer David:
```java
package custom.tools;

public class Collections {
    // custom implementation
}
```
Now the **JVM** distinguishes these classes by their fully qualified names: `dev.alice.Cat`, `dev.bob.Cat`, `custom.tools.Collections`, and `java.util.Collections`.

### III. Directory Structure and Compilation
The directory hierarchy should reflect the package structure. For example:
```

project_root/
└── src/
    ├── dev/
    │   ├── alice/
    │   │   └── Cat.java
    │   └── bob/
    │       └── Cat.java
    └── custom/
        └── tools/
            └── Collections.java
```
If we omit the package declaration, the class belongs to the **default package**. This is strongly discouraged.

### III. Package Visibility 
1. A class *method* or *field* with NO modifier (not `public`, `protected`, or `private`) is package-private — accessible only within the same package.

    ```java
    package animals;

    public class Dog {
        void bark() {
            System.out.println("Woof!");
        }
    }
    ```
    ```java
    package animals;

    public class Main {
        public static void main(String[] args) {
            Dog d = new Dog();
            d.bark(); // OK: Same package
        }
    }
    ```
    But if `Main` is in a different package, `bark()` will NOT be accessible.

2. Importing Classes

    To use classes from other packages, we can either: 
    - Use the fully qualified name:
    
        ```java
        package dev.alice;

        public class Rabbit {
            public void hop() {
                custom.tools.Collections utils = new custom.tools.Collections();
            }
        }
        ```
    - Use `import`
        ```java
        package dev.alice;

        import custom.tools.Collections;

        public class Rabbit {
            public void hop() {
                Collections utils = new Collections();
            }
        }
        ``` 
3. How Java Resolves Class Names
   
    When the compiler encounters a class name like `Cat`, it checks in this order:
    - The current package.

    - All explicitly imported classes.

    - The `java.lang` package (automatically imported).

    If the class is not found in any of these, we get a compilation error.

