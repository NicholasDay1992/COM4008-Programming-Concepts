# COM4008 Programming Concepts: Inheritance, Encapsulation and Polymorphism

This content is designed as three linked VLE information pages. A short classes-and-objects recap is incorporated into Page 1 rather than presented as a separate page.

---

# Page 1: Inheritance

## On this page

- A short prerequisite recap
- Composition compared with inheritance
- Base classes and subclasses
- Inherited and specialised behaviour
- Initialising inherited state with `super()`
- Method overriding and the method-resolution order
- Type relationships
- Custom exception classes

## Learning outcomes

By the end of this page, you should be able to:

- recall how classes define and initialise objects;
- distinguish **has-a** composition from **is-a** inheritance;
- define a subclass in Python;
- initialise shared and specialised state;
- override and extend inherited methods;
- explain `super()` at an introductory level;
- test object relationships using `isinstance()` and `issubclass()`;
- define a simple custom exception class.

## Ready for inheritance? A short recap

A class defines state and behaviour for its objects:

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def get_summary(self):
        return f"{self.name}: {self.student_id}"
```

Calling the class creates and initialises an instance:

```python
nick = Student("Nick", 21345628)
sam = Student("Sam", 29876543)
```

`self` receives the current object in an instance method. `__init__()` establishes its initial state. Each separately created object has its own instance attributes.

Lecture 7 also introduced composition:

```python
student.course = computing_course
```

A student **has a** course. Inheritance represents a different relationship.

## The **is-a** test

Inheritance lets one class specialise another:

```text
Student is a Person
Staff is a Person
Dog is an Animal
```

The broader class is called a **base class**, **parent class**, or **superclass**. The specialised class is called a **subclass**, **child class**, or **derived class**.

Use inheritance when an object of the subclass can genuinely be used wherever the base type is expected. This substitutability is stronger than merely sharing a few attributes.

Do not use inheritance for a **has-a** relationship:

```text
Student has a Course     → composition
Course has Modules       → composition
Student is a Person      → possible inheritance
```

## Defining a subclass

Place the base class in parentheses:

```python
class Person:
    def get_category(self):
        return "Person"


class Student(Person):
    pass
```

`Student` inherits accessible behaviour from `Person`:

```python
student = Student()
print(student.get_category())   # Person
```

`pass` means the subclass adds nothing yet. It is still a distinct class.

## Shared and specialised state

Put genuinely shared state in the base class:

```python
class Person:
    def __init__(self, name, university_id):
        self.name = name
        self.university_id = university_id

    def get_summary(self):
        return f"{self.name} ({self.university_id})"
```

Subclasses add their specialised state:

```python
class Student(Person):
    def __init__(self, name, university_id, mark):
        super().__init__(name, university_id)
        self.mark = mark


class Staff(Person):
    def __init__(self, name, university_id, objective):
        super().__init__(name, university_id)
        self.objective = objective
```

`Student` and `Staff` avoid duplicating the common initialisation.

## What `super()` means

`super()` returns a proxy that searches for methods after the current class in Python's **method-resolution order**, or MRO:

```python
super().__init__(name, university_id)
```

For this simple single-inheritance hierarchy, that finds `Person.__init__()`. It is useful shorthand to say “call the base implementation,” but `super()` does not create or return a separate parent object. The same child object is being initialised.

Using the MRO matters when multiple inheritance is involved. Multiple inheritance is possible in Python but is not required for the core Lecture 8 work.

Inspect the resolution order when useful:

```python
print(Student.mro())
```

## Overriding a method

A subclass can supply its own implementation of an inherited method:

```python
class Person:
    def get_summary(self):
        return self.name


class Student(Person):
    def get_summary(self):
        return f"{self.name}, mark: {self.mark}"
```

Calling `student.get_summary()` uses the `Student` implementation because Python searches the object's class before its base classes.

A subclass can extend rather than replace base behaviour:

```python
class Staff(Person):
    def get_summary(self):
        base_summary = super().get_summary()
        return f"{base_summary}, objective: {self.objective}"
