# COM4008 Programming Concepts: Introduction to Java

This content is designed as five linked VLE information pages. Lecture 13 introduces the Java language and platform by connecting new syntax to programming concepts already encountered in Python.

---

# 13.1 Java, Bytecode and the JVM

## On this page

- The origins and purpose of Java
- Portability and automatic memory management
- Source code, bytecode and machine code
- Compilation and runtime execution
- The JVM, JDK and Java API
- Preparing a Java development environment

## Learning outcomes

By the end of this page, you should be able to:

- summarise why Java was designed;
- distinguish Java source, bytecode and native machine instructions;
- explain the role of `javac`, the JVM and just-in-time compilation;
- distinguish the JDK from the JVM and Java API;
- verify that a Java development environment is available;
- compare Java's execution model with the simplified Python model used earlier in the module.

## Different language, same concepts

You already understand values, variables, selection, iteration, collections, functions and objects. Java expresses the same broad programming concepts with different rules and syntax.

Learning a second language helps separate:

- the **concept**—for example, repetition;
- from one language's **expression** of it—for example, Python indentation or Java braces.

The objective is not to translate every Python character mechanically. It is to recognise familiar ideas and learn Java's conventions.

## Where Java came from

Java was designed at Sun Microsystems by a team led by James Gosling in the early 1990s. The project sought a language suitable for software running across different devices, with fewer of the memory-management and portability difficulties associated with lower-level development.

Java was publicly announced in 1995, and JDK 1.0 followed in 1996. Sun Microsystems was later acquired by Oracle in 2010.

Important design themes include:

- object-oriented organisation;
- strong compile-time checks;
- portability through a defined virtual-machine platform;
- automatic garbage collection;
- a large standard API;
- support for concurrent and networked programs.

Historical popularity claims change over time. The more durable reason for studying Java is that it demonstrates a widely used statically typed, class-based approach and supports substantial desktop, server and mobile ecosystems.

## Java is statically typed

In Java, a variable normally has a declared type that the compiler checks:

```java
int score = 100;
String playerName = "Aisha";
```

Python associates a type with the current object/value and does not normally require a variable declaration:

```python
score = 100
player_name = "Aisha"
```

Static typing allows many incompatible operations to be detected before the program begins running. It also means Java code contains more explicit type information.

## From source code to execution

A traditional Java workflow has two visible stages:

```text
Hello.java
   │
   │ javac compiles source
   ▼
Hello.class (Java bytecode)
   │
   │ java starts a JVM and loads the class
   ▼
program executes on the current platform
```

### Java source

Human-readable Java source is normally stored in a `.java` file.

### Bytecode

`javac` translates source into Java bytecode, normally stored in a `.class` file. Bytecode is an instruction format defined for the Java Virtual Machine rather than for one particular processor.

### Runtime execution

The `java` launcher starts a JVM, loads the required class and invokes its entry point. A modern JVM can interpret bytecode and compile frequently executed code into native machine instructions using a just-in-time compiler.

It is therefore too simplistic to call Java only compiled or only interpreted. Compilation and runtime execution work together.

## Portability

The same compatible bytecode can run on different systems that provide a suitable JVM:

```text
                     ┌─ JVM for Windows ─→ Windows instructions
Java bytecode ───────┼─ JVM for macOS   ─→ macOS instructions
                     └─ JVM for Linux   ─→ Linux instructions
```

This supports the phrase “write once, run anywhere”, but portability is not automatic in every program. Platform-specific libraries, file paths, native code and environmental assumptions can still reduce portability.

## Automatic memory management

Java allocates objects in managed memory. The garbage collector can reclaim objects that are no longer reachable by the program.

This removes the need for ordinary Java code to manually free most object memory. It does not prevent every resource problem: files, network connections and other external resources still need deliberate closing, and retaining unwanted references can still consume memory.

## JVM, JDK and API

| Term | Meaning | Learner-focused role |
|---|---|---|
| JVM | Java Virtual Machine | Loads and executes Java bytecode |
| JDK | Java Development Kit | Provides the runtime plus development tools such as `javac`, `java` and `javadoc` |
| Java API | Standard classes and interfaces | Supplies reusable facilities such as strings, collections and input/output |
| JRE | Java Runtime Environment | A historical/common term for a runtime without development tools; modern development normally begins by installing a JDK |
| IDE | Integrated Development Environment | Helps edit, compile, run and debug code |

Install the JDK version specified for the module rather than choosing different versions independently. This avoids language and project compatibility differences.

## Verify the environment

In a terminal:

```text
java --version
javac --version
```

Both commands should report a version. If `java` works but `javac` does not, a complete JDK may be missing or the command path may be configured incorrectly.

An IDE can automate compilation and running, but understanding the two commands makes error messages and project configuration less mysterious.

## Java and Python execution: a careful comparison

