# COM4008 Programming Concepts: Python Basics

This content is designed as three linked VLE information pages. Code examples can be copied into a Python editor or notebook and run by learners.

---

# Page 1: Introduction to Python and Your First Program

## On this page

- What Python is
- Why Python is widely used
- How to run a first Python program
- How the `print()` function produces output
- How to recognise strings and simple syntax errors

## Learning outcomes

By the end of this page, you should be able to:

- describe some of Python's main characteristics and uses;
- use `print()` to display text;
- recognise a string value in Python;
- identify and correct simple errors in a line of code.

## What is Python?

Python is a high-level, general-purpose programming language. Its syntax is designed to be readable, allowing programmers to express ideas without a large amount of code.

Python was created by Guido van Rossum and first released publicly in 1991. Its name was inspired by the comedy group Monty Python, rather than the snake.

Readability is central to Python's design. The *Zen of Python* includes principles such as:

- beautiful is better than ugly;
- explicit is better than implicit;
- simple is better than complex;
- readability counts.

You do not need to memorise these principles. For now, notice that clear code is considered an important part of writing good Python programs.

## Why learn Python?

Python is a useful first programming language because it is:

- **Readable:** its syntax is relatively close to plain language.
- **Productive:** useful programs can often be written with comparatively little code.
- **Portable:** Python is available on all major operating systems.
- **Extensible:** a large collection of libraries adds tools for specialist tasks.

Python is used in web development, data analysis, artificial intelligence and machine learning, computer vision, automation, Internet of Things projects, and game development.

## Your first Python program

Run the following instruction:

```python
print("Hello World")
```

The output should be:

```text
Hello World
```

`print()` is a built-in Python function. A function is a reusable piece of code that performs a task. Here, its task is to display a value as output.

The text `"Hello World"` is a **string**. A string is a sequence of characters used to represent text. The quotation marks tell Python where the string begins and ends; they are not displayed in the output.

## Printing more than one line

Each call to `print()` normally starts a new line of output:

```python
print("Hello Nick")
print("Your ID is 12345678")
```

This produces:

```text
Hello Nick
Your ID is 12345678
```

## Pause and predict

Before running this code, write down exactly what you think it will display:

```python
print("Welcome to COM4008")
print("Programming Concepts")
```

Then run it and compare the result with your prediction.

## Common mistakes

Python requires precise syntax. For example:

- `Print` is not the same as `print`; Python is case-sensitive.
- Text values must be enclosed in matching quotation marks.
- The opening and closing parentheses in `print()` must both be present.

When Python cannot understand an instruction, it reports an error. Read the final line of the error message and look carefully at the indicated line of code.

## Check your understanding

1. What is the purpose of `print()`?
2. What tells Python that `"Hello World"` is a string?
3. How would you display your name and student number on separate lines?
4. Would `PRINT("Hello")` work? Explain your answer.

## Try it yourself

Write a short program that displays:

1. your name;
2. the title `COM4008 Programming Concepts`;
3. a sentence explaining why you are learning Python.

Place each item on a separate line.

## Page summary

Python is a readable, general-purpose programming language used in many fields. A Python program consists of instructions. The built-in `print()` function displays output, and quotation marks identify text as a string.

**Next:** Continue to **Page 2: Receiving Input** to make a program respond to its user.

---

# Page 2: Receiving Input

## On this page

- How interactive programs receive input
- How to use the `input()` function
- How to store and display user input
- Why input is initially treated as text
- How comments can document code

## Learning outcomes

By the end of this page, you should be able to:

- prompt a user to enter a value;
- store the result returned by `input()`;
- display a response using the entered value;
- explain why `input()` returns a string;
- add an appropriate single-line comment to Python code.

## From output to interaction

The programs on Page 1 displayed fixed messages. An interactive program can also receive information from its user.

Python's built-in `input()` function displays a prompt and pauses the program until the user enters a response:

```python
input("Please enter your name: ")
```

The user's response is a value returned by the function. A useful program normally stores that value so it can use it later:

```python
name = input("Please enter your name: ")
print("Hello", name)
```

If the user enters `Aisha`, the output will be:

```text
Hello Aisha
```

The name `name` identifies a variable. Variables are explored fully on Page 3; for now, think of `name` as a label that lets the program remember the user's response.

## Input is returned as text

The `input()` function returns a string, even when the user types digits:

```python
age = input("Please enter your age: ")
print("You are", age, "years old")
print(type(age))
```

