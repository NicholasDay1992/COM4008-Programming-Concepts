# COM4008 Programming Concepts: Imports, Python Programs and File I/O

This content is designed as three linked VLE information pages. Lecture 6 marks a transition from working mainly inside notebooks to organising and running programs stored in `.py` files.

---

# Page 1: Imports and Modules

## On this page

- Why programs are divided into modules
- Modules, packages, libraries, and frameworks
- Importing modules and names
- Namespaces and aliases
- Creating and importing your own module
- Import paths and import side effects
- Exploring module documentation

## Learning outcomes

By the end of this page, you should be able to:

- explain why reusable code is organised into modules;
- distinguish modules, packages, libraries, and frameworks at an introductory level;
- use `import` and `from ... import ...` appropriately;
- call imported functions through a module namespace;
- create a simple `.py` module and import it elsewhere;
- explain why imported files should avoid unintended top-level activity.

## From one notebook to several files

A notebook is useful for explanation, experimentation, and immediate feedback. As programs grow, keeping every function and instruction in one notebook or script becomes difficult to navigate and reuse.

Python lets us divide a program into **modules**. A module is normally a `.py` file containing related definitions and statements. For example:

```text
program/
├── main.py
├── input_utils.py
└── file_utils.py
```

`input_utils.py` might contain reusable input-validation functions, while `file_utils.py` contains file-reading and writing functions. `main.py` coordinates them into an application.

This supports **separation of concerns**: each part has a focused responsibility.

## Module, package, library, and framework

These terms overlap in everyday discussion, but the following distinctions are useful:

| Term | Introductory meaning |
|---|---|
| Module | An importable unit, commonly one `.py` file |
| Package | A way of organising related modules under one import name, commonly using a directory |
| Library | Reusable code intended to be called by other programs; it may contain modules and packages |
| Framework | A larger structure that helps organise an application and often calls user-supplied code at defined points |

Modern Python supports several forms of package, so an `__init__.py` file is common and useful but not required for every possible package. At this stage, a normal directory containing `__init__.py` is a clear way to create a regular package.

NumPy is better described as a third-party package and library ecosystem than as merely a group of scripts. Terminology matters less than recognising how to install, import, and use a dependency responsibly.

## Importing a module

Use `import` to make a module available through its namespace:

```python
import math

result = math.sqrt(25)
print(result)
```

`math` identifies the module and `sqrt` identifies a name within it. The qualified form makes the origin of the function visible.

```python
import random

numbers = [1, 2, 3, 4, 5, 6]
random.shuffle(numbers)
print(numbers)
```

`shuffle()` changes the list in place and returns `None`.

## Aliases

An alias provides a shorter local name:

```python
import numpy as np

values = np.array([1, 2, 3])
```

Use established aliases where they are widely understood, such as `np` for NumPy. Avoid obscure abbreviations that make code harder to read.

An alias changes only the name used in the current module. It does not rename the installed package.

## Importing selected names

Use `from` to import a particular name:

```python
from random import randint

number = randint(0, 10)
```

This can be concise, but it hides the module prefix. Compare:

```python
import random
number = random.randint(0, 10)
```

The qualified version immediately shows where `randint` came from. Choose based on clarity and the risk of name collisions.

Avoid wildcard imports:

```python
from random import *
```

They introduce many names without making their origins clear and can overwrite existing names.

## Namespaces prevent collisions

Different modules may define the same function name. Module qualification keeps them separate:

```python
import statistics
import custom_statistics

print(statistics.mean(values))
print(custom_statistics.mean(values))
```

A **namespace** is a mapping from names to objects. `module.name` explicitly selects the name stored in that module's namespace.

## Creating your own module

Create `input_utils.py`:

```python
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
```

Use it from `main.py` in the same project directory:

```python
from input_utils import get_integer

first = get_integer("Enter the first number: ")
second = get_integer("Enter the second number: ")
print(first + second)
```

