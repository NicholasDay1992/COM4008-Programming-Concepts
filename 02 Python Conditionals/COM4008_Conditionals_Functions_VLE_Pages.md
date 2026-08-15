# COM4008 Programming Concepts: Conditionals, Operators, Iteration and Functions

This content is designed as four linked VLE information pages. Learners should run the examples and complete the practical activities in a Python notebook or coding environment.

---

# Page 1: Selection

## On this page

- Sequence and selection
- Boolean conditions
- `if`, `else`, and `elif`
- Indented code blocks
- Ordering mutually exclusive decisions
- Optional extension: `match`

## Learning outcomes

By the end of this page, you should be able to:

- explain how selection changes the flow of a program;
- use `if`, `elif`, and `else` to select a path;
- indent a conditional block correctly;
- order related conditions so that the intended branch runs;
- distinguish one decision chain from several independent decisions.

## From sequence to selection

Programs normally execute instructions in **sequence**, from top to bottom. **Selection** allows a program to choose whether a block of instructions should run.

A selection statement evaluates a condition. A condition has one of two Boolean values:

- `True`
- `False`

If the condition is `True`, the associated block runs. If it is `False`, Python skips that block or follows another available path.

## The `if` statement

An `if` statement runs a block only when its condition is true:

```python
score = 45

if score >= 40:
    print("You passed!")
```

Read the condition as a question: “Is `score` greater than or equal to 40?” Here, the answer is `True`, so the indented instruction runs.

If `score` were `35`, the condition would be `False` and the message would not appear.

## Syntax and indentation

The colon at the end of the `if` line begins a code block. Every instruction belonging to that block must be indented consistently:

```python
score = 40

if score == 40:
    print("The score is exactly 40")
    print("This line is also inside the block")

print("This line is outside the block")
```

Indentation is part of Python's syntax. Most editors insert four spaces when you press Tab. Incorrect or inconsistent indentation can cause an `IndentationError` or make an instruction run in the wrong place.

## Adding an alternative with `else`

Use `else` when exactly one of two paths should run:

```python
score = 35

if score >= 40:
    print("You passed!")
else:
    print("Try again")
```

`else` has no condition of its own. Its block runs only when the preceding `if` condition is false.

## Testing several alternatives with `elif`

Use `elif`—short for “else if”—when a decision has more than two mutually exclusive outcomes:

```python
score = 75

if score >= 70:
    print("Grade A")
elif score >= 60:
    print("Grade B")
elif score >= 50:
    print("Grade C")
elif score >= 40:
    print("Pass")
else:
    print("Not yet passed")
```

Python tests these conditions from top to bottom and runs the first true branch. It then skips the rest of the chain. For this reason, overlapping thresholds should normally be ordered from highest to lowest.

If `score >= 40` appeared first, a score of `75` would satisfy it immediately and Python would never reach the Grade A test.

## One chain or several decisions?

An `if`/`elif`/`else` chain selects no more than one branch. Separate `if` statements are independent, so several blocks may run:

```python
score = 55

if score >= 50:
    print("At least 50")

if score >= 40:
    print("A passing score")
```

Both messages appear. This is correct when both facts matter. Use `elif` when the outcomes are alternatives; use separate `if` statements when each condition should be checked independently.

## Input and selection

Selection becomes especially useful when a program responds to user input:

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are under 18")
```

Remember that `input()` returns a string. `int()` converts suitable text to an integer before the numeric comparison.

## Pause and predict

What will this program display when `score` is `65`?

```python
score = 65

if score >= 70:
    print("A")
elif score >= 60:
    print("B")
elif score >= 40:
    print("Pass")
else:
    print("Not passed")
```

Would the result change if each `elif` were replaced by `if`? Explain your prediction before running either version.

## Optional extension: structural pattern matching

Python 3.10 introduced `match`, which can select a case by matching a value or pattern:

```python
grade = "C"

match grade:
    case "A":
        print("First-class range")
    case "B":
        print("Upper second-class range")
    case "C":
        print("Lower second-class range")
    case "D":
        print("Third-class range")
    case _:
        print("Grade not recognised")
