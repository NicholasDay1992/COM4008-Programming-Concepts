# COM4008 Programming Concepts: Reliable Programming and Testing

This content is designed as five linked VLE information pages. Lecture 16 concludes the module by connecting readable design, defensive programming, debugging and systematic testing to the requirements and risks identified in Lecture 15.

---

# 16.1 Reliability, Faults and Defensive Programming

## On this page

- Reliability as a software quality
- Faults, errors and failures
- Fault avoidance, input validation and failure management
- Problem, technology and interaction risks
- Defensive programming
- Reliability requirements and evidence

## Learning outcomes

By the end of this page, you should be able to:

- explain reliability from a user's perspective;
- distinguish a fault, an erroneous state and an observable failure;
- identify common sources of software faults;
- distinguish fault avoidance, validation and failure management;
- write a measurable reliability requirement;
- select proportionate evidence for a reliability claim.

## Reliability creates justified trust

Users rely on software to behave consistently under stated conditions. A messaging service that loses half its messages is not useful; an online store must protect orders and customer data; safety-critical systems demand much stronger evidence because failure can cause harm.

Reliability is therefore not simply “the program ran once.” It concerns the probability or consistency of correct service over time and under defined operating conditions.

Reliability interacts with other qualities:

- **availability:** whether the service is ready when needed;
- **security:** whether information and behaviour are protected;
- **resilience:** whether the product can tolerate and recover from disruption;
- **maintainability:** whether faults can be corrected safely;
- **usability:** whether people can operate it without creating avoidable errors;
- **responsiveness:** whether it responds within an acceptable time.

## Fault, error and failure

These terms are often used informally, but a useful distinction is:

```text
fault in code or design
        ↓ executes
incorrect internal state (error)
        ↓ reaches an observable boundary
failure visible to a user or another system
```

An off-by-one loop condition is a **fault**. If it leaves the last Invader unprocessed, the program enters an incorrect state. If the level never ends, the user observes a **failure**.

Not every fault produces a failure on every run. A particular input or state may be required to activate it. Testing deliberately searches for those revealing conditions.

## Where faults come from

Faults may arise because developers:

- misunderstand the problem or omit a requirement;
- make mistakes while translating a design into code;
- misunderstand a language, library or platform;
- combine components whose assumptions conflict;
- fail to consider malformed input or an unavailable resource;
- change one part without recognising its dependencies;
- optimise or generalise before the behaviour is understood.

This is why reliability cannot be added only at the end. Requirements, design, coding, review and testing all contribute.

## Three complementary approaches

### Fault avoidance

Make faults less likely to enter the product:

- keep responsibilities clear;
- use meaningful names and language conventions;
- prefer simple control flow;
- compile, lint and review frequently;
- reuse well-understood components;
- make small, reviewed changes;
- write tests alongside behaviour.

### Input validation

Check information entering a trusted part of the program:

- type and format;
- permitted range;
- length and required fields;
- relationships between values;
- file or resource availability;
- authorisation where relevant.

Validation should occur at system boundaries. Internal functions can then rely on clearer contracts.

### Failure management

Reduce the impact when something still goes wrong:

- preserve or restore a safe state;
- provide a clear, non-sensitive message;
- log diagnostic context;
- release files and other resources;
- retry only when appropriate;
- isolate damage and continue unaffected work;
- stop safely when continued operation would be dangerous.

## Defensive programming example

```python
def set_volume(level: int) -> int:
    if not isinstance(level, int):
        raise TypeError("volume must be an integer")
    if not 0 <= level <= 100:
        raise ValueError("volume must be between 0 and 100")
    return level
```

The function makes its accepted domain explicit and rejects invalid calls close to their source. It does not silently convert arbitrary input or continue with a corrupt value.

Defensive programming does not mean checking every variable repeatedly. Choose checks according to trust boundaries, consequences and cost.

## Write reliability requirements

“The game shall be reliable” cannot be tested. Better requirements define behaviour and conditions:

```text
REL-01: If the level file is missing or unreadable, the application shall
display a user-readable message and return to the level-selection screen
without losing saved progress.
```