The module filename becomes the import name without `.py`. Use valid, descriptive Python names such as `input_utils.py`, not spaces or hyphens.

## What happens during import?

The first time a module is imported in a running Python process, Python executes its top-level statements and creates a module object. Function bodies are defined but do not run until called.

This module has an unwanted side effect:

```python
# input_utils.py
print("input_utils has loaded")

def get_integer(prompt):
    return int(input(prompt))

get_integer("Enter a number: ")
```

Importing it unexpectedly prints and requests input. Reusable modules should normally keep top-level work to imports, constants, and definitions. Entry-point behaviour belongs behind a main guard, introduced on Page 2.

Python normally caches imported modules in `sys.modules`, so another import in the same process reuses the existing module rather than executing it again. Notebook development can therefore retain an earlier version after a file changes; restart the kernel or use deliberate reload tools during development.

## How Python locates modules

Python searches locations recorded in `sys.path`:

```python
import sys
print(sys.path)
```

The list normally includes the script directory or working context, standard-library locations, and installed package locations. An import can fail because:

- the module is not installed;
- its file is not in an importable location;
- its filename or import name is misspelled;
- the wrong Python environment is running;
- a local file shadows a standard or installed module.

For example, naming your own file `random.py` can interfere with `import random`.

Do not routinely modify `sys.path` inside beginner programs to hide an unclear project structure. Arrange related files coherently and run the intended Python environment.

## Standard library and third-party dependencies

Modules such as `math`, `random`, `sys`, `json`, `pathlib`, and `argparse` are in Python's standard library. They do not need a separate package installation.

NumPy and Requests are third-party packages. They must be installed into the Python environment running the program. An IDE, notebook kernel, and terminal can accidentally use different environments, so check the selected interpreter when an installed dependency cannot be imported.

## Exploring an imported module

Useful discovery tools include:

```python
import math

print(dir(math))
help(math.sqrt)
print(math.sqrt.__doc__)
```

`dir()` lists names but does not explain how to use them. Prefer `help()` and official documentation for parameters, return values, edge cases, and examples.

## Pause and predict

Suppose `utilities.py` contains:

```python
print("Loading utilities")

def double(number):
    return number * 2
```

What happens when this runs?

```python
import utilities
print(utilities.double(5))
```

Which lines run during import, and which run because of the function call?

## Common mistakes

- Including `.py` in an import statement.
- Giving a module a filename containing spaces or hyphens.
- Naming a local file after a standard-library module.
- Using `from module import *` and obscuring name origins.
- Expecting importing a function to call it automatically.
- Placing interactive or application behaviour at module top level.
- Installing a package in one environment while running another.
- Treating `dir()` as a replacement for documentation.

## Check your understanding

1. What is a Python module?
2. What is the benefit of `math.sqrt()` over importing many names directly?
3. What does an alias change?
4. What top-level code runs during import?
5. Why might a local `random.py` cause trouble?
6. How does a third-party package differ operationally from a standard-library module?

## Apply your learning

1. Import `random`, shuffle a list, and display it before and after.
2. Create `number_utils.py` containing `get_integer()` and `get_total()`.
3. Import both functions into another file and call them.
4. Add a print statement at module level, observe its import side effect, and then remove it.
5. Use `help()` to investigate one standard-library function and record its parameters and return value.

## Page summary

Modules divide programs into reusable, focused units. `import module` preserves a clear namespace, while aliases and selective imports offer controlled convenience. Importing executes a module's top-level statements, so reusable files should avoid unintended activity. Standard-library and third-party modules also differ in whether installation is required.

**Next:** Continue to **Page 2: `main.py`, `__name__`, and Command-Line Arguments**.

---

# Page 2: `main.py`, `__name__`, and Command-Line Arguments

## On this page

- Moving from notebooks to `.py` programs
- Running a script from a terminal
- The `main()` convention
- `__name__` and the main guard
- Designing a testable entry point
- `sys.argv`
- Validating command-line input
- `argparse` for usable command-line interfaces

