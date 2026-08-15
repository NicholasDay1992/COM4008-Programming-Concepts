# COM4008 Programming Concepts: Exceptions, Control Flow and Assertions

This content is designed as four linked VLE information pages. Learners should run the examples and complete the practical activities in a Python notebook or coding environment.

---

# Page 1: Exception Theory and the Hierarchy

## On this page

- Errors and exceptional events
- Syntax errors compared with runtime exceptions
- Common built-in exception types
- Reading a traceback
- The exception hierarchy at recognition level
- When recovery is appropriate

## Learning outcomes

By the end of this page, you should be able to:

- explain what a runtime exception is;
- distinguish a syntax error from an exception raised during execution;
- recognise several common built-in exception types;
- extract useful information from a traceback;
- explain why related exception types form a hierarchy;
- identify which failures a program might reasonably handle.

## What is an exception?

An **exception** is an object that represents an unusual or unsuccessful event encountered while Python is executing a program. When an exception is raised, normal execution is interrupted. Python looks for suitable handling code; if none is found, the program or current notebook cell stops and a traceback is displayed.

Exceptions can result from user input, unavailable resources, invalid operations, or programming defects. Examples include:

- converting unsuitable text to a number;
- dividing by zero;
- requesting an unavailable list index;
- looking up a missing dictionary key;
- opening a file that does not exist;
- importing a module that is unavailable.

Handling an anticipated problem can let a program explain the issue, ask again, choose an alternative, or shut down cleanly. Exception handling does not make every operation safe, and it should not conceal defects that the developer needs to fix.

## Syntax errors and runtime exceptions

Some code cannot be parsed as valid Python:

```python
print("Hello"
```

Python reports a `SyntaxError` before it can execute that code. Indentation problems are related parsing errors. An editor may identify them before the program runs.

Other instructions are valid Python syntax but fail when executed:

```python
result = 10 / 0
```

This raises `ZeroDivisionError` at runtime.

The distinction is useful:

- **Syntax error:** Python cannot correctly parse the program.
- **Runtime exception:** Python understands the instruction, but execution encounters a problem.
- **Logic error:** the program runs but produces an unintended result; no exception is required.

A `try` statement cannot catch a syntax error in the same malformed source code because that code cannot begin executing. Some operations such as `compile()` and `exec()` can raise `SyntaxError` while processing text dynamically, but that is not the normal beginner use case.

## Common built-in exceptions

### `TypeError`

An operation receives an object of an inappropriate type:

```python
first_mark = 60
second_mark = "40"
total = first_mark + second_mark
```

Adding an integer and a string has no defined meaning here.

### `ValueError`

An operation receives an acceptable type but an unsuitable value:

```python
mark = int("forty")
```

`int()` accepts strings, but `"forty"` is not a valid integer literal.

### `ZeroDivisionError`

An arithmetic operation attempts division or remainder by zero:

```python
average = 10 / 0
```

### `IndexError`

A sequence index lies outside its valid range:

```python
name = "Nick"
print(name[4])
```

The valid positive indexes are 0 to 3.

### `KeyError`

A mapping does not contain the requested key:

```python
student_ids = {"Nick": 12345}
print(student_ids["Sam"])
```

### `FileNotFoundError`

A file-opening operation cannot locate the requested file:

```python
with open("missing.txt", "r") as file:
    contents = file.read()
```

### `ModuleNotFoundError`

Python cannot locate an imported module:

```python
import module_that_is_not_installed
```

### `NameError`

A name has not been defined in the current accessible scope:

```python
print(total_mark)
```

## Read the traceback

An unhandled exception normally produces a **traceback**. It reports the sequence of calls that led to the failure, followed by the exception type and message.

```text
Traceback (most recent call last):
  File "example.py", line 2, in <module>
    result = 10 / divisor
ZeroDivisionError: division by zero
```

Start with the final line:

1. Identify the exception type: `ZeroDivisionError`.
2. Read its message: `division by zero`.
3. Inspect the indicated line and the values involved.
4. Work upwards through earlier calls if the source of the value is not obvious.