Possible evidence includes:

- automated tests for missing and malformed files;
- a manual recovery scenario;
- inspection of saved state before and after failure;
- logs showing the technical cause without exposing private data.

The strength of evidence should reflect the harm caused by failure. A classroom game and aircraft control software require very different assurance.

## Pause and follow the failure chain

Suppose the code assumes a list always contains at least one Invader. The final Invader is removed, and the next update accesses `invaders[0]`.

Identify:

- the faulty assumption;
- the erroneous program state;
- the possible user-visible failure;
- one avoidance measure;
- one validation or guard;
- one safe failure response;
- one test that would expose it.

## Common mistakes

- **Calling one successful execution reliable:** reliability concerns repeated service under stated conditions.
- **Using fault, error and failure interchangeably:** separating cause, internal state and observed outcome improves diagnosis.
- **Validating only happy-path input:** include boundaries, malformed data and missing resources.
- **Silently correcting every invalid value:** callers may need to know that their request was rejected.
- **Catching a failure without recovery:** suppressing an error can leave incorrect state hidden.
- **Logging confidential data:** diagnostics must not create a security problem.
- **Demanding identical assurance for every project:** match evidence to risk and consequences.
- **Treating testing as the only reliability practice:** prevention, validation and failure management also matter.

## Check your understanding

1. What does reliability mean from a user's perspective?
2. How do a fault, error and failure differ?
3. Give one problem fault and one technology fault.
4. How do fault avoidance and failure management complement each other?
5. Where should input validation normally occur?
6. Why must reliability requirements include operating conditions?

## Apply your learning

1. Find a possible fault in one earlier exercise and trace its failure chain.
2. Write three measurable reliability requirements for the assignment.
3. Identify untrusted inputs and define their valid domains.
4. Add clear validation to one function and test the boundary values.
5. Design a safe response to a missing file or unavailable API.
6. Rank three failures by impact and propose proportionate evidence for each.

## Page summary

Reliability is justified confidence that software will provide correct service under stated conditions. Faults can create erroneous states and observable failures. Reliable products combine fault avoidance, input validation and failure management throughout development. Requirements and evidence must be specific and proportionate to risk.

**Next:** Continue to **16.2 Controlling Complexity and Refactoring**.

---

# 16.2 Controlling Complexity and Refactoring

## On this page

- Single responsibility and cohesion
- Structural and conditional complexity
- Side effects, coupling and inheritance depth
- Code smells
- Refactoring without changing external behaviour
- Guard clauses and readable conditions
- Using tests to protect refactoring

## Learning outcomes

By the end of this page, you should be able to:

- explain how complexity increases fault risk;
- apply the single responsibility principle proportionately;
- identify common code smells;
- simplify nested conditionals with guard clauses;
- distinguish refactoring from adding functionality;
- use regression tests to preserve behaviour during change.

## Complexity consumes attention

Reliable programming is partly the management of human cognitive limits. When a method has many responsibilities, conditions and hidden dependencies, it becomes harder to predict the consequences of a change.

Two useful categories are:

- **structural complexity:** how components, responsibilities and dependencies are organised;
- **conditional complexity:** how many paths and combinations the control flow creates.

Complexity is not automatically poor design. Some problems are genuinely complex. The aim is to avoid accidental complexity and express necessary complexity clearly.

## Single responsibility

A class or function should have one coherent reason to change. This is more useful than the literal slogan “do one line of work.”

```python
def load_validate_score_and_email_report(path, address):
    ...
```

This function mixes file input, validation, calculation and communication. Smaller responsibilities are easier to understand and test:

```python
def load_scores(path): ...
def validate_scores(scores): ...
def calculate_summary(scores): ...
def send_report(address, summary): ...
```

Related behaviour should remain cohesive; splitting every three lines into a new function can make navigation worse rather than better.

## Side effects and dependencies

A side effect changes or interacts with something outside a function's returned value—for example, modifying shared state, writing a file, displaying output or calling a network service.

Useful software needs side effects. The practical rule is to **isolate and make them explicit**, while keeping calculation logic as pure as practical. This makes behaviour more predictable and tests less dependent on the environment.

