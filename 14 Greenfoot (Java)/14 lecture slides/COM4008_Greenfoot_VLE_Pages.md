# COM4008 Programming Concepts: Greenfoot and the Mario Pyramid

This content is designed as four linked VLE information pages. Lecture 14 applies the Java concepts from Lecture 13 in Greenfoot, using a Mario-inspired pyramid to connect requirements, two-dimensional coordinates, objects, iteration, movement and collision.

---

# 14.1 From Game Requirements to a Grid Model

## On this page

- Analysing a familiar game as a software system
- Separating requirements from implementation ideas
- Using sketches and paper prototypes
- Modelling a scene as a two-dimensional grid
- Reducing the scope to a testable Mario pyramid
- Connecting the problem to earlier Python work

## Learning outcomes

By the end of this page, you should be able to:

- identify functional requirements in a platform game;
- distinguish a requirement from a proposed implementation;
- use a paper design to expose objects, rules and relationships;
- represent positions using two-dimensional coordinates;
- explain how a repeated arrangement of blocks can be generated algorithmically;
- define a manageable first increment for a larger game.

## From playing a game to analysing one

Super Mario Bros. may feel simple when it is played: move, jump, avoid enemies and reach the end. From a programmer's perspective, however, even a short platform level combines many interacting systems.

Possible requirements include:

- a player-controlled character;
- horizontal movement and jumping;
- platforms and ground tiles;
- gravity and collision with solid surfaces;
- enemies with their own behaviours;
- coins, power-ups or other collectable objects;
- a scrolling camera;
- a time limit, score, lives and a win condition.

This list is useful, but it is too large for one first implementation. Good software development begins by deciding what the next small, demonstrable result should be.

## Requirements and implementation are different

A **requirement** describes an outcome or behaviour:

> The player must not be able to pass through a solid block.

An **implementation idea** describes a possible way of achieving it:

> Before changing the player's position, check whether a `Block` object occupies the next grid cell.

Keeping these separate matters. A requirement should remain meaningful even if the implementation changes later.

| Requirement | Possible implementation idea |
|---|---|
| Display a level made from tiles | Store or generate tile positions on a two-dimensional grid |
| Let the player move | Read keyboard state during each action step |
| Prevent movement through blocks | Detect a block before moving, or move and undo an invalid move |
| Build a pyramid of blocks | Use nested loops and a coordinate rule |
| Recreate the level after Reset | Construct its objects in the world's setup code |

## Start with paper

A sketch is not decoration. It is an inexpensive model that helps answer questions before code becomes complicated:

- What objects appear in the scene?
- Which objects can move?
- Which objects are solid?
- Where is the origin of the coordinate system?
- How many rows and columns are required?
- Which behaviours belong to the world, and which belong to an actor?
- What is the smallest version worth building first?

Annotate the sketch with coordinates, dimensions and rules. A box labelled “Mario” is an object candidate. An arrow labelled “moves left/right” is a behaviour candidate. Repeated rectangles suggest a `Block` class and an algorithm for placing its objects.

## A two-dimensional grid

Greenfoot worlds are two-dimensional grids of cells. A position is represented by an ordered pair:

```text
(x, y)
```

The `x` coordinate identifies a column and increases from left to right. The `y` coordinate identifies a row and increases from top to bottom.

```text
             x →
        0   1   2   3   4
      ┌───┬───┬───┬───┬───┐
 y  0 │   │   │   │   │   │
 ↓    ├───┼───┼───┼───┼───┤
    1 │   │   │ M │   │   │   Mario is at (2, 1)
      ├───┼───┼───┼───┼───┤
    2 │ B │ B │ B │ B │ B │   blocks form the ground
      └───┴───┴───┴───┴───┘
```

The top-left cell is `(0, 0)`. In a world containing 24 columns, valid `x` coordinates run from `0` to `23`. This is the same zero-based indexing encountered in Python lists and Java arrays.

## From pixels to logical cells

A cell can be larger than one screen pixel. For example:

```java
super(24, 20, 30);
```