Tracebacks are diagnostic evidence, not merely failure notices. Avoid replacing them with a vague message until you understand the problem being handled.

## Why is there an exception hierarchy?

Python groups related exception classes into a hierarchy. You do not need to understand object-oriented inheritance yet. At this stage, treat the hierarchy as a family tree of categories: a broader category can represent several more specific exception types.

A simplified view is:

```text
BaseException
├── KeyboardInterrupt
├── SystemExit
└── Exception
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── OSError
    │   └── FileNotFoundError
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── AssertionError
    ├── NameError
    ├── TypeError
    └── ValueError
```

Most application-level exceptions derive from `Exception`. System-exiting events such as `KeyboardInterrupt` and `SystemExit` sit directly under `BaseException`, which is one reason ordinary handling code normally catches `Exception` rather than `BaseException`.

More specific handlers should appear before broader ones:

```python
try:
    value = int(input("Enter a divisor: "))
    print(10 / value)
except ValueError:
    print("Please enter a whole number.")
except ZeroDivisionError:
    print("The divisor cannot be zero.")
except Exception:
    print("An unexpected problem occurred.")
```

If `except Exception` came first, it would also match the more specific application exceptions, making the later handlers unreachable.

## “Error” and “exception” in Python

Python built-in names include both `TypeError` and `Exception`, but the everyday terms do not divide neatly into “serious error” and “recoverable exception.” Many classes whose names end in `Error` derive from `Exception` and can be caught.

A more useful question is whether the current part of the program can respond meaningfully:

- Invalid interactive input may be handled by explaining and reprompting.
- A missing optional file might use a default.
- A programmer's misspelled variable name should normally be fixed, not hidden.
- An unexpected system-level failure may need to propagate or terminate safely.

## Ask permission or ask forgiveness?

Some situations can be handled by checking first:

```python
if "Sam" in student_ids:
    print(student_ids["Sam"])
```

Others naturally use exception handling:

```python
try:
    mark = int(user_text)
except ValueError:
    print("That is not a whole number.")
```

Neither approach is universally superior. Use a direct condition for an ordinary expected branch when it is clear and reliable. Use exception handling around operations whose failure is naturally reported by an exception, especially when checking separately would duplicate work or introduce a timing gap.

## Pause and classify

Classify each example as a syntax error, runtime exception, or logic error:

```python
print("Hello"
```

```python
price = "12.50"
total = price + 5
```

```python
width = 5
height = 4
area = width + height
```

For the runtime exception, predict its type before running it.

## Common misconceptions

- Not every unwanted result raises an exception; logic errors may run successfully.
- A `try` block cannot rescue malformed syntax in the same source code.
- Exception names ending in `Error` are not automatically uncatchable.
- User mistakes are not the only source of exceptions.
- The hierarchy does not need to be memorised before using `try` and `except`.
- Catching every exception is not the same as handling every problem.
- `BaseException` is normally too broad for application code.

## Check your understanding

1. What happens when an exception is raised and not handled?
2. How does a syntax error differ from a runtime exception?
3. Which exception is likely when `int("abc")` runs?
4. Which exception is likely for a missing dictionary key?
5. Why should specific handlers precede `except Exception`?
6. What is the first useful place to read in a traceback?

## Try it yourself

Run small examples that deliberately produce `TypeError`, `ValueError`, `ZeroDivisionError`, `IndexError`, and `KeyError`. For each one:

1. record the final traceback line;
2. identify the failing operation;
3. explain whether user input, program data, or a coding defect caused it;
4. decide whether the program should handle it or the developer should fix it.

## Page summary

Exceptions represent problems encountered during execution. They differ from parsing failures and from incorrect results that raise nothing. Python provides specific exception types and groups related types into a hierarchy, but beginners need only recognise the practical categories. A traceback identifies the exception and the path to the failing instruction.

**Next:** Continue to **Page 2: `try`, `except`, `else`, `finally`, and `raise`**.

---

# Page 2: `try`, `except`, `else`, `finally`, and `raise`

## On this page