Prefer passing dependencies into a component rather than creating hidden global dependencies. A function that receives data is easier to test than one that secretly reads a particular file.

## Avoid unnecessarily deep inheritance

Inheritance can express genuine specialisation, but a deep hierarchy increases coupling. To understand one subclass, a developer may need to inspect several ancestors; changing a superclass may affect many descendants.

Ask:

- Is every subclass genuinely substitutable for its parent?
- Does the shared behaviour belong in the parent?
- Would composition make the dependency clearer?
- Can the hierarchy remain shallow?

Avoiding deep inheritance is guidance, not a ban on inheritance.

## Code smells

A **code smell** is an indicator worth investigating, not proof of a defect.

Common smells include:

- a large class with unrelated responsibilities;
- a long method with multiple levels of abstraction;
- duplicated logic;
- deeply nested conditionals;
- long parameter lists;
- meaningless names;
- unexplained constants;
- a change that repeatedly requires edits across many files;
- comments that compensate for unclear code.

The correct response depends on context. Duplicating two obvious lines once may be clearer than inventing a premature abstraction.

## Refactoring

Refactoring changes the internal structure of code while preserving its externally observable behaviour. Examples include:

- rename variable or method;
- extract function;
- remove duplication;
- simplify a condition;
- move responsibility to another class;
- replace inheritance with composition.

Adding a new game mechanic is not refactoring because behaviour changes. Correcting a faulty result is a bug fix. A single commit may contain both, but separating them reduces risk.

## Simplify conditional flow

Deep nesting forces the reader to remember several unresolved conditions:

```python
def premium_multiplier(age, experience):
    if age <= 25:
        if experience <= 2:
            return 4
        else:
            return 2
    else:
        if 70 < age <= 80:
            if experience <= 5:
                return 1.5
            else:
                return 1
        else:
            if age > 80:
                return 2
    return 1
```

Guard clauses and direct returns flatten the main path:

```python
def premium_multiplier(age, experience):
    if age <= 25 and experience <= 2:
        return 4
    if age <= 25:
        return 2
    if 70 < age <= 80 and experience <= 5:
        return 1.5
    if age > 80:
        return 2
    return 1
```

This version is shorter, but readability still depends on agreed boundary rules. What should happen at ages 25, 70 and 80? What about negative age or experience? Validation and tests make those assumptions explicit.

## Refactor safely

```text
establish passing tests
        ↓
make one small structural change
        ↓
run tests and inspect the code
        ↓
commit the coherent improvement
        └────────────↺
```

Tests do not prove the refactoring safe for every possible input, but they provide rapid regression evidence. Add characterisation tests first when existing behaviour is poorly documented.

## Pause and smell the code

Review one earlier notebook or class. Identify one smell, then answer:

- What maintenance risk does it suggest?
- Is the smell justified by the context?
- What small refactoring could improve it?
- Which existing behaviour must remain unchanged?
- Which tests would provide confidence?

## Common mistakes

- **Interpreting single responsibility as tiny code:** seek one coherent reason to change.
- **Claiming functions must never have side effects:** isolate necessary effects rather than denying them.
- **Treating every smell as a defect:** investigate before changing.
- **Removing all duplication immediately:** wait until the shared concept is understood.
- **Refactoring and adding features simultaneously:** separate structural and behavioural changes where practical.
- **Using early returns without clear conditions:** guard clauses must still express correct boundaries.
- **Using inheritance only to reuse code:** the relationship should also make conceptual sense.
- **Refactoring without regression tests:** establish behavioural evidence first.

## Check your understanding

1. What is accidental complexity?
2. How does cohesion relate to single responsibility?
3. Why should side effects be isolated?
4. What does a code smell tell you?
5. How does refactoring differ from a bug fix?
6. Why can guard clauses improve readability?
7. How do automated tests support refactoring?

## Apply your learning

1. Extract responsibilities from one long function.
2. Replace one deeply nested conditional with clear guard clauses.
3. Add tests for every boundary before and after the change.
4. Find duplicated logic and decide whether an abstraction is justified.
5. Review an inheritance hierarchy and propose composition where appropriate.
6. Commit the refactoring separately from the next feature.