## Learning outcomes

By the end of this page, you should be able to:

- create and run a `.py` program from a terminal;
- define a `main()` function as an application entry point;
- explain what the main guard prevents;
- pass a controlled list of arguments into `main()`;
- parse and validate simple command-line arguments;
- use `argparse` for a small command-line program;
- distinguish notebook state from script execution.

## From notebook cells to a script

Jupyter notebooks store code in cells that may be run in any order. Names remain in the kernel until it is restarted. This flexibility is useful for exploration but can hide dependencies on earlier execution.

A `.py` script normally begins in a fresh process and executes from top to bottom:

```python
# main.py
print("Hello from main.py")
```

Run it from a terminal whose current directory contains the file:

```text
python main.py
```

Some systems use `python3`:

```text
python3 main.py
```

Use the command configured for the intended environment. In Visual Studio Code, open the integrated terminal and confirm the selected Python interpreter.

## Working directories and paths

The terminal's current working directory affects relative paths. Display it with the platform's terminal command or from Python:

```python
from pathlib import Path
print(Path.cwd())
```

Change directory in the terminal before running the program:

```text
cd "06 Python Imports and File IO"
python main.py
```

Quotation marks are important when a path contains spaces.

The script file's location and the current working directory are related but not identical concepts. Relative file paths usually resolve from the current working directory, a point revisited on Page 3.

## The `main()` convention

Python does not require a specially named main method. Defining `main()` is a useful convention for collecting the application-level sequence:

```python
def main():
    print("Hello from main.py")


main()
```

This runs correctly as a script, but importing the file also calls `main()`. That may be undesirable when another module wants only its definitions.

## `__name__` and the main guard

Python assigns each module a special `__name__` value:

- when a file is executed as the top-level script, `__name__` is `"__main__"`;
- when imported, `__name__` is normally its module name.

Use this convention:

```python
def main():
    print("Hello from main.py")


if __name__ == "__main__":
    main()
```

Now `python main.py` calls `main()`, while `import main` defines the function without running the application automatically.

The guard is not what “routes” Python to the function. It is an ordinary condition comparing a special module name, followed by an explicit call.

## Keep entry points small

`main()` should coordinate focused functions rather than contain every implementation detail:

```python
from number_utils import get_integer, get_total


def main():
    numbers = [1, 2, 3, 4]
    numbers.append(get_integer("Supply a number: "))
    total = get_total(numbers)
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
```

This arrangement separates:

- reusable calculation and input functions;
- application coordination;
- the decision to launch the application.

## Make `main()` testable

Passing data into `main()` avoids hard-wiring all dependencies to global state:

```python
import sys


def main(arguments):
    print(f"Arguments: {arguments}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
```

Here, `main()` receives only user arguments rather than the script filename. Returning an integer provides an exit status: zero conventionally means success. `SystemExit` communicates it to the operating system.

For an introductory program, calling `main(sys.argv[1:])` without an exit code is also acceptable. The key idea is to make dependencies explicit.

## Understanding `sys.argv`

The `sys` module exposes command-line arguments:

```python
import sys
print(sys.argv)
```

For:

```text
python main.py hello world
```

the list is approximately:

```python
["main.py", "hello", "world"]
```

`sys.argv[0]` identifies the script invocation, while subsequent elements are arguments. Every element is a string.

In a notebook, `sys.argv` belongs to the notebook kernel process and can contain launcher options unrelated to your program. Command-line behaviour should be tested by running the `.py` script in a terminal.

## Parse and validate arguments

For:

```text
python main.py 1 2 3 4
```

the numbers initially arrive as strings. Convert them deliberately:

```python
import sys


def main(arguments):
    try:
        numbers = [int(argument) for argument in arguments]
    except ValueError:
        print("Every argument must be a whole number.")
        return 1

    if not numbers:
        print("Supply at least one number.")
        return 1

    print(numbers)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
```

