# COM4008 Programming Concepts: Sets and Dictionaries

This content is designed as three linked VLE information pages. Learners should run the examples and complete the practical activities in a Python notebook or coding environment.

---

# Page 1: Recap on Lists and Tuples

## On this page

- Python's main collection types
- Lists as mutable sequences
- Tuples as immutable sequences
- Indexing, iteration, and membership
- Choosing a collection by the relationships in the data
- Preparing to study sets and dictionaries

## Learning outcomes

By the end of this page, you should be able to:

- recall the defining properties of lists and tuples;
- access and process values in a sequence;
- distinguish mutation from rebinding;
- choose between a list and tuple for a simple collection;
- explain why some problems need uniqueness or key-based lookup rather than position.

## Four important collection types

Python provides several built-in ways to organise collections of values. This lecture completes an introductory comparison of four important types:

| Collection | Literal example | Main relationship |
|---|---|---|
| List | `[10, 20, 30]` | Mutable ordered sequence |
| Tuple | `(10, 20, 30)` | Immutable ordered sequence |
| Set | `{10, 20, 30}` | Unique membership |
| Dictionary | `{"A": 10, "B": 20}` | Keys associated with values |

The punctuation helps you recognise a literal, but choosing a structure should be based on the meaning of the data and the operations required.

## Lists: mutable ordered sequences

A list stores an ordered sequence of object references and can change after creation:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
```

Elements are indexed from zero:

```python
print(numbers[0])    # 1
print(numbers[-1])   # 8
print(numbers[2:5])  # [3, 4, 5]
```

Lists can grow, shrink, and have elements replaced:

```python
numbers.append(9)
numbers[0] = 10
numbers.remove(5)
```

`append()` adds one element at the end. `remove(value)` removes the first element equal to the supplied value and raises `ValueError` if it is absent.

## Duplicate values and position

Lists may contain duplicate values, with every occurrence occupying its own position:

```python
numbers = [1, 2, 2, 3]

print(len(numbers))       # 4
print(numbers.count(2))   # 2
```

This is useful when repetition carries meaning—for example, individual survey responses, transactions, or scores. If the purpose is simply to represent which distinct values occur, a set may be more appropriate.

## List references and copying

Assignment gives another name to the same list rather than copying it:

```python
first = [1, 2, 3]
second = first

second.append(4)
print(first)   # [1, 2, 3, 4]
```

Use `copy()` or slicing when an independent outer list is required:

```python
second = first.copy()
```

This is a shallow copy. Nested mutable objects remain shared unless copied separately.

## Tuples: immutable ordered sequences

A tuple also stores an ordered, indexed sequence:

```python
values = (1, 1, 1, 2, 3, 4, 5)

print(values[0])
print(values[-1])
print(values.count(1))   # 3
```

Its element references cannot be replaced, added, or removed:

```python
values[0] = 0   # TypeError
```

Tuple immutability does not make a variable name constant. A name can be rebound to another object:

```python
position = (4, 7)
position = (8, 2)
```

It also does not recursively freeze mutable objects contained inside a tuple.

## Shared sequence operations

Lists and tuples both support common sequence operations:

```python
values = (10, 20, 30)

print(len(values))
print(values[1])
print(20 in values)

for value in values:
    print(value)
```

They preserve order, permit duplicates, and allow integer indexing. Lists add structural mutation; tuples communicate a fixed grouping.

## Choosing between a list and tuple

Choose a list when the collection is expected to change:

```python
shopping_basket = ["milk", "pasta"]
shopping_basket.append("strawberries")
```

Choose a tuple when the number and meaning of positions form a fixed record:

```python
coordinate = (53.7647, -2.7080)
```

Do not choose a tuple solely because the current example happens not to modify its values. Use it when fixed structure is part of the data's meaning.

## Converting between collections

Constructors can convert compatible iterables:

```python
values = (1, 1, 2, 3)

as_list = list(values)
unique_values = set(values)