## Page summary

Structural and conditional complexity make software harder to reason about and change safely. Cohesive responsibilities, explicit dependencies, shallow hierarchies and readable control flow reduce avoidable risk. Code smells guide investigation; refactoring improves internal structure while regression tests check that external behaviour remains stable.

**Previous:** Return to **16.1 Reliability, Faults and Defensive Programming**.

**Next:** Continue to **16.3 Validation, Exceptions, Assertions and Debugging**.

---

# 16.3 Validation, Exceptions, Assertions and Debugging

## On this page

- Validating data at boundaries
- Raising and handling exceptions
- Catching specific exceptions
- Cleanup and safe failure
- Appropriate use of assertions
- Reading tracebacks
- Breakpoints, stepping, variables and the call stack
- A disciplined debugging process

## Learning outcomes

By the end of this page, you should be able to:

- validate input against an explicit contract;
- raise a suitable exception when a function cannot fulfil its contract;
- handle expected failures at an appropriate boundary;
- distinguish assertions from ordinary validation;
- interpret a traceback and call stack;
- use breakpoints and stepping to test a debugging hypothesis.

## Validate before trusting data

External input may come from a user, file, API, command-line argument or saved game. Define its valid domain before processing it.

```python
def parse_level(value: str) -> int:
    try:
        level = int(value)
    except ValueError as error:
        raise ValueError("level must be a whole number") from error

    if not 1 <= level <= 10:
        raise ValueError("level must be between 1 and 10")

    return level
```

Conversion and range validation are separate concerns. The function returns a valid level or raises a clear exception; it does not return a mixture of integers and error strings.

## Raise where the problem is recognised

An exception communicates that normal processing cannot continue as requested:

```python
def withdraw(amount, balance):
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount > balance:
        raise ValueError("insufficient funds")
    return balance - amount
```

The function detects the violated rule. A user-interface layer can decide how to present the failure.

In Java, the corresponding concepts use `throw`, `try` and `catch`. The syntax differs, but the design question is the same: where is the failure understood, and where can it be handled responsibly?

## Handle only what you can handle

```python
try:
    level = load_level(path)
except FileNotFoundError:
    show_message("That level file could not be found.")
except PermissionError:
    show_message("The level file cannot be read.")
```

Catch specific expected exceptions. A broad `except Exception:` can hide programming faults if it merely continues. Unexpected exceptions should often be logged and allowed to propagate to an appropriate boundary.

Use `finally` or a context manager for necessary cleanup:

```python
with open(path, encoding="utf-8") as source:
    data = source.read()
```

The context manager closes the file whether reading succeeds or fails.

## Assertions express internal assumptions

An assertion checks a condition that the programmer expects to be true:

```python
assert remaining_invaders >= 0, "count cannot be negative"
```

Assertions are useful in tests and for internal invariants during development. They are not a substitute for validating user input or enforcing essential runtime rules. Python can omit assertion code when run with optimisation, so correctness must not depend on an assertion being executed.

Use ordinary conditional checks and exceptions for conditions that can arise legitimately in production:

```python
if height < 1:
    raise ValueError("height must be at least 1")
```

## Read the traceback from the failure backwards

A Python traceback reports the call sequence leading to an unhandled exception. Begin with the final line:

- exception type;
- message;
- line where the exception emerged.

Then move backwards through the frames to understand how execution reached that line. The detected line is not always where the faulty assumption began.

## Debugging is controlled investigation

A productive debugging cycle is:

1. reproduce the failure consistently;
2. state expected and actual behaviour;
3. reduce the input or scenario;
4. form a specific hypothesis;
5. collect evidence using a test, log or debugger;
6. correct the cause rather than the symptom;
7. add a regression test;
8. rerun relevant and wider tests.

Random edits followed by repeated running make learning slower and can introduce additional faults.

## Debugger tools