- Handling an anticipated exception
- Catching specific exception types
- Multiple handlers
- Exception objects and useful messages
- `else` and `finally`
- Repeated input validation
- Raising exceptions from functions

## Learning outcomes

By the end of this page, you should be able to:

- wrap a risky operation in `try` and handle a specific exception;
- provide different responses for different failures;
- access an exception object's message;
- use `else` for code that requires successful completion;
- use `finally` for cleanup that must run;
- reprompt until valid input is received;
- raise an appropriate built-in exception when a function's requirements are violated.

## Handling one anticipated exception

Place only the operation that may fail inside `try`, then name the exception that can be handled:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("A number cannot be divided by zero.")
```

When division raises `ZeroDivisionError`, Python stops the remaining instructions in the `try` block and runs the matching handler.

Keep the protected region focused:

```python
try:
    divisor = int(input("Enter a divisor: "))
except ValueError:
    print("Please enter a whole number.")
else:
    print(10 / divisor)
```

This is not yet complete because division can still fail when `divisor` is zero. It illustrates that only exceptions covered by suitable handlers are handled.

## Multiple exception handlers

Different exceptions often require different messages or recovery:

```python
try:
    divisor = int(input("Enter a divisor: "))
    result = 10 / divisor
except ValueError:
    print("Please enter a whole number.")
except ZeroDivisionError:
    print("Please enter a non-zero divisor.")
else:
    print(f"Result: {result}")
```

Separate handlers improve the user's guidance and document the failures the developer anticipated.

If several exception types genuinely need the same response, group them in a tuple:

```python
try:
    value = records[user_key]
except (KeyError, TypeError):
    print("That key could not be used.")
```

Do not group unrelated failures simply to shorten the program.

## Avoid bare `except`

A bare handler catches almost everything, including interrupts used to stop a program:

```python
try:
    value = int(input("Enter a number: "))
except:
    print("Something went wrong.")
```

This is usually too broad. It hides the exception type, can conceal coding defects, and makes debugging difficult.

Prefer the expected type:

```python
except ValueError:
    print("Please enter a whole number.")
```

At an application boundary, `except Exception` may be used for logging or controlled shutdown, but it should not replace understanding and specific handling.

## The exception object

Use `as` to bind the exception object to a name:

```python
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print(f"Calculation failed: {error}")
```

`str(error)` provides its human-readable message. `repr(error)` gives a developer-oriented representation, while `error.args` stores constructor arguments. These can assist diagnostics, but raw technical messages are not always appropriate user guidance.

A good pattern separates audiences:

- tell the user how to correct their action;
- record technical detail in a log for developers;
- avoid exposing sensitive system paths or internal data.

## The `else` clause

`else` runs only when the `try` block completes without an exception:

```python
try:
    number = int(input("Enter a whole number: "))
except ValueError:
    print("That was not a whole number.")
else:
    print(f"You entered {number}.")
```

Placing the success-only instruction in `else` avoids accidentally catching exceptions it may raise.

Python does not create block scope for `try`, so a successfully assigned name remains accessible afterwards. However, if conversion fails, `number` is never assigned:

```python
try:
    number = int(input("Enter a whole number: "))
except ValueError:
    print("Invalid input")

print(number)  # NameError if assignment did not complete
```

Use `else`, return from a function, or initialise deliberately rather than relying on a name that may not exist. A notebook's retained state can mask this bug if `number` was created in an earlier cell; restart and run all cells when checking notebook correctness.

## The `finally` clause

`finally` runs whether the protected operation succeeds or raises an exception. It is used for cleanup:

```python
file = None

try:
    file = open("data.txt", "r")
    contents = file.read()
except FileNotFoundError:
    print("The data file was not found.")
finally:
    if file is not None:
        file.close()
```

For files, a context manager is normally clearer and closes the file automatically:

```python
try:
    with open("data.txt", "r") as file:
        contents = file.read()
except FileNotFoundError:
    print("The data file was not found.")