```

The `_` case acts as a fallback. `match` supports more than simple equality, but `if`/`elif` remains the clearest starting point for ranges such as marks.

## Common mistakes

- Using `=` for comparison instead of `==`.
- Omitting the colon after `if`, `elif`, or `else`.
- Failing to indent the controlled block.
- Placing a broad condition before a more specific overlapping condition.
- Expecting an `elif` to be checked after an earlier branch has already run.
- Comparing input text with a number before converting it.

## Check your understanding

1. What two values can a Boolean condition have?
2. When does an `else` block run?
3. Why should grade thresholds usually be tested from highest to lowest?
4. When would separate `if` statements be more appropriate than `elif`?
5. What role does indentation play in a conditional statement?

## Try it yourself

### Activity 1: Adult or child

Ask the user for their age and display an appropriate message indicating whether they are an adult or under 18.

### Activity 2: Greatest number

Ask the user for two numbers and display the greater value. Extend the program to recognise when the values are equal.

### Activity 3: Mark to grade

Ask for a mark from 0 to 100 and display a suitable grade. Test boundary values such as 39, 40, 49, 50, 69, and 70.

## Page summary

Selection allows a program to choose an execution path. `if` tests the first condition, `elif` provides further mutually exclusive tests, and `else` provides a fallback. Conditions are checked in order, and indentation identifies the instructions controlled by each branch.

**Next:** Continue to **Page 2: Operators**.

---

# Page 2: Operators

## On this page

- Comparison operators
- Arithmetic operators
- Operator precedence
- Logical operators
- Combining conditions
- Validating ranges

## Learning outcomes

By the end of this page, you should be able to:

- construct Boolean expressions using comparison operators;
- perform calculations with arithmetic operators;
- use parentheses to make calculation order explicit;
- combine conditions using `and`, `or`, and `not`;
- select appropriate operators for boundary and validation checks.

## Comparison operators

Comparison operators compare values and produce either `True` or `False`.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `score == 40` |
| `!=` | Not equal to | `name != "Sam"` |
| `<` | Less than | `age < 18` |
| `>` | Greater than | `temperature > 25` |
| `<=` | Less than or equal to | `mark <= 100` |
| `>=` | Greater than or equal to | `mark >= 40` |

For example:

```python
score = 45
print(score >= 40)   # True
print(score == 45)   # True
print(score != 45)   # False
```

Types matter in comparisons. The integer `45` and string `"45"` represent different kinds of value:

```python
print(45 == "45")   # False
```

## Assignment is not equality

Use `=` to assign a value and `==` to compare values:

```python
score = 45           # assignment
print(score == 45)   # equality comparison
```

Reading `==` as “is equal to” can help you distinguish the two operations.

## Arithmetic operators

| Operator | Operation | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 5` | `10` |
| `-` | Subtraction | `5 - 4` | `1` |
| `*` | Multiplication | `5 * 10` | `50` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor division | `5 // 2` | `2` |
| `%` | Remainder (modulo) | `50 % 4` | `2` |
| `**` | Exponentiation | `5 ** 2` | `25` |

Floor division rounds the quotient down towards negative infinity. The remainder operator is especially useful for testing divisibility. A number is even when its remainder after division by 2 is zero:

```python
number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## Operator precedence

Python follows an order of operations. Parentheses are evaluated first, then exponentiation, then multiplication and division operations, followed by addition and subtraction.

```python
print(4 + 4 ** 2)     # 20
print((4 + 4) ** 2)   # 64
```

Use parentheses whenever they make your intention clearer, even if you know the precedence rules.

## Logical operators

Logical operators combine or reverse Boolean expressions.

| Operator | Result |
|---|---|
| `and` | `True` only when both conditions are true |
| `or` | `True` when at least one condition is true |
| `not` | Reverses `True` and `False` |

Use `and` when both requirements must be satisfied:

```python
score = 45

if score >= 40 and score <= 100:
    print("Passing mark within the valid range")
```

Python also allows a chained comparison, which is concise and readable:

```python
if 40 <= score <= 100:
    print("Passing mark within the valid range")
```

Use `or` when either condition indicates the same outcome:

```python
score = 101

if score < 0 or score > 100:
    print("Invalid mark")
