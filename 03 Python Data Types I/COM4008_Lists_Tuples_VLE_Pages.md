# COM4008 Programming Concepts: Data Representation, Strings, Lists and Tuples

This content is designed as four linked VLE information pages. Learners should run the examples and complete the practical activities in a Python notebook or coding environment.

---

# Page 1: Data Structures and Memory

## On this page

- Values, variables, and collections
- What a data structure is
- Why different structures exist
- Bits, bytes, binary, and decimal
- How Python objects use memory
- References and object identity

## Learning outcomes

By the end of this page, you should be able to:

- explain why programs use data structures;
- distinguish a value, a variable, and a collection;
- convert simple values between decimal and binary using Python;
- explain the relationship between bits and bytes;
- describe variables as names that refer to Python objects;
- interpret memory-size measurements cautiously.

## From individual values to collections

A variable gives a meaningful name to a value:

```python
num1 = 10
num2 = 20
num3 = 30
```

This is manageable for a few unrelated values. It becomes repetitive when the values belong together:

```python
num1 = 10
num2 = 20
num3 = 30
num4 = 40
num5 = 50
num6 = 60
num7 = 70
num8 = 80
num9 = 90
num10 = 100
```

A data structure collects related values so they can be stored and processed systematically:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

Instead of writing ten almost identical instructions, a program can iterate over `numbers`, find its length, retrieve an item, calculate a total, or sort the collection.

## What is a data structure?

A **data structure** is a way of organising values so that a program can store, access, and modify them appropriately.

Different structures support different operations and relationships. Examples include:

- sequences, in which values have an order;
- mappings, which associate keys with values;
- sets, which hold unique values;
- trees and graphs, which represent hierarchical or connected data.

This lecture concentrates on Python sequences: strings, lists, and tuples.

The choice of structure affects how clearly a problem can be expressed and how efficiently operations such as searching, inserting, deleting, and sorting can be performed. Algorithm analysis and Big O notation examine how resource requirements grow with the input size; these ideas will be developed further elsewhere.

## Indexed and linked access

An indexed sequence gives each item a numeric position. This allows a program to request a particular item directly:

```python
numbers = [10, 20, 30, 40]
print(numbers[2])
```

The output is `30` because Python indexing begins at zero.

Other structures may be followed through connections. In a linked list, for example, each node refers to the next node. Reaching a later node normally requires following the preceding links.

“Random access” means retrieving an indexed item without first visiting every earlier item. It does not mean choosing an item randomly, and it should not be confused with RAM—the hardware memory in which active programs and data are held.

## Recap: values have types

You have already worked with several built-in types:

| Type | Represents | Example |
|---|---|---|
| `str` | Text | `"Nick"` |
| `int` | Whole numbers | `5` |
| `float` | Floating-point numbers | `3.14` |
| `bool` | Boolean values | `True` |

```python
name = "Nick"
number = 5
pi = 3.14
is_enrolled = True
```

Strings, lists, and tuples are also objects with types. Unlike a single integer or Boolean value, they can represent a sequence containing several elements.

## Bits, bytes, and binary

Computers ultimately represent information using binary states. A **bit** is a binary digit whose value is either `0` or `1`. A **byte** normally contains eight bits.

Humans commonly write numbers in decimal, or base 10. Binary is base 2. The binary number `1010` represents decimal 10:

```text
1 × 8 + 0 × 4 + 1 × 2 + 0 × 1 = 10
```

Python's `bin()` function produces a string containing the binary representation of an integer:

```python
number = 10
print(bin(number))
```

The output is:

```text
0b1010
```

The prefix `0b` identifies a binary literal. It can be removed for display using a format specification:

```python
print(f"{number:b}")
```

Convert binary text back to an integer by supplying base 2 to `int()`:

```python
binary_text = "1010"
decimal_number = int(binary_text, 2)
print(decimal_number)
```

## Signed and unsigned fixed-width integers

In a fixed number of bits, an **unsigned** integer uses all bit patterns for zero and positive values. Eight unsigned bits represent values from 0 to 255.

A **signed** representation also includes negative values. The common two's-complement representation uses eight bits for values from −128 to 127.