```

`finally` remains important for resources and state that require cleanup when no suitable context manager is available.

## Reprompting until input is valid

Exception handling can be combined with a loop:

```python
while True:
    try:
        number = int(input("Enter a whole number: "))
    except ValueError:
        print("That is not a whole number. Please try again.")
    else:
        break

print(f"Accepted value: {number}")
```

The loop repeats after invalid input. Successful conversion reaches `else`, and `break` exits the loop.

A reusable function can return directly:

```python
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
```

`return` ends the function, so no separate `break` is necessary.

## Input conversion details

`input()` always returns a string. Therefore:

- `int("12")` succeeds;
- `int("12.5")` raises `ValueError`;
- `int("True")` raises `ValueError`;
- `float("12.5")` succeeds.

Keyboard input cannot directly return the Boolean object `True`; it returns the characters typed. Converting arbitrary non-empty text with `bool()` is also not a validity check:

```python
print(bool("False"))   # True, because the string is non-empty
```

Parse accepted words explicitly when Boolean input is needed.

## Raising an exception

Sometimes a function detects a value that is syntactically valid but violates its requirements. Use `raise` to report that failure:

```python
def withdraw(amount, balance):
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    if amount > balance:
        raise ValueError("Insufficient funds.")
    return balance - amount
```

The function communicates that no valid result can be produced. Calling code decides how to handle it:

```python
try:
    new_balance = withdraw(100, 50)
except ValueError as error:
    print(error)
else:
    print(f"New balance: £{new_balance:.2f}")
```

Use exception types consistently:

- `TypeError` when an argument has an inappropriate type;
- `ValueError` when its type is acceptable but its value is invalid;
- a more specific built-in exception when one accurately describes the problem.

For division by zero, Python normally raises `ZeroDivisionError` itself. If validating beforehand, raising that same type preserves the conventional meaning:

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisor cannot be zero.")
    return a / b
```

## Optional look ahead: custom exception classes

Larger applications sometimes define domain-specific exception types:

```python
class InsufficientFundsError(Exception):
    pass
```

This syntax uses classes and inheritance, which will be taught during object-oriented programming. For now, recognise only the purpose: a custom name can let callers distinguish a domain rule from a general `ValueError`.

Built-in exceptions are sufficient for this lecture's practical work. Detailed custom-class design and exception chaining belong more naturally after OOP.

## Pause and predict

Suppose the user enters `zero`, then `0`, then `5`. Trace which handler or clause runs on each attempt:

```python
while True:
    try:
        divisor = int(input("Enter a divisor: "))
        result = 10 / divisor
    except ValueError:
        print("Whole numbers only.")
    except ZeroDivisionError:
        print("Zero is not permitted.")
    else:
        print(result)
        break
```

## Common mistakes

- Protecting a large block when only one or two operations are expected to fail.
- Using bare `except` and hiding programmer defects.
- Placing `except Exception` before specific handlers.
- Giving every exception the same vague message.
- Assuming a name was assigned when the assignment itself failed.
- Expecting `else` to run after an exception was handled.
- Using `bool(user_text)` to interpret the words `True` and `False`.
- catching an exception and immediately raising the same issue without adding value.

## Check your understanding

1. When does an `except` block run?
2. When does the `else` clause run?
3. When does `finally` run?
4. Why is a bare `except` usually undesirable?
5. What is the difference between handling and raising an exception?
6. Which exception type suits an unacceptable numeric value?
7. Why can a notebook hide an unassigned-variable bug?

## Apply your learning

1. Write `get_integer(prompt)` so it reprompts after non-integer input.
2. Ask for two integers and divide the first by the second, handling invalid text and zero separately.
3. Define `validate_age(age)` that raises `TypeError` for a non-integer and `ValueError` for an implausible range. Catch these around the function call.
4. Safely retrieve an index from a list, considering conversion errors and out-of-range indexes.
5. Create a food-price dictionary and functions that add and remove entries while reporting invalid keys, invalid prices, and missing products appropriately.

## Page summary

`try` protects operations that may raise; specific `except` clauses handle anticipated types. `else` contains success-only work, while `finally` guarantees cleanup. Loops enable reprompting, and functions can `raise` appropriate built-in exceptions when their requirements are violated. Catch only failures that the current code can handle meaningfully.