print(as_list)        # [1, 1, 2, 3]
print(unique_values)  # {1, 2, 3}, display order not guaranteed
```

Conversion may change important properties. Turning a tuple into a list makes the outer collection mutable. Turning a sequence into a set removes duplicates and does not preserve positional meaning.

## From position to other relationships

Lists and tuples answer questions based on order and position:

- What is the first item?
- What occurs at index 3?
- What is the next item?

Other problems emphasise different relationships:

- Which unique values have appeared?
- Is a value a member of a collection?
- Which values occur in both groups?
- What price belongs to `"milk"`?
- What student record belongs to a particular ID?

Sets address uniqueness and membership. Dictionaries associate unique keys with values.

## Pause and predict

Predict each result:

```python
values = [1, 1, 2, 3]
alias = values
copied = values.copy()

alias.append(4)
copied.append(5)

print(values)
print(alias)
print(copied)
print(set(values))
```

Explain the effects of aliasing, copying, and removing duplicate values.

## Common misconceptions

- A Python list is not the same structure as a fixed-size homogeneous array.
- Assignment does not copy a list.
- `remove(5)` removes the first equal value, not the item at index 5.
- A tuple is immutable, but the variable referring to it is not a constant.
- Converting to a set is not harmless when order or duplicate occurrences matter.
- Brackets identify syntax; they are not sufficient reasons for choosing a collection.

## Check your understanding

1. Which properties do lists and tuples share?
2. What does list mutability allow?
3. What exactly is immutable about a tuple?
4. What information is lost when `[1, 1, 2]` is converted to a set?
5. When is a tuple a clearer choice than a list?
6. Which new relationship will a dictionary represent?

## Try it yourself

1. Create a list containing repeated values and use `count()` to examine repetition.
2. Create an independent shallow copy and demonstrate that changing the outer copy does not change the original.
3. Convert the list to a tuple and a set. Compare their displayed values, lengths, and supported operations.
4. Give one real-world example suited to each of a list, tuple, set, and dictionary.

## Page summary

Lists and tuples are ordered, indexed sequences that permit duplicate values. Lists are mutable; tuples have a fixed outer structure. Conversions can change mutability, order, and duplicate information. Sets and dictionaries serve different relationships: unique membership and key–value association.

**Next:** Continue to **Page 2: Sets**.

---

# Page 2: Sets

## On this page

- Creating sets
- Uniqueness and membership
- Hashable set elements
- Adding and removing values
- Set comprehensions
- Subsets and equality
- Union, intersection, difference, and symmetric difference

## Learning outcomes

By the end of this page, you should be able to:

- create empty and populated sets;
- explain uniqueness and the absence of positional indexing;
- add, remove, and test membership of values;
- build a set using a comprehension;
- calculate standard set operations;
- use subset and superset comparisons;
- recognise when a set would discard meaningful information.

## What is a set?

A set represents a collection of distinct, hashable values. Membership matters; duplicate occurrences and positional indexes do not.

```python
values = {1, 2, 3, 4, 5, 6}
```

Repeating an equal value does not create another element:

```python
values = {1, 2, 3, 1, 2, 3}
print(values)      # contains 1, 2, and 3 once each
print(len(values)) # 3
```

Sets are useful for:

- removing duplicate values when order is unimportant;
- fast membership tests;
- comparing groups;
- calculating unions, intersections, and differences.

## Creating an empty set

Curly braces alone create an empty dictionary, not an empty set:

```python
empty_dictionary = {}
empty_set = set()

print(type(empty_dictionary))
print(type(empty_set))
```

Use a non-empty literal or the `set()` constructor to create a set.

## Sets are not positional sequences

A set has no user-controlled positional index:

```python
values = {10, 20, 30}
print(values[0])   # TypeError
```

Iteration order must not be treated as a meaningful or stable ordering. The displayed order may differ from insertion order and may vary between runs or environments.

If values need to be processed in sorted order, request that explicitly:

```python
for value in sorted(values):
    print(value)
```

`sorted()` returns a list; it does not change the set into an ordered set.

## Membership

Use `in` and `not in` to test membership:

```python
enrolled_ids = {1001, 1002, 1003}