| Width | Unsigned range | Signed two's-complement range |
|---|---:|---:|
| 8 bits | 0 to 255 | −128 to 127 |
| 16 bits | 0 to 65,535 | −32,768 to 32,767 |

These ranges describe fixed-width integer formats used by hardware and many programming languages. Python's ordinary `int` does not have one fixed 8-, 32-, or 64-bit width. It can grow to represent much larger values, subject to available memory.

## Python objects and references

A useful introductory model is that a Python variable is a **name referring to an object**:

```python
number = 10
```

Python creates or locates an integer object representing `10`, then associates the name `number` with it. Assignment does not place an unlabelled block of raw bits directly “inside” the variable.

Two names can refer to the same object:

```python
first = [10, 20]
second = first

print(first is second)   # True
```

`is` checks object identity: whether two references point to the same object. `==` checks whether values compare as equal. Identity will matter when mutable lists are introduced on Page 3.

## Measuring memory in Python

`sys.getsizeof()` reports the size, in bytes, of a Python object in the current interpreter:

```python
import sys

number = 10
print(type(number))
print(sys.getsizeof(number))
```

The result may be much larger than four or eight bytes. A Python object normally carries implementation information in addition to its numeric data, such as its type and reference-management data.

The exact result can differ between Python implementations, versions, platforms, and values. It should not be memorised as the universal size of an integer.

For containers, `sys.getsizeof()` is normally a **shallow** measurement: it reports the container itself, not the complete memory occupied by every object reachable from it. Measuring a full object graph requires a more careful method.

## What about Boolean values?

Conceptually, one bit is sufficient to distinguish two states. However, a Python `bool` is a Python object, not normally stored as an isolated one-bit variable. Representation depends on the language, data structure, and implementation.

This distinction is useful:

- **information requirement:** two states can be encoded using one bit;
- **runtime representation:** a high-level language may use additional memory to provide object behaviour and efficient access.

## Pause and predict

Predict the result and type of each expression:

```python
bin(13)
int("1101", 2)
type(bin(13))
```

Then test your predictions. Why does `bin()` return text rather than a new numeric type?

## Common misconceptions

- A data structure is not simply “a variable containing more values”; it also defines organisation and supported operations.
- Random access does not mean random selection.
- One byte is eight bits, not eight decimal digits.
- A signed byte normally ranges from −128 to 127, not −127 to 128.
- Python integers do not have one universal fixed size.
- `sys.getsizeof()` does not automatically calculate the deep size of a collection and everything it refers to.
- A Boolean needs one bit of information, but a Python Boolean object may occupy more memory.

## Check your understanding

1. Why is one list often preferable to ten similarly named variables?
2. What is an index?
3. How many bits are normally in one byte?
4. What does the `0b` prefix indicate?
5. How does a Python `int` differ from a fixed-width integer?
6. What is the limitation of `sys.getsizeof()` when used on a container?

## Try it yourself

1. Store a decimal integer and display its binary representation.
2. Convert three binary strings back to decimal integers.
3. Create a list containing the integers 1 to 10 and compare its shallow size with the shallow size of one integer.
4. Explain why adding the reported sizes may still not be a complete measurement of the program's memory use.

## Page summary

Data structures organise related values and support operations on them. Computers encode information using bits, commonly grouped into bytes. Python provides convenient binary conversion functions, but its high-level objects include runtime information beyond raw value bits. Variables are best understood as names referring to objects, and memory measurements must be interpreted in context.

**Next:** Continue to **Page 2: Strings, Arrays and Characters**.

---

# Page 2: Strings, Arrays and Characters

## On this page

- Characters and text encoding
- ASCII and Unicode
- Python strings as sequences
- Indexing and negative indexing
- Slicing and iteration
- String immutability
- Strings compared with character arrays

## Learning outcomes

By the end of this page, you should be able to:

- explain how numeric codes can represent characters;
- use `ord()` and `chr()` for Unicode code points;
- access characters using positive and negative indexes;
- extract part of a string using slicing;
- iterate over the characters in a string;
- explain why Python strings are immutable sequences rather than character arrays.

## Representing text

Computers represent text using numeric codes. A **character encoding** defines the relationship between characters and numeric values.

ASCII is an early encoding covering English letters, digits, punctuation, and control characters. For example:

| Character | ASCII decimal value |
|---|---:|
| `A` | 65 |
| `N` | 78 |
| `a` | 97 |

Python 3 strings use **Unicode**, a much larger standard designed to represent writing systems and symbols from around the world. ASCII characters form a compatible subset of Unicode, which is why the familiar values above still appear.

## `ord()` and `chr()`

`ord()` returns the Unicode code point of a single character:

```python
print(ord("A"))   # 65
print(ord("a"))   # 97
print(ord("N"))   # 78
```

`chr()` performs the reverse operation for a valid code point:

```python
print(chr(65))     # A
```

Because uppercase and lowercase letters have different code points, they are different values:

```python
print("A" == "a")   # False
```

These functions work with Unicode, not only ASCII:

```python
character = "£"
print(ord(character))
print(chr(ord(character)))
```

A Unicode code point is an abstract number assigned to a character. Its encoded byte representation depends on an encoding such as UTF-8 or UTF-16.

## Python strings are sequences

A Python `str` is an immutable sequence of Unicode characters:

```python
name = "Nick"
```

Each character has an indexed position:

| Character | `N` | `i` | `c` | `k` |
|---|---:|---:|---:|---:|
| Positive index | 0 | 1 | 2 | 3 |
| Negative index | −4 | −3 | −2 | −1 |

Retrieve a character with the subscription operator `[]`:

```python
print(name[0])    # N
print(name[3])    # k
print(name[-1])   # k
```

Python has no separate built-in `char` type. Indexing a string returns another string of length one:

```python
print(type(name[0]))   # <class 'str'>
print(len(name[0]))    # 1
```

## Index boundaries

For a string of length `n`, valid positive indexes run from `0` to `n - 1`.

```python
name = "Nick"
print(len(name))       # 4
print(name[len(name) - 1])
```

Negative indexing provides a more convenient way to access the last character:

```python
print(name[-1])
```

Requesting an unavailable position causes an `IndexError`:

```python
print(name[4])
```

## Slicing strings

A slice extracts a range using `[start:stop]`. The start is included and the stop is excluded:

```python
language = "Python"

print(language[0:3])   # Pyt
print(language[3:6])   # hon
print(language[:2])    # Py
print(language[2:])    # thon
```

A slice can also include a step:

```python
print(language[::2])   # Pto
print(language[::-1])  # nohtyP
```

Unlike indexing, an out-of-range slice boundary is normally adjusted safely rather than raising `IndexError`.

## Iterating over a string

A `for` loop visits each character in order:

```python
name = "Nick"

for character in name:
    print(character)
```

Use `enumerate()` when both the index and character are needed:

```python
for index, character in enumerate(name):
    print(f"[{index}] : {character}")
```

This is clearer than manually maintaining a counter.

## Useful string methods

Objects provide methods appropriate to their type. Some useful string methods include:

```python
name = "Nick"

print(name.lower())       # nick
print(name.upper())       # NICK
print(name.find("c"))     # 2
print(name.find("C"))     # -1
```

`find()` returns the first matching index or `-1` when the substring is absent. Use the `in` operator when the question is simply whether text occurs:

```python
print("c" in name)        # True
```

`dir(str)` displays many attributes and methods, but official documentation or `help(str.method_name)` usually gives more useful explanations.

## Strings are immutable

An immutable object cannot be changed after creation. This instruction therefore fails:

```python
name = "Nick"
name[0] = "R"
```

To produce changed text, create a new string:

```python
name = "Nick"
updated_name = "R" + name[1:]
print(updated_name)   # Rick
```

Methods such as `upper()` also return new strings; they do not modify the original:

```python
name = "Nick"
upper_name = name.upper()

print(name)        # Nick
print(upper_name)  # NICK
```

## Strings and character arrays

In languages such as C, a string may be represented as an array of character values terminated by a null character. Python shields the programmer from that low-level representation.

A Python string supports sequence operations such as indexing, slicing, iteration, and `len()`, so it can behave like other sequences in many algorithms. However, it is not accurate to call it a Python list or assume it has the same memory layout as a C character array.

The useful comparison is:

| Feature | Python `str` | Python `list` |
|---|---|---|
| Ordered | Yes | Yes |
| Indexed | Yes | Yes |
| Sliceable | Yes | Yes |
| Mutable | No | Yes |
| Intended content | Unicode text | General object references |