creates a world that is:

- 24 cells wide;
- 20 cells high;
- displayed using 30 pixels per cell.

The resulting display is 720 by 600 pixels, but actors are still placed using cell coordinates such as `(3, 17)`. A tile-sized cell makes the early pyramid logic easier to understand. More fluid platform movement may later use one-pixel cells or a more detailed physics model.

## Scope the first increment

Instead of building an entire platform game, this lecture focuses on a vertical slice:

1. create a Greenfoot world;
2. represent ground and pyramid tiles as `Block` actors;
3. generate a Mario-style pyramid using loops;
4. add a `Mario` actor;
5. move the actor and prevent it entering a block.

This increment is small, but it connects several important programming ideas:

- decomposition;
- classes and objects;
- inheritance;
- constants and variables;
- two-dimensional coordinates;
- nested iteration;
- selection;
- methods and parameters;
- state that changes over time.

## Transfer from the earlier Mario exercise

In the earlier console exercise, a pyramid was represented by characters printed in rows. The program controlled **what character appeared at each textual position**.

In Greenfoot, the underlying algorithmic idea remains the same, but each visible tile is an object placed at an `(x, y)` coordinate. We are transferring a familiar pattern into a graphical, object-oriented environment.

| Console pyramid | Greenfoot pyramid |
|---|---|
| a line of text | a row in the world |
| a character such as `#` | a `Block` object |
| spaces before the hashes | unused cells before the blocks |
| printing a character | calling `addObject(...)` |
| nested string-building loops | nested object-placement loops |

## Pause and model the scene

Draw a 12-column by 8-row grid. Add:

- a ground row;
- a half-pyramid with height four;
- a player to the left of the pyramid.

Label the coordinates of the player, the top block and both ends of the ground. Then describe one rule that changes an object's position and one rule that prevents a change.

## Common mistakes

- **Trying to build the full game immediately:** first establish one small, working increment.
- **Writing code before defining coordinates:** the grid model should be clear before the loops are written.
- **Treating a feature idea as a requirement:** state the learner-visible outcome first.
- **Assuming `y` increases upwards:** in Greenfoot, row numbers increase downwards.
- **Forgetting zero-based coordinates:** the last column is `width - 1`, not `width`.
- **Confusing pixels with cells:** world dimensions are given in cells; cell size is given in pixels.
- **Placing every block manually:** repeated geometry is evidence that a loop or method is needed.
- **Using copyrighted game assets indiscriminately:** use module-provided or appropriately licensed assets for submitted work.

## Check your understanding

1. Give one game requirement and one possible implementation for it.
2. Why is a paper design useful before coding?
3. In which directions do Greenfoot's `x` and `y` coordinates increase?
4. What are the largest valid coordinates in a 24 by 20 world?
5. What does the third argument of `super(24, 20, 30)` represent?
6. How does the Greenfoot pyramid reuse the idea from the console pyramid?

## Apply your learning

1. Produce an annotated paper design for the first playable scene.
2. Write five requirements without prescribing their implementation.
3. Mark the `(x, y)` coordinates of every block in a height-three half-pyramid.
4. Identify which requirements belong in this lecture and which should be placed in a later backlog.
5. Express the number of blocks in a height `h` pyramid as a sequence for `h = 1` to `5`.
6. Explain why a repeated tile layout is a suitable problem for nested loops.

## Page summary

A familiar game contains many interacting requirements, so the first task is to select a manageable increment. Paper designs expose objects, behaviours and coordinates before implementation. Greenfoot represents a scene as a two-dimensional grid, allowing the earlier console-pyramid algorithm to become a repeated arrangement of `Block` objects.

**Next:** Continue to **14.2 Greenfoot Worlds, Actors and the Scenario Lifecycle**.

---

# 14.2 Greenfoot Worlds, Actors and the Scenario Lifecycle

## On this page

- Greenfoot as a Java learning environment
- The relationship between `World`, `Actor`, classes and objects
- Creating a scenario and compiling it
- Configuring a world with a constructor
- Creating and adding actors
- The Act, Run, Pause and Reset controls
- Organising initial setup in a `prepare()` method