| Java | Python |
|---|---|
| Source is statically checked and normally compiled to JVM bytecode | Source is normally compiled internally to Python bytecode and executed by a Python implementation |
| `javac` compilation is commonly visible to the developer | Compilation is commonly hidden from the developer |
| JVM is the defined execution platform for Java bytecode | CPython's virtual machine is the most common Python implementation, but it is not the Java JVM |
| Variable types are normally declared | Variable names do not normally include declared types |

Both descriptions are simplified. The important point is that “compiled” and “interpreted” are not mutually exclusive labels for modern language implementations.

## Pause and sequence the stages

Put these items into a sensible order:

- JVM starts;
- developer saves `Hello.java`;
- `javac` checks and compiles the source;
- operating system executes native instructions;
- JVM loads `Hello.class`;
- bytecode is produced;
- frequently executed code may be just-in-time compiled.

Which stages happen once during development, and which happen each time the application is launched?

## Common mistakes

- **Calling Java only interpreted:** modern JVMs also use just-in-time compilation.
- **Calling bytecode native machine code:** bytecode targets the JVM instruction set.
- **Confusing JVM and JDK:** one executes bytecode; the other supplies the development environment and tools.
- **Installing only a runtime:** learners need `javac`, so they need a JDK.
- **Assuming portability means identical behaviour everywhere:** dependencies and operating-system assumptions still matter.
- **Treating garbage collection as complete resource management:** external resources still need closing.
- **Assuming Python performs no compilation:** common Python implementations also use an intermediate bytecode internally.
- **Choosing an arbitrary JDK version:** use the module's supported version.

## Check your understanding

1. What problem did Java's virtual-machine approach help address?
2. What does `javac` produce?
3. What happens when the `java` launcher runs a class?
4. How do the JDK and JVM differ?
5. Why is Java neither simply “compiled” nor simply “interpreted”?
6. What limitation applies to the phrase “write once, run anywhere”?

## Apply your learning

1. Run `java --version` and `javac --version` and record the results.
2. Draw the journey from `.java` source to a running application.
3. Explain bytecode to a learner who already understands Python source files.
4. Classify five Java terms: language, tool, file format, runtime or library/API.
5. Identify one portability risk in a program that reads files.
6. Compare Java's type declaration with an equivalent Python assignment.

## Page summary

Java is a statically typed, class-based language supported by the Java platform. `javac` compiles source into JVM bytecode, while the `java` launcher starts a JVM that loads and executes the program, potentially using interpretation and just-in-time compilation. A JDK provides the tools needed to develop as well as run Java applications.

**Next:** Continue to **13.2 Your First Java Program and Input/Output**.

---

# 13.2 Your First Java Program and Input/Output

## On this page

- The structure of a Java source file
- Classes and the `main` method
- Compiling and running a program
- Output with `System.out`
- Input with `Scanner`
- Syntax, formatting and comments
- Comparing a first Java program with Python

## Learning outcomes

By the end of this page, you should be able to:

- create a correctly named Java source file;
- explain the role of the class and `main` method;
- compile and launch a small Java program;
- produce formatted output;
- read text and numerical input safely;
- recognise braces, semicolons and case sensitivity;
- write ordinary and documentation comments.

## Hello, World

Create a file named `Hello.java`:

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Compile it:

```text
javac Hello.java
```

If compilation succeeds, the directory contains `Hello.class`. Run the class name without a file extension:

```text
java Hello
```

Modern Java can also launch a simple source file directly:

```text
java Hello.java
```

The explicit `javac` then `java` sequence remains useful because it makes the compile and run stages visible.

## Read the program from the outside in

```java
public class Hello {
```

The public class is named `Hello`, matching `Hello.java`. Java is case-sensitive: `Hello`, `hello` and `HELLO` are different identifiers.

```java
public static void main(String[] args) {
```

This declares the conventional application entry point:

- `public`: the launcher can access it;
- `static`: it belongs to the class, so no `Hello` object is needed first;
- `void`: it does not return a value;
- `main`: the recognised entry-point name;
- `String[] args`: an array containing command-line arguments.

You do not need to memorise every keyword instantly. Begin by recognising the pattern and gradually connect it to classes, methods and arrays.

## Java and Python comparison

Java:

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Python:

```python
def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
```

The Python guard is a useful convention but is not required for every small Python script. Java's class and `main` method reflect the language and launcher structure.

## Braces, semicolons and indentation

Java uses braces to mark blocks:

```java
if (score >= 50) {
    System.out.println("Pass");
}
```

Many statements end with a semicolon. Indentation is not what defines the block, but consistent indentation is still essential for readability.

Python uses indentation as part of its grammar:

```python
if score >= 50:
    print("Pass")
```

## Output

`println()` adds a line break:

```java
System.out.println("First line");
System.out.println("Second line");
```