- **Breakpoint:** pause before a selected line executes.
- **Step over:** execute the current line without entering called functions.
- **Step into:** enter the called function.
- **Step out:** complete the current function and return to its caller.
- **Variables/watch:** inspect current values and expressions.
- **Call stack:** inspect the active chain of function or method calls.
- **Exception breakpoint:** pause when a chosen exception is raised.
- **Debug console:** evaluate expressions in the paused context.

Place a breakpoint where your expectation and the program's state may diverge, not automatically on the first line.

## Pause and diagnose

A game ends one Invader too early. Before changing code, write:

- the smallest reproducible starting state;
- the expected count after one collision;
- the actual count;
- one hypothesis;
- a breakpoint location;
- the variables you will inspect;
- the regression test you will add after fixing it.

## Common mistakes

- **Returning error text instead of raising:** this creates inconsistent return types.
- **Catching every exception:** unexpected programming faults become hidden.
- **Catching at a layer that cannot recover:** allow the failure to reach a responsible boundary.
- **Using assertions for user input:** assertions may be disabled and describe programmer assumptions.
- **Ignoring traceback frames:** the cause may begin before the final line.
- **Changing several lines before reproducing the issue:** preserve evidence and isolate the cause.
- **Printing everywhere without a hypothesis:** targeted diagnostics are more informative.
- **Fixing without a regression test:** the same fault can return unnoticed.

## Check your understanding

1. Why separate conversion from range checking?
2. Where should an exception be raised and handled?
3. Why prefer specific exception types?
4. What does a context manager contribute?
5. When is an assertion appropriate?
6. Why should essential validation not use `assert`?
7. What information does the call stack provide?

## Apply your learning

1. Add validation and clear exceptions to one earlier function.
2. Test a valid input, both boundaries and three invalid inputs.
3. Replace one broad exception handler with specific handling.
4. Use a context manager for file access.
5. Set a breakpoint in a loop and inspect how values change.
6. Document one debugging session as hypothesis, evidence, correction and regression test.

## Page summary

Validation defines what data is acceptable, while exceptions communicate that normal processing cannot continue. Raise failures where rules are known and handle expected failures where recovery is possible. Assertions express internal assumptions rather than production input rules. Tracebacks, breakpoints and the call stack support evidence-driven debugging, which should conclude with a regression test.

**Previous:** Return to **16.2 Controlling Complexity and Refactoring**.

**Next:** Continue to **16.4 Designing an Effective Test Strategy**.

---

# 16.4 Designing an Effective Test Strategy

## On this page

- Testing as evidence rather than proof
- Programming and understanding faults
- Unit, integration, system and acceptance testing
- Functional and non-functional testing
- Test cases and oracles
- Equivalence partitioning and boundary-value analysis
- Positive, negative and state-based tests
- Coverage and residual risk

## Learning outcomes

By the end of this page, you should be able to:

- explain what a passing or failing test establishes;
- distinguish major levels and purposes of testing;
- derive test cases from requirements and risks;
- identify a suitable test oracle;
- use equivalence partitions and boundary values;
- include invalid, empty and repeated cases;
- interpret coverage without treating it as proof of correctness.

## Testing compares actual and expected behaviour

A test needs:

1. a known starting state;
2. an input or action;
3. an expected result—the **test oracle**;
4. an actual result;
5. a comparison and recorded outcome.

A passing test shows that the observed behaviour matched its expectation in that case and environment. It does not prove that the program is correct for all inputs. A failing test shows a mismatch that must be investigated; the product, test, requirement or environment could be wrong.

## Two broad sources of bugs

- **Programming fault:** the intended rule is understood but represented incorrectly—for example, `<=` instead of `<`.
- **Understanding fault:** the developer's model of required behaviour or real data is incomplete—for example, assuming every imported row contains a valid number.

Tests derived only from the existing code may repeat its misunderstanding. Requirements, examples, user feedback and independent review provide additional oracles.

## Levels of testing

| Level | Main focus | Example |
|---|---|---|
| Unit | one small function, method or class in isolation | calculate pyramid coordinates |
| Integration | interaction between components | collision updates score and removes actors |
| System | the complete product in a representative environment | play a whole level |
| Acceptance | evidence that stakeholder needs are met | assessor/player checks assignment scenarios |