```

Returning strings keeps presentation flexible. Avoid naming a method `print`, which is less descriptive and resembles the built-in function.

## Type relationships

`isinstance()` includes inheritance relationships:

```python
student = Student("Sam", 29876543, 75)

print(isinstance(student, Student))  # True
print(isinstance(student, Person))   # True
print(type(student) is Person)       # False
```

Use `isinstance()` when subclasses should count as instances of a base type.

`issubclass()` tests class relationships:

```python
print(issubclass(Student, Person))   # True
```

## Validate at the right level

Shared rules belong in the base class; specialised rules belong in subclasses:

```python
class Person:
    def __init__(self, name, university_id):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name.strip():
            raise ValueError("name must not be empty")

        self.name = name.strip()
        self.university_id = university_id


class Student(Person):
    def __init__(self, name, university_id, mark):
        super().__init__(name, university_id)
        if not isinstance(mark, int) or isinstance(mark, bool):
            raise TypeError("mark must be an integer")
        if not 0 <= mark <= 100:
            raise ValueError("mark must be from 0 to 100")
        self.mark = mark
```

This avoids repeating name validation in every kind of person.

## Revisiting the exception hierarchy

Lecture 5 introduced exception families without requiring inheritance syntax. You can now read this properly:

```python
class InvalidMarkError(Exception):
    """Raised when a mark is outside the permitted format or range."""
```

`InvalidMarkError` **is an** `Exception`, so it can be caught specifically or by a broader `except Exception` handler.

```python
def validate_mark(mark):
    if not isinstance(mark, int) or isinstance(mark, bool):
        raise InvalidMarkError("Mark must be an integer.")
    if not 0 <= mark <= 100:
        raise InvalidMarkError("Mark must be from 0 to 100.")
    return mark
```

The base `Exception` initialiser already stores the message, so an empty subclass is often sufficient. Add a custom `__init__()` only when the exception genuinely needs structured context:

```python
class InvalidMarkError(Exception):
    def __init__(self, mark):
        self.mark = mark
        super().__init__(f"Mark must be an integer from 0 to 100; received {mark!r}")
```

Catch it at a boundary that can respond meaningfully:

```python
try:
    validate_mark(101)
except InvalidMarkError as error:
    print(error)
```

## Prefer composition when it fits

Inheritance creates coupling between a subclass and its base class. Ask whether shared behaviour truly represents an **is-a** relationship.

A course should not inherit from a module merely because both have a code. Extracting a tiny base class solely to reuse two assignments may be less clear than composition or a helper function.

Prefer shallow, meaningful hierarchies over deep family trees.

## Pause and predict

Predict which implementation runs:

```python
class Person:
    def role(self):
        return "person"


class Student(Person):
    def role(self):
        return "student"


person = Person()
student = Student()