`print()` does not:

```java
System.out.print("Name: ");
System.out.println("Aisha");
```

Concatenate values with `+`:

```java
int score = 75;
System.out.println("Score: " + score);
```

Formatted output is also available:

```java
double average = 72.456;
System.out.printf("Average: %.2f%n", average);
```

`%n` requests a platform-appropriate line separator.

## Text input with Scanner

Import `Scanner` above the class:

```java
import java.util.Scanner;
```

Then create and use one scanner:

```java
public class InputExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        System.out.println("Hello, " + name + "!");

        scanner.close();
    }
}
```

`new Scanner(System.in)` constructs an object that reads standard input. `nextLine()` returns a `String` containing the entered line.

## Numerical input

One robust introductory pattern is to read a line, then convert it:

```java
System.out.print("Enter your age: ");
int age = Integer.parseInt(scanner.nextLine());
```

This mirrors the Python pattern:

```python
age = int(input("Enter your age: "))
```

If the text is not a valid integer, Java throws `NumberFormatException`. Validation and exception handling can be added when needed.

`Scanner` also has methods such as `nextInt()` and `nextDouble()`. Mixing them with `nextLine()` requires care because the line-ending character may remain unread. Consistently reading lines and parsing them avoids that common first-program surprise.

## Comments

Single-line comment:

```java
// Explain why this value is required.
```

Block comment:

```java
/*
 * A comment spanning several lines.
 */
```

Javadoc comment:

```java
/**
 * Calculates the area of a rectangle.
 *
 * @param width rectangle width
 * @param height rectangle height
 * @return calculated area
 */
public static double area(double width, double height) {
    return width * height;
}
```

Javadoc comments can be processed by the `javadoc` tool to produce API documentation. Use them for public classes and methods whose purpose, parameters or return values need explanation—not as commentary for every obvious line.

## Compiler errors and runtime errors

A missing semicolon or unmatched brace is normally reported during compilation. Invalid numerical input may compile successfully but fail while running.

When an error occurs:

1. identify whether it came from `javac` or `java`;
2. read the first relevant message and line number;
3. inspect the surrounding statement and earlier braces;
4. make one focused change;
5. compile again before running.

## Pause and annotate

Annotate each part of:

```java
public static void main(String[] args)
```

Then predict what files or output exist after each command:

```text
javac Hello.java
java Hello
java Hello.class
```

Which final command is incorrect, and why?

## Common mistakes

- **Class and filename do not match:** `public class Hello` belongs in `Hello.java`.
- **Case differs:** Java identifiers and filenames are case-sensitive.
- **Running `java Hello.class`:** pass the class name, not the filename extension.
- **Missing semicolons or braces:** check the compiler's first useful line number.
- **Using Python's `print()`:** Java console output uses `System.out`.
- **Forgetting to import `Scanner`:** it belongs to `java.util`.
- **Creating several scanners for `System.in`:** normally reuse one scanner.
- **Mixing `nextInt()` and `nextLine()` without understanding the remaining newline:** line-based parsing is simpler initially.
- **Closing the scanner before the final input:** subsequent reads cannot occur.
- **Commenting what the code already says:** explain intention, assumptions and public behaviour.

## Check your understanding

1. Why should the source filename match the public class?
2. What is the role of `main`?
3. How do `print()` and `println()` differ in Java?
4. What does `new Scanner(System.in)` create?
5. Why might line-based numerical parsing be simpler?
6. What is special about a Javadoc comment?

## Apply your learning

1. Create, compile and run `Hello.java`.
2. Change the output and observe when the `.class` file changes.
3. Ask for a learner's name and print a greeting.
4. Read two rectangle dimensions and display area and perimeter.
5. Use `printf()` to show a decimal result to two places.
6. Add a Javadoc comment to a calculation method.
7. Deliberately create one compiler error and one input conversion error; record how their reports differ.

## Page summary

A traditional Java application begins in a public class containing `public static void main(String[] args)`. `javac` compiles the source and `java` launches the class. Braces define blocks, statements commonly end in semicolons, `System.out` produces console output and `Scanner` can read input. Comments and Javadoc document purpose and public behaviour.

**Previous:** Return to **13.1 Java, Bytecode and the JVM**.  
**Next:** Continue to **13.3 Types, Strings, Control Flow and Methods**.

---

# 13.3 Types, Strings, Control Flow and Methods

## On this page

- Primitive and reference types
- Variables and constants
- Characters and immutable strings
- Value equality for strings
- Selection with `if` and `switch`
- Iteration with `for`, enhanced `for`, `while` and `do-while`
- Java methods compared with Python functions

## Learning outcomes

By the end of this page, you should be able to:

- declare and initialise variables using suitable Java types;
- distinguish primitive values from object references at an introductory level;
- compare strings by content;
- write selection and repetition constructs;
- choose between common loop forms;
- declare and invoke a static method;
- recognise familiar programming concepts across Java and Python.