If the user enters `18`, `type(age)` reports `<class 'str'>`. The characters `1` and `8` have been stored as text, not as a numeric value on which arithmetic can yet be performed.

To request an integer, convert the returned string using `int()`:

```python
age = int(input("Please enter your age: "))
print("Next year you will be", age + 1)
```

This pattern works from the inside out:

1. `input()` receives text from the user.
2. `int()` converts that text to an integer.
3. the integer is stored using the name `age`.

If the user enters something that cannot be interpreted as a whole number, such as `eighteen`, Python will report a `ValueError`. Later in the module, you will learn how to validate input and respond to such errors.

## Pause and predict

Suppose the user enters `20`. What will each line display?

```python
age = input("Enter your age: ")
print(age + age)
print(type(age))
```

Run the code after making your prediction. Why does the first output differ from the result of `20 + 20`?

## Comments in Python

A comment is a note for a human reader. Python ignores text following `#` on that line:

```python
# Ask the user for their age
age = int(input("Please enter your age: "))
print("You are", age, "years old")
```

Comments should explain intent or an important decision. Avoid comments that merely repeat an obvious instruction.

A triple-quoted string is not a general-purpose block comment. When it appears as the first statement in a module, class, or function, it forms a **docstring** used to document that object. You will encounter functions and docstrings later in the module.

## Check your understanding

1. What causes an `input()` call to finish?
2. Which type does `input()` return?
3. Why is `int(input("Enter a number: "))` useful?
4. What error might occur if a user enters `ten` where an integer is required?
5. Which symbol begins a single-line Python comment?

## Try it yourself

### Activity 1: Personal greeting

Ask the user to enter their name. Store the response and display a personalised greeting.

### Activity 2: Two numbers

Ask the user to enter two numbers. Convert both inputs to an appropriate numeric type, calculate their average, and display the result.

### Activity 3: Rectangle calculator

Ask for the length and height of a rectangle. Calculate and display its perimeter and area.

Extension: ask the user for a unit such as `cm` or `metres` and include it in the output. Remember that area uses square units.

## Page summary

`input()` lets a program receive a value from its user. It always returns a string, so numeric input must be converted before arithmetic. The `#` symbol introduces a single-line comment that can help explain the purpose of code.

**Previous:** Page 1: Introduction to Python and Your First Program  
**Next:** Continue to **Page 3: Variables, Types and Values** to understand how Python stores and processes data.

---

# Page 3: Variables, Types and Values

## On this page

- Values and variables
- Assignment and reassignment
- Naming and case sensitivity
- Common data types
- Dynamic typing
- Type conversion
- Formatting output with f-strings

## Learning outcomes

By the end of this page, you should be able to:

- assign values to meaningfully named variables;
- distinguish assignment from comparison;
- identify common Python data types;
- inspect a value using `type()`;
- convert values between compatible types;
- combine variables and text in readable output.

## Values and variables

A program works with **values**. Examples include the text `"Nick"`, the whole number `30`, and the decimal number `4.5`.

A **variable** is a name associated with a value so that the program can use that value later:

```python
name = "Nick"
age = 30
```

The `=` symbol is the **assignment operator**. It evaluates the value on the right and assigns it to the name on the left. Here it does not mean “is mathematically equal to”. Python uses `==` when comparing two values for equality; comparisons are covered later in the module.

## Choosing variable names

A useful variable name communicates what its value represents:

```python
first_mark = 60
student_name = "Aisha"
```

Python variable names:

- may contain letters, digits, and underscores;
- cannot begin with a digit;
- cannot contain spaces;
- are case-sensitive;
- cannot use reserved Python keywords such as `if` or `class`.

By convention, Python variable names use lowercase words separated by underscores, known as `snake_case`.

Because Python is case-sensitive, `age` and `Age` are two different names:

```python
age = 30
Age = 35
print(age)
print(Age)
```

Using names that differ only by capitalisation is legal but confusing, so it should be avoided.

## Values can be reassigned

A variable name can be assigned a new value:

```python
name = "Nick"
name = "Sam"
print(name)
```

The output is `Sam` because the second assignment replaces the value previously associated with `name`.

## Common Python types

Every value has a type. Types determine how values can be used.

| Type | Meaning | Example |
|---|---|---|
| `str` | Text | `"Hello"` |
| `int` | Whole number | `30` |
| `float` | Number with a decimal component | `30.5` |
| `bool` | Logical value | `True` or `False` |

Use `type()` to inspect a value:

```python
age = 30
name = "Nick"
print(type(age))
print(type(name))
```

This reports that `age` contains an `int` and `name` contains a `str`.

## Python is dynamically typed

Python is dynamically typed: a name is not permanently restricted to one type. For example, this code is valid:

```python
value = 30
value = "thirty"
```

The type belongs to the value, and the name can later be reassigned to another value. This flexibility is useful, but changing the meaning or type of a variable unexpectedly can make a program difficult to understand. Prefer consistent, descriptive names.

## Combining values in output

`print()` can receive several values separated by commas:

```python
name = "Nick"
age = 30
print("Hello", name, "you are", age)
```

Python inserts spaces between these values.

An **f-string** offers a readable way to embed values inside text. Prefix the string with `f` and place expressions inside braces:

```python
name = "Nick"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

F-strings are the recommended formatting approach for most examples in this module. Older `%` formatting may appear in existing Python code, but you do not need it for these introductory activities.

F-strings can also control numeric presentation. For example, `.2f` displays a number to two decimal places:

```python
balance = 104.5
print(f"Balance: £{balance:.2f}")
```

The output is:

```text
Balance: £104.50
```

## Type conversion

Values of compatible types can be converted using functions such as `int()`, `float()`, and `str()`:

```python
first_mark = 60
second_mark = int("40")
total = first_mark + second_mark
print(total)
```

The output is `100` because `"40"` is converted from a string to an integer before addition.

Compare this with:

```python
first_mark = "60"
second_mark = "40"
print(first_mark + second_mark)
```

The output is `6040`. For strings, `+` performs **concatenation**: it joins text rather than doing arithmetic.

Not every conversion is possible. For example, `int("forty")` causes a `ValueError` because the text does not represent an integer.

## Pause and predict

Predict the result of each example before running it:

```python
first_mark = "60"
second_mark = "40"
print(first_mark + second_mark)
```

```python
first_mark = 60
second_mark = int("40")
print(first_mark + second_mark)
```

```python
name = "Aisha"
age = 20
print(f"{name} will be {age + 1} next year.")
```

## Common mistakes

- Using a variable before assigning it a value causes a `NameError`.
- Referring to `Name` after assigning `name` also causes a `NameError`.
- Adding a string directly to an integer causes a `TypeError`.
- Converting unsuitable text with `int()` causes a `ValueError`.
- Using `=` when you intend to compare values changes or assigns a value rather than testing equality.

Error messages are evidence. Identify the error type, inspect the indicated line, and compare the types involved with what the operation requires.

## Check your understanding

1. What does the assignment operator do?
2. What is the difference between `age` and `Age`?
3. What type is the value `"25"`?
4. What does `int("25")` produce?
5. Why does `"6" + "4"` produce `"64"` rather than `10`?
6. What is the advantage of using an f-string?

## Apply your learning

### Activity 1: Miles to feet

Ask the user to enter a number of miles. Convert the input to a numeric type and display the equivalent number of feet. There are 5,280 feet in one mile.

Extension: convert the resulting number of feet back to miles and confirm that it matches the original input.

### Activity 2: Savings calculator

Create a program that asks for a deposit amount and calculates its value after one year at a chosen annual interest rate. Display the result as pound sterling with two decimal places.

### Activity 3: Explain the behaviour

Run the following code and explain both the output and the type of `result`:

```python
first_value = input("Enter 6: ")
second_value = input("Enter 4: ")
result = first_value + second_value
print(result)
print(type(result))
```

Modify the program so that it produces the numeric result `10`.

## Page summary

Variables associate meaningful names with values. Python values have types, including `str`, `int`, `float`, and `bool`. Python is dynamically typed, but operations still require compatible values. Conversion functions change compatible values from one type to another, while f-strings provide a readable way to combine values with explanatory text.

**Previous:** Page 2: Receiving Input  
**Next step:** Complete the Python Basics practical exercises and test your programs with several inputs.

---

# Suggested VLE setup

Create the pages in this order:

1. **Introduction to Python and Your First Program**
2. **Receiving Input**
3. **Variables, Types and Values**

Add previous/next links at the bottom of each page. If the VLE supports an on-page contents menu, use each second-level heading as an anchor. Keep runnable exercises in the practical notebook or coding environment and link to them from each page's **Try it yourself** or **Apply your learning** section.

The notebook's advanced date-of-birth exercises depend on conditionals, date handling, functions, and validation that have not yet been taught. They are better moved to the relevant later units or clearly labelled as optional preview challenges.