## Pause and predict

For `word = "Python"`, predict each result:

```python
word[-1]
word[1:4]
word[::-1]
ord(word[0])
word.find("z")
```

Then run the expressions and explain the start-inclusive, stop-exclusive slicing rule.

## Common misconceptions

- Python 3 text is Unicode, not limited to ASCII.
- A code point is not necessarily the same as one encoded byte.
- Python has no separate built-in character type; one indexed character is a length-one `str`.
- A Python string is not a list and is not simply a C character array.
- The final positive index is `len(value) - 1`, not `len(value)`.
- String methods such as `upper()` return new strings because strings are immutable.

## Check your understanding

1. What relationship does a character encoding define?
2. What do `ord()` and `chr()` return?
3. What is the final character of `"Python"` at positive and negative indexes?
4. Why does `word[1:4]` contain three characters?
5. What type is `word[0]`?
6. What does string immutability mean?

## Try it yourself

1. Store your name and display its first and last characters.
2. Use `enumerate()` to display every character with its index.
3. Display each character and its Unicode code point.
4. Produce a reversed copy of your name.
5. Extension: display the binary representation of every character's code point.

## Page summary

Python strings are immutable, indexed sequences of Unicode characters. Indexes begin at zero, negative indexes count from the end, and slices use an excluded stop boundary. `ord()` and `chr()` connect characters with Unicode code points. Although strings share sequence operations with lists, their purpose, mutability, and representation differ.

**Previous:** Page 1: Data Structures and Memory  
**Next:** Continue to **Page 3: Lists**.

---

# Page 3: Lists

## On this page

- Creating and accessing lists
- Mixed value types and references
- Mutability and aliasing
- Slicing and iteration
- Adding, removing, and sorting
- List comprehensions
- Optional extension: NumPy arrays

## Learning outcomes

By the end of this page, you should be able to:

- create a list and retrieve elements using indexes;
- modify a list using assignment and common methods;
- explain how two names can refer to the same mutable list;
- iterate over list values and indexes;
- use slicing to create a new list;
- construct a simple list comprehension;
- distinguish a Python list from a NumPy array.

## Creating a list

A Python list is a mutable, ordered sequence. List literals use square brackets:

```python
numbers = [1, 2, 3, 4, 5]
```

Lists can contain references to objects of different types:

```python
values = [1, 2.25, "Nick", True]
```

Mixed types are permitted, but a collection of values with a consistent purpose is normally easier to process. A list of student marks is likely to contain numbers; a list representing a record might legitimately combine fields of different types, although other structures may express that record more clearly.

## Accessing list elements

Lists use the same indexing conventions as strings:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])    # 10
print(numbers[2])    # 30
print(numbers[-1])   # 50
print(len(numbers))  # 5
```

The first index is zero. The final positive index is `len(numbers) - 1`.

## Slicing a list

List slices use start-inclusive, stop-exclusive boundaries:

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[2:4])   # [30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[3:])    # [40, 50, 60]
```

A normal list slice creates a new list containing references to the selected objects. It is a **shallow copy**: nested mutable objects are still shared.

## Lists are mutable

List elements can be replaced after creation:

```python
numbers = [10, 20, 30]
numbers[1] = 99
print(numbers)   # [10, 99, 30]
```

The list object remains the same list, but one stored reference is changed.

Common mutating methods include:

```python
numbers = [3, 1, 2]

numbers.append(4)       # add one item at the end
numbers.insert(0, 10)   # insert at an index
numbers.remove(3)       # remove the first equal value
last = numbers.pop()    # remove and return the last item
numbers.sort()          # sort the list in place
```

`remove(value)` removes by value, while `pop(index)` removes and returns an item by index. Both can raise errors when the requested value or index is unavailable.

## Methods that mutate and functions that return

`list.sort()` changes the existing list and returns `None`:

```python
numbers = [7, 1, 4]
result = numbers.sort()

print(numbers)   # [1, 4, 7]
print(result)    # None
```

The built-in `sorted()` function returns a new list instead:

```python
numbers = [7, 1, 4]
sorted_numbers = sorted(numbers)

print(numbers)         # [7, 1, 4]
print(sorted_numbers)  # [1, 4, 7]
```