Terminology varies between organisations. The important point is to test small rules, component relationships and whole user outcomes.

## Different quality questions

- **Functional testing:** does required behaviour work?
- **Usability/user testing:** can relevant users achieve their goals effectively?
- **Performance/load testing:** are response time, throughput and capacity acceptable?
- **Security testing:** does the system resist misuse and protect information?
- **Compatibility testing:** does it work in supported environments?
- **Recovery testing:** does it return to a safe, useful state after disruption?

One unit-test suite cannot answer every quality question.

## Design a test case

```text
ID: FR-04-B2
Requirement: Defender remains within the play area
Starting state: Defender at x = 0
Action/input: request movement left
Expected result: x remains 0
Actual result: [recorded during execution]
Outcome: pass/fail/not run
```

Give each case a purpose. A large table of inputs without explanations is difficult to maintain.

## Equivalence partitioning

Inputs that the program should treat similarly can form a partition. For a permitted height of 1 to 8:

- values below 1: invalid;
- values 1 through 8: valid;
- values above 8: invalid;
- non-integer input: invalid.

Choose representatives from each partition rather than testing arbitrary values only from the middle.

## Boundary-value analysis

Faults cluster around boundaries. For the same range, test:

```text
0, 1, 2, 7, 8, 9
```

These values sit immediately below, on and immediately above each boundary. Also consider empty input, zero, one item, duplicate values, maximum capacity and repeated operations where relevant.

## State and sequence matter

Some failures depend on a sequence rather than one input:

- fire repeatedly until a projectile limit is reached;
- remove the last Invader;
- pause, resume and reset;
- save, modify and reload;
- collide two objects during the same update;
- retry after a failed file read.

State-transition tests should name the starting state and expected next state explicitly.

## Coverage is evidence, not a target by itself

Code coverage reports which statements or branches executed during tests. Unexecuted code indicates an obvious testing gap. High coverage does not show that assertions were meaningful or that every input combination was considered.

```python
def is_even(number):
    return True
```

A test calling `is_even(2)` can execute every line and pass while the function remains wrong for odd numbers. Coverage must be combined with good test design.

## Prioritise by risk

Test most deeply where:

- failure has serious impact;
- logic is complex;
- code changes frequently;
- dependencies are uncertain;
- earlier defects occurred;
- recovery is difficult;
- requirements are ambiguous.

Testing resources are finite. Risk helps decide where additional evidence is most valuable.

## Pause and design the boundaries

For a function accepting player names of 2 to 40 permitted characters, define:

- valid and invalid equivalence partitions;
- boundary lengths;
- empty and single-character cases;
- punctuation rules;
- repeated or malicious-looking input;
- the exact expected result for each case.

## Common mistakes

- **Calling a pass proof of correctness:** it supports one claim under specified conditions.
- **Assuming every failure means faulty product code:** the expectation or environment may be wrong.
- **Testing only typical valid input:** add boundaries and invalid partitions.
- **Confusing a test level with a test purpose:** unit/system and functional/security answer different dimensions.
- **Omitting a test oracle:** “observe what happens” is not a precise check.
- **Measuring coverage without assertions:** execution alone does not verify behaviour.
- **Testing implementation details unnecessarily:** prefer stable observable behaviour.
- **Ignoring state sequences:** many game faults emerge only after several actions.

## Check your understanding

1. What does a passing test establish?
2. What is a test oracle?
3. How do unit and integration testing differ?
4. Which testing purpose investigates response time?
5. What is an equivalence partition?
6. Why test immediately around boundaries?
7. Why does 100% statement coverage not prove correctness?

## Apply your learning

1. Build a test table for one assignment requirement.
2. Include normal, boundary, invalid, empty and repeated cases.
3. Add one state-transition sequence.
4. Identify the oracle for every expected result.
5. Classify each case by test level and purpose.
6. Prioritise the cases using likelihood and impact of failure.
7. Review whether the tests could pass while the implementation remains wrong.

## Page summary