**Previous:** Page 1: Exception Theory and the Hierarchy  
**Next:** Continue to **Page 3: `pass`, `break`, `continue`, and `return`**.

---

# Page 3: `pass`, `break`, `continue`, and `return`

## On this page

- Why these keywords are not exception handlers
- `pass` as an empty statement
- `break` for terminating a loop
- `continue` for starting the next iteration
- `return` for ending a function
- Control flow in input-validation loops
- Avoiding silent failure

## Learning outcomes

By the end of this page, you should be able to:

- explain the distinct purposes of `pass`, `break`, `continue`, and `return`;
- use `break` to terminate a validation loop;
- use `continue` to retry explicitly;
- use `return` to end a function with a result;
- identify when `pass` hides a failure;
- trace control flow through a loop containing exception handling.

## Control-flow keywords and exceptions

`pass`, `break`, `continue`, and `return` do not catch exceptions. They control what Python does next after execution reaches them.

| Keyword | Valid context | Effect |
|---|---|---|
| `pass` | Any statement block | Do nothing and continue normally |
| `break` | Loop | Exit the nearest loop |
| `continue` | Loop | Start the next iteration |
| `return` | Function | End the function and optionally return a value |

They often appear near `try` and `except` during validation, but their meanings remain independent.

## `pass`: an intentional empty statement

Python requires a statement inside a block. `pass` provides a placeholder that performs no action:

```python
def function_to_complete_later():
    pass
```

It can also represent an intentionally empty branch:

```python
if feature_enabled:
    pass  # implementation will be added later
```

The comment explains why the empty block exists.

## The danger of `pass` in an exception handler

This code silently ignores invalid input and repeats:

```python
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
```

It technically works, but the user receives no explanation. More seriously, broad silent handlers can conceal defects:

```python
try:
    perform_important_operation()
except Exception:
    pass
```

The program now hides every ordinary exception from that call. Silent handling should be rare and deliberate. At minimum, consider:

- giving the user actionable guidance;
- logging the technical failure;
- catching a narrower type;
- allowing the exception to propagate.

For interactive validation, feedback is usually better:

```python
except ValueError:
    print("Please enter a whole number.")
```

## `break`: exit the nearest loop

`break` immediately exits the nearest containing `for` or `while` loop:

```python
while True:
    user_text = input("Type quit to finish: ")
    if user_text.lower() == "quit":
        break
    print(f"You entered: {user_text}")
```

Execution continues with the first instruction after the loop.

In an input-validation loop:

```python
while True:
    try:
        number = int(input("Enter a whole number: "))
    except ValueError:
        print("Invalid input.")
    else:
        break

print(number)
```

`break` runs only after successful conversion because it is inside `else`.

## `continue`: start the next iteration

`continue` skips the remainder of the current iteration and returns to the loop condition or next item:

```python
for number in range(-2, 3):
    if number == 0:
        continue
    print(10 / number)
```

This avoids division when the current value is zero.

It can make retry behaviour explicit:

```python
while True:
    try:
        number = int(input("Enter a positive integer: "))
    except ValueError:
        print("Whole numbers only.")
        continue

    if number <= 0:
        print("The number must be positive.")
        continue

    break
```

At the end of a loop body, `continue` may be unnecessary because the next iteration would begin anyway. Use it when it clarifies that no later instructions in the current iteration should run.

## `return`: exit a function

`return` ends the current function and supplies an optional result to the caller:

```python
def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Whole numbers only.")
            continue

        if number > 0:
            return number

        print("The number must be positive.")
```

The successful `return` exits both the loop and the function. This differs from `break`, which exits only the loop and remains in the function.

Compare:

```python
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
    return None
```

When an even value is found, no further loop iterations or function instructions run.

## Loop `else`

Python loops can have an `else` clause. It runs when the loop finishes normally, but not when `break` exits it:

```python
numbers = [1, 3, 5, 8, 9]

for number in numbers:
    if number % 2 == 0:
        print(f"Found {number}")
        break
else:
    print("No even number found")
```

This `else` belongs to the `for` loop, not to an `if` statement or `try` block. It is useful for search loops but can surprise readers, so keep the structure simple.

## Trace the flow explicitly

Consider:

```python
def read_mark():
    while True:
        try:
            mark = int(input("Enter a mark from 0 to 100: "))
        except ValueError:
            print("Enter a whole number.")
            continue

        if not 0 <= mark <= 100:
            print("Mark must be from 0 to 100.")
            continue

        return mark
```

The possible routes are:

```text
Input
├── conversion fails → except → message → continue
├── number outside range → if → message → continue
└── valid number → return from function
```

This separates two problems:

- exception handling deals with text that cannot become an integer;
- ordinary selection deals with an integer outside the permitted range.

An invalid value does not always need to become an exception. A condition is often clearer when the current function can respond directly.

## Avoid exceptions for ordinary loop termination

Do not deliberately cause `IndexError` to finish a normal iteration:

```python
values = list(range(10))

index = 0
while True:
    try:
        print(values[index])
        index += 1
    except IndexError:
        break
```

Use the sequence's iteration protocol:

```python
for value in values:
    print(value)
```

Exceptions are valuable for exceptional or operation-specific failures. Normal sequence traversal already has a clearer construct.

## Pause and predict

For each keyword, identify where execution continues:

```python
for number in range(5):
    if number == 1:
        continue
    if number == 3:
        break
    print(number)
```

Then predict the output before running it. Would replacing `break` with `return` be valid at the top level? Why not?

## Common mistakes

- Believing `pass` catches or resolves an exception.
- Silently ignoring broad exceptions.
- Using `break` outside a loop.
- Expecting `break` to exit the containing function.
- Using `continue` outside a loop.
- Placing necessary cleanup after `continue` where it will be skipped.
- Forgetting that `return` ends the entire function immediately.
- using exceptions to control ordinary iteration when a `for` loop is clearer.

## Check your understanding

1. What does `pass` do?
2. What is the difference between `break` and `continue`?
3. How does `return` differ from `break` inside a function loop?
4. Why is `except Exception: pass` risky?
5. When does a loop's `else` clause run?
6. Why should normal list traversal not depend on `IndexError`?

## Apply your learning

1. Trace a validation loop on paper for invalid text, an out-of-range integer, and a valid integer.
2. Write a function that repeatedly asks for a mark from 0 to 100 and returns the first valid result.
3. Search a list for the first negative number using `break`, then implement the same search as a function using `return`.
4. Modify a loop to skip zeros using `continue` before performing division.
5. Find one earlier use of `pass` in your practical code and decide whether a message, log, narrower handler, or propagated exception would be better.

## Page summary

`pass` is an empty statement, `break` exits the nearest loop, `continue` begins its next iteration, and `return` exits a function. They are control-flow tools rather than exception handlers. Used with focused exception handling and ordinary conditions, they support clear validation loops; used indiscriminately, they can hide failures or make execution difficult to follow.

**Previous:** Page 2: `try`, `except`, `else`, `finally`, and `raise`  
**Next:** Continue to **Page 4: Assertions**.

---

# Page 4: Assertions

## On this page

- Expressing programmer assumptions
- The `assert` statement
- `AssertionError`
- Preconditions, postconditions, and invariants
- Assertions compared with validation and exceptions
- Assertions in tests
- Why essential checks must not depend on `assert`

## Learning outcomes

By the end of this page, you should be able to:

- write an assertion containing a condition and diagnostic message;
- explain when `AssertionError` is raised;
- use assertions to state internal assumptions during development;
- distinguish assertions from user-input validation;
- explain why assertions must not enforce essential runtime rules;
- recognise how tests provide a more systematic verification approach.

## What is an assertion?

An assertion states a condition that the programmer believes must be true at a particular point in the program:

```python
x = 10
assert x > 5
```

Python evaluates the expression:

- if it is truthy, execution continues;
- if it is falsy, Python raises `AssertionError`.