Use `reverse=True` for descending order:

```python
numbers.sort(reverse=True)
```

Values being sorted must support meaningful comparison with one another. A mixed list containing unrelated strings and numbers cannot normally be sorted directly.

## Iterating over lists

Iterate directly when only values are required:

```python
names = ["Aisha", "Sam", "Robin"]

for name in names:
    print(name)
```

Use `enumerate()` when indexes are also needed:

```python
for index, name in enumerate(names):
    print(index, name)
```

Avoid changing the length of a list while iterating directly over it; removals can cause elements to be skipped. Build a new list or iterate over a copy when filtering.

## References and aliasing

Assignment does not copy a list. It gives another name to the same mutable object:

```python
first = [1, 2, 3]
second = first

second.append(4)

print(first)    # [1, 2, 3, 4]
print(second)   # [1, 2, 3, 4]
```

This relationship is called **aliasing**. Both names refer to the same list.

Create a shallow copy when the outer list should be independent:

```python
first = [1, 2, 3]
second = first.copy()
second.append(4)

print(first)    # [1, 2, 3]
print(second)   # [1, 2, 3, 4]
```

For nested lists, shallow copies do not copy every inner object. Later study can introduce `copy.deepcopy()` where genuinely independent nested data is required.

## List comprehensions

A list comprehension creates a list from an iterable using a compact expression:

```python
squares = [number ** 2 for number in range(6)]
print(squares)
```

The result is:

```text
[0, 1, 4, 9, 16, 25]
```

An optional condition filters the values:

```python
even_squares = [number ** 2 for number in range(11) if number % 2 == 0]
```

This corresponds to:

```python
even_squares = []

for number in range(11):
    if number % 2 == 0:
        even_squares.append(number ** 2)
```

List comprehensions are valuable when the expression remains easy to read. Prefer an ordinary loop when logic becomes complicated or needs several statements.

## Functions that process lists

Lists can be passed into functions like other objects:

```python
def get_first(values):
    return values[0]


def get_last(values):
    return values[-1]
```

These functions require a non-empty sequence. Decide how a function should behave with an empty list and either validate it or document that requirement.

A function can return a transformed list:

```python
def square_all(numbers):
    return [number ** 2 for number in numbers]
```

## Optional extension: NumPy arrays

NumPy is a third-party package for efficient numerical computing:

```python
import numpy as np

array = np.array([1, 2, 3], dtype="float32")
print(array)
print(array.dtype)
```

A NumPy array and a Python list are different structures:

| Feature | Python list | NumPy array |
|---|---|---|
| Built into Python | Yes | No; NumPy required |
| Typical element types | May be mixed | Usually one fixed data type |
| Numerical operations | General Python behaviour | Vectorised numerical operations |
| Memory layout | References to Python objects | Often compact homogeneous data buffer |
| Resizing | Designed to grow and shrink | Usually fixed-size after creation |

When NumPy receives mixed numeric values, it selects a common type capable of representing them where possible:

```python
array = np.array([3.14, 2, 3])
print(array.dtype)
```

Explicit `dtype` choices affect precision, range, and memory per element. NumPy is particularly valuable for large numerical datasets, matrices, data science, and scientific computing. It is not a replacement for every Python list.

## Pause and predict

Predict all four outputs:

```python
first = [1, 2, 3]
second = first
third = first.copy()

second.append(4)
third.append(5)

print(first)
print(second)
print(third)
print(first is second)
```

Then run the code and explain the difference between equality, identity, and copying.

## Common mistakes

- Using index `len(values)` for the final item rather than `len(values) - 1` or `-1`.
- Assuming assignment copies a list.
- Writing `sorted_values = values.sort()` and expecting a list rather than `None`.
- Confusing `remove(value)` with `pop(index)`.
- Modifying a list's length while iterating over it.
- Assuming a shallow copy duplicates every nested object.
- Treating Python lists and NumPy arrays as interchangeable.

## Check your understanding

1. What does it mean for a list to be mutable?
2. What does `values[-1]` return?
3. How do `sort()` and `sorted()` differ?
4. Why does changing `second` also change `first` after `second = first`?
5. What does a list comprehension produce?
6. Give two differences between a Python list and a NumPy array.