print(1002 in enrolled_ids)      # True
print(9999 not in enrolled_ids)  # True
```

Membership testing is a central set operation. For large collections, set membership is typically much faster on average than scanning a list, although exact performance depends on hashing behaviour and the data.

## Hashable elements

Set elements must be **hashable**. A hashable object has a stable hash value and equality behaviour suitable for locating it in a hash-based structure.

Many immutable built-in values are hashable:

```python
valid = {1, 2.5, "Aisha", (4, 7)}
```

Mutable lists and sets are not hashable and cannot be elements of a set:

```python
invalid = {[1, 2], [3, 4]}   # TypeError
```

A tuple is hashable only when all values it contains are hashable.

## Adding and removing values

Sets are mutable. Use `add()` to insert one value:

```python
values = {1, 2, 3}
values.add(4)
```

Adding an existing value has no effect:

```python
values.add(4)
print(len(values))   # still 4
```

Use `remove()` when absence should be treated as an error:

```python
values.remove(4)
```

Use `discard()` when absence is acceptable:

```python
values.discard(99)   # no error
```

`pop()` removes and returns an arbitrary element; it does not mean “remove the final item,” because sets have no final positional element.

## Removing duplicates from a sequence

The constructor removes equal duplicates:

```python
responses = [1, 1, 2, 2, 3, 3]
distinct_responses = set(responses)
print(distinct_responses)
```

This is appropriate when only distinct values matter. It is inappropriate when occurrence counts or original order matter. To remove duplicates while preserving first-occurrence order, a dictionary-based technique can be used:

```python
distinct_in_order = list(dict.fromkeys(responses))
```

## Set comprehensions

A set comprehension constructs a set from an iterable:

```python
numbers = [-2, -1, 0, 1, 2, 3]
positives = {number for number in numbers if number > 0}
```

Its structure is:

```text
{expression for item in iterable if condition}
```

Unlike a list comprehension, duplicate results collapse into one set element:

```python
remainders = {number % 3 for number in range(10)}
print(remainders)   # contains 0, 1, and 2
```

## Mathematical notation and Python

Common mathematical number sets include:

- **ℕ**, the natural numbers; whether zero is included depends on convention;
- **ℤ**, the integers;
- **ℚ**, the rational numbers;
- **ℝ**, the real numbers.

These are infinite mathematical sets and cannot be created by writing an ellipsis in a Python set. In this expression, `...` is a real Python object called `Ellipsis`:

```python
values = {0, 1, 2, ...}
```

It does not mean “continue for ever.” Programs instead generate or test the finite values they need.

Set-builder notation such as:

```text
S = {x ∈ numbers | x > 0}
```

can often be expressed using a comprehension:

```python
S = {x for x in numbers if x > 0}
```

## Equality, subsets, and supersets

Set equality depends on membership, not display or insertion order:

```python
print({1, 2, 3} == {3, 2, 1})   # True
```

Test subset and superset relationships with methods or operators:

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5, 6}

print(A.issubset(B))    # True
print(B.issuperset(A))  # True
print(A <= B)           # subset or equal
print(A < B)            # proper subset
```

`A < B` means every element of `A` is in `B` and the sets are not equal.

## Set operations

Suppose two groups contain:

```python
A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8, 9}
```

### Intersection

The intersection contains values in both sets:

```python
print(A & B)                 # {4, 5, 6}
print(A.intersection(B))
```

### Union

The union contains values in either set:

```python
print(A | B)
print(A.union(B))
```

### Difference

The difference contains values in the left set but not the right:

```python
print(A - B)   # {1, 2, 3}
print(B - A)   # {7, 8, 9}
```

Difference is directional, so these results are not normally equal.

### Symmetric difference

The symmetric difference contains values in either set but not both:

```python
print(A ^ B)   # {1, 2, 3, 7, 8, 9}
```

## Immutable sets

`frozenset` is an immutable set type:

```python
fixed_permissions = frozenset({"read", "write"})
```

It supports non-mutating set operations and, when its elements are hashable, can itself be placed in a set or used as a dictionary key. It is an extension rather than a requirement for the initial activities.

## Pause and predict

Predict the results:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5}