## Learning outcomes

By the end of this page, you should be able to:

- explain the purpose of Greenfoot;
- distinguish a world class, actor class and object instance;
- extend the supplied `World` and `Actor` classes;
- configure a cell-based world in its constructor;
- add an actor at a specified coordinate;
- explain when `act()` is called;
- create a repeatable initial world state.

## Java with immediate visual feedback

Greenfoot is an educational Java environment for building two-dimensional games and simulations. It supplies a visual world, an editor, compilation support and controls for stepping or running a scenario.

It does not replace Java. The scenario is still organised using Java classes, objects, fields, constructors and methods. Greenfoot supplies a framework in which those concepts produce visible results quickly.

## The two central framework classes

Every scenario begins with two important Greenfoot classes:

```text
World                         Actor
  ▲                             ▲
  │ extends                     │ extends
MarioWorld                    Mario
                              Block
```

- A `World` is the two-dimensional space in which actors exist.
- An `Actor` is an object that can appear in a world and have behaviour.
- `MarioWorld` is our specific kind of `World`.
- `Mario` and `Block` are specific kinds of `Actor`.

This is inheritance in a practical setting. `MarioWorld` receives useful world operations such as `addObject(...)`, while an actor receives operations such as `getX()`, `setLocation(...)` and `isTouching(...)`.

## Classes and objects

The class describes a type; an object is one instance created from it.

```java
Block block = new Block();
```

This statement:

1. declares a variable named `block` whose type is `Block`;
2. creates a new `Block` object by calling its constructor;
3. stores a reference to that object in the variable.

One class can produce many objects:

```java
Block firstBlock = new Block();
Block secondBlock = new Block();
```

The pyramid therefore needs one `Block` class but many `Block` objects.

## Configure the world

A clear first version of the world class is:

```java
import greenfoot.*;

public class MarioWorld extends World
{
    public static final int COLUMNS = 24;
    public static final int ROWS = 20;
    public static final int TILE_SIZE = 30;
    public static final int GROUND_ROW = 17;

    public MarioWorld()
    {
        super(COLUMNS, ROWS, TILE_SIZE);
        prepare();
    }

    private void prepare()
    {
        // The initial objects will be added here.
    }
}
```

The `super(...)` call invokes the `World` constructor. It must occur before the other statements in this constructor.

Named constants make the dimensions meaningful and prevent “magic numbers” from being scattered through later methods. Because the values belong to the world design and do not change, `public static final` is appropriate here.

## Create an actor subclass

A minimal solid tile can begin as:

```java
import greenfoot.*;

public class Block extends Actor
{
    public Block()
    {
        GreenfootImage image = getImage();
        image.scale(MarioWorld.TILE_SIZE, MarioWorld.TILE_SIZE);
        setImage(image);
    }
}
```

Choose an appropriate image when creating the subclass, or set one in code. Scaling it to the tile dimensions aligns the visual object with the logical grid used in this lecture.

## Add objects to the world

An actor is not visible merely because it has been constructed. It must be inserted into a world:

```java
Block block = new Block();
addObject(block, 5, GROUND_ROW);
```

This can be shortened when no separate variable is needed:

```java
addObject(new Block(), 5, GROUND_ROW);
```

`addObject` receives:

1. the actor object;
2. its `x` coordinate;
3. its `y` coordinate.

## A repeatable initial state

Objects can be placed interactively while exploring Greenfoot, but a learner should be able to press Reset and reproduce the same scene. Put the setup in code:

```java
private void prepare()
{
    drawGround();
    buildHalfPyramid(5, 15);

    Mario mario = new Mario();
    addObject(mario, 2, GROUND_ROW - 1);
}
```

The constructor describes the world's creation. A separate `prepare()` method keeps it readable and provides one obvious location for assembling the initial scene.

Some Greenfoot versions can generate setup code from interactively placed objects. Even when using that facility, read and refactor the generated code rather than treating it as mysterious boilerplate.