```

Use `not` to reverse a Boolean result:

```python
logged_in = False

if not logged_in:
    print("Please sign in")
```

Often a direct positive expression is easier to read than several uses of `not`. For example, `0 <= score <= 100` is clearer than `not score < 0 and not score > 100`.

## Truth tables

The following table summarises `and` and `or`:

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| `False` | `False` | `False` | `False` |
| `False` | `True` | `False` | `True` |
| `True` | `False` | `False` | `True` |
| `True` | `True` | `True` | `True` |

## Pause and predict

For `score = 55`, predict the result of each expression:

```python
score >= 40
score == "55"
score < 0 or score > 100
score >= 40 and score <= 100
not score >= 40
```

Then run the expressions and explain any result that surprised you.

## Common mistakes

- Confusing `=` with `==`.
- Writing `score >= 40 or score <= 100`, which is true for almost every number, when both boundaries must hold.
- Forgetting that inputs are strings until converted.
- Assuming `/` performs whole-number division.
- Using `%` as though it calculates a percentage; it returns a division remainder.
- Relying on precedence when parentheses would make the expression clearer.

## Check your understanding

1. Which operator checks equality?
2. What is the difference between `/` and `//`?
3. How can `%` be used to identify an even number?
4. When does an `and` expression evaluate to `True`?
5. Write one expression that tests whether `mark` is from 0 to 100 inclusive.

## Try it yourself

### Activity 1: Range validator

Ask for a mark. Display an error if it is below 0 or above 100; otherwise, confirm that it is valid.

### Activity 2: Even or odd

Ask for an integer and use the remainder operator to report whether it is even or odd.

### Activity 3: Ticket eligibility

Create two Boolean conditions representing eligibility for a discounted ticket—for example, an age condition and a membership condition. Combine them using an appropriate logical operator and explain your choice.

## Page summary

Comparison operators produce Boolean values, arithmetic operators calculate new values, and logical operators combine conditions. Types and boundaries matter. Parentheses and direct, positive conditions make expressions easier to read and verify.

**Previous:** Page 1: Selection  
**Next:** Continue to **Page 3: Iteration**.

---

# Page 3: Iteration

## On this page

- Sequence, selection, and iteration
- `while` loops
- Counters and termination
- `for` loops and `range()`
- Iterating over strings
- Choosing an appropriate loop

## Learning outcomes

By the end of this page, you should be able to:

- explain iteration as one of the core programming constructs;
- write a terminating `while` loop;
- use `for` with `range()` for count-controlled repetition;
- iterate over the characters in a string;
- choose between `while` and `for` for a simple task.

## The three core constructs

Many algorithms combine three fundamental constructs:

- **Sequence:** execute instructions in order.
- **Selection:** execute a block when a condition is true.
- **Iteration:** repeat a block of instructions.

An `if` statement makes a decision once when execution reaches it. A loop may execute its block many times.

## The `while` loop

A `while` loop repeats while its condition remains true:

```python
count = 0

while count < 3:
    print("Loop", count)
    count += 1
```

The output is:

```text
Loop 0
Loop 1
Loop 2
```

This loop has three important parts:

1. `count = 0` establishes the initial state.
2. `count < 3` is checked before every iteration.
3. `count += 1` updates the state so the condition eventually becomes false.

`count += 1` is an augmented assignment equivalent to `count = count + 1`.

## Avoiding infinite loops

If the condition never becomes false, a `while` loop does not terminate:

```python
count = 0

while count < 3:
    print(count)
```

Here, `count` never changes. Before running a `while` loop, identify what will change and why the condition will eventually become false. If a loop runs indefinitely in a notebook or editor, use its stop or interrupt control.

## The `for` loop and `range()`

A `for` loop iterates over the items in an iterable. `range()` generates a sequence of integers suitable for count-controlled repetition:

```python
for number in range(3):
    print(number)
```

This displays `0`, `1`, and `2`. The stop value is excluded.

`range()` can take a start, stop, and step:

```python
for number in range(1, 11):
    print(number)
```

This displays the integers 1 to 10 because the loop stops before 11.

```python
for number in range(2, 11, 2):
    print(number)
```