print(A & B)
print(A | B)
print(A - B)
print(B - A)
print(A ^ B)
print({1, 2} < A)
```

Explain why the two difference expressions produce different sets.

## Common misconceptions

- `{}` creates an empty dictionary, not an empty set.
- A set's displayed order must not be treated as positional ordering.
- Sets cannot be indexed.
- Duplicate removal also loses duplicate counts and positional information.
- `remove()` raises an error for an absent value; `discard()` does not.
- `pop()` removes an arbitrary set element, not the “last” one.
- `...` does not create an infinite Python set.
- Mutable lists cannot be set elements because they are unhashable.

## Check your understanding

1. How do you create an empty set?
2. Why can a set contain a tuple in some cases but not a list?
3. What is the difference between `remove()` and `discard()`?
4. Which operation finds values shared by two sets?
5. Why is `A - B` different from `B - A`?
6. When would converting a list to a set be inappropriate?

## Apply your learning

1. Write functions that return the union and intersection of two sets.
2. Generate the first 12 positive multiples of a supplied integer and return them as a set. Explain whether a set or list best communicates the required order.
3. Write `is_prime(number)`, then use a set comprehension to select the prime values from 0 to 20.
4. Given two sets of module codes, report those taken by both groups, either group, and only the first group.
5. Compare `remove()` and `discard()` using a value that is not present.

## Page summary

Sets represent unique, hashable members without positional indexing. They support efficient membership tests, mutation, comprehensions, subset comparisons, and mathematical operations including intersection, union, difference, and symmetric difference. Sets are appropriate when membership matters and duplicate counts or order do not.

**Previous:** Page 1: Recap on Lists and Tuples  
**Next:** Continue to **Page 3: Dictionaries**.

---

# Page 3: Dictionaries

## On this page

- Keys and values
- Creating and accessing dictionaries
- Unique, hashable keys
- Adding, updating, and removing entries
- Safe lookup
- Iterating through keys, values, and items
- Creating dictionaries with `zip()` and comprehensions
- Ordering and sorting
- Nested dictionaries, JSON, and APIs

## Learning outcomes

By the end of this page, you should be able to:

- create a dictionary containing meaningful key–value pairs;
- retrieve, add, update, and remove entries;
- explain key uniqueness and hashability;
- choose between direct lookup and `get()`;
- iterate through dictionary keys, values, and items;
- construct a dictionary from correctly paired sequences;
- distinguish a Python dictionary from JSON text;
- retrieve values from a simple nested structure.

## What is a dictionary?

A dictionary is a mutable mapping from unique keys to values. An ordinary dictionary lets a reader look up a word to find its definition. A Python dictionary similarly uses a key to locate an associated value:

```python
food_prices = {
    "milk": 1.30,
    "pasta": 0.75,
    "strawberries": 1.50,
}
```

The colon separates each key from its value. Commas separate entries.

Dictionaries are useful for relationships such as:

- product name → price;
- student ID → student record;
- country → average temperature;
- configuration name → setting;
- word → frequency count.

## Keys are not positional indexes

Retrieve a value by supplying its key:

```python
print(food_prices["milk"])   # 1.3
```

`food_prices[0]` does not mean “the first value.” It requests the key `0` and raises `KeyError` unless that key exists.

Keys are case-sensitive when they are strings:

```python
print(food_prices["Milk"])   # KeyError
```

Normalise user input when appropriate:

```python
item = input("Enter an item: ").strip().lower()
```

## Unique and hashable keys

Dictionary keys must be hashable, like set elements. Strings, numbers, and suitable tuples can be keys; lists cannot.

Keys are unique. Reusing an equal key replaces its associated value:

```python
prices = {"milk": 1.30, "milk": 1.45}
print(prices)   # {'milk': 1.45}
```

Values do not need to be unique and may be mutable:

```python
regional_targets = {
    "UK": 200,
    "EU": 200,
    "USA": 200,
}
```

Several keys can legitimately map to the same value.

## Adding and updating entries

Assign to a new key to add an entry:

```python
food_prices["bread"] = 1.20
```

Assign to an existing key to update its value:

```python
food_prices["milk"] = 1.40
```

`update()` can add or replace several entries:

```python
food_prices.update({"rice": 2.10, "pasta": 0.85})
```

Dictionaries do not have `append()` because entries are established through keys rather than appended as anonymous positional elements.

## Safe lookup

Direct lookup is appropriate when a missing key indicates a programming or data error:

```python
price = food_prices["milk"]
```

Use membership testing when absence is expected:

```python
if "coffee" in food_prices:
    print(food_prices["coffee"])
else:
    print("Coffee has no recorded price")