## Act, Run, Pause and Reset

- **Act** performs one action step. Greenfoot gives the world and each actor an opportunity to run its `act()` method.
- **Run** repeats action steps until the scenario is paused or stopped.
- **Pause** stops repeated action steps without reconstructing the world.
- **Reset** discards the current world and creates its initial state again.

An actor can define behaviour by overriding `act()`:

```java
public class Mario extends Actor
{
    public void act()
    {
        // This behaviour is considered once per action step.
    }
}
```

The number of calls per second is not a fixed property of `act()`. It varies with Greenfoot's speed setting and the work performed by the scenario. Describe behaviour in action steps rather than assuming a particular frame rate.

## Compile frequently

Compilation translates the Java source and reports syntax or type errors. Compile after small changes so that any new error is close to the code that caused it.

A useful cycle is:

```text
make one small change → compile → Act once → inspect → Run → Reset
```

Using Act before Run is particularly helpful when debugging movement. One action step produces one observable change.

## Pause and trace object creation

Trace this expression:

```java
addObject(new Block(), 7, 16);
```

Identify:

- the class;
- the constructor call;
- the new object;
- the inherited world method;
- the `x` and `y` arguments;
- what should be visible after the statement completes.

## Common mistakes

- **Creating an actor but not adding it:** `new Block()` constructs an object; `addObject(...)` places it in the world.
- **Extending the wrong class:** a visible game object should normally extend `Actor`; the scene should extend `World`.
- **Reversing coordinates:** `addObject(actor, x, y)` uses the horizontal coordinate first.
- **Placing setup only by hand:** manually positioned actors disappear when the world is reconstructed unless setup is saved in code.
- **Omitting `super(...)`:** the world must be configured through its superclass constructor.
- **Putting code before `super(...)`:** a constructor's explicit superclass call must be its first statement.
- **Assuming `act()` has a fixed frame rate:** it is called once per action step, whose speed can vary.
- **Pressing Run before checking one step:** Act is often the clearer debugging tool.
- **Changing several classes before compiling:** small compile-and-test cycles make errors easier to locate.

## Check your understanding

1. What is the difference between `World` and `Actor`?
2. Which statements describe classes, and which describe objects?
3. What does `super(COLUMNS, ROWS, TILE_SIZE)` configure?
4. Why is `GROUND_ROW` declared as a constant?
5. Why does constructing a `Block` not automatically display it?
6. What is the difference between Act, Run and Reset?
7. Why should we avoid claiming that `act()` always runs a fixed number of times per second?

## Apply your learning

1. Create a new Greenfoot scenario and a `MarioWorld` subclass.
2. Configure a 24 by 20 world with 30-pixel cells.
3. Create `Mario` and `Block` subclasses of `Actor`.
4. Add one object interactively, then reproduce it through `prepare()`.
5. Add three blocks at different coordinates and predict their positions before compiling.
6. Override `act()` in `Mario` so that it prints or displays a short diagnostic message for one action step.
7. Use Reset to confirm that the scene always returns to the same initial state.

## Page summary

Greenfoot provides a visual Java framework centred on `World` and `Actor`. A scenario defines specialised subclasses and constructs object instances from them. The world's constructor configures its grid and can call a setup method that creates a repeatable initial state. Act performs one action step; Run repeats those steps at a speed controlled by the environment.

**Previous:** Return to **14.1 From Game Requirements to a Grid Model**.

**Next:** Continue to **14.3 Building the Mario Pyramid**.

---

# 14.3 Building the Mario Pyramid

## On this page

- Drawing the ground with iteration
- Translating a pyramid pattern into coordinates
- Using nested loops to create actors
- Moving repeated logic into methods
- Parameterising the pyramid's height and position
- Validating dimensions
- Extending from one half to two halves

## Learning outcomes

By the end of this page, you should be able to:

- use a loop to create a row of actor objects;
- explain why a pyramid requires nested iteration;
- calculate block coordinates from loop variables;
- implement a parameterised half-pyramid method;
- validate a requested height against world boundaries;
- refactor repeated object-placement code;
- adapt the algorithm to construct a mirrored half.

## Draw a ground row

The ground contains one block in every column. The world's inherited `getWidth()` method gives the number of cells across the world:

```java
private void drawGround()
{
    for (int x = 0; x < getWidth(); x++)
    {
        addObject(new Block(), x, GROUND_ROW);
    }
}
```

On every iteration:

1. `x` identifies the next column;
2. a new `Block` object is constructed;
3. that object is added at `(x, GROUND_ROW)`.

The condition uses `< getWidth()`, not `<= getWidth()`, because valid coordinates end at `getWidth() - 1`.

## Describe the half-pyramid first

For a right-aligned half-pyramid of height five:

```text
row 0 from the bottom: 5 blocks
row 1 from the bottom: 4 blocks
row 2 from the bottom: 3 blocks
row 3 from the bottom: 2 blocks
row 4 from the bottom: 1 block
```

If `level` begins at zero on the bottom row:

```text
number of blocks = height - level
y coordinate      = GROUND_ROW - 1 - level
```

If every row ends at `rightEdgeX`, successive blocks extend leftwards:

```text
x coordinate = rightEdgeX - offset
```

These three rules are the algorithm. The Java loops are their expression.

## Implement the nested loops

```java
private void buildHalfPyramid(int height, int rightEdgeX)
{
    for (int level = 0; level < height; level++)
    {
        int y = GROUND_ROW - 1 - level;
        int blocksInRow = height - level;

        for (int offset = 0; offset < blocksInRow; offset++)
        {
            int x = rightEdgeX - offset;
            addObject(new Block(), x, y);
        }
    }
}
```

The outer loop selects a level. The inner loop creates all blocks on that level. A height-five pyramid produces 5 + 4 + 3 + 2 + 1 = 15 block objects.

Call the method from `prepare()`:

```java
buildHalfPyramid(5, 15);
```

Changing `5` changes the height; changing `15` moves the right edge. The method now describes a reusable operation rather than one fixed picture.

## Dry-run the algorithm

For `buildHalfPyramid(3, 6)`:

| `level` | `y` | `blocksInRow` | generated `x` values |
|---:|---:|---:|---|
| 0 | `GROUND_ROW - 1` | 3 | 6, 5, 4 |
| 1 | `GROUND_ROW - 2` | 2 | 6, 5 |
| 2 | `GROUND_ROW - 3` | 1 | 6 |

Dry-running a small example is often faster than guessing why a larger graphical result looks wrong.

## Validate the request

A requested pyramid can fail if it extends above the world or left of column zero. For this right-aligned design:

```java
private void validatePyramid(int height, int rightEdgeX)
{
    if (height < 1)
    {
        throw new IllegalArgumentException("Height must be at least 1");
    }

    if (height > GROUND_ROW)
    {
        throw new IllegalArgumentException("Pyramid is too tall");
    }

    if (rightEdgeX < height - 1 || rightEdgeX >= getWidth())
    {
        throw new IllegalArgumentException("Pyramid does not fit horizontally");
    }
}
```

Call this method at the start of `buildHalfPyramid`. This is an example of **defensive programming**: invalid arguments are rejected close to their source.

For an introductory activity, a fixed valid height is preferable to interrupting the scenario with a dialog. Once the construction works, input can be added using `Greenfoot.ask(...)` and converted with `Integer.parseInt(...)`, with appropriate exception handling.

## Refactor around intentions

Method names should explain the design:

```java
private void prepare()
{
    drawGround();
    buildHalfPyramid(5, 15);
    addPlayer();
}
```

The reader can understand the broad setup without reading every loop. Each helper method can then be tested and debugged separately.

Avoid creating one enormous method containing world setup, input, pyramid geometry and movement. Those responsibilities change for different reasons.

## Build the other half

A mirrored half can extend to the right of a left-edge coordinate:

```java
private void buildMirroredHalfPyramid(int height, int leftEdgeX)
{
    for (int level = 0; level < height; level++)
    {
        int y = GROUND_ROW - 1 - level;
        int blocksInRow = height - level;

        for (int offset = 0; offset < blocksInRow; offset++)
        {
            int x = leftEdgeX + offset;
            addObject(new Block(), x, y);
        }
    }
}
```

The two algorithms differ only in the direction used to calculate `x`. A later refinement could pass a direction value of `-1` or `1` into one general method, but clarity is more important than eliminating every repeated line immediately.

## Pause and predict the blocks

Without running the scenario, list every coordinate created by:

```java
buildHalfPyramid(4, 8);
```

Then answer:

- How many blocks should appear?
- What is the top coordinate?
- What is the leftmost coordinate on the bottom row?
- Which expression would need to change to mirror it?

## Common mistakes

- **Using `<= getWidth()`:** this attempts to place an actor one cell beyond the last valid column.
- **Reusing one block object:** each location requires a distinct `new Block()` object.
- **Changing `y` in the inner loop:** all blocks on one level should share the same row.
- **Growing the pyramid in the wrong direction:** subtract from `y` to move upwards.
- **An off-by-one ground collision:** the lowest pyramid row should normally be `GROUND_ROW - 1` if the ground occupies `GROUND_ROW`.
- **Hard-coding every coordinate:** derive positions from `height`, `level`, `offset` and an anchor point.
- **Accepting impossible dimensions:** validate the height and horizontal position.
- **Refactoring too early into a clever general method:** establish a correct, readable half first.
- **Changing formulas without a dry run:** trace a height-two or height-three example on paper.

## Check your understanding

1. Why does the ground require only one loop?
2. What responsibility belongs to each loop in the pyramid method?
3. For height five and `level == 2`, what is `blocksInRow`?
4. Why is the first pyramid row placed at `GROUND_ROW - 1`?
5. How does `rightEdgeX` make the method reusable?
6. Which invalid inputs should be rejected?
7. What is the simplest change that mirrors horizontal placement?

## Apply your learning

1. Implement `drawGround()` and verify its first and last coordinates.
2. Build fixed pyramids of heights one, two and five.
3. Add a `validatePyramid(...)` method and deliberately test invalid values.
4. Move the same pyramid to three different horizontal positions.
5. Implement the mirrored half and leave a two-cell gap between the halves.
6. Refactor the two halves into one method with a `direction` argument after both versions work.
7. Add a different `Rock` or `Coin` actor and generate a repeated pattern with it.

## Page summary

The pyramid is a coordinate-generation problem. An outer loop selects each level, while an inner loop creates the required objects across that row. Parameters separate the reusable rule from one fixed height and position. Validation protects the world boundaries, and small helper methods keep setup readable.

**Previous:** Return to **14.2 Greenfoot Worlds, Actors and the Scenario Lifecycle**.

**Next:** Continue to **14.4 Movement, Collision and Managing the Scenario**.

---

# 14.4 Movement, Collision and Managing the Scenario

## On this page

- Giving the `Mario` actor behaviour
- Reading keyboard state in `act()`
- Keeping movement inside the world
- Detecting blocks before movement
- Distinguishing grid collision from richer platform physics
- Testing visual and logical behaviour
- Managing the Greenfoot scenario with Git
- Extending the prototype responsibly

## Learning outcomes

By the end of this page, you should be able to:

- implement keyboard-controlled actor movement;
- calculate and validate a proposed next position;
- prevent an actor moving into a solid block;
- use Act and temporary diagnostics to investigate behaviour;
- distinguish this grid prototype from a complete platform physics system;
- identify the scenario files that should be version controlled;
- define suitable extensions and acceptance checks.

## Behaviour belongs to the actor

The world creates and arranges the scene. The `Mario` actor is responsible for interpreting player controls and changing its own position.

A first movement method can be written clearly as:

```java
import greenfoot.*;

public class Mario extends Actor
{
    public void act()
    {
        handleMovement();
    }

    private void handleMovement()
    {
        if (Greenfoot.isKeyDown("left"))
        {
            tryMove(-1, 0);
        }
        else if (Greenfoot.isKeyDown("right"))
        {
            tryMove(1, 0);
        }
    }
}
```

`Greenfoot.isKeyDown(...)` reports whether a named key is currently held. The two calls to `tryMove` express direction as a change in coordinates:

- left is `(-1, 0)`;
- right is `(1, 0)`.

Using `else if` prevents both horizontal moves during the same action step. Other control policies are possible, but the intended behaviour should be deliberate.

## Check before changing state

For a tile-based prototype, inspect the destination cell before moving:

```java
private void tryMove(int dx, int dy)
{
    int nextX = getX() + dx;
    int nextY = getY() + dy;

    if (!isInsideWorld(nextX, nextY))
    {
        return;
    }

    Actor obstacle = getOneObjectAtOffset(dx, dy, Block.class);

    if (obstacle == null)
    {
        setLocation(nextX, nextY);
    }
}

private boolean isInsideWorld(int x, int y)
{
    return x >= 0
        && x < getWorld().getWidth()
        && y >= 0
        && y < getWorld().getHeight();
}
```

This follows a useful pattern:

1. calculate the proposed state;
2. check the rules;
3. commit the state change only if it is valid.

An alternative is to move, use `isTouching(Block.class)`, and return to the previous position if a collision occurs. Checking the destination first is particularly easy to reason about when every object occupies one logical cell.

## Why unconditional movement fails

This method makes the actor move during every action step:

```java
public void act()
{
    move(1);
}
```

It is a useful first experiment, but it does not satisfy the game requirements because:

- the player has no control;
- speed depends on the scenario's action rate;
- world boundaries are not an intentional rule;
- solid blocks are ignored;
- the actor may move in its current rotation rather than specifically left or right.

A visible result is not automatically a correct implementation. Always compare behaviour with the requirement.

## Grid collision is not complete platform physics

The destination-cell approach suits this lecture's tile model. A polished platform game may instead need:

- sub-cell or pixel positions;
- horizontal and vertical velocity;
- acceleration caused by gravity;
- jump impulses;
- collision resolution on separate axes;
- detection of whether the player is standing on a surface;
- prevention of tunnelling through objects at high speed;
- animation state and a scrolling camera.

These are excellent later extensions, but should not obscure the present learning goal: using Java objects and logic to make a small scenario obey explicit rules.

## Test one action step at a time

Visual programs still need systematic testing. Use Greenfoot's **Act** control to observe one state transition at a time.

Suggested movement checks:

| Starting situation | Action | Expected result |
|---|---|---|
| empty cell to the right | press right for one step | Mario moves right one cell |
| block immediately to the right | press right for one step | Mario remains in place |
| Mario at the left boundary | press left for one step | Mario remains inside the world |
| no movement key held | perform one step | Mario remains in place |
| scenario has been changed | press Reset | initial world is reconstructed |

Record the starting state, action, expected result and actual result. “It looked okay while running” is weaker evidence than a reproducible check.

Temporary diagnostics can help:

```java
System.out.println("Mario: " + getX() + ", " + getY());
```

Remove or disable noisy diagnostics when the behaviour is understood.

## Separate logic where practical

Greenfoot makes visual behaviour convenient, but coordinate rules can still be separated into small methods. For example, `isInsideWorld(...)` is a deterministic Boolean rule. Keeping rules small makes them easier to reason about and, in a larger design, easier to unit test outside the visual loop.

Possible tests for the pyramid itself include:

- a height-one pyramid creates one block;
- a height-three pyramid creates six blocks;
- every generated coordinate is inside the world;
- the top row contains one block;
- invalid heights are rejected;
- mirrored halves generate coordinates in opposite horizontal directions.

## Manage the project with Git

A Greenfoot scenario is a project folder. Place that folder under version control so that code and required assets evolve together.

Commit:

- Java source files;
- the Greenfoot project/scenario metadata required to open the project;
- images and sounds that the scenario requires;
- useful documentation such as a README.