print(person.role())
print(student.role())
print(isinstance(student, Person))
```

Then explain why `Student` satisfies the **is-a** test.

## Common mistakes

- Using inheritance for a **has-a** relationship.
- Repeating base initialisation instead of using `super()` appropriately.
- Treating `super()` as a separate parent object.
- Forgetting to initialise specialised subclass attributes.
- Calling `type(value) is Person` when subclasses should be accepted.
- Creating deep hierarchies merely to reuse small amounts of code.
- Catching custom exceptions only with a broad handler when a specific response is available.
- Adding a complicated custom exception initialiser without a need for extra context.

## Check your understanding

1. What is the difference between composition and inheritance?
2. What does a subclass inherit?
3. Why is `Student(Person)` an **is-a** claim?
4. What does `super()` search?
5. How does overriding differ from extending a method?
6. Why is `isinstance(student, Person)` true?
7. Why does a custom exception inherit from `Exception`?

## Apply your learning

1. Refactor `Student` and `Staff` to inherit genuinely shared state from `Person`.
2. Give each subclass one specialised attribute and behaviour.
3. Override a summary method and extend the base result with `super()`.
4. Use `isinstance()` and `issubclass()` to explore the relationships.
5. Define and handle `InvalidMarkError`.
6. Identify one relationship in the course model that should remain composition and explain why.

## Page summary

Inheritance represents an **is-a** relationship in which a subclass specialises a base class. Subclasses inherit behaviour, add state, and override methods. `super()` follows the method-resolution order and commonly invokes shared base initialisation. Meaningful, shallow inheritance complements rather than replaces composition. Custom exceptions provide an authentic example of specialised classes.

**Next:** Continue to **Page 2: Encapsulation, Information Hiding and Properties**.

---

# Page 2: Encapsulation, Information Hiding and Properties

## On this page

- Encapsulation and abstraction
- Public attributes
- Internal-use underscore conventions
- Name mangling
- Validation through methods
- Python properties
- Read-only and derived properties
- Designing a useful public interface

## Learning outcomes

By the end of this page, you should be able to:

- distinguish encapsulation, information hiding, and abstraction;
- interpret Python's public and underscore naming conventions;
- explain what name mangling does and does not do;
- validate state changes through behaviour;
- define a property and setter;
- create a read-only derived property;
- avoid unnecessary Java-style getter and setter methods.

## What is encapsulation?

**Encapsulation** groups state and the behaviour that operates on it inside a coherent object:

```python
class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def get_grade(self):
        if self.mark >= 70:
            return "A"
        if self.mark >= 60:
            return "B"
        return "Other"
```

The student state and grade behaviour live together.

**Information hiding** limits dependence on implementation details. **Abstraction** presents the essential operation while hiding unnecessary complexity. These ideas reinforce one another but are not exact synonyms.

A caller can ask for a grade without knowing the thresholds:

```python
print(student.get_grade())
```

## Python does not use Java-style access modifiers

Java, C#, and C++ provide keywords such as `public`, `private`, and `protected`. Python generally relies on naming conventions, properties, and thoughtful interfaces instead of strictly enforced per-member access controls.

An ordinary attribute is public:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

```python
student = Student("Nick")
print(student.name)
student.name = "Sam"
```

Public data is not automatically poor design. Direct access is appropriate when no invariant or behaviour needs protection.

## A single leading underscore

A leading underscore communicates that a name is intended for internal use:

```python
class Student:
    def __init__(self, name):
        self._name = name
```

External code can still access it:

```python
print(student._name)
```

The underscore is a convention, not enforced protection. It asks callers not to depend on that implementation detail. Calling it “protected” can be misleading because Python does not enforce subclass-only access.

## Double leading underscores and name mangling

A name beginning with two underscores and not ending with two triggers class name mangling:

```python
class Student:
    def __init__(self, name):
        self.__name = name
```

Python rewrites `__name` approximately as `_Student__name`. Direct `student.__name` access fails, but deliberately accessing the mangled name is possible.

Name mangling mainly prevents accidental name collisions in subclasses. It is not security, encryption, or true privacy. Use it sparingly; a single underscore and a property are often clearer.

Do not confuse user-defined `__name` with documented dunder methods such as `__init__()`.

## Preserve valid object state

If a mark must remain from 0 to 100, unrestricted assignment can break the invariant:

```python
student.mark = 500
```

A method can control the change:

```python
class Student:
    def __init__(self, name, mark):
        self.name = name
        self.set_mark(mark)

    def set_mark(self, mark):
        if not isinstance(mark, int) or isinstance(mark, bool):
            raise TypeError("mark must be an integer")
        if not 0 <= mark <= 100:
            raise ValueError("mark must be from 0 to 100")
        self._mark = mark

    def get_mark(self):
        return self._mark
```

This works, but Python properties provide normal attribute syntax with the same control.

## Properties

Define a getter with `@property` and an optional setter:

```python
class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("mark must be an integer")
        if not 0 <= value <= 100:
            raise ValueError("mark must be from 0 to 100")
        self._mark = value