## Apply your learning

1. Create a list containing 1 to 10, then display its first, middle, and last values.
2. Write functions that return the first and last values of any non-empty sequence.
3. Rewrite the following loop as a list comprehension:

   ```python
   names = ["nick", "sam", "andrew", "claire"]
   name_lengths = []
   for name in names:
       name_lengths.append(len(name))
   ```

4. Write `square_all(numbers)` first using a loop and then using a comprehension.
5. Write a function that finds the middle value of an odd-length list. Decide and document its behaviour for even and empty lists.

## Page summary

Python lists are mutable, indexed sequences containing references to objects. They support indexing, slicing, iteration, insertion, removal, and sorting. Assignment creates another reference rather than a copy, so aliasing matters. List comprehensions concisely construct transformed or filtered lists. NumPy arrays are separate, usually homogeneous structures designed for efficient numerical work.

**Previous:** Page 2: Strings, Arrays and Characters  
**Next:** Continue to **Page 4: Tuples**.

---

# Page 4: Tuples

## On this page

- Creating tuples
- Indexing, slicing, and iteration
- Tuple immutability
- Rebinding and mutable contents
- Packing and unpacking
- Tuple methods
- Choosing between lists and tuples

## Learning outcomes

By the end of this page, you should be able to:

- create tuples, including an empty and single-item tuple;
- access tuple elements using sequence operations;
- explain tuple immutability accurately;
- unpack tuple values into variables;
- use `count()` and `index()`;
- choose appropriately between a list and a tuple.

## Creating tuples

A tuple is an ordered, immutable sequence. Tuple literals commonly use parentheses:

```python
coordinates = (4, 7)
numbers = (1, 2, 3, 4, 5, 6)
```

The comma creates the tuple; parentheses usually make its boundaries clear. A single-item tuple therefore needs a trailing comma:

```python
not_a_tuple = (5)
single_item_tuple = (5,)

print(type(not_a_tuple))         # <class 'int'>
print(type(single_item_tuple))   # <class 'tuple'>
```

Create an empty tuple using `()`:

```python
empty = ()
```

## Tuple sequence operations

Tuples share many read-only sequence operations with strings and lists:

```python
values = (10, 20, 30, 40)

print(values[0])       # 10
print(values[-1])      # 40
print(values[1:3])     # (20, 30)
print(len(values))     # 4
```

They can be iterated over:

```python
for value in values:
    print(value)
```

They can also contain objects of different types:

```python
record = (12345678, "Aisha", True)
```

## Tuples are immutable

After a tuple is created, its element references cannot be replaced, inserted, or removed:

```python
values = (1, 2, 3)
values[0] = 5
```

This produces a `TypeError`. Tuples do not provide mutating methods such as `append()`, `remove()`, or `sort()`.

Immutability can communicate that a collection represents a fixed grouping—for example, a coordinate, colour triple, or function result whose structure should not change.

## Immutability is not the same as a constant name

The name referring to a tuple can be reassigned:

```python
position = (4, 7)
position = (8, 2)
```

The original tuple was not changed. Instead, `position` was made to refer to another tuple. Python does not enforce constant variable names through tuple syntax.

## A tuple can contain a mutable object

Tuple immutability applies to the tuple's element references, not recursively to every contained object:

```python
record = ("Aisha", [60, 70])
record[1].append(80)

print(record)   # ('Aisha', [60, 70, 80])
```

The tuple still refers to the same list, but that list is mutable and has changed internally. Therefore, “a tuple can never change in any way” is too broad; its structure and element references cannot be reassigned.

## Packing and unpacking

Creating a tuple from several values is sometimes called packing:

```python
student = (12345678, "Aisha", 68.5)
```

Unpacking assigns its elements to separate names:

```python
student_id, name, average = student

print(student_id)
print(name)
print(average)
```

The number of names must normally match the number of elements. Extended unpacking captures remaining values in a list:

```python
first, *middle, last = (10, 20, 30, 40, 50)

print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50
```

Functions can return more than one value using a tuple:

```python
def minimum_and_maximum(values):
    return min(values), max(values)


smallest, largest = minimum_and_maximum([7, 2, 9, 4])
```

