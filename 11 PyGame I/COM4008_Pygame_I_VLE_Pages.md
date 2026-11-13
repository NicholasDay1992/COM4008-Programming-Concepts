# COM4008 Programming Concepts: Pygame I — From Requirements to Movement

This content is designed as four linked VLE information pages. Lecture 11 uses a Space Invaders-style game to connect requirements, coordinate modelling, event-driven programming and a first Pygame movement prototype.

---

# 11.1 Scoping the Game: Requirements and a First Prototype

## On this page

- Games as software systems
- Observing behaviour before writing code
- Functional and non-functional requirements
- Choosing a minimum viable prototype
- Turning broad ideas into acceptance criteria
- Separating the game model from its presentation

## Learning outcomes

By the end of this page, you should be able to:

- identify observable behaviours in a familiar game;
- distinguish a feature idea from a testable requirement;
- reduce a large game concept to a manageable first prototype;
- write acceptance criteria for player and invader movement;
- distinguish game state, rules, input and presentation.

## Why begin with requirements?

A game may look like a collection of images and animations, but its behaviour is controlled by rules. Before choosing Pygame functions, we need to decide what the program must do.

Space Invaders provides a useful case study because its rules are recognisable:

- the player moves horizontally near the bottom of the screen;
- a formation of invaders moves as a coordinated group;
- the formation reverses direction and descends at an edge;
- the player and invaders fire projectiles;
- collisions remove or damage game objects;
- barriers deteriorate when hit;
- score, lives, levels and speed change over time.

These are not all equally suitable for a first implementation. Trying to build the complete game at once creates too many interacting problems.

## Functional and non-functional requirements

A **functional requirement** describes behaviour the system must provide:

> The player shall move left while the left-arrow key is held.

A **non-functional requirement** describes a quality or constraint:

> Player movement should remain visually smooth on supported computers.

For this prototype, our functional requirements are more important, but frame rate, responsiveness and maintainability will influence the implementation.

## From observation to specification

“Make the player move” is an idea, not yet a precise requirement. Useful questions include:

- Which keys control it?
- Does one press cause one step, or does holding the key cause continuous movement?
- Can the player leave the visible screen?
- Does vertical position change?
- How fast should it move?
- What happens if left and right are held together?

The answers become acceptance criteria.

### Requirement 1: move the player

For the first prototype:

1. The player begins horizontally centred near the bottom of the window.
2. Holding the left-arrow key moves the player left.
3. Holding the right-arrow key moves the player right.
4. Releasing the key stops horizontal movement.
5. The player cannot move beyond either side of the window.
6. The player's vertical position remains fixed.

### Requirement 2: move the invader formation

For the first prototype:

1. Invaders appear in aligned rows and columns.
2. Every live invader moves horizontally in the same direction.
3. The formation reverses direction when its outer edge would cross the window boundary.
4. When direction changes, the formation moves down by one defined amount.
5. Relative spacing between invaders remains constant.

These statements describe results. They do not yet prescribe classes, arrays or particular Pygame functions.

## Choosing the minimum viable prototype

Our Lecture 11 prototype contains:

- one window;
- one movable player shape or image;
- a formation of invaders;
- player boundary detection;
- fleet edge detection and reversal;
- a reliable way to close the application.

It deliberately omits:

- projectiles;
- collisions;
- barriers;
- score and lives;
- sound;
- start, win and game-over screens;
- increasing difficulty.

Those omissions are good scope control, not failure. A working movement system becomes the foundation for Lecture 12.

## Four parts of the design

It helps to separate four concerns:

| Concern | Question | Example |
|---|---|---|
| State | What must the game remember? | Player position, fleet direction |
| Rules | How may the state change? | The player cannot cross an edge |
| Input | What has the user or system done? | Right arrow is currently held |
| Presentation | How is the state shown? | Draw the player image at its position |

This distinction prevents drawing code from becoming the only representation of the game. Coordinates and direction exist as data even before an image is displayed.

## A simple state sketch

```text
Game
├── running
├── screen width and height
├── player
│   ├── position
│   ├── size
│   └── speed
└── invader formation
    ├── positions
    ├── direction
    ├── speed
    └── downward step
```

The sketch is not a finished class diagram. It is a list of information the program will need.

## Pause and refine

Consider this requirement:

> The invaders move across the screen.

Rewrite it as at least four observable acceptance criteria. Include what happens at an edge and what must remain unchanged while the formation moves.

Then consider which values the program must store to satisfy your criteria.

## Common mistakes

- **Starting with assets rather than behaviour:** an attractive sprite does not define how the game works.
- **Treating every original feature as essential:** a small complete prototype is more useful than many unfinished systems.
- **Writing ambiguous requirements:** words such as “fast”, “smooth” and “correctly” need measurable interpretation.
- **Describing implementation instead of outcome:** requirements should not unnecessarily demand a particular loop or class.
- **Forgetting edge cases:** movement needs explicit behaviour at both boundaries.
- **Mixing Lecture 11 and Lecture 12 scope:** shooting and collisions depend on a stable movement model.

## Check your understanding

1. What is the difference between a feature idea and an acceptance criterion?
2. Give one functional and one non-functional game requirement.
3. Why are projectiles excluded from the first prototype?
4. What is the difference between game state and presentation?
5. Which values must be stored for the invader formation?

## Apply your learning

1. Observe a short sequence from a fixed-screen arcade game and list its visible rules.
2. Classify each rule as essential to the first prototype, suitable for Lecture 12, or optional polish.
3. Write acceptance criteria for player movement.
4. Write acceptance criteria for the invader formation.
5. Create a state sketch listing the data required by both systems.
6. Identify two requirements that could later be checked with unit tests without opening a game window.

## Page summary

Requirements give development a target. Lecture 11 focuses on a minimum viable movement prototype: a horizontally controlled player and a coordinated invader formation that reacts to screen edges. Separating state, rules, input and presentation makes the design easier to reason about and prepares the movement rules for implementation and testing.

**Next:** Continue to **11.2 Modelling Movement and Boundaries**.

---

# 11.2 Modelling Movement and Boundaries

## On this page

- The Pygame coordinate system
- Modelling horizontal player movement
- Boundary detection and clamping
- Generating rows and columns of invaders
- Treating multiple invaders as one formation
- Pure movement functions

## Learning outcomes

By the end of this page, you should be able to:

- explain the screen coordinate system used by Pygame;
- update a position using direction, speed and elapsed time;
- constrain a rectangular object to the screen;
- generate an evenly spaced formation using nested loops;
- detect fleet boundaries using the outermost invaders;
- implement movement rules separately from drawing.

## Screen coordinates

In a Pygame window, the origin is at the top-left:

```text
(0, 0) ───────────────→ increasing x
  │
  │
  ↓
increasing y
```

Therefore:

- moving right increases `x`;
- moving left decreases `x`;
- moving down increases `y`;
- moving up decreases `y`.

The player in this prototype changes `x` but keeps a fixed `y`.

## Position, direction and speed

We can describe horizontal movement as:

```text
new position = old position + direction × speed × elapsed time
```

Use `-1` for left, `0` for stationary and `1` for right:

```python
direction = -1
speed = 300
elapsed_seconds = 0.016

x = x + direction * speed * elapsed_seconds
```

Expressing speed in pixels per second and including elapsed time makes movement much less dependent on frame rate.

## Keeping the player on screen

If `x` represents the left edge of the player, its legal range is:

```text
0 ≤ x ≤ screen width − player width
```

A reusable calculation is:

```python
def move_player(x, direction, speed, elapsed, player_width, screen_width):
    new_x = x + direction * speed * elapsed
    maximum_x = screen_width - player_width

    return max(0, min(new_x, maximum_x))
```

`min()` prevents the value exceeding the right boundary. `max()` prevents it becoming negative. This is called **clamping**.

The function contains no Pygame drawing code. It can be reasoned about and tested independently:

```python
assert move_player(5, -1, 300, 1, 35, 500) == 0
assert move_player(490, 1, 300, 1, 35, 500) == 465
```

## Representing a board before drawing it

A small character grid can make coordinates visible:

```python
board = [
    ["_", "_", "_", "_", "_"],
    ["_", "O", "O", "O", "_"],
    ["_", "_", "_", "_", "_"],
    ["_", "_", "X", "_", "_"],
]
```

Here, `X` represents the player and `O` represents an invader. A NumPy array can provide a similar model, but NumPy is not required by Pygame. In the game itself, positions and `pygame.Rect` objects will be more useful than repeatedly clearing and rebuilding a character board.