This connects Lecture 6 to exception handling: conversion can fail, while absence is an ordinary condition.

## Quoting command-line values

Shells split arguments at spaces unless values are quoted:

```text
python main.py "Ada Lovelace" "Grace Hopper"
```

This supplies two names. Commas outside quotes are normally literal characters, not Python list separators. For example:

```text
python main.py "Nick", "Charlie", "Sam"
```

may include commas in the arguments depending on the shell. Prefer space-separated quoted arguments without commas.

Command-line arguments are already strings. Checking that a supplied name “is a string” does not validate that it is a plausible name. Validate meaningful constraints such as non-empty content or allowed characters if the problem requires them.

## `argparse`

Manual `sys.argv` processing becomes awkward as an interface grows. The standard-library `argparse` module provides parsing, conversion, help messages, and error reporting:

```python
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Display information about a file."
    )
    parser.add_argument("filename", help="File to process")
    parser.add_argument(
        "--uppercase",
        action="store_true",
        help="Display text in uppercase",
    )
    return parser.parse_args()


def main():
    arguments = parse_arguments()
    print(arguments.filename)
    print(arguments.uppercase)


if __name__ == "__main__":
    main()
```

Example invocations:

```text
python main.py data.txt
python main.py data.txt --uppercase
python main.py --help
```

`argparse` can convert types:

```python
parser.add_argument("numbers", nargs="+", type=int)
```

`nargs="+"` requires one or more values, and `type=int` reports invalid integers through the command-line interface.

## Avoid importing `main` just to run it

This notebook pattern works:

```python
from main import main
main()
```

However, it is not the same as testing how a script behaves from the terminal. It bypasses shell argument parsing and shares notebook state. Use direct function calls for function-level testing, and execute `python main.py ...` for entry-point and command-line testing.

## Pause and predict

Given:

```python
# main.py
print(f"Module name: {__name__}")

def main():
    print("Application started")

if __name__ == "__main__":
    main()
```

Predict the output when:

1. running `python main.py`;
2. running `import main` from another Python file.

Why does only one route print `Application started`?

## Common mistakes

- Believing Python requires a `main()` method.
- Calling `main()` unconditionally in an importable module.
- Forgetting that command-line arguments are strings.
- Reading `sys.argv[1]` without checking its length.
- Assuming notebook `sys.argv` represents the intended program arguments.
- Including commas when supplying separate shell arguments.
- Confusing the script directory with the current working directory.
- Putting every application detail inside `main()`.

## Check your understanding

1. How does script execution differ from notebook cell execution?
2. What value does `__name__` have for the top-level script?
3. What does the main guard prevent during import?
4. What is stored at `sys.argv[0]`?
5. Which type does every `sys.argv` element initially have?
6. Why is `argparse` preferable for a larger interface?

## Apply your learning

1. Create `main.py` with a guarded `main()` and run it in a terminal.
2. Accept one or more integer arguments, convert them, shuffle them, and display the result.
3. Handle no arguments and invalid integers clearly.
4. Accept several quoted student names and collect a validated mark for each.
5. Rebuild one exercise using `argparse`, including `--help` output.

## Page summary

Scripts execute afresh from top to bottom, while notebooks retain interactive state. `main()` is a useful convention, and the `__name__` guard ensures application behaviour runs only when the file is the top-level script. `sys.argv` supplies string arguments; validation or `argparse` turns them into a reliable interface.

**Previous:** Page 1: Imports and Modules  
**Next:** Continue to **Page 3: File Handling (I/O)**.

---

# Page 3: File Handling (I/O)

## On this page

- Persistent data and file paths
- Opening files safely
- Read, write, append, and exclusive-create modes
- Text encodings
- Reading methods and the file cursor
- Writing lines
- Exceptions and validation
- Serialising dictionaries with JSON
- Organising file utilities