## Variables have declared types

```java
char grade = 'A';
String studentName = "Nick";
int mark = 78;
double average = 72.5;
boolean passed = true;
```

The declaration identifies a type, name and initial value:

```text
int mark = 78;
│   │      │
type name   value
```

Java convention uses `lowerCamelCase` for local variables and methods. Use meaningful names and avoid Java keywords.

## Primitive types

Java has eight primitive types:

| Type | Purpose | Example |
|---|---|---|
| `byte` | Very small integer | `byte level = 3;` |
| `short` | Small integer | `short year = 2026;` |
| `int` | Usual whole number | `int score = 100;` |
| `long` | Larger whole number | `long population = 8_000_000_000L;` |
| `float` | Single-precision decimal | `float speed = 2.5F;` |
| `double` | Usual decimal | `double average = 72.5;` |
| `char` | One UTF-16 code unit | `char grade = 'A';` |
| `boolean` | `true` or `false` | `boolean active = true;` |

`String` is not primitive. It is a class whose objects represent text.

Numeric range and precision matter. Choose `int` and `double` as sensible introductory defaults unless the problem requires something else.

## Assignment and compatibility

The compiler rejects an incompatible assignment:

```java
int score = 75;
score = "high"; // compilation error
```

Some widening numeric conversions happen automatically:

```java
int count = 5;
double measuredCount = count;
```

A narrowing conversion requires an explicit cast and may lose information:

```java
double average = 72.9;
int whole = (int) average; // 72
```

## Constants

Use `final` when a variable should be assigned once:

```java
final int MAX_MARK = 100;
final double PI = 3.141592653589793;
```

Constants commonly use `UPPER_SNAKE_CASE`. `final` prevents reassigning the variable; for an object reference, it does not automatically make the referenced object immutable.

Python relies mainly on naming convention:

```python
MAX_MARK = 100
```

## Characters and strings

Java distinguishes one `char` from a `String`:

```java
char initial = 'N';
String name = "Nick";
```

Single quotes represent a character; double quotes represent a string.

A `String` is immutable: operations that appear to change it produce another string object.

Useful methods and properties include:

```java
String course = "COM4008";

int length = course.length();
char first = course.charAt(0);
String lower = course.toLowerCase();
boolean startsCorrectly = course.startsWith("COM");
```

Valid indexes begin at zero and end at `length() - 1`.

## Compare strings with `equals()`

For primitives, `==` compares values:

```java
int first = 5;
int second = 5;
System.out.println(first == second); // true
```

For object references, `==` asks whether both references identify the same object. Compare string content with `equals()`:

```java
String enteredName = scanner.nextLine();

if (enteredName.equals("Nick")) {
    System.out.println("Name matched");
}
```

When a reference may be `null`, a known non-null string can call the method:

```java
if ("Nick".equals(enteredName)) {
    ...
}
```

Use `equalsIgnoreCase()` only when the requirement genuinely says case should not matter.

## Selection with `if`

Java:

```java
if (mark >= 70) {
    System.out.println("Distinction");
} else if (mark >= 40) {
    System.out.println("Pass");
} else {
    System.out.println("Not passed");
}
```

Python:

```python
if mark >= 70:
    print("Distinction")
elif mark >= 40:
    print("Pass")
else:
    print("Not passed")
```

Java uses `&&`, `||` and `!` for logical AND, OR and NOT.

## Selection with `switch`

`switch` can express selection based on one value:

```java
switch (grade) {
    case 'A':
        System.out.println("Excellent");
        break;
    case 'B':
    case 'C':
        System.out.println("Passed");
        break;
    default:
        System.out.println("Check the grade");
}
```

In this traditional form, `break` prevents execution falling through into the next case. Grouped cases can intentionally share one response.

Python's `match` statement can address similar multi-case selection, although the languages' pattern-matching capabilities are not identical.

## Conditional operator

The conditional operator is concise when selecting between two values:

```java
String outcome = mark >= 40 ? "Pass" : "Not passed";
```

Prefer an `if` statement when conditions or actions become difficult to read.

## Counting `for` loop

```java
for (int index = 0; index < 5; index++) {
    System.out.println(index);
}
```

The header contains:

1. initialisation: `int index = 0`;
2. continuation condition: `index < 5`;
3. update: `index++`.

Python commonly expresses the same count with `range()`:

```python
for index in range(5):
    print(index)
```

## Enhanced `for` loop

Use an enhanced loop when each value is needed and its index is not:

```java
int[] marks = {70, 75, 80};

for (int mark : marks) {
    System.out.println(mark);
}
```

This resembles Python's direct iteration:

```python
for mark in marks:
    print(mark)
```

## `while` and `do-while`

`while` tests before every iteration:

```java
while (attempts < 3) {
    attempts++;
}
```

`do-while` performs the body once before testing:

```java
String response;

do {
    System.out.print("Continue? (y/n): ");
    response = scanner.nextLine();
} while (response.equalsIgnoreCase("y"));
```

Python has no direct `do-while` syntax; a `while True` loop with a conditional `break` is a common equivalent.

## Methods in Java

Java functions are declared as methods inside a class:

```java
public static int square(int number) {
    return number * number;
}
```

Invoke it from another static method in the same class:

```java
int result = square(6);
System.out.println(result);
```

The method signature states:

- accessibility: `public`;
- whether it belongs to the class: `static`;
- return type: `int`;
- name: `square`;
- typed parameter: `int number`.

Python:

```python
def square(number):
    return number * number
```

The concept is familiar; Java makes types and class membership explicit.

## Pause and translate concepts

For each Java fragment, name the programming concept rather than only translating punctuation:

```java
final int MAX_ATTEMPTS = 3;
```

```java
for (String name : names) {
    System.out.println(name);
}
```

```java
if ("yes".equals(response)) {
    continueProgram();
}
```

Then write an equivalent Python fragment and identify one semantic difference.

## Common mistakes

- **Omitting the variable type:** Java declarations normally state it.
- **Using double quotes for `char`:** characters use single quotes.
- **Comparing strings with `==`:** use `equals()` for content.
- **Calling `length` instead of `length()`:** string length is a method; array length is a field.
- **Accessing index `length()`:** the final valid index is one less.
- **Writing Python logical words:** Java uses `&&`, `||` and `!`.
- **Forgetting `break` in a traditional `switch`:** unintended fall-through may occur.
- **Using an enhanced loop when an index is required:** choose a counting loop.
- **Assuming `do-while` might run zero times:** its body runs at least once.
- **Declaring a method outside a class:** Java methods belong to a class or other type.
- **Leaving out the return type:** use `void` explicitly when no value is returned.

## Check your understanding

1. What is the difference between a primitive type and `String`?
2. What does `final` prevent?
3. Why should strings normally be compared with `equals()`?
4. When is an enhanced `for` loop appropriate?
5. How do `while` and `do-while` differ?
6. What information does a Java method declaration include that a Python function often does not?

## Apply your learning

1. Declare variables representing a student's name, ID, average and active status.
2. Read two strings and compare their content correctly.
3. Classify a mark with an `if`/`else if` chain.
4. Use `switch` to respond to a menu choice or grade.
5. Print the values 1 to 10 with a counting loop.
6. Calculate the total of an integer array with an enhanced loop.
7. Write and invoke methods for rectangle area and perimeter.
8. Compare one solution with its Python equivalent and explain the conceptual similarities.

## Page summary

Java variables normally have declared types, primitive values follow defined representations, and `final` prevents reassignment. Strings are immutable objects and content comparison uses `equals()`. Familiar decisions and loops use braces and Java operators, while Java methods explicitly state parameter and return types and live inside classes.

**Previous:** Return to **13.2 Your First Java Program and Input/Output**.  
**Next:** Continue to **13.4 Arrays and the Collections Framework**.

---

# 13.4 Arrays and the Collections Framework

## On this page

- Fixed-size Java arrays
- Indexing and iteration
- Arrays compared with Python lists
- Generic collection types
- `ArrayList`
- `HashMap`
- Choosing an appropriate structure

## Learning outcomes

By the end of this page, you should be able to:

- create, access and update Java arrays;
- explain why an array's size is fixed;
- iterate over arrays safely;
- create a typed `ArrayList` and use its common methods;
- store and retrieve key-value entries in a `HashMap`;
- explain the role of generic type arguments;
- compare Java collections with Python lists and dictionaries.

## Java arrays

An array stores a fixed number of values of one declared component type:

```java
int[] marks = {70, 75, 80, 65};
```

Alternatively, allocate the size first:

```java
int[] marks = new int[4];

marks[0] = 70;
marks[1] = 75;
```

The remaining elements initially contain the default integer value `0`.

## Indexing and length

```java
int first = marks[0];
marks[2] = 82;
int numberOfMarks = marks.length;
```

Notice that array `length` has no parentheses. Valid indexes are from `0` to `marks.length - 1`.

A counting loop exposes indexes:

```java
for (int index = 0; index < marks.length; index++) {
    System.out.println(index + ": " + marks[index]);
}
```

An enhanced loop focuses on values:

```java
for (int mark : marks) {
    System.out.println(mark);
}
```

## Java arrays and Python lists

| Java array | Python list |
|---|---|
| Fixed length after creation | Can normally grow and shrink |
| One declared component type | Can contain references to different object types |
| Uses `.length` | Uses `len(list_name)` |
| Primitive arrays can store primitive values directly | Values are Python objects/references |