Ignore generated compiler output such as `.class` files and operating-system or editor caches. Check the actual file changes before every commit rather than assuming that an entire folder is appropriate.

A simple workflow is:

1. create or add the scenario folder as a local repository;
2. make one coherent improvement;
3. compile and test it;
4. review the changed files;
5. commit with a descriptive message;
6. push to the configured remote repository.

Useful commit messages describe completed behaviour:

```text
Create tile-based Mario world
Generate parameterised half-pyramid
Prevent Mario entering block cells
Add boundary movement checks
```

The default branch is commonly named `main`, but it is not the only branch a Git repository can contain. Branches can later support isolated experiments or features.

Never place passwords, access tokens or private keys in the scenario folder or commit history.

## A staged extension route

Build extensions in dependency order:

1. fixed ground;
2. fixed half-pyramid;
3. parameterised pyramid;
4. mirrored half;
5. keyboard movement;
6. world-boundary checks;
7. collision with blocks;
8. gravity and jumping;
9. coins, enemies or a goal;
10. scrolling and richer levels.

Each stage should leave the scenario in a compilable, demonstrable state. That gives you useful Git checkpoints and prevents several unfinished systems becoming entangled.

## Pause and trace a blocked move

Mario is at `(5, 16)`, and a block is at `(6, 16)`. Trace `tryMove(1, 0)` line by line:

- What values are assigned to `nextX` and `nextY`?
- Does the boundary check pass?
- What should `getOneObjectAtOffset(...)` return?
- Is `setLocation(...)` called?
- What visible result should the learner observe?

Now repeat the trace with no block at `(6, 16)`.

## Common mistakes

- **Moving on every action step without checking input:** the actor should respond to an explicit control rule.
- **Checking collision after losing the old coordinates:** store or calculate the previous state if using move-and-revert.
- **Ignoring world boundaries:** validate the proposed coordinates as well as nearby actors.
- **Using `isTouching` as a complete physics engine:** it detects contact; the program still needs a response rule.
- **Assuming one cell per step gives smooth platform movement:** this lecture uses a deliberately simple tile model.
- **Testing only with Run:** use Act for precise, reproducible state changes.
- **Mixing world construction into `Mario.act()`:** setup belongs to the world; player behaviour belongs to the actor.
- **Committing generated `.class` files:** version the source and required project assets instead.
- **Writing vague commit messages:** describe the behaviour added or corrected.
- **Attempting gravity, enemies and scrolling together:** add one testable capability at a time.

## Check your understanding

1. When should `Greenfoot.isKeyDown(...)` be checked?
2. What do `dx` values of `-1` and `1` represent?
3. Why calculate a proposed position before calling `setLocation(...)`?
4. What does `getOneObjectAtOffset(dx, dy, Block.class)` return when the destination is clear?
5. How would move-and-revert collision differ from checking first?
6. Why is this not yet a complete platform physics system?
7. Which Greenfoot project files should be committed, and which generated files should generally be ignored?

## Apply your learning

1. Add left and right keyboard movement to `Mario`.
2. Prevent the actor leaving either horizontal edge of the world.
3. Place blocks immediately on each side of Mario and verify both blocked moves using Act.
4. Create a short test table containing at least six starting situations and expected results.
5. Add a second solid actor type and decide whether the same movement rule should block it.
6. Commit the working stages separately with descriptive messages.
7. As an extension, design—but do not initially code—the fields and rules needed for gravity and jumping.

## Page summary

An actor receives repeated opportunities to behave through `act()`. Keyboard state can be translated into a proposed coordinate change, checked against world boundaries and nearby blocks, and applied only when valid. Greenfoot's visual controls support careful step-by-step testing, while Git preserves coherent working increments. The result is a small but genuine object-oriented game prototype and a foundation for later movement, physics and level features.

**Previous:** Return to **14.3 Building the Mario Pyramid**.

**End of Lecture 14.** Revisit your requirements and identify the smallest reliable extension you could implement next.