## Tuple methods

Because tuples are immutable, they have relatively few methods.

`count()` reports how many elements compare equal to a value:

```python
values = (1, 1, 2, 2, 2, 3)
print(values.count(2))   # 3
```

`index()` returns the first index of an equal value:

```python
print(values.index(3))   # 5
```

If the value is absent, `index()` raises a `ValueError`. Check membership first when absence is expected:

```python
target = 5

if target in values:
    print(values.index(target))
else:
    print("Value not present")
```

## Lists compared with tuples

| Feature | List | Tuple |
|---|---|---|
| Literal form | `[1, 2, 3]` | `(1, 2, 3)` |
| Ordered and indexed | Yes | Yes |
| Sliceable and iterable | Yes | Yes |
| Element references replaceable | Yes | No |
| Can grow or shrink | Yes | No |
| Typical use | Changing collection | Fixed grouping or record |

Choose a list when elements need to be added, removed, reordered, or replaced. Choose a tuple when the grouping has a fixed structure and immutability communicates intent.

Immutability may also allow a tuple to be used as a dictionary key or set element, provided all its contained values are hashable. Lists cannot be used in those positions because they are mutable.

Do not choose solely on a small presumed speed difference. Clarity, required operations, and the meaning of the data are stronger reasons.

## Nested tuples and flattening

A tuple can contain other tuples:

```python
rows = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
```

Flatten the values into a list using nested iteration:

```python
flattened = []

for row in rows:
    for value in row:
        flattened.append(value)

print(flattened)
```

Or, once comfortable with comprehensions:

```python
flattened = [value for row in rows for value in row]
```

The ordinary nested loop is preferable if the comprehension is difficult to read.

## Pause and predict

Predict which instructions work and what each successful line produces:

```python
data = ("A", [1, 2])

print(data[-1])
data[0] = "B"
data[1].append(3)
print(data)
```

Explain why tuple immutability permits one operation but rejects another.

## Common mistakes

- Writing `(5)` and expecting a tuple rather than an integer.
- Calling `append()` or `sort()` on a tuple.
- Describing a tuple as a constant variable.
- Assuming every object contained by a tuple becomes immutable.
- Unpacking into the wrong number of variables.
- Expecting `index()` to return every matching position rather than the first.
- Choosing a tuple when the collection genuinely needs to change.

## Check your understanding

1. What punctuation creates a one-item tuple?
2. Which sequence operations do lists and tuples share?
3. What exactly is prevented by tuple immutability?
4. How can a list inside a tuple still change?
5. What is tuple unpacking?
6. When would a tuple communicate intent better than a list?

## Apply your learning

1. Create a tuple containing several repeated values and use `count()` to tally one value.
2. Write a function that returns every index at which a target occurs in either a list or tuple.
3. Unpack a three-element tuple into meaningful variable names.
4. Flatten a tuple of tuples into one list.
5. Design two small datasets: one for which a list is appropriate and one for which a tuple is appropriate. Explain each choice.

## Page summary

Tuples are immutable, indexed sequences. They support reading, indexing, slicing, iteration, membership tests, counting, and searching, but not structural mutation. Names can be rebound, and mutable objects contained within a tuple can still change. Packing and unpacking make tuples useful for fixed records and multi-value function results.

**Previous:** Page 3: Lists  
**Next step:** Complete the Lists and Tuples practical exercises, testing empty, single-item, repeated-value, mixed-type, and nested collections where appropriate.

---

# Suggested VLE setup

Create one learning module titled **3 Python Data Structures I: Lists and Tuples**, containing:

1. **Start here: overview and learning outcomes**
2. **3.1 Data Structures and Memory**
3. **3.2 Strings, Arrays and Characters**
4. **3.3 Lists**
5. **3.4 Tuples**
6. **Lists and Tuples practical notebook**
7. **Check your learning**

Add previous/next navigation and use each second-level heading in the page contents. Keep the interview-style consecutive-sequence problem as an optional challenge rather than a core exercise; its terminology needs care because a consecutive-value sequence is not necessarily a subsequence in the original-order sense.

NumPy is retained as an optional extension within the Lists page. If numerical arrays receive substantial practical coverage later in the module, move it to that later unit and link forward from this page.