Java also has collection classes for dynamic data structures.

## The Collections Framework

The Java Collections Framework provides interfaces and classes for common structures, including:

- `List` and implementations such as `ArrayList` and `LinkedList`;
- `Set` and implementations such as `HashSet`;
- `Map` and implementations such as `HashMap`.

Program to the most appropriate abstraction when possible:

```java
List<String> names = new ArrayList<>();
```

The variable uses the `List` interface; the constructed object is an `ArrayList` implementation.

## Generic type arguments

Angle brackets identify the permitted element type:

```java
ArrayList<String> names = new ArrayList<>();
```

This allows the compiler to check additions and retrievals:

```java
names.add("Aisha");
String firstName = names.get(0);
```

Collections store objects, so primitive values use wrapper types:

```java
ArrayList<Integer> scores = new ArrayList<>();
scores.add(100);
```

Java automatically boxes the `int` into an `Integer` object here.

## ArrayList

Import the types:

```java
import java.util.ArrayList;
import java.util.List;
```

Create and modify a list:

```java
List<String> students = new ArrayList<>();

students.add("Aisha");
students.add("Charlie");
students.add("Sophie");

String first = students.get(0);
students.set(1, "Charles");
students.remove("Sophie");

System.out.println(students.size());
```

Common operations include:

| Operation | Purpose |
|---|---|
| `add(value)` | Append a value |
| `add(index, value)` | Insert at an index |
| `get(index)` | Retrieve a value |
| `set(index, value)` | Replace a value |
| `remove(index)` | Remove by index |
| `remove(value)` | Remove a matching object |
| `contains(value)` | Test membership |
| `size()` | Return the number of elements |
| `clear()` | Remove all elements |

For `ArrayList<Integer>`, `remove(1)` selects the index overload. To remove the value `1`, make the object intention explicit:

```java
scores.remove(Integer.valueOf(1));
```

## Iterate through an ArrayList

```java
for (String student : students) {
    System.out.println(student);
}
```

For objects:

```java
for (Student student : students) {
    if (student.getId() == soughtId) {
        return student;
    }
}

return null;
```

Returning `null` is an introductory approach to “not found”. Later designs may use `Optional<Student>` or another explicit result strategy.

## HashMap

A map stores associations between unique keys and values:

```java
import java.util.HashMap;
import java.util.Map;


Map<Integer, String> studentsById = new HashMap<>();

studentsById.put(1001, "Aisha");
studentsById.put(1002, "Charlie");

String name = studentsById.get(1001);
boolean known = studentsById.containsKey(1002);
studentsById.remove(1002);
```

If the application repeatedly finds students by ID, a map expresses that relationship more directly than scanning a list.

Iterate through entries:

```java
for (Map.Entry<Integer, String> entry : studentsById.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}
```

Hash-based collections use hash codes and equality to organise and find keys. Custom key classes therefore require consistent `equals()` and `hashCode()` implementations.

## Java and Python collection comparison

| Requirement | Java | Python |
|---|---|---|
| Fixed-size indexed values | Array | No exact everyday equivalent; tuple is immutable but semantically different |
| Dynamic ordered sequence | `ArrayList<T>` through `List<T>` | `list` |
| Unique values | `HashSet<T>` through `Set<T>` | `set` |
| Key-value association | `HashMap<K,V>` through `Map<K,V>` | `dict` |

The structures are comparable, not identical. Their APIs, type rules, equality behaviour and performance details differ.

## Choosing a structure

Ask:

- Is the number of elements fixed?
- Is order important?
- Are duplicates permitted?
- Is access primarily by numerical index or meaningful key?
- Will values be added and removed frequently?
- What type should every element or key/value have?

Choose from requirements rather than familiarity alone.

## Pause and choose

Choose a suitable Java structure for each case and justify it:

1. the twelve months of a year;
2. a playlist that can grow and preserve order;
3. unique module codes;
4. student records retrieved by student ID;
5. the last ten fixed sensor readings;
6. game objects that can appear and disappear.

## Common mistakes

- **Treating an array as dynamically resizable:** its length is fixed.
- **Using `length()` for an array:** arrays use `.length`; strings use `.length()`.
- **Using `size` for an ArrayList:** call `.size()`.
- **Accessing index equal to the size:** the last valid index is one less.
- **Omitting generic type arguments:** typed collections provide useful compiler checks.
- **Using primitive names in generics:** write `Integer`, not `int`.
- **Confusing `get()` and array indexing:** lists use methods; arrays use brackets.
- **Calling `remove(1)` on `ArrayList<Integer>` expecting value removal:** it normally selects index 1.
- **Choosing a list for repeated key lookup:** a map may express the requirement better.
- **Assuming Java and Python collection APIs are interchangeable:** compare concepts, then learn each API.

## Check your understanding