This starts at 2, stops before 11, and advances by 2, producing the even numbers from 2 to 10.

## Iterating over a string

A string is an iterable sequence of characters:

```python
name = "Nick"

for letter in name:
    print(letter)
```

The loop runs once for each character. Python assigns the next character to `letter` on each iteration.

## Choosing between `while` and `for`

Use a `for` loop when iterating over a collection or a known range of values. Use a `while` loop when repetition depends on a condition whose duration is not known in advance.

For example:

- printing 12 rows of a multiplication table suits `for` with `range()`;
- repeatedly asking for a guess until it is correct suits `while`.

## Combining iteration and selection

Selection can control what happens during each iteration:

```python
for number in range(1, 11):
    if number % 2 == 0:
        print(number)
```

The loop visits every integer from 1 to 10, while the `if` statement selects only the even values for output.

## Pause and predict

Predict every line of output:

```python
total = 0

for number in range(1, 4):
    total += number
    print(total)
```

What is the final value of `total`, and how is it built across the iterations?

## Common mistakes

- Forgetting to update the state in a `while` loop.
- Expecting the stop value of `range()` to be included.
- Starting at 0 when the required output begins at 1.
- Altering indentation so instructions accidentally fall outside the loop.
- Using `while` for a simple known range when `for` would be clearer.
- Reusing a loop variable later without considering its final value.

## Check your understanding

1. How does iteration differ from selection?
2. What three elements make the example `while` loop terminate?
3. Which values are produced by `range(1, 6)`?
4. What does the third argument to `range()` control?
5. When is a `while` loop preferable to a `for` loop?

## Try it yourself

### Activity 1: Two loop forms

Print the numbers 1 to 10 using a `for` loop. Then produce the same output using a `while` loop.

### Activity 2: Even and odd numbers

Print the even numbers from 1 to 10. Amend the condition to print only odd numbers.

### Activity 3: Multiplication table

Use a loop to display the 7 times table from `1 × 7` to `12 × 7`.

Extension: ask the user which multiplication table they want and generate it using the same loop.

### Activity 4: Guessing game

As a larger challenge, generate a random integer from 1 to 100 and repeatedly ask the user to guess it. Report whether each guess is too high or too low, count the attempts, and stop when the answer is correct.

Use `random.randint(1, 100)` to generate an integer directly. Design the loop and decisions on paper before coding.

## Page summary

Iteration repeats instructions. A `while` loop continues while its condition is true and therefore needs a route to termination. A `for` loop visits items in an iterable; `range()` is useful for sequences of integers. Selection inside a loop allows only particular values or actions to be processed.

**Previous:** Page 2: Operators  
**Next:** Continue to **Page 4: Functions**.

---

# Page 4: Functions

## On this page

- Why functions are useful
- Defining and calling functions
- Parameters and arguments
- Returning values
- Local variables
- Decomposing a program into tasks

## Learning outcomes

By the end of this page, you should be able to:

- explain how functions support reuse and decomposition;
- define and call a simple function;
- pass arguments into parameters;
- return a value to the calling code;
- distinguish printing a value from returning it;
- divide a small program into functions with clear responsibilities.

## What is a function?

A function is a named, reusable block of code that performs a well-defined task. You have already called built-in functions including `print()`, `input()`, `int()`, and `type()`.

You can define your own functions to:

- avoid repeating code;
- give a meaningful name to a task;
- divide a larger problem into manageable parts;
- test one behaviour at a time.

## Defining and calling a function

Use `def` to define a function:

```python
def display_welcome():
    print("Welcome to COM4008")
```

Defining the function does not run its body. Call it using its name followed by parentheses:

```python
display_welcome()
```

The indented block is the function body. Function names normally follow the same `snake_case` convention as variable names.

## Parameters and arguments

A parameter is a name in a function definition that receives a value:

```python
def greet(name):
    print(f"Hello {name}")

greet("Aisha")
greet("Sam")
```

`name` is a **parameter**. `"Aisha"` and `"Sam"` are **arguments** supplied by the calls. The same function can therefore work with different values.

## Returning a value

`return` sends a result back to the calling location:

```python
def add(x, y):
    return x + y

total = add(80, 10)
print(total)
```