## Generating an invader formation

A formation repeats an object across columns and rows. Store its geometry as named values:

```python
rows = 4
columns = 8
invader_width = 30
invader_height = 24
horizontal_gap = 12
vertical_gap = 16
origin_x = 50
origin_y = 70
```

Nested loops can generate the positions:

```python
def create_invader_positions(
    rows,
    columns,
    origin_x,
    origin_y,
    width,
    height,
    horizontal_gap,
    vertical_gap,
):
    positions = []

    for row in range(rows):
        for column in range(columns):
            x = origin_x + column * (width + horizontal_gap)
            y = origin_y + row * (height + vertical_gap)
            positions.append((x, y))

    return positions
```

The inner loop creates one row. The outer loop repeats it at different `y` positions.

## One formation, many invaders

Moving every invader independently invites inconsistencies. For movement, think of the live invaders as one formation.

At any moment, the formation has an outer boundary:

```python
fleet_left = min(invader.left for invader in invaders)
fleet_right = max(invader.right for invader in invaders)
```

Before moving horizontally, calculate the proposed change:

```python
horizontal_change = direction * speed * elapsed
```

If that change would cross an edge, reverse and descend. Otherwise, move horizontally:

```python
def move_fleet(invaders, direction, speed, elapsed, drop, screen_width):
    change = direction * speed * elapsed
    fleet_left = min(invader.left for invader in invaders)
    fleet_right = max(invader.right for invader in invaders)

    crosses_left = fleet_left + change < 0
    crosses_right = fleet_right + change > screen_width

    if crosses_left or crosses_right:
        direction *= -1

        for invader in invaders:
            invader.y += drop
    else:
        for invader in invaders:
            invader.x += round(change)

    return direction
```

This version expects objects with rectangular `left`, `right`, `x` and `y` attributes. Pygame's `Rect` supplies those attributes.

## Why the outermost live invaders matter

If an invader at the edge is later destroyed, the formation boundary changes. Hard-coded `startcol` and `endcol` values can become inaccurate. Calculating `min(left)` and `max(right)` from the current live invaders continues to work as the formation changes.

For this lecture, no invaders are removed yet, but the representation anticipates Lecture 12.

## Pause and predict

Assume:

```text
screen width = 500
fleet left = 420
fleet right = 490
direction = 1
proposed change = 15
drop = 20
```

Predict:

1. whether the formation should move horizontally;
2. its new direction;
3. the change to each invader's `y` coordinate;
4. why moving first and detecting afterwards may produce a visible overshoot.

## Common mistakes

- **Forgetting that positive `y` moves down:** screen coordinates differ from many mathematical graphs.
- **Checking only the object's `x` value:** the right boundary also depends on object width.
- **Using a fixed number of pixels per frame:** game speed then varies with frame rate.
- **Moving each invader with unrelated state:** the formation can lose alignment.
- **Confusing a position with a grid index:** pixel coordinates and array indices serve different representations.
- **Clearing the model by recreating unrelated state:** movement should update positions deliberately.
- **Using hard-coded outer columns forever:** destroyed edge invaders would make those values stale.
- **Reversing on every frame at the boundary:** descend and change direction once, then allow movement away from the edge.

## Check your understanding

1. Where is `(0, 0)` in a Pygame window?
2. What legal range applies to the left edge of a player that has non-zero width?
3. Why include elapsed time in a movement calculation?
4. What roles do the inner and outer loops play when creating a formation?
5. Why should fleet boundaries be calculated from live invaders?

## Apply your learning

1. Draw a coordinate diagram for a 500 × 500 window.
2. Implement and test `move_player()` at the left edge, centre and right edge.
3. Generate a formation with four rows and eight columns.
4. Change the gaps and explain the effect on its total width and height.
5. Represent the positions as `pygame.Rect` objects without opening a display.
6. Implement fleet reversal and test both boundaries.
7. Explain which parts of your model can be unit-tested without Pygame graphics.

## Page summary

Movement is a change to stored coordinates. Direction, speed and elapsed time determine that change, while object dimensions determine legal boundaries. Nested loops generate a regular formation, and the current outermost invaders provide a reliable fleet boundary. Keeping these rules separate from drawing makes the game easier to understand and test.