1. What is fixed about a Java array?
2. How do array, string and ArrayList length operations differ?
3. What does `<String>` mean in `ArrayList<String>`?
4. Why do generic collections use `Integer` rather than `int`?
5. When is a `HashMap` preferable to an `ArrayList`?
6. Why must custom map keys have consistent equality and hash behaviour?

## Apply your learning

1. Create an integer array and calculate its total and average.
2. Print an array with both counting and enhanced loops.
3. Create an `ArrayList<String>` and exercise `add`, `get`, `set` and `remove`.
4. Demonstrate removal by index and by value from an integer list.
5. Create a `HashMap<Integer, String>` of student IDs and names.
6. Retrieve, update and remove map entries.
7. Choose structures for three requirements from an earlier Python exercise and justify any different Java choices.

## Page summary

Java arrays store a fixed number of values of one component type. The Collections Framework provides generic structures such as `ArrayList`, `HashSet` and `HashMap` for dynamic requirements. Type arguments allow compile-time checks, while interfaces such as `List` and `Map` describe capabilities independently of one implementation.

**Previous:** Return to **13.3 Types, Strings, Control Flow and Methods**.  
**Next:** Continue to **13.5 Classes, Objects and the Wider Java Ecosystem**.

---

# 13.5 Classes, Objects and the Wider Java Ecosystem

## On this page

- Java classes and objects
- Encapsulation and constructors
- Instance methods
- Creating and using objects
- Inheritance and method overriding
- Java and Python OOP comparison
- Desktop, mobile and server-side Java

## Learning outcomes

By the end of this page, you should be able to:

- define a Java class with private fields;
- initialise objects through a constructor;
- expose behaviour through instance methods;
- create and use objects from another class;
- explain the basic purpose of `extends`, `super` and overriding;
- compare Java and Python class syntax;
- recognise several directions in the wider Java ecosystem.

## A Student class

Create `Student.java`:

```java
public class Student {
    private int id;
    private String name;

    public Student(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void printDetails() {
        System.out.println(id + ": " + name);
    }
}
```

The class groups student state and behaviour.

## Encapsulation

The fields are `private`, so unrelated code cannot directly assign them. Public methods provide a controlled interface.

Encapsulation is not merely adding getters and setters to everything. The class should protect its rules. For example:

```java
public void setName(String name) {
    if (name == null || name.isBlank()) {
        throw new IllegalArgumentException("Name cannot be blank");
    }

    this.name = name;
}
```

The constructor should establish valid initial state too.

## Constructor and `this`

```java
public Student(int id, String name) {
    this.id = id;
    this.name = name;
}
```

The constructor has the same name as the class and no return type. `this.id` refers to the current object's field; `id` refers to the parameter.

## Create and use an object

Create `Program.java`:

```java
public class Program {
    public static void main(String[] args) {
        Student student = new Student(1234, "Aisha");

        student.printDetails();
        student.setName("Aisha Khan");

        System.out.println(student.getName());
    }
}
```

The declaration can be read as:

```text
Student student = new Student(1234, "Aisha");
│       │         │   └─ constructor call
│       │         └─ create an object
│       └─ reference variable
└─ declared reference type
```

The variable stores a reference to the object rather than containing the complete object inline.

## Java and Python comparison

Java:

```java
public class Student {
    private int id;
    private String name;

    public Student(int id, String name) {
        this.id = id;
        this.name = name;
    }
}
```

Python:

```python
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
```

Both initialise object state. Java declares field and parameter types and supports enforced access modifiers. Python commonly uses naming conventions and properties rather than Java-style private fields and accessor methods.

## Useful object methods

Every Java class ultimately inherits methods from `Object`. Overriding `toString()` gives a useful text representation:

```java
@Override
public String toString() {
    return id + ": " + name;
}
```

Then:

```java
System.out.println(student);
```

prints the returned representation.

The `@Override` annotation asks the compiler to verify that the method genuinely overrides an inherited declaration.

## Introductory inheritance

```java
public class PostgraduateStudent extends Student {
    private String researchTopic;

    public PostgraduateStudent(
        int id,
        String name,
        String researchTopic
    ) {
        super(id, name);
        this.researchTopic = researchTopic;
    }

    public String getResearchTopic() {
        return researchTopic;
    }

    @Override
    public String toString() {
        return super.toString() + " — " + researchTopic;
    }
}
```

- `extends Student` establishes inheritance;
- `super(id, name)` invokes the parent constructor;
- the child adds its own state;
- the overridden method specialises behaviour.

Use inheritance for a genuine “is-a” relationship with substitutable behaviour. Composition is often preferable when one object merely uses or contains another.

## Java files and compilation

With both source files in one directory:

```text
javac Student.java Program.java
java Program
```

An IDE normally manages compilation automatically. As projects grow, packages, build tools and dependency management become important, but the class and object principles remain the same.