The call `add(80, 10)` evaluates to `90`, which is then assigned to `total`.

Returning is different from printing:

- `print()` displays a value to the user.
- `return` gives a value back to the code that called the function.

A returned value can be stored, printed, compared, or used in another expression. A function ends when it reaches `return`.

## A function that receives input

This function prompts the user and returns their response:

```python
def get_name():
    return input("Please enter your name: ")

name = get_name()
print(f"Hello {name}")
```

For a more reusable design, let the calling code provide the prompt:

```python
def get_integer(prompt):
    return int(input(prompt))

age = get_integer("Enter your age: ")
mark = get_integer("Enter your mark: ")
```

## Local variables and scope

Variables created inside a function are normally local to that function:

```python
def calculate_area(width, height):
    area = width * height
    return area
```

The name `area` is used inside the function. Code outside should use the returned result rather than depend on that local name:

```python
rectangle_area = calculate_area(5, 3)
print(rectangle_area)
```

Passing values through parameters and return values makes relationships explicit and reduces reliance on global variables.

## Combining functions and selection

Functions can contain conditional logic:

```python
def convert_mark_to_grade(mark):
    if mark < 0 or mark > 100:
        return "Invalid"
    elif mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

grade = convert_mark_to_grade(65)
print(grade)
```

Notice that this function has one clear responsibility: convert a mark into a grade. The calling code decides what to do with the result.

## Decomposing a program

A unit-conversion program could be divided into tasks such as:

- `display_menu()` — show the available units;
- `get_menu_choice()` — obtain and return a choice;
- `get_distance()` — obtain and return a numeric distance;
- `convert_distance(...)` — calculate and return a conversion;
- `display_result(...)` — present the result.

Aim for each function to do one well-defined job. Parameters should provide the information it needs, and `return` should provide any result needed elsewhere.

## Pause and predict

What is displayed, and what value is stored in `result`?

```python
def multiply(a, b):
    product = a * b
    return product

result = multiply(4, 5)
print(result)
```

Now predict what happens if the `return product` line is removed. Run it and inspect `type(result)`.

## Common mistakes

- Defining a function but never calling it.
- Forgetting the parentheses in a function call.
- Passing the wrong number of arguments.
- Printing a result when the calling code needs it returned.
- Expecting a local variable to be available outside its function.
- Relying unnecessarily on global variables.
- Placing code after an unconditional `return` and expecting it to run.

## Check your understanding

1. What is the difference between defining and calling a function?
2. How does a parameter differ from an argument?
3. What does `return` do?
4. Why is returning a result often more flexible than printing it inside the function?
5. What does it mean for a variable to be local?
6. Why might a larger program be divided into several small functions?

## Apply your learning

### Activity 1: Greatest value function

Define `get_greatest(a, b)` so it returns the greater of two values. Decide what it should return when the values are equal.

### Activity 2: Grade conversion

Define `convert_mark_to_grade(mark)`. Validate the 0–100 range and return either a grade or an invalid-input result. Test boundary values.

Extension: define a second function that converts the returned grade to a degree-classification label.

### Activity 3: Unit converter

Build a program that lets a user choose a source unit and destination unit, enter a distance, and receive the converted result. Begin with miles and feet, then add metres.

Separate input, conversion, and output responsibilities. Avoid duplicating the same calculation or interaction code unnecessarily.

## Page summary

Functions package a well-defined task behind a meaningful name. Parameters receive information, arguments provide concrete values, and `return` passes a result back to the caller. Small functions with clear responsibilities make programs easier to understand, test, reuse, and extend.

**Previous:** Page 3: Iteration  
**Next step:** Complete the Conditionals and Functions practical exercises, testing normal values, boundary values, and invalid values.

---

# Suggested VLE setup

Create the pages in this order:

1. **Selection**
2. **Operators**
3. **Iteration**
4. **Functions**

Add previous/next links at the bottom of each page. Use each second-level heading in the page navigation. Keep the longer programming exercises in the practical notebook or coding environment and link to them from the activity sections.

The guessing game and multi-unit converter are valuable consolidation tasks because they combine several constructs. They are better positioned after the individual concepts have been introduced, rather than embedded within a single explanatory section.