## Learning outcomes

By the end of this page, you should be able to:

- explain why files provide persistence beyond a program run;
- use a context manager to open and close a text file safely;
- choose an appropriate file mode;
- read an entire file, one line, or iterate over lines;
- write and append text deliberately;
- handle common file-related exceptions;
- use `pathlib` to construct and inspect paths;
- save and reload structured dictionary data using JSON.

## Why use files?

Variables and collections normally exist only while a program is running. A file stores data persistently so that it can be used later or shared with another program.

File I/O means **input and output** involving files:

- input: reading data from a file into a program;
- output: writing program data to a file.

Files are external resources. They may be missing, inaccessible, moved, malformed, or changed by another process, so file code needs clear paths, safe resource management, and appropriate error handling.

## Open files with a context manager

The recommended pattern is:

```python
with open("message.txt", "r", encoding="utf-8") as file:
    contents = file.read()

print(contents)
```

`open()` returns a file object. The `with` statement closes it automatically when the block ends, even if an exception occurs.

Without `with`, the programmer must close it explicitly:

```python
file = open("message.txt", "r", encoding="utf-8")
contents = file.read()
file.close()
```

Forgetting to close files can waste resources and delay buffered writes.

## File modes

| Mode | Purpose | If file is absent | Important behaviour |
|---|---|---|---|
| `"r"` | Read | Raises `FileNotFoundError` | Does not modify file |
| `"w"` | Write | Creates it | Truncates existing contents |
| `"a"` | Append | Creates it | Writes at the end |
| `"x"` | Exclusive create | Creates it | Raises `FileExistsError` if present |

Modes may include `b` for binary data or `+` for reading and writing, but text modes are sufficient for the core work.

Be especially careful with `"w"`: opening an existing file successfully erases its previous contents before new writing begins.

## Text encoding

Text must be encoded as bytes when stored. Specify an encoding explicitly:

```python
with open("message.txt", "w", encoding="utf-8") as file:
    file.write("Hello £ — こんにちは")
```

UTF-8 is a widely used Unicode encoding. Explicit encoding makes behaviour more predictable across operating systems.

Binary files such as images use binary modes such as `"rb"` and return bytes rather than strings. Do not decode arbitrary binary files as text.

## Writing and appending

`write()` writes a string and returns the number of characters written:

```python
with open("message.txt", "w", encoding="utf-8") as file:
    count = file.write("Hello from Python\n")

print(count)
```

`write()` does not add a newline automatically. Include `\n` where required.

Append without replacing existing content:

```python
with open("message.txt", "a", encoding="utf-8") as file:
    file.write("An additional line\n")
```

Write several strings with `writelines()`:

```python
lines = ["First\n", "Second\n", "Third\n"]

with open("message.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
```

`writelines()` also does not invent newline characters.

## Reading methods

Read all remaining text:

```python
with open("message.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

Read one line:

```python
with open("message.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
```

Read all lines into a list:

```python
with open("message.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
```

For large text files, iterate without loading everything at once:

```python
with open("message.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip("\n"))
```

## The file cursor

A file object tracks its current position. After `read()` reaches the end, another `read()` returns an empty string:

```python
with open("message.txt", "r", encoding="utf-8") as file:
    first = file.read()
    second = file.read()

print(repr(second))   # ''
```

Use `seek(0)` to return to the beginning when genuinely necessary:

```python
file.seek(0)
```

Often it is clearer to retain the text already read or reopen the file in a new context.

## File objects and file contents are different

This returns a file object:

```python
file = open("message.txt", "r", encoding="utf-8")
print(type(file))
file.close()
```

`str(file)` produces a description of that object, not the text stored in the file. Call `read()` to obtain a string:

```python
with open("message.txt", "r", encoding="utf-8") as file:
    file_text = file.read()

print(type(file_text))   # str
```

String operations can then process the content:

```python
words = file_text.split()
position = file_text.find("Python")
uppercase = file_text.upper()
```

## Paths with `pathlib`

The standard-library `pathlib` module represents paths as objects:

```python
from pathlib import Path

path = Path("data") / "message.txt"
print(path)
print(path.exists())
print(path.suffix)
```

Create parent directories when appropriate:

```python
path.parent.mkdir(parents=True, exist_ok=True)
```

Relative paths resolve from the process's current working directory. To locate a file relative to a script itself:

```python
BASE_DIR = Path(__file__).resolve().parent
path = BASE_DIR / "data" / "message.txt"
```

`__file__` is normally available in `.py` modules but not in the same way in every notebook environment. Notebooks should use a deliberate project path or `Path.cwd()`.

## Handling file exceptions

Catch failures that can be explained or recovered from:

```python
from pathlib import Path


def read_text(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except PermissionError:
        print(f"Permission denied: {path}")
        return None
    except UnicodeDecodeError:
        print(f"The file is not valid UTF-8 text: {path}")
        return None
```

Alternatively, let a reusable utility propagate the exception and handle it at the user-interface boundary. Returning `None` requires the caller to distinguish failure from valid content deliberately.

`OSError` is a broad parent category for many operating-system and I/O failures. Catch specific subclasses when responses differ.

## Validate intent, not just filename suffixes

This rule may be useful for a deliberately text-only exercise:

```python
if path.suffix.lower() != ".txt":
    raise ValueError("Only .txt files are supported.")
```

Use `ValueError` for an unsupported argument rather than the old `IOError` name. In modern Python, `IOError` is an alias of `OSError`, while the problem here is a program rule detected before I/O.

A suffix does not prove that the file contains valid text. The actual read may still raise decoding or operating-system exceptions.

## Structured data: do not rely on `str(dictionary)`

Writing a dictionary with `str()` creates a Python-style representation, not a robust interchange format:

```python
marks = {"Aisha": 72, "Sam": 64}
```

JSON preserves basic dictionary and list structure as text:

```python
import json

marks = {"Aisha": 72, "Sam": 64}

with open("marks.json", "w", encoding="utf-8") as file:
    json.dump(marks, file, indent=2)
```

Read it back:

```python
with open("marks.json", "r", encoding="utf-8") as file:
    marks = json.load(file)

print(type(marks))   # dict
```

`json.dump()` writes to a file, whereas `json.dumps()` returns a string. `json.load()` reads from a file, whereas `json.loads()` parses a string.

JSON supports strings, numbers, Booleans, null values, lists, and objects with string keys. Custom Python objects and sets require explicit conversion.

## Matching data from two files

Suppose one file contains one name per line and another contains one mark per line:

```python
from pathlib import Path

names = Path("names.txt").read_text(encoding="utf-8").splitlines()
mark_texts = Path("marks.txt").read_text(encoding="utf-8").splitlines()

if len(names) != len(mark_texts):
    raise ValueError("Names and marks must have the same length.")

marks = [int(value) for value in mark_texts]
student_marks = dict(zip(names, marks))
```

Different lengths do not cause `zip()` to raise an exception; it silently stops at the shorter iterable. Therefore, check the lengths explicitly when missing pairings would lose data.

Use `splitlines()` for line-based data. If supporting comma-separated input too, define the format clearly rather than guessing from arbitrary text.

## Organising file utilities

Move reusable operations into `file_utils.py`:

```python
import json
from pathlib import Path


def read_json(path):
    with Path(path).open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path, data):
    with Path(path).open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
```

Then coordinate them in `main.py`:

```python
from file_utils import read_json, write_json


def main():
    marks = {"Aisha": 72, "Sam": 64}
    write_json("marks.json", marks)
    loaded_marks = read_json("marks.json")
    print(loaded_marks)


if __name__ == "__main__":
    main()
```

Decide where exceptions belong. A low-level utility often lets exceptions propagate; `main()` can translate them into user-facing guidance and an exit status.

## Optional extension: APIs

An API response is not file I/O, but it reinforces imports, structured data, and exceptions. A Requests example might retrieve JSON:

```python
import requests


def search_service(url, parameters):
    response = requests.get(url, params=parameters, timeout=10)
    response.raise_for_status()
    return response.json()
```

This can raise network, timeout, HTTP, or JSON-decoding exceptions. Handle these at an appropriate application boundary.

External APIs may change, impose terms or rate limits, and return missing fields. Use `.get()` carefully for optional dictionary fields and consult current service documentation.

The notebook's `Song` class work belongs after the OOP introduction. For now, process an API response as nested dictionaries and lists, or save selected JSON data to a file.

## Pause and predict

What remains in `message.txt` after each block?

```python
with open("message.txt", "w", encoding="utf-8") as file:
    file.write("First\n")

with open("message.txt", "a", encoding="utf-8") as file:
    file.write("Second\n")

with open("message.txt", "w", encoding="utf-8") as file:
    file.write("Third\n")
```

Explain precisely when the previous contents are discarded.

## Common mistakes

- Opening files without closing them or using `with`.
- Using `"w"` without recognising that it truncates existing data.
- Expecting `write()` or `writelines()` to add newlines automatically.
- Calling `read()` twice and expecting the cursor to restart.
- Treating `str(file_object)` as the file's contents.
- Relying on platform-default text encoding.
- Assuming a `.txt` suffix guarantees valid text.
- Writing `str(dictionary)` and expecting reliable structured restoration.
- Expecting `zip()` to raise when inputs have different lengths.
- Assuming relative paths are based on the source file rather than the working directory.

## Check your understanding

1. What does a context manager guarantee for a file?
2. How do `"w"` and `"a"` differ?
3. Why is an explicit encoding helpful?
4. Why does a second `read()` return an empty string?
5. What is the difference between a file object and its contents?
6. Why should paired file lengths be checked before `zip()`?
7. Which JSON functions work with files and which work with strings?

## Apply your learning

1. Write and append several lines to a UTF-8 text file, then read them by iteration.
2. Create a marks dictionary, save it as JSON, reload it, and verify equality.
3. Handle a missing input file and an invalid numeric value separately.
4. Read names and marks from separate line-based files, validate their lengths, and combine them into a dictionary.
5. Move reusable operations into `file_utils.py` and import them into a guarded `main.py`.
6. Extension: retrieve JSON from an API, extract selected fields, and save only those fields locally.

## Page summary

Files persist data beyond a program run. Context managers close resources safely, modes determine whether data is read, replaced, appended, or exclusively created, and encodings translate between text and bytes. File objects maintain a cursor and differ from their contents. Exceptions address environmental failures, while JSON provides a reliable format for basic structured data.

**Previous:** Page 2: `main.py`, `__name__`, and Command-Line Arguments  
**Next step:** Complete the Imports and File I/O practical work in `.py` files, testing both normal execution and missing, malformed, or mismatched input data.

---

# Suggested VLE setup

Create one learning module titled **6 Python Imports and File I/O**, containing:

1. **Start here: moving from notebooks to Python programs**
2. **6.1 Imports and Modules**
3. **6.2 `main.py`, `__name__`, and Command-Line Arguments**
4. **6.3 File Handling (I/O)**
5. **Imports and File I/O practical project**
6. **Check your learning**

Add previous/next navigation and use each second-level heading in the page contents.

The practical should now require learners to create and run actual `.py` files rather than complete every task inside the notebook. Supply a starter directory containing `main.py`, an initially small utility module, and a `data` directory if reducing setup friction is desirable.

Keep API retrieval as an optional extension. Move the conversion of API records into `Song` objects to Lecture 7 or 8 after classes have been introduced. Revisit custom exceptions and inheritance alongside that later OOP material.