```

`get()` can return a fallback without raising `KeyError`:

```python
price = food_prices.get("coffee")          # None if absent
price = food_prices.get("coffee", 0.0)     # chosen default
```

Choose a default carefully. A price of `0.0` may mean “free,” which is different from “unknown.”

## Removing entries

`del` removes a known key and raises `KeyError` if it is absent:

```python
del food_prices["bread"]
```

`pop()` removes a key and returns its value:

```python
removed_price = food_prices.pop("pasta")
```

A default makes `pop()` safe for an absent key:

```python
removed_price = food_prices.pop("coffee", None)
```

`clear()` removes all entries from the existing dictionary.

## Keys, values, and items

Dictionary view objects expose different parts of the mapping:

```python
print(food_prices.keys())
print(food_prices.values())
print(food_prices.items())
```

Iterating over a dictionary directly visits its keys:

```python
for item in food_prices:
    print(item)
```

Use `items()` to process each pair:

```python
for item, price in food_prices.items():
    print(f"{item}: £{price:.2f}")
```

The views are dynamic: they reflect subsequent changes to the dictionary.

## The `zip()` function

`zip()` pairs elements at corresponding positions in iterables:

```python
countries = ["Japan", "Italy", "Brazil", "India"]
life_expectancy = [83.7, 82.7, 75.9, 68.3]

pairs = list(zip(countries, life_expectancy))
print(pairs)
```

The result contains tuples:

```text
[("Japan", 83.7), ("Italy", 82.7), ("Brazil", 75.9), ("India", 68.3)]
```

Pass the zipped pairs to `dict()`:

```python
life_by_country = dict(zip(countries, life_expectancy))
```

By default, `zip()` stops when the shortest iterable is exhausted. Validate lengths when silently losing unpaired data would be a problem.

Use ordered sequences with an established positional relationship. Do not zip two independent sets to invent pairings: sets do not provide a meaningful corresponding order.

## Dictionary comprehensions

A dictionary comprehension creates key–value pairs:

```python
squares = {number: number ** 2 for number in range(1, 6)}
```

Its general form is:

```text
{key_expression: value_expression for item in iterable if condition}
```

For example, select positive temperatures:

```python
temperatures = {"A": -2.5, "B": 4.0, "C": 12.3}
positive = {place: value for place, value in temperatures.items() if value > 0}
```

If a comprehension generates the same key repeatedly, the later value replaces the earlier one.

## Insertion order and sorting

Python dictionaries preserve insertion order as a language guarantee in Python 3.7 and later. This does not mean they automatically sort their keys.

Iterate in sorted key order without changing the dictionary:

```python
for country in sorted(life_by_country):
    print(country, life_by_country[country])
```

`sorted(life_by_country)` returns a list of sorted keys.

Sort pairs by key and construct a new insertion-ordered dictionary:

```python
sorted_by_country = dict(sorted(life_by_country.items()))
```

Sort by value using a key function:

```python
sorted_by_value = dict(
    sorted(life_by_country.items(), key=lambda pair: pair[1])
)
```

Sorting creates a new list of items and optionally a new dictionary; it does not alter the fundamental key-based nature of lookup.

## Converting pairs to a dictionary

`dict()` expects each pair in a two-item iterable to supply a key followed by a value:

```python
month_data = [(28, "February"), (30, "April"), (31, "July")]
```

Here, the desired output uses month names as keys, so reverse each pair:

```python
days_by_month = {month: days for days, month in month_data}
```

This produces:

```python
{"February": 28, "April": 30, "July": 31}
```

Always identify which component is the unique lookup key before constructing the dictionary.

## Nested dictionaries

Dictionary values may themselves be dictionaries:

```python
countries = {
    "Japan": {
        "temperature": 11.9,
        "population": 125.7,
        "gdp": 4937,
    },
    "India": {
        "temperature": 24.6,
        "population": 1393,
        "gdp": 3173,
    },
}
```

Retrieve a nested value by following its keys:

```python
print(countries["Japan"]["population"])
```

Use clear names and formatting; deeply nested structures can become difficult to navigate and validate.

## Dictionaries and JSON

JSON—JavaScript Object Notation—is a text format widely used for exchanging structured data. A JSON object resembles a Python dictionary, but they are not identical types.

Convert a Python object to JSON text with `json.dumps()`:

```python
import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