Testing supplies evidence by comparing actual behaviour with an explicit oracle. A balanced strategy checks units, integrations, the whole system and stakeholder outcomes, as well as functional and non-functional qualities. Partitions, boundaries and state sequences reveal more than typical examples. Coverage identifies unexecuted code but cannot replace thoughtful assertions and risk-based test design.

**Previous:** Return to **16.3 Validation, Exceptions, Assertions and Debugging**.

**Next:** Continue to **16.5 Automated Testing and Test-Driven Development**.

---

# 16.5 Automated Testing and Test-Driven Development

## On this page

- Executable and repeatable tests
- Arrange-Act-Assert
- Testing with `pytest`
- Expected exceptions, approximate values and parametrisation
- Test isolation and fixtures
- Test-driven development
- Regression suites and continuous integration
- Transferring testing concepts between languages

## Learning outcomes

By the end of this page, you should be able to:

- explain the benefits and limitations of test automation;
- structure a focused test using Arrange-Act-Assert;
- write and run basic `pytest` tests;
- test expected exceptions and floating-point results;
- use parametrisation for related cases;
- explain the Red-Green-Refactor TDD cycle;
- recognise equivalent testing concepts in Python and Java.

## Make checks executable

An automated test stores its setup, action and expectation as executable code. It can be rerun quickly after a change and can produce a report showing passed, failed, skipped or erroneous tests.

Automation is particularly valuable for:

- deterministic unit and integration rules;
- regression checks run after every change;
- many input combinations;
- tests required across supported environments;
- feedback in a continuous-integration workflow.

Automation does not remove exploratory, usability or visual testing. Automate stable, repeatable checks and retain human investigation where judgement is essential.

## Arrange-Act-Assert

```python
def test_rectangle_area():
    # Arrange
    width = 4
    height = 5

    # Act
    result = rectangle_area(width, height)

    # Assert
    assert result == 20
```

- **Arrange:** create the starting state and inputs.
- **Act:** perform the behaviour under test.
- **Assert:** compare the observed result with the oracle.

Keep the Act phase focused. A test that performs many unrelated actions is harder to diagnose when it fails.

## A small `pytest` suite

Application code:

```python
def rectangle_area(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("dimensions must be positive")
    return width * height
```

Tests in `test_geometry.py`:

```python
import pytest

from geometry import rectangle_area


def test_rectangle_area_for_integers():
    assert rectangle_area(4, 5) == 20


def test_rectangle_area_for_floats():
    assert rectangle_area(0.1, 0.2) == pytest.approx(0.02)


def test_rectangle_rejects_zero_width():
    with pytest.raises(ValueError, match="positive"):
        rectangle_area(0, 5)
```

Run the suite from the project directory:

```text
python -m pytest
```

Test files and functions follow pytest's discovery conventions, commonly using names beginning with `test_`.

## Parametrise related cases

```python
@pytest.mark.parametrize(
    "width, height, expected",
    [
        (1, 1, 1),
        (4, 5, 20),
        (2.5, 4, 10),
    ],
)
def test_rectangle_areas(width, height, expected):
    assert rectangle_area(width, height) == pytest.approx(expected)
```

Parametrisation separates the general testing rule from its data. Give unusual cases descriptive IDs when raw values do not communicate their purpose.

## Keep tests independent

One test should not rely on another test running first. Shared mutable state creates order-dependent or flaky results.

A **fixture** supplies a defined, repeatable context such as a sample object, temporary file or configured service. It can also perform cleanup. Use the narrowest sensible fixture scope and keep dependencies explicit.

For file behaviour, pytest's `tmp_path` fixture supplies a separate temporary directory:

```python
def test_save_score(tmp_path):
    destination = tmp_path / "score.txt"

    save_score(destination, 120)

    assert destination.read_text() == "120"
```

## Test-driven development

TDD uses a small repeating cycle:

```text
RED: write a test for one desired behaviour and see it fail
  ↓
GREEN: write the simplest code that makes the test pass
  ↓
REFACTOR: improve structure while all tests remain green
  └────────────────────────────────────────────────────↺
```