**Previous:** Return to **11.1 Scoping the Game: Requirements and a First Prototype**.  
**Next:** Continue to **11.3 Pygame Foundations and the Game Loop**.

---

# 11.3 Pygame Foundations and the Game Loop

## On this page

- Installing and importing Pygame
- Why a game is better developed as a Python script
- Creating a window and drawing surface
- The event queue
- The update-render loop
- Frame rate and elapsed time
- Event input compared with held-key state

## Learning outcomes

By the end of this page, you should be able to:

- install and import Pygame in the correct Python environment;
- create and close a Pygame window safely;
- explain each stage of the game loop;
- process the event queue every frame;
- draw a shape and update the display;
- limit frame rate and calculate elapsed time;
- choose between discrete events and continuous key state.

## Use a `.py` file for the game

The notebook is useful for explanations and small modelling experiments. A real-time Pygame window is better run from a Python script such as `main.py`.

Reasons include:

- the game loop runs continuously until the window closes;
- notebook cells can retain old variables and display state;
- restarting or interrupting a graphical loop can be confusing;
- cloud notebook environments may not provide a normal desktop display;
- asset paths are easier to manage from a project folder.

Use the notebook as the guide, but build the prototype in a dedicated folder:

```text
pygame-prototype/
├── main.py
└── assets/
    ├── defender.png
    └── invader.png
```

## Installing Pygame

In a terminal using the same Python environment as the project:

```text
python -m pip install pygame
```

Confirm the import:

```text
python -c "import pygame; print(pygame.version.ver)"
```

Run `main.py` from its project directory:

```text
python main.py
```

If the import fails in an editor, check that the editor has selected the Python interpreter in which Pygame was installed.

## A minimal game loop

```python
import pygame


WIDTH = 500
HEIGHT = 500
BACKGROUND = (10, 12, 24)
PLAYER_COLOUR = (80, 220, 140)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("COM4008 Movement Prototype")
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, PLAYER_COLOUR, (250, 420), 25)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
```

## The stages of one frame

The loop repeats four responsibilities:

1. **Input:** collect and interpret events or current device state.
2. **Update:** change positions and other game state.
3. **Render:** clear the previous frame and draw the current state.
4. **Present and time:** display the completed frame and control its rate.

```text
process input → update state → draw frame → display frame
       ↑                                      │
       └──────────────── repeat ──────────────┘
```

The screen is filled on every frame so that previously drawn positions do not remain as trails.

## The event queue must be processed

`pygame.event.get()` retrieves pending events, including a request to close the window:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```

Do not test `event.type` outside the loop. There may have been no events, or the variable may refer only to the final event retrieved. Process each event where it is received.

## Events and current key state

`KEYDOWN` represents the moment a key is pressed:

```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE:
        print("Fire once")
```

That is suitable for a discrete action such as firing one projectile or pausing.

Continuous movement should normally ask which keys are currently held:

```python
keys = pygame.key.get_pressed()

if keys[pygame.K_LEFT]:
    direction = -1
elif keys[pygame.K_RIGHT]:
    direction = 1
else:
    direction = 0