json_text = json.dumps(person)
print(type(json_text))   # str
```

Parse JSON text with `json.loads()`:

```python
json_text = '{"name": "John", "age": 30, "city": "New York"}'
person = json.loads(json_text)
print(type(person))      # dict
```

Important differences include:

- JSON object keys are strings;
- JSON uses `true`, `false`, and `null`, while Python uses `True`, `False`, and `None`;
- tuples and sets do not have direct JSON equivalents;
- JSON is a serialised text representation, not a live Python dictionary.

Keys do not automatically represent database columns, nor values rows. JSON can represent nested objects and arrays in many shapes.

## Reading an API response

Web APIs often return JSON. The `requests` package can retrieve and decode a response:

```python
import requests

url = "https://randomuser.me/api/"
response = requests.get(url, timeout=10)
response.raise_for_status()
data = response.json()
```

The exact structure belongs to that external API and may change. Inspect the returned data or consult its documentation before following nested keys:

```python
name = data["results"][0]["name"]
print(name)
```

Production programs should handle timeouts, network failures, unexpected status codes, invalid JSON, and missing keys. The example introduces the data journey rather than providing complete error handling.

## Pause and predict

Predict the final dictionary and every printed value:

```python
prices = {"milk": 1.30, "pasta": 0.75}
prices["milk"] = 1.40
prices["bread"] = 1.20

print(prices.get("coffee"))
print("pasta" in prices)
print(list(prices.keys()))
print(prices)
```

Explain why updating `"milk"` does not create a second key.

## Common misconceptions

- A dictionary is accessed by keys, not positional indexes.
- `{}` creates a dictionary, while `set()` creates an empty set.
- Dictionary keys must be unique and hashable; values need not be unique.
- Assigning to an existing key updates its value.
- Dictionaries preserve insertion order but are not automatically sorted.
- `zip()` pairs by iteration position and stops at the shortest input.
- Independent sets should not be zipped when specific pairings matter.
- JSON text resembles a dictionary but is a `str` until parsed.
- JSON keys and values do not simply correspond to database columns and rows.

## Check your understanding

1. What relationship does a dictionary represent?
2. What happens when an existing key is assigned a new value?
3. When is `get()` preferable to direct subscription?
4. What do `keys()`, `values()`, and `items()` expose?
5. Why can a list not be a dictionary key?
6. What does `zip()` do with inputs of different lengths?
7. How does JSON text differ from a Python dictionary?

## Apply your learning

1. Create a food-price dictionary, retrieve one price, add an item, and update another.
2. Write a function that calculates the arithmetic mean of numeric dictionary values. Decide how it should handle an empty dictionary.
3. Convert a list of `(days, month)` tuples into a dictionary whose month names are keys.
4. Merge separate temperature, population, and GDP dictionaries into one nested dictionary keyed by country.
5. Add a calculated GDP-per-capita entry to each nested country record, checking the units of the supplied figures.
6. Convert a dictionary to JSON text and back, inspecting the type at each stage.

## Page summary

Dictionaries are mutable mappings from unique, hashable keys to values. They support direct lookup, safe retrieval, mutation, deletion, iteration, comprehensions, and nesting. Insertion order is preserved, while sorting is explicit. JSON provides a related text representation used in data exchange and APIs, but it is not itself a Python dictionary.

**Previous:** Page 2: Sets  
**Next step:** Complete the Sets and Dictionaries practical notebook and check your understanding using membership, comparison, lookup, mutation, and nested-data tasks.

---

# Suggested VLE setup

Create one learning module titled **4 Python Data Structures II: Sets and Dictionaries**, containing:

1. **Start here: overview and learning outcomes**
2. **4.1 Recap on Lists and Tuples**
3. **4.2 Sets**
4. **4.3 Dictionaries**
5. **Sets and Dictionaries practical notebook**
6. **Check your learning**

Add previous/next navigation and use each second-level heading in the page contents. The short recap should activate prior knowledge without reteaching all of Lecture 3.

Keep the JSON/API material at the end of the Dictionaries page as an authentic application. It can be labelled as an extension if network access or the `requests` package is unavailable in the practical environment.