```python
x = 5
assert x > 10
```

Assertions make assumptions executable. When an assumption fails during development, the failure directs attention to a likely defect in the program or test setup.

## Adding a diagnostic message

Supply a message after a comma:

```python
total = 15
count = 0
assert count > 0, "count must be positive before calculating a mean"
mean = total / count
```

The message should explain the violated assumption, not merely repeat “assertion failed.”

Avoid placing function calls with required side effects inside an assertion. If assertions are disabled, the expression is not evaluated.

## Preconditions, postconditions, and invariants

Assertions can document several kinds of internal expectation.

### Precondition

Something expected to be true when an internal operation begins:

```python
def midpoint_of_nonempty_sorted(values):
    assert values, "values must not be empty"
    assert values == sorted(values), "values must already be sorted"
    return values[len(values) // 2]
```

This is appropriate only if callers are internal code that has already established these conditions. A public-facing function may need explicit validation instead.

### Postcondition

Something expected to be true after an operation:

```python
result = sorted(values)
assert result == sorted(result), "result should be sorted"
```

### Invariant

A relationship expected to remain true at a particular stage:

```python
assert balance >= 0, "internal balance invariant violated"
```

If ordinary users or external data can legitimately trigger the condition, explicit handling is usually more appropriate than an assertion.

## Assertions are for programmer assumptions

This is a tempting but unsafe validation design:

```python
def withdraw(amount, balance):
    assert amount <= balance, "Insufficient funds"
    return balance - amount
```

A user requesting too much money is an expected runtime possibility, not necessarily a programmer defect. It should use an ordinary condition and exception or return result:

```python
def withdraw(amount, balance):
    if amount > balance:
        raise ValueError("Insufficient funds.")
    return balance - amount
```

Similarly, do not use `assert` as the only check for:

- user-entered marks or ages;
- authentication or authorisation;
- financial limits;
- file or network data;
- public function arguments;
- any requirement needed for safety or correctness in production.

## Assertions can be disabled

Python normally enables assertions, but the `-O` optimisation option removes assert statements:

```text
python -O program.py
```

The special constant `__debug__` is normally `True` and becomes `False` under optimisation. Since essential behaviour cannot depend on interpreter options, assertions are not a substitute for validation or error handling.

This also means the assertion expression and message should not perform necessary work.

## Validation, exceptions, and assertions compared

| Mechanism | Best suited to | Example |
|---|---|---|
| `if` / selection | Ordinary expected alternatives | Mark is within a range |
| `raise` | A function cannot fulfil its contract | Invalid public argument |
| `try` / `except` | An operation reports a failure | Numeric conversion fails |
| `assert` | An internal programmer assumption | An earlier step must have sorted data |
| Test assertion | Verifying expected behaviour externally | Function output equals known result |

The same condition may appear in different places for different purposes. A function can explicitly validate a public argument, while its tests assert that invalid arguments raise the promised exception.

## Improving the `average()` exercise

The notebook proposes assertions about a list. As a learning exercise, assertions can reveal assumptions:

```python
def average_for_internal_use(numbers):
    assert isinstance(numbers, list), "numbers should be a list"
    assert numbers, "numbers should not be empty"
    assert all(
        isinstance(number, (int, float)) and not isinstance(number, bool)
        for number in numbers
    ), "every element should be an int or float"

    return sum(numbers) / len(numbers)
```

The explicit Boolean exclusion matters because `bool` is a subclass of `int` in Python, so `isinstance(True, int)` is `True`.

For a reusable public function, explicit exceptions are more reliable:

```python
def average(numbers):
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    if not numbers:
        raise ValueError("numbers must not be empty")
    if not all(
        isinstance(number, (int, float)) and not isinstance(number, bool)
        for number in numbers
    ):
        raise TypeError("every element must be an int or float")

    return sum(numbers) / len(numbers)
```

This distinction is more important than mechanically replacing every check with `assert`.

## Assertions in testing

Tests use assertion-style checks to compare actual behaviour with expected behaviour:

```python
def get_grade(mark):
    if not 0 <= mark <= 100:
        raise ValueError("mark must be from 0 to 100")
    if mark >= 70:
        return "A"
    if mark >= 60:
        return "B"
    if mark >= 50:
        return "C"
    if mark >= 40:
        return "D"
    if mark >= 35:
        return "E"
    return "F"


assert get_grade(70) == "A"
assert get_grade(69) == "B"
assert get_grade(40) == "D"
```

These checks are useful for exploration, but a testing framework such as `pytest` provides discovery, reporting, isolation, and explicit facilities for checking exceptions. Formal unit testing will be introduced later.

Boundary values deserve particular attention. A grade function should be checked immediately below, at, and above each threshold.

## Testing that an exception occurs

Without a test framework, a small teaching check can use `try`:

```python
try:
    get_grade(101)
except ValueError:
    pass
else:
    raise AssertionError("get_grade(101) should raise ValueError")
```

This is one context in which `pass` is intentional: receiving the expected exception means no additional action is needed. A testing framework makes the intent clearer:

```python
# Later, with pytest:
# with pytest.raises(ValueError):
#     get_grade(101)
```

## Pause and decide

For each condition, decide whether an ordinary `if`, an explicitly raised exception, an internal assertion, or a test assertion is most appropriate:

1. A user enters `"forty"` for a mark.
2. A withdrawal exceeds the available balance.
3. An internal sorting function reaches a stage that should already be ordered.
4. A test checks that `get_grade(70)` returns `"A"`.
5. An API supplies a required field in the wrong type.

More than one mechanism may appear in the complete solution, but identify the primary responsibility at each boundary.

## Common misconceptions

- Assertions are not a general substitute for validation.
- `AssertionError` does not automatically mean the user made a mistake.
- Essential business and security rules must not depend on `assert`.
- Assertions may be removed under optimisation.
- Assertion expressions should not perform required side effects.
- `isinstance(True, int)` is `True`, so Boolean values need explicit exclusion when inappropriate.
- A handful of inline assertions is not a complete testing strategy.

## Check your understanding

1. What happens when an assertion expression is false?
2. What kind of assumption should an assertion represent?
3. Why should user-input validation not rely on `assert`?
4. What effect can `python -O` have?
5. How does an assertion inside production code differ from an assertion in a test?
6. Why might a numeric validation check exclude `bool` explicitly?

## Apply your learning

1. Add diagnostic assertions to a small internal calculation and deliberately violate each assumption.
2. Implement a reliable public `average(numbers)` using explicit exceptions for the wrong container type, an empty list, and non-numeric elements.
3. Implement `get_grade(mark)` with explicit range validation.
4. Write boundary assertions for every grade threshold.
5. Explain which of your checks are required at runtime and which exist to detect developer mistakes.

## Page summary

Assertions make programmer assumptions executable and raise `AssertionError` when those assumptions fail. They can document preconditions, postconditions, and invariants during development, and assertion-style checks underpin testing. Because assertions may be disabled, essential validation and business rules require ordinary conditions and explicit exceptions.

**Previous:** Page 3: `pass`, `break`, `continue`, and `return`  
**Next step:** Complete the Exceptions practical notebook, testing valid input, invalid formats, boundary values, missing lookups, and deliberately raised exceptions.

---

# Suggested VLE setup

Create one learning module titled **5 Python Exceptions**, containing:

1. **Start here: overview and learning outcomes**
2. **5.1 Exception Theory and the Hierarchy**
3. **5.2 `try`, `except`, `else`, `finally`, and `raise`**
4. **5.3 `pass`, `break`, `continue`, and `return`**
5. **5.4 Assertions**
6. **Exceptions practical notebook**
7. **Check your learning**

Add previous/next navigation and use each second-level heading in the page contents.

Keep the hierarchy at recognition level. Custom exception classes, explicit inheritance, exception chaining, traceback internals, and detailed Java comparisons should be moved to the later OOP or advanced error-handling material. A short custom-exception preview remains on Page 2 so students recognise the idea without needing to design class hierarchies.