```

This avoids depending on the operating system's keyboard-repeat settings.

## Frame rate and delta time

Without a timing control, the loop runs as quickly as the computer permits. Different computers may then produce different movement speeds.

`Clock.tick()` can limit the frame rate and report elapsed milliseconds:

```python
elapsed = clock.tick(60) / 1000
```

Dividing by 1000 converts milliseconds to seconds. A speed such as `300` can then mean approximately 300 pixels per second:

```python
player_x += direction * 300 * elapsed
```

The first frame can use `elapsed = 0` before the loop. At the end of each frame, `tick()` calculates the value for the next update.

## Drawing and presenting

Pygame draws onto a `Surface`. The window surface is returned by:

```python
screen = pygame.display.set_mode((WIDTH, HEIGHT))
```

Drawing changes that surface in memory:

```python
pygame.draw.rect(screen, (80, 220, 140), player_rect)
```

The completed frame becomes visible when the display is updated:

```python
pygame.display.flip()
```

## Pause and order the loop

Put these operations into a sensible frame order:

- draw the player;
- calculate movement;
- process the close event;
- fill the background;
- update the display;
- read held keys;
- limit the frame rate.

Explain why drawing before clearing the background would make the object disappear.

## Common mistakes

- **Running a desktop game loop in Colab:** a cloud notebook does not normally provide the required local display window.
- **Installing Pygame into a different interpreter:** the terminal and editor must use the same environment.
- **Omitting event processing:** the window may become unresponsive.
- **Reading `event` outside its loop:** it may be undefined or represent the wrong event.
- **Using only `KEYDOWN` for held movement:** movement depends on key-repeat behaviour.
- **Forgetting to clear each frame:** old drawings remain visible as trails.
- **Forgetting `pygame.display.flip()`:** drawing occurs, but the completed frame is not presented.
- **Omitting `Clock.tick()`:** CPU usage and game speed can vary unnecessarily.
- **Calling `sys.exit()` inside reusable notebook code:** it terminates the host process rather than simply ending the game loop.
- **Using `%reset` in a `.py` file:** it is notebook syntax, not ordinary Python.

## Check your understanding

1. Why is `main.py` preferable to a notebook cell for the complete game loop?
2. What four responsibilities repeat in each frame?
3. Why must the event queue be processed?
4. When is `KEYDOWN` more appropriate than `get_pressed()`?
5. What does `clock.tick(60) / 1000` provide?

## Apply your learning

1. Install Pygame and print its version.
2. Create a 500 × 500 window with an informative caption.
3. Draw a green rectangle or circle on a dark background.
4. Close the window through the `QUIT` event.
5. Add a `Clock` and limit the game to 60 frames per second.
6. Print a message once for a space-bar `KEYDOWN` event.
7. Use `get_pressed()` to report while an arrow key remains held.

## Page summary

A Pygame application repeatedly processes input, updates state, renders the current frame and presents it at a controlled rate. Events suit one-off actions, while current keyboard state suits continuous movement. A script provides a more reliable home for this real-time loop than a notebook cell, especially when assets and a desktop window are involved.

**Previous:** Return to **11.2 Modelling Movement and Boundaries**.  
**Next:** Continue to **11.4 Building the Movement Prototype**.

---

# 11.4 Building the Movement Prototype

## On this page

- Representing the player with a rectangle
- Continuous movement and boundary control
- Creating a fleet of invader rectangles
- Coordinated horizontal movement, reversal and descent
- Replacing shapes with image assets
- Organising and extending the prototype

## Learning outcomes

By the end of this page, you should be able to:

- represent game-object position and size with `pygame.Rect`;
- implement frame-rate-independent held-key movement;
- clamp the player to the window;
- construct and draw a formation of invaders;
- reverse and descend the fleet at screen edges;
- replace prototype shapes with loaded and scaled images;
- identify a sensible boundary between Lectures 11 and 12.

## Begin with shapes

Coloured shapes allow us to verify movement before introducing file paths, transparency and image scaling.

Create a player rectangle:

```python
player_rect = pygame.Rect(0, 0, 35, 30)
player_rect.midbottom = (WIDTH // 2, HEIGHT - 30)
player_x = float(player_rect.x)
player_speed = 300
```

The `Rect` stores position and size together. Attributes such as `left`, `right`, `center` and `midbottom` make alignment and boundary checks more expressive.

## Continuous player movement

Inside the loop, read the current keys:

```python
keys = pygame.key.get_pressed()
direction = 0

if keys[pygame.K_LEFT]:
    direction -= 1
if keys[pygame.K_RIGHT]:
    direction += 1
```

If both keys are held, the changes cancel and direction becomes zero. Update and constrain the position:

```python
player_x += direction * player_speed * elapsed
player_x = max(0, min(player_x, WIDTH - player_rect.width))
player_rect.x = round(player_x)
```

The floating-point value preserves small movement changes; the rectangle receives an integer pixel coordinate for drawing.

## Create the invader formation

```python
def create_invaders(rows, columns):
    invaders = []
    width = 30
    height = 24
    horizontal_gap = 12
    vertical_gap = 14
    origin_x = 50
    origin_y = 60

    for row in range(rows):
        for column in range(columns):
            x = origin_x + column * (width + horizontal_gap)
            y = origin_y + row * (height + vertical_gap)
            invaders.append(pygame.Rect(x, y, width, height))

    return invaders
```

For a 500-pixel window, choose the column count and spacing so that the initial formation fits. Calculate rather than guess if you change these values.

## Move the fleet

Set initial movement values:

```python
invaders = create_invaders(rows=4, columns=8)
fleet_direction = 1
fleet_speed = 70
fleet_drop = 18
fleet_offset = 0.0
```

The fleet moves horizontally until its proposed change would cross an edge:

```python
def update_fleet(
    invaders,
    direction,
    speed,
    elapsed,
    drop,
    screen_width,
):
    change = direction * speed * elapsed
    left = min(invader.left for invader in invaders)
    right = max(invader.right for invader in invaders)

    if left + change < 0 or right + change > screen_width:
        direction *= -1

        for invader in invaders:
            invader.y += drop
    else:
        movement = round(change)

        for invader in invaders:
            invader.x += movement

    return direction
```

For very slow speeds, rounding each frame may discard movement. A more advanced design stores a floating-point fleet offset or uses `pygame.Vector2`. The values above normally produce visible integer changes at 60 frames per second.

## Draw the prototype

After updating the state, clear and draw:

```python
screen.fill((10, 12, 24))

pygame.draw.rect(screen, (80, 220, 140), player_rect)

for invader_rect in invaders:
    pygame.draw.rect(screen, (220, 220, 245), invader_rect)

pygame.display.flip()
```

The list contains the model's positions. The loop renders every current position.

## Complete shape-based prototype

```python
import pygame


WIDTH = 500
HEIGHT = 500
FPS = 60


def create_invaders(rows, columns):
    invaders = []
    width, height = 30, 24
    gap_x, gap_y = 12, 14
    origin_x, origin_y = 50, 60

    for row in range(rows):
        for column in range(columns):
            x = origin_x + column * (width + gap_x)
            y = origin_y + row * (height + gap_y)
            invaders.append(pygame.Rect(x, y, width, height))

    return invaders


def update_fleet(invaders, direction, speed, elapsed, drop):
    change = direction * speed * elapsed
    left = min(rect.left for rect in invaders)
    right = max(rect.right for rect in invaders)

    if left + change < 0 or right + change > WIDTH:
        direction *= -1

        for rect in invaders:
            rect.y += drop
    else:
        movement = round(change)

        for rect in invaders:
            rect.x += movement

    return direction


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("COM4008 Invader Movement")
clock = pygame.time.Clock()

player_rect = pygame.Rect(0, 0, 35, 30)
player_rect.midbottom = (WIDTH // 2, HEIGHT - 30)
player_x = float(player_rect.x)
player_speed = 300

invaders = create_invaders(4, 8)
fleet_direction = 1
fleet_speed = 70
fleet_drop = 18

running = True
elapsed = 0.0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_direction = 0

    if keys[pygame.K_LEFT]:
        player_direction -= 1
    if keys[pygame.K_RIGHT]:
        player_direction += 1

    player_x += player_direction * player_speed * elapsed
    player_x = max(0, min(player_x, WIDTH - player_rect.width))
    player_rect.x = round(player_x)

    fleet_direction = update_fleet(
        invaders,
        fleet_direction,
        fleet_speed,
        elapsed,
        fleet_drop,
    )

    screen.fill((10, 12, 24))
    pygame.draw.rect(screen, (80, 220, 140), player_rect)

    for invader_rect in invaders:
        pygame.draw.rect(screen, (220, 220, 245), invader_rect)

    pygame.display.flip()
    elapsed = clock.tick(FPS) / 1000

pygame.quit()
```

## Replace shapes with assets

Once movement works, load images relative to the script rather than changing the working directory:

```python
from pathlib import Path


ASSET_DIRECTORY = Path(__file__).resolve().parent / "assets"

player_image = pygame.image.load(
    ASSET_DIRECTORY / "defender.png"
).convert_alpha()

player_image = pygame.transform.scale(
    player_image,
    player_rect.size,
)
```

Draw the image at the rectangle:

```python
screen.blit(player_image, player_rect)
```

Use the same principle for invaders. The `Rect` remains the position and boundary model; the `Surface` supplies the appearance.

## Shapes, sprites and classes

The shape-based prototype is intentionally direct. Because you have already studied classes and inheritance, a later refactor could introduce:

- a `Player` class containing its image, rectangle and update behaviour;
- an `Invader` sprite class;
- a `pygame.sprite.Group` for drawing and updating invaders;
- a formation controller responsible for shared direction and edge behaviour.

Do not refactor merely to create more files. First establish working behaviour, then identify responsibilities that genuinely belong together.

## Where Lecture 11 stops

At the end of this lecture, the prototype should demonstrate:

- a reliable game loop;
- smooth held-key player movement;
- player boundary control;
- a regular invader formation;
- coordinated reversal and descent;
- clean shutdown;
- optional replacement of shapes with assets.

Lecture 12 can build on this with projectiles, collisions, removal, score, lives and game states.

## Pause and diagnose

Suppose the player moves only once when the key is pressed. Which input mechanism is probably being used?

Suppose the invaders leave trails. Which stage of the frame is probably missing?

Suppose the fleet reverses continuously without moving away from the edge. Which part of the boundary logic should you inspect?

Suppose movement is faster on one computer. Which timing value is probably absent?

## Common mistakes

- **Using an image's position separately from its rectangle:** one authoritative position model prevents disagreement.
- **Allowing the player's right edge beyond the window:** clamp against `WIDTH - player_rect.width`.
- **Handling movement only within `KEYDOWN`:** use current key state for continuous control.
- **Checking each invader against the edge and reversing repeatedly:** make one decision for the formation.
- **Loading images inside the game loop:** load and transform assets once before the loop.
- **Using fragile working-directory changes:** resolve asset paths relative to `__file__`.
- **Adding classes before the rules work:** abstraction cannot compensate for incorrect movement logic.
- **Combining shooting, collisions and movement in the first attempt:** complete and verify one increment at a time.
- **Forgetting the empty-fleet case:** later, when all invaders can be removed, avoid calling `min()` or `max()` on an empty list.

## Check your understanding

1. Why retain a floating-point `player_x` as well as `player_rect.x`?
2. What information does a `Rect` combine?
3. Why calculate one boundary for the whole fleet?
4. What is the difference between an image `Surface` and its positioning `Rect`?
5. Which systems should be postponed until Lecture 12?

## Apply your learning

1. Build and verify the complete shape-based prototype.
2. Change the player speed and report how this affects control.
3. Change fleet spacing while keeping every invader initially on screen.
4. Replace the player shape with the supplied defender image.
5. Replace the invader shapes with one or more supplied assets.
6. Add Escape as a second clean way to end the game.
7. Refactor one responsibility into a well-named function and justify the boundary.
8. Run `python -m pygame.examples.aliens`, then identify how its player, projectiles and collision responsibilities are organised. Treat the example as material to study, not code to copy without understanding.

## Page summary

The first prototype turns requirements into visible behaviour. A `Rect` provides position, size and useful boundaries; held-key state drives the player; elapsed time stabilises speed; and the current fleet boundary controls coordinated reversal and descent. Shapes establish correctness before assets add appearance. This stable movement foundation is ready for projectiles and collisions in Lecture 12.

**Previous:** Return to **11.3 Pygame Foundations and the Game Loop**.  
**Next step:** Complete the Lecture 11 movement prototype, then continue to Lecture 12 for projectiles, collisions and game state.

---

# Suggested lecture and VLE structure

Create one learning module titled **11 Pygame I: From Requirements to Movement**, containing:

1. **11.1 Scoping the Game: Requirements and a First Prototype**
2. **11.2 Modelling Movement and Boundaries**
3. **11.3 Pygame Foundations and the Game Loop**
4. **11.4 Building the Movement Prototype**

This four-page structure is preferable to using “Requirement 1” and “Requirement 2” as complete pages. Requirements remain the thread running across the lecture: each is specified on Page 1, modelled on Page 2 and implemented through Pages 3 and 4.

The original NumPy board remains a useful short modelling demonstration, particularly as a connection to Lecture 9. It should not become the main game-state representation: Pygame rectangles and lists map more directly to pixel positions, boundaries and later collision detection.

## Further reading

- [Pygame documentation and quick start](https://www.pygame.org/docs/)
- [Pygame event reference](https://www.pygame.org/docs/ref/event.html)
- [Pygame keyboard reference](https://www.pygame.org/docs/ref/key.html)
- [Pygame Rect reference](https://www.pygame.org/docs/ref/rect.html)
- [Pygame examples](https://www.pygame.org/docs/ref/examples.html)