Seeing the new test fail first matters. It demonstrates that the test can detect the absence of the behaviour and is not passing accidentally.

TDD can clarify interfaces, encourage small increments and create a regression suite. It does not automatically produce good requirements, good tests or good design. Exploratory work may also be needed when the solution is not yet understood.

## From requirement to automated evidence

```text
FR-07: Defender cannot move outside play area
        ↓
design: move_left() checks proposed x-coordinate
        ↓
tests: left boundary, interior, right boundary, repeated input
        ↓
automated report: pass/fail with diagnostic values
        ↓
review: requirement status and remaining manual evidence
```

This trace is the connection between Lectures 15 and 16.

## Regression and continuous integration

A regression suite reruns established tests after changes. In a collaborative project, a continuous-integration service can run it when code is pushed or a pull request is opened.

A useful result includes:

- which tests ran;
- which passed, failed, skipped or errored;
- diagnostic details;
- environment and revision;
- overall status.

A green report means the selected checks passed. It does not eliminate untested risk. Keep failed tests visible and investigate flaky tests rather than rerunning until they happen to pass.

## Transfer between frameworks

The syntax changes, but core concepts transfer:

| Concept | `pytest` | Python `unittest` | JUnit |
|---|---|---|---|
| identify test | `def test_...` | method on `TestCase` | method annotated as a test |
| equality check | plain `assert` | `self.assertEqual` | `assertEquals` |
| expected exception | `pytest.raises` | `assertRaises` | `assertThrows` |
| setup/context | fixture | `setUp`/helpers | lifecycle methods/extensions |
| report | pytest runner | unittest runner | build tool/IDE runner |

Learn the testing idea first, then consult the current documentation for a framework's exact version and syntax.

## Pause and write the first failing test

Choose one unimplemented or faulty requirement. Write:

- the smallest expected behaviour;
- a test name that describes it;
- the Arrange, Act and Assert phases;
- the expected failure before implementation;
- the minimal change to make it pass;
- one refactoring you might perform afterward.

## Common mistakes

- **Writing a test that never failed:** it may not detect the missing behaviour.
- **Combining many behaviours in one test:** a failure becomes hard to interpret.
- **Asserting only that no exception occurred:** verify the required result or state.
- **Comparing floating-point results with exact equality:** use an appropriate tolerance.
- **Sharing mutable state between tests:** tests become order-dependent.
- **Testing private implementation details unnecessarily:** tests become fragile during refactoring.
- **Treating TDD as test-after development:** the failing test guides the next small behaviour.
- **Assuming automation covers usability and visual quality:** retain suitable human evaluation.
- **Trusting a green report as complete proof:** it represents only the checks that ran.

## Check your understanding

1. What makes a test executable and repeatable?
2. What belongs in Arrange, Act and Assert?
3. Why use `pytest.approx()`?
4. How do you test an expected exception?
5. Why must tests remain independent?
6. What are the Red, Green and Refactor stages?
7. Why should a new TDD test be observed failing?
8. Which testing concepts transfer from pytest to JUnit?

## Apply your learning

1. Create a `pytest` file for one earlier exercise.
2. Write normal, boundary and invalid-input tests.
3. Parametrise at least four related examples.
4. Test one expected exception and one floating-point result.
5. Use `tmp_path` to test a file operation without touching a real learner file.
6. Follow one complete Red-Green-Refactor cycle and retain the commit history.
7. Produce a traceability table linking requirements to automated and manual evidence.
8. Run the full suite and interpret every reported outcome.

## Page summary

Automated tests turn examples and expectations into repeatable checks. Arrange-Act-Assert gives each test a clear shape, while pytest supports expressive assertions, expected exceptions, parametrisation and fixtures. TDD uses a failing test to guide a small implementation, followed by structural improvement. Framework syntax varies, but isolation, meaningful oracles, regression evidence and traceability transfer across languages.

**Previous:** Return to **16.4 Designing an Effective Test Strategy**.

**End of Lecture 16 and COM4008.** Reliable programming is a continuous practice: understand the requirement, reduce avoidable complexity, manage failure deliberately, test according to risk and use evidence to guide the next improvement.