```

Callers use natural syntax:

```python
student = Student("Nick", 65)
print(student.mark)
student.mark = 72
```

The assignment invokes validation automatically. `self.mark = mark` inside `__init__()` deliberately uses the setter so initial and later values follow the same rule.

## Read-only properties

Omit a setter when callers should not assign through the property:

```python
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
```

`full_name` is derived from existing state:

```python
print(student.full_name)
```

Attempting `student.full_name = "..."` raises `AttributeError` because no setter exists.

“Read-only property” does not make every underlying attribute immutable. It controls this route of assignment.

## Avoid mechanical getters and setters

This method adds little:

```python
def get_name(self):
    return self.name
```

If access is simple and unrestricted, use `student.name`. Add a property when retrieval or assignment needs validation, calculation, compatibility, logging, or another meaningful behaviour.

Python lets a public attribute evolve into a property later without changing the caller's syntax:

```python
student.mark
student.mark = 72
```

This is one reason Java-style accessor methods are not required from the outset.

## Interfaces and abstraction

A useful interface communicates what an object can do without exposing every detail:

```python
class BankAccount:
    def __init__(self, opening_balance=0):
        self._balance = opening_balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
```

Callers use `deposit()` and `withdraw()` rather than reproducing balance rules. Encapsulation protects a coherent model, not merely an attribute name.

## Encapsulation across inheritance

Subclasses should use the base class's intended interface rather than depend unnecessarily on its internals:

```python
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def get_summary(self):
        return f"Student: {self.name}"
```

Double-underscore name mangling can make subclass collaboration awkward. Use public or single-underscore names deliberately and document which behaviour subclasses may rely on.

## Pause and decide

For each item, choose public access, a single-underscore internal attribute, a property, or a behaviour method:

1. a student's freely displayed name;
2. a mark that must stay from 0 to 100;
3. a calculated full name;
4. a bank withdrawal that must check balance;
5. a cache used only by the class implementation.

Explain the reason for each choice.

## Common mistakes

- Treating a single underscore as enforced protection.
- Treating name mangling as security or true privacy.
- Using double underscores for every attribute.
- Writing getters and setters that add no behaviour.
- Validating later assignments but not initial state.
- Bypassing a property by assigning directly to its backing attribute.
- Calling encapsulation and abstraction identical concepts.
- Exposing internal representation that callers do not need.

## Check your understanding

1. What does encapsulation group together?
2. What does a single underscore communicate?
3. What is the main purpose of name mangling?
4. When is a property useful?
5. How does a read-only property work?
6. Why might `deposit()` be preferable to direct balance assignment?
7. How does abstraction relate to an object's public interface?

## Apply your learning

1. Replace explicit mark getter/setter methods with a validated property.
2. Add a read-only grade property derived from the mark.
3. Give `Course` a controlled `enrol_student()` method rather than exposing mutation rules everywhere.
4. Identify public and internal parts of your Lecture 7 class design.
5. Experiment with name mangling, then explain why accessing the mangled name should not be normal application code.

## Page summary

Encapsulation groups state with the behaviour that maintains it. Python uses public attributes, internal-use underscore conventions, selective name mangling, methods, and properties rather than Java-style enforced access modifiers. Properties preserve natural attribute syntax while adding validation or calculation. Good interfaces expose meaningful operations and hide unnecessary implementation detail.

**Previous:** Page 1: Inheritance  
**Next:** Continue to **Page 3: Polymorphism**.

---

# Page 3: Polymorphism

## On this page

- One interface, several forms
- Method overriding
- Subtype polymorphism
- Duck typing
- Polymorphic collections
- Operator overloading
- Designing compatible methods
- Polymorphism compared with inheritance

## Learning outcomes

By the end of this page, you should be able to:

- explain polymorphism as common operations with type-specific behaviour;
- use overridden methods through a common base-type interface;
- write a function that relies on duck typing;
- process mixed objects through the same method call;
- implement a simple special method for operator overloading;
- explain why inheritance is neither necessary nor sufficient for good polymorphism.

## What is polymorphism?

Polymorphism means “many forms.” In programming, the same operation or interface can produce behaviour appropriate to different objects.

You have already used polymorphic operations:

```python
print(len("Python"))
print(len([1, 2, 3]))
print(len({"A": 1, "B": 2}))
```

`len()` works with different types because they implement the expected length protocol.

The `+` operator also has type-specific behaviour:

```python
print(60 + 40)       # numeric addition
print("60" + "40") # string concatenation
```

Polymorphism lets calling code focus on an operation rather than repeatedly inspecting exact types.

## Method overriding and subtype polymorphism

Subclasses can override a common method:

```python
class Person:
    def get_role(self):
        return "Person"