## Where Java leads

The final slides demonstrate several directions:

### Desktop interfaces

AWT and Swing are long-standing Java desktop UI toolkits. JavaFX is a newer UI framework developed separately from the core JDK distribution and can support structured interfaces, graphics and media.

### Android

Java has played a major role in Android development. Contemporary Android projects commonly use Kotlin, while Java code and libraries remain relevant and interoperable within the ecosystem.

### Server applications

Frameworks such as Spring and Spring Boot support web applications, APIs and larger server-side systems. They introduce dependency injection, configuration, HTTP routing, persistence and many additional concepts beyond this introductory lecture.

These are destinations, not three extra tutorials to complete today. The key transferable foundations are types, objects, collections, methods and program structure.

## Pause and review the model

For the `Student` class, identify:

1. its private state;
2. its constructor;
3. its public interface;
4. one invariant the class should protect;
5. one method that reveals behaviour rather than simply returning a field;
6. whether a `Course` should inherit from `Student` or be associated with it.

## Common mistakes

- **Giving fields public access:** protect object state through a meaningful interface.
- **Writing a return type on a constructor:** constructors have no return type.
- **Forgetting `new`:** object construction normally uses it.
- **Confusing a class and an object:** a class defines a type; an object is an instance.
- **Forgetting `this` when parameter and field names match:** assignment may otherwise target only the parameter.
- **Adding setters without validation:** encapsulation should protect rules.
- **Using `==` for object content:** equality behaviour requires appropriate methods.
- **Overriding without `@Override`:** the annotation helps detect spelling/signature mistakes.
- **Using inheritance only to reuse code:** require a meaningful is-a relationship.
- **Treating ecosystem screenshots as timeless setup instructions:** tools and templates change; use current official documentation.
- **Trying to learn JavaFX, Android and Spring simultaneously:** consolidate core Java first.

## Check your understanding

1. What is the difference between a class and an object?
2. Why make fields private?
3. What does a constructor establish?
4. What does `this` refer to?
5. What do `extends`, `super` and `@Override` contribute?
6. When might composition be preferable to inheritance?
7. Which Java concepts transfer into desktop, mobile and server development?

## Apply your learning

1. Implement the `Student` class and create two objects.
2. Add validation that prevents a blank name.
3. Override `toString()` and print each object.
4. Store students in an `ArrayList<Student>` and iterate through it.
5. Store students in a `HashMap<Integer, Student>` keyed by ID.
6. Add a suitable child class and justify the is-a relationship.
7. Model a `Course` association using composition rather than inheritance.
8. Choose JavaFX, Android or Spring as a future direction and identify which core concepts from this lecture it builds upon.

## Page summary

Java classes combine declared state with constructors and methods. Private fields and deliberate public behaviour support encapsulation; `new` creates objects; and inheritance uses `extends`, `super` and overriding where a genuine specialised relationship exists. These foundations support Java development across collections, desktop interfaces, Android-compatible code and server frameworks.

**Previous:** Return to **13.4 Arrays and the Collections Framework**.  
**Next step:** Complete the Lecture 13 Java comparison activities, then continue to Lecture 14 for further Java development.

---

# Suggested lecture and VLE structure

Create one learning module titled **13 Introduction to Java**, containing:

1. **13.1 Java, Bytecode and the JVM**
2. **13.2 Your First Java Program and Input/Output**
3. **13.3 Types, Strings, Control Flow and Methods**
4. **13.4 Arrays and the Collections Framework**
5. **13.5 Classes, Objects and the Wider Java Ecosystem**

The five-page structure is recommended because the 97-page deck contains several substantial conceptual transitions. Combining all syntax comparisons into one page would turn the VLE into a reference dump rather than a navigable learning experience.

The final JavaFX, Android Studio and Spring slides are condensed into an ecosystem orientation. Their original screenshots demonstrate possible applications but should not be used as current installation tutorials because IDE layouts, templates and framework versions change.

## Recommended emphasis

The core Lecture 13 outcome should be that learners can:

- explain the Java compile-and-run model;
- create, compile and run a console program;
- read and write simple values;
- recognise types, strings, decisions, loops and methods;
- use arrays, `ArrayList` and `HashMap` at an introductory level;
- define and instantiate a simple encapsulated class;
- compare Java constructs with familiar Python concepts.

JavaFX, Android and Spring should motivate future study rather than become required practical outcomes in this lecture.

## Further reading

- [Dev.java: Getting Started](https://dev.java/learn/getting-started/)
- [Dev.java: Launching simple source-code programs](https://dev.java/learn/launch-simple-source-code-programs/)
- [Oracle Java SE documentation](https://docs.oracle.com/en/java/javase/)
- [Java language specification](https://docs.oracle.com/javase/specs/)
- [OpenJFX](https://openjfx.io/)