class Student(Person):
    def get_role(self):
        return "Student"


class Staff(Person):
    def get_role(self):
        return "Staff"
```

A common function can accept any compatible person:

```python
def display_role(person):
    print(person.get_role())
```

Python chooses the method using the object's runtime type:

```python
people = [Student(), Staff(), Person()]

for person in people:
    display_role(person)
```

The call has one form—`person.get_role()`—but different implementations run. This is subtype polymorphism.

## Polymorphic collections

A list can hold objects of several subclasses:

```python
people = [
    Student("Sam", 29876543, 75),
    Staff("Nick", 21345628, "Curriculum development"),
]

for person in people:
    print(person.get_summary())
```

Each class should honour the expected method contract. If `get_summary()` returns a string for one subclass but unexpectedly prints or returns `None` for another, the interface is harder to use.

Polymorphism depends on compatible meaning, parameters, results, and exceptions—not merely identical method names.

## Duck typing

Python often uses behaviour rather than declared inheritance:

```python
class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


def announce(animal):
    print(animal.speak())
```

`Dog` and `Cat` need not share a custom base class. Both satisfy the operation needed by `announce()`.

```python
announce(Dog())
announce(Cat())
```

This informal approach is called **duck typing**: suitability is determined by supported behaviour.

The familiar saying predates Python and is not a quote that should be attributed confidently to Guido van Rossum. Its lesson is that code can depend on an interface rather than an exact nominal type.

## Handle incompatible objects deliberately

Passing an object without the expected method raises `AttributeError`:

```python
announce(42)
```

Do not automatically guard every call with `hasattr()`. If the function's contract requires `speak()`, an incompatible argument is often a caller defect and a clear exception is useful.

For public APIs, documentation, type hints, protocols, or explicit validation can communicate expectations. These are later refinements.

## Inheritance is not required for polymorphism

Duck typing demonstrates polymorphism without a shared custom base class. Conversely, merely inheriting does not create useful polymorphism unless subclasses provide behaviour that honours a common interface.

Use inheritance when the **is-a** relationship and shared implementation are meaningful. Use duck typing when compatible behaviour is enough.

## Operator overloading

Python maps operators to special methods. For example, `a + b` can call `a.__add__(b)`.

```python
print(int.__add__(60, 40))
print(str.__add__("60", "40"))
```

Custom classes can implement appropriate operators:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"
```

```python
first = Vector(1, 2)
second = Vector(3, 4)
print(first + second)  # Vector(4, 6)
```

Returning `NotImplemented` for an unsupported operand lets Python try reflected behaviour or raise an appropriate `TypeError`. Do not raise `NotImplemented`; it is a special value, distinct from `NotImplementedError`.

## Comparisons between objects

A student comparison needs a clearly defined meaning. Comparing average marks may be reasonable if documented:

```python
class Student(Person):
    def __init__(self, name, university_id, marks):
        super().__init__(name, university_id)
        self.marks = list(marks)

    @property
    def average_mark(self):
        if not self.marks:
            raise ValueError("student has no marks")
        return sum(self.marks) / len(self.marks)

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_mark > other.average_mark
```

```python
print(nick > sam)
```

Be cautious: “greater student” is ambiguous. A named method such as `has_higher_average_than()` may communicate intent better than an overloaded operator.

Overloading `+` to mutate a student's marks would be surprising because `+` normally returns a new value rather than changing the left operand. A clear `add_mark()` method is preferable:

```python
def add_mark(self, mark):
    self.marks.append(validate_mark(mark))
```

## Special methods as protocols

Special methods let objects participate in Python operations:

| Operation | Special method |
|---|---|
| `len(value)` | `value.__len__()` |
| `str(value)` | `value.__str__()` |
| `repr(value)` | `value.__repr__()` |
| `left + right` | `left.__add__(right)` |
| `left > right` | `left.__gt__(right)` |
| iteration | `__iter__()` and related protocol |

Application code normally uses `len(value)` or `left + right`, not direct dunder calls. Implement special methods only when the operation has a natural meaning.

## Polymorphism and abstraction

Polymorphism supports abstraction because calling code depends on an interface:

```python
def print_summaries(items):
    for item in items:
        print(item.get_summary())
```

The function does not need a chain such as:

```python
if isinstance(item, Student):
    ...
elif isinstance(item, Staff):
    ...
```

Repeated exact-type branching is often a sign that behaviour belongs in the classes. Type checks still have valid uses, particularly at data boundaries, but polymorphism can remove unnecessary branching from core behaviour.

## Pause and predict

Predict the output:

```python
class EmailNotification:
    def send(self):
        return "Email sent"


class TextNotification:
    def send(self):
        return "Text sent"


def deliver(notification):
    print(notification.send())


for item in [EmailNotification(), TextNotification()]:
    deliver(item)
```

Do these classes require inheritance for `deliver()` to work? Explain why.

## Common mistakes

- Assuming polymorphism always requires inheritance.
- Giving methods the same name but incompatible meanings or return types.
- Checking exact types everywhere instead of using a common interface.
- Calling dunder methods directly in normal application code.
- Raising `NotImplemented` instead of returning it.
- Overloading operators whose meaning is surprising or ambiguous.
- Mutating an object with `+` when callers expect a new result.
- Defining `Staf` accidentally and later constructing `Staff`.

## Check your understanding

1. What does “one interface, many forms” mean?
2. How does method overriding support polymorphism?
3. What is duck typing?
4. Why does duck typing not require inheritance?
5. What should an unsupported binary special method normally return?
6. Why might `add_mark()` be clearer than overloading `+`?
7. How can polymorphism reduce type-based conditional chains?

## Apply your learning

1. Override `get_summary()` in `Student` and `Staff`, then process both in one list.
2. Create two unrelated notification classes sharing a `send()` interface and write one delivery function.
3. Implement `__repr__()` for one domain class.
4. Compare students by average mark using either a well-documented `__gt__()` or a clearly named method; justify the choice.
5. Find a type-based conditional in your class project and decide whether polymorphism would improve it.

## Page summary

Polymorphism allows common operations to produce behaviour appropriate to different objects. Inherited method overriding provides subtype polymorphism, while duck typing depends only on compatible behaviour. Special methods integrate custom objects with operators and built-in protocols, but should reflect natural meanings. A reliable polymorphic interface requires compatible contracts, not merely matching names.

**Previous:** Page 2: Encapsulation, Information Hiding and Properties  
**Next step:** Complete the OOP II practical project by refining the Lecture 7 model with a meaningful hierarchy, protected invariants, and polymorphic behaviour.

---

# Suggested VLE setup

Create one learning module titled **8 Python OOP II: Inheritance, Encapsulation and Polymorphism**, containing:

1. **Start here: relationships and interfaces**
2. **8.1 Inheritance**
3. **8.2 Encapsulation, Information Hiding and Properties**
4. **8.3 Polymorphism**
5. **OOP II practical project**
6. **Check your learning**

Do not create a separate 8.0 recap page. The short recap at the beginning of 8.1 is enough to reactivate `self`, `__init__()`, instances, and composition before introducing the **is-a** relationship.

Use the exception hierarchy as an authentic inheritance revisit in 8.1. Keep multiple inheritance, abstract base classes, protocols, and advanced MRO cases outside the core lecture. These can become extensions once students can confidently distinguish inheritance, composition, encapsulation, and polymorphism.
