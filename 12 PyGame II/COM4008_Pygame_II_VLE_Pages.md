# COM4008 Programming Concepts: Pygame II — Objects, Collisions and Testing

This content is designed as four linked VLE information pages. Lecture 12 develops the movement prototype from Lecture 11 into a better-organised game containing player projectiles, collision responses, score and testable rules.

---

# 12.1 From Prototype to Maintainable Design

## On this page

- Reviewing the Lecture 11 prototype
- Selecting the next requirements
- Refactoring without changing behaviour
- Identifying objects and shared responsibilities
- Using `pygame.Rect` as the positional source of truth
- Organising the project into modules

## Learning outcomes

By the end of this page, you should be able to:

- distinguish completed requirements from the next development increment;
- explain the purpose of refactoring;
- identify appropriate responsibilities for player, invader, projectile and fleet code;
- avoid duplicated position state;
- separate asset loading, game logic and the main loop;
- protect a module from starting the game when it is imported by a test.

## Where Lecture 11 ended

The first prototype established:

- a window and controlled game loop;
- continuous left and right player movement;
- player boundary detection;
- a formation of invaders;
- coordinated fleet reversal and descent;
- drawing with shapes or image assets.

Lecture 12 should not rebuild those features from scratch. It should preserve the working behaviour while making the program easier to extend.

## The next development increment

The next essential requirements are:

### Requirement 3: player projectiles

1. Pressing Space creates a projectile at the player's current position.
2. The projectile moves upwards independently of the player.
3. More than one projectile may exist at the same time.
4. A projectile is removed after leaving the screen.

### Requirement 4: collisions

1. A projectile that overlaps a live invader removes both objects.
2. Destroying an invader adds its point value to the score.
3. A hostile projectile that overlaps the player removes the projectile and reduces lives.
4. The game enters an appropriate state when lives reach zero or no invaders remain.

Barriers, sound, animation and increasing difficulty remain valuable extensions, but the collision-and-state loop should work first.

## What is refactoring?

**Refactoring** changes the internal organisation of code without deliberately changing its externally observable behaviour.

Examples include:

- replacing related global variables with object attributes;
- extracting repeated code into a function;
- moving a class into its own module;
- replacing duplicated `x` and `y` values with one `Rect`;
- loading an image once instead of during every frame;
- giving shared fleet behaviour to a formation controller.

Refactoring is not the same as adding collisions. A safe sequence is:

1. confirm that the current movement works;
2. make one structural change;
3. run the game or tests again;
4. commit or record the working stage;
5. then add the new behaviour.

## Identify responsibilities, not just nouns

Potential game objects include:

| Component | Owns | Does not need to own |
|---|---|---|
| Player | Image, rectangle, movement speed | Every invader's position |
| Invader | Image, rectangle, point value | Shared fleet direction |
| Projectile | Rectangle, vertical speed, owner/type | Overall score |
| Fleet controller | Collection, direction, speed, edge response | Player keyboard input |
| Game | Groups, score, lives, current state, main loop | Pixel details for each image |

Not every noun needs a class. A class is useful when state and related behaviour belong together.

## One authoritative position

This design is fragile:

```python
self.x = x
self.y = y
self.rect = pygame.Rect(x, y, width, height)
```

If code changes `self.x` but forgets to update `self.rect`, drawing and collision detection disagree.

Prefer one authoritative rectangle:

```python
self.rect = image.get_rect(topleft=(x, y))
```

Move it directly:

```python
self.rect.x += movement
```

Draw with it:

```python
screen.blit(self.image, self.rect)
```

Test collisions with it:

```python
if projectile.rect.colliderect(invader.rect):
    ...
```

The image controls appearance; the rectangle controls position, size and broad collision boundaries.

## Objects should be created once

Do not create invaders or load their image inside the drawing function:

```python
# Avoid this inside every frame.
image = pygame.image.load("invader.png")
invader = Invader(image, position)
```

Create the fleet during setup. During each frame, update and draw the existing objects. This preserves each invader's identity and makes removal possible.

## A maintainable project structure

```text
space_game/
├── main.py
├── game_objects.py
├── game_rules.py
├── assets.py
├── assets/
│   ├── defender.png
│   └── invader.png
└── tests/
    └── test_game_rules.py
```

A smaller project may combine some files. The important separation is conceptual:

- `main.py` coordinates the real-time application;
- game objects contain local state and behaviour;
- game rules contain calculations and collision responses;
- asset loading deals with files;
- tests import logic without starting the game.

## Make imports safe

Do not start the window and infinite loop at module import time. Put the application entry point behind a guard:

```python
def main():
    pygame.init()
    # Create the window, objects and game loop.
    ...


if __name__ == "__main__":
    main()
```

Running `python main.py` calls `main()`. Importing classes into a test does not.

## Brief class recap

Lecture 12 applies earlier OOP concepts rather than reteaching them in full:

```python
class Invader:
    def __init__(self, image, position, points):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.points = points
```

- the class defines a type;
- `__init__()` establishes valid initial state;
- `self` identifies the current object;
- attributes store its state;
- methods provide behaviour associated with that state.

Inheritance can represent genuinely different invader behaviour, but separate `Squid`, `Crab` and `Octopus` subclasses are unnecessary if their only difference is a point value and image. Data passed to one `Invader` class is simpler:

```python
invader = Invader(squid_image, (50, 80), points=30)
```

Use inheritance when behaviour differs, not merely because labels differ.

## Pause and allocate responsibility

Decide which component should be responsible for each action:

1. clamp the player to the window;
2. reverse all invaders at an edge;
3. remove an off-screen projectile;
4. add points after a collision;
5. load and scale an image;
6. decide whether the game is won;
7. draw the current score.

There can be more than one defensible design, but each responsibility should have a clear home.

## Common mistakes

- **Repeating the whole Lecture 11 implementation:** begin from a verified movement prototype.
- **Calling new features “refactoring”:** structural improvement and behavioural change should be distinguished.
- **Storing position twice:** duplicated `x/y` values and `rect` coordinates drift apart.
- **Creating invaders while drawing them:** objects then lose identity and collections grow repeatedly.
- **Loading files in the game loop:** disk access and transformations should occur during setup.
- **Giving every invader its own fleet direction:** formation-level state belongs to a controller.
- **Using inheritance for point values alone:** configuration data is often sufficient.
- **Starting the game on import:** pytest then opens a window or becomes trapped in the loop.
- **Splitting into too many modules immediately:** separate genuine responsibilities, not every short function.

## Check your understanding

1. What distinguishes refactoring from adding a feature?
2. Why should `Rect` be the authoritative position?
3. Why must invader objects be created before the game loop?
4. Which state belongs to an individual invader, and which belongs to the fleet?
5. What problem does the `if __name__ == "__main__"` guard solve?

## Apply your learning

1. Make a copy of the working Lecture 11 prototype.
2. List its global variables and assign each to an appropriate responsibility.
3. Replace duplicated position state with rectangles.
4. Ensure images are loaded and scaled once.
5. Place the game loop inside `main()` and add the entry-point guard.
6. Run the prototype after each change and record any regression.
7. Sketch the modules you expect to need for collisions and tests.

## Page summary

Lecture 12 begins by stabilising and reorganising the movement prototype. Refactoring preserves working behaviour while clarifying responsibilities. Rectangles provide one authoritative position, objects are created once, fleet-wide state is separated from individual invaders, and a guarded `main()` keeps modules safe to import for testing.

**Next:** Continue to **12.2 Game Objects, the Fleet and Projectiles**.

---

# 12.2 Game Objects, the Fleet and Projectiles

## On this page

- Pygame sprites and groups
- Player and invader classes
- A formation controller
- Alternating horizontal movement and descent
- Creating multiple projectiles
- Removing off-screen objects
- Integrating objects into the game loop

## Learning outcomes

By the end of this page, you should be able to:

- implement game objects as Pygame sprites;
- use groups to manage collections of sprites;
- separate individual invader state from fleet behaviour;
- move the formation in alternating directions;
- create a new projectile for each valid firing action;
- remove sprites that are no longer required;
- integrate input, update and drawing responsibilities.

## Why use sprites and groups?

`pygame.sprite.Sprite` is a base class for visible game objects. A typical sprite provides:

- an `image` surface;
- a `rect` describing its position and size;
- optionally, an `update()` method.

A `pygame.sprite.Group` stores sprites and can update or draw the collection. Groups also work with Pygame's collision functions.

## The player

```python
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, image, centre, speed=300):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=centre)
        self.speed = speed
        self._x = float(self.rect.x)

    def move(self, direction, elapsed, screen_rect):
        self._x += direction * self.speed * elapsed
        self.rect.x = round(self._x)
        self.rect.clamp_ip(screen_rect)
        self._x = float(self.rect.x)

    def create_projectile(self, image):
        return Projectile(
            image=image,
            midbottom=self.rect.midtop,
            vertical_speed=-420,
        )
```

`clamp_ip()` moves the rectangle back inside the screen if necessary. Resetting `_x` after clamping prevents the hidden floating-point value continuing beyond an edge.

## Invaders as configured objects

```python
class Invader(pygame.sprite.Sprite):
    def __init__(self, image, position, points):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.points = points
```

Different rows can use different images and point values without requiring subclasses:

```python
row_designs = [
    (squid_image, 30),
    (crab_image, 20),
    (crab_image, 20),
    (octopus_image, 10),
]
```

## Create the fleet once

```python
def create_fleet(row_designs, columns, origin, gap):
    group = pygame.sprite.Group()
    origin_x, origin_y = origin
    gap_x, gap_y = gap

    for row, (image, points) in enumerate(row_designs):
        for column in range(columns):
            x = origin_x + column * (image.get_width() + gap_x)
            y = origin_y + row * (image.get_height() + gap_y)
            group.add(Invader(image, (x, y), points))

    return group
```

The group contains persistent objects. Drawing the group does not create more invaders.

## Shared formation behaviour

Direction and descent belong to the formation as a whole:

```python
class FleetController:
    def __init__(self, invaders, speed=70, drop=18):
        self.invaders = invaders
        self.speed = speed
        self.drop = drop
        self.direction = 1
        self._remainder = 0.0

    def update(self, elapsed, screen_rect):
        if not self.invaders:
            return

        exact_change = (
            self.direction * self.speed * elapsed
            + self._remainder
        )
        movement = int(exact_change)
        self._remainder = exact_change - movement

        left = min(sprite.rect.left for sprite in self.invaders)
        right = max(sprite.rect.right for sprite in self.invaders)

        crosses_edge = (
            left + movement < screen_rect.left
            or right + movement > screen_rect.right
        )

        if crosses_edge:
            self.direction *= -1
            self._remainder = 0.0

            for invader in self.invaders:
                invader.rect.y += self.drop
        else:
            for invader in self.invaders:
                invader.rect.x += movement
```

The controller makes one edge decision per frame. The invaders remain aligned and change direction together.

The empty-group check matters because `min()` and `max()` cannot operate on an empty collection. Once all invaders are destroyed, the fleet update should do nothing.

## A projectile class

```python
class Projectile(pygame.sprite.Sprite):
    def __init__(self, image, midbottom, vertical_speed):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(midbottom=midbottom)
        self.vertical_speed = vertical_speed
        self._y = float(self.rect.y)

    def update(self, elapsed, screen_rect):
        self._y += self.vertical_speed * elapsed
        self.rect.y = round(self._y)

        if not self.rect.colliderect(screen_rect):
            self.kill()
```

`kill()` removes the sprite from every group containing it. The Python object can then be reclaimed when nothing else refers to it.

Negative vertical speed moves a player projectile upward. A positive value can move an enemy projectile downward.

## Create one object per shot

Do not reuse one global bullet and a `fired` Boolean. That design permits only one shot and requires awkward resets.

Create a fresh projectile when Space is pressed:

```python
player_projectiles = pygame.sprite.Group()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            projectile = player.create_projectile(projectile_image)
            player_projectiles.add(projectile)
```

Each object stores its own position and movement. The group can contain zero, one or many projectiles.

You may add a firing cooldown if unrestricted key presses produce too many objects:

```python
if event.key == pygame.K_SPACE and current_time >= next_fire_time:
    player_projectiles.add(player.create_projectile(projectile_image))
    next_fire_time = current_time + 250
```

Here, the cooldown is expressed in milliseconds.

## Integrate update and drawing

```python
keys = pygame.key.get_pressed()
direction = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])

player.move(direction, elapsed, screen_rect)
fleet.update(elapsed, screen_rect)
player_projectiles.update(elapsed, screen_rect)

screen.fill(BACKGROUND)
invaders.draw(screen)
player_projectiles.draw(screen)
screen.blit(player.image, player.rect)
pygame.display.flip()
```

The order remains input, update, collision handling, render and display. Collision handling is added on the next page.

## Pause and trace object lifetime

Trace one player projectile through the program:

1. Which event creates it?
2. Where is its initial position obtained?
3. Which group stores it?
4. Which method changes its position?
5. What removes it after it leaves the screen?
6. What additional event will remove it on the next page?

## Common mistakes

- **Creating objects inside the draw loop:** setup creates objects; rendering only displays them.
- **Reloading an image for every invader:** sprites can share one loaded surface.
- **Using one projectile with a `fired` flag:** create an object for each shot.
- **Giving every invader an independent direction:** the fleet controller owns shared movement.
- **Reversing once per colliding invader:** calculate the outer fleet boundary and decide once.
- **Ignoring the empty fleet:** boundary calculations then raise an exception.
- **Never removing off-screen projectiles:** invisible objects continue accumulating.
- **Confusing `Sprite.kill()` with ending the program:** it removes a sprite from its groups.
- **Updating positions during drawing:** keep state changes in the update stage.
- **Expecting `Group.draw()` to call `update()`:** updating and drawing are separate operations.

## Check your understanding

1. What two attributes does a drawable Pygame sprite normally provide?
2. Why is a group useful for projectiles and invaders?
3. Which state belongs to the fleet controller?
4. Why does each shot need a new projectile object?
5. What does `kill()` do?

## Apply your learning

1. Refactor the player into a sprite using one rectangle for position.
2. Create persistent invader sprites from row configuration data.
3. Implement alternating fleet movement and descent through a controller.
4. Verify that movement continues after the outermost invader is removed manually.
5. Implement player projectiles and allow multiple simultaneous shots.
6. Remove projectiles after they leave the screen.
7. Add a short firing cooldown and explain why it belongs to input/game rules rather than rendering.

## Page summary

Sprites pair an image with a rectangle, while groups manage collections of persistent objects. Individual invaders own local state; a fleet controller owns shared direction and edge response. Each firing action creates an independent projectile, and off-screen projectiles remove themselves from their groups. These structures prepare the program for reliable group collision handling.

**Previous:** Return to **12.1 From Prototype to Maintainable Design**.  
**Next:** Continue to **12.3 Collisions, Score, Lives and Game State**.

---

# 12.3 Collisions, Score, Lives and Game State

## On this page

- Rectangle collision detection
- Resolving collisions between groups
- Removing collided objects safely
- Updating score and lives
- Player, enemy and fleet collision rules
- Game states and end conditions
- Rectangle and pixel-perfect collision boundaries

## Learning outcomes

By the end of this page, you should be able to:

- distinguish collision detection from collision response;
- use rectangle collision functions appropriately;
- resolve projectile-invader collisions across groups;
- remove objects without mutating a list during iteration;
- update score and lives from collision outcomes;
- recognise win, lose and running states;
- explain when rectangle collisions may be insufficient.

## Detection and response

Collision handling has two separate questions:

1. **Detection:** do these areas overlap?
2. **Response:** what should the game do because they overlap?

For example:

```python
if projectile.rect.colliderect(invader.rect):
    projectile.kill()
    invader.kill()
    score += invader.points
```

`colliderect()` detects overlap. Removing objects and changing score are responses defined by the game rules.

## Rectangle collision semantics

Pygame rectangles cover a left/top-inclusive area whose right and bottom coordinates lie just outside the covered pixels. Two rectangles that touch exactly at an edge do not overlap, so `colliderect()` returns `False` until their areas intersect.

Rectangle collision is fast and usually suitable for small arcade sprites. It detects overlap between bounding boxes, not necessarily between opaque pixels in irregular images.

## Groups avoid unsafe list mutation

This is risky:

```python
for invader in invaders:
    if projectile.rect.colliderect(invader.rect):
        invaders.remove(invader)
```

Removing from a list while iterating changes subsequent indices and can skip elements.

With sprite groups, Pygame can detect and remove collisions deliberately:

```python
collisions = pygame.sprite.groupcollide(
    invaders,
    player_projectiles,
    dokilla=True,
    dokillb=True,
)
```

The return value is a dictionary:

- each key is a sprite from the first group that collided;
- its value is the list of colliding sprites from the second group.

Both Boolean arguments are `True`, so collided invaders and projectiles are removed from their groups.

## Update the score

```python
def resolve_player_hits(invaders, projectiles):
    collisions = pygame.sprite.groupcollide(
        invaders,
        projectiles,
        True,
        True,
    )

    return sum(invader.points for invader in collisions)
```

In the game loop:

```python
score += resolve_player_hits(invaders, player_projectiles)
```

Returning the points makes the collision rule easier to test than modifying an unexplained global variable.

## Enemy projectiles and lives

Suppose enemy projectiles are stored in another group:

```python
hits = pygame.sprite.spritecollide(
    player,
    enemy_projectiles,
    dokill=True,
)

if hits:
    lives -= 1
```

`spritecollide()` compares one sprite with a group. The collided enemy projectiles are removed.

Decide whether several projectiles hitting during one frame should remove one life or several. The code above removes one life for any non-empty set of hits. That is a game-design decision and should be captured in the requirement.

Many games add a brief invulnerability period after damage so that overlapping objects do not remove lives every frame.

## Fleet reaches the player

The game may also be lost when the formation descends too far:

```python
def fleet_reached_player(invaders, player):
    if not invaders:
        return False

    lowest_invader = max(
        invader.rect.bottom for invader in invaders
    )

    return lowest_invader >= player.rect.top
```

This is a boundary rule rather than necessarily a pixel collision with one invader.

## Game state

A Boolean `running` answers whether the main loop continues, but the game also needs to distinguish play outcomes:

```python
PLAYING = "playing"
WON = "won"
LOST = "lost"

game_state = PLAYING
```

After collision resolution:

```python
if lives <= 0 or fleet_reached_player(invaders, player):
    game_state = LOST
elif not invaders:
    game_state = WON
```

The game can continue rendering a win or loss screen while the application itself remains open.

## Display score and lives

Create the font once:

```python
font = pygame.font.Font(None, 32)
```

Render updated text during the frame:

```python
status_surface = font.render(
    f"Score: {score}    Lives: {lives}",
    True,
    (240, 240, 255),
)

screen.blit(status_surface, (16, 14))
```

The displayed text is presentation. The integer variables remain the authoritative game state.

## Collision ordering

A sensible frame order is:

1. collect input and create any projectiles;
2. update positions;
3. remove off-screen objects;
4. detect and resolve collisions;
5. update score, lives and game state;
6. render the resulting state.

This ensures a destroyed invader is not drawn for an unnecessary extra frame.

## Bounding boxes and masks

Rectangle collision may report a hit in a transparent corner of an irregular image. If that becomes visibly unfair, Pygame can use masks for pixel-level collision checks.

Begin with rectangles. Move to masks only when the game and sprite shapes justify the additional complexity and cost.

## Pause and decide the rule

For each situation, state the detection and response separately:

1. one player projectile overlaps two invaders in the same frame;
2. two projectiles hit one invader;
3. two enemy projectiles hit the player together;
4. the final invader and the player are hit during the same frame;
5. an invader's bounding box overlaps the transparent corner of a projectile image.

There is not always one correct design, but the chosen outcome should be explicit and testable.

## Common mistakes

- **Treating detection as the whole rule:** the program must also define removal, points, lives and state changes.
- **Mutating a list during iteration:** use groups, a copied list or a separate removal collection.
- **Passing an object without a `rect` to sprite collision functions:** Pygame expects sprite rectangle attributes by default.
- **Recreating rectangles only occasionally:** the collision rectangle must move with the object.
- **Using `invaders != None` to test whether a collection has members:** use `if invaders:` or `if not invaders:`.
- **Leaving a collided projectile active:** it can score repeatedly on later frames.
- **Using a global score inside low-level collision code:** return the points or update a clear game-state owner.
- **Decreasing lives every overlapping frame:** define projectile removal or temporary invulnerability.
- **Ending the whole process immediately on win/loss:** a game state allows a result screen and restart option.
- **Starting with pixel masks:** rectangle collision is usually the appropriate first implementation.

## Check your understanding

1. What is the difference between collision detection and response?
2. What does `groupcollide()` return?
3. Why is removing from a list during iteration unsafe?
4. Why should `resolve_player_hits()` return points?
5. What is the difference between `running` and `game_state`?

## Apply your learning

1. Add player projectile collisions with the invader group.
2. Remove both objects and add the invader's configured point value.
3. Display score and lives in the window.
4. Add one downward enemy projectile and detect a player hit.
5. Decide and implement the response to simultaneous hits.
6. Detect when the fleet reaches the player line.
7. Add `WON` and `LOST` states without immediately closing the window.
8. Document one limitation of rectangle-based collision for your assets.

## Page summary

Collision detection establishes overlap; collision response changes the game. Sprite collision functions handle collections safely and return useful evidence of which objects collided. Those outcomes drive score, lives and explicit game states. Rectangle collision is an appropriate foundation, with masks available later if image transparency makes bounding boxes visibly inaccurate.

**Previous:** Return to **12.2 Game Objects, the Fleet and Projectiles**.  
**Next:** Continue to **12.4 Testing Game Rules with pytest**.

---

# 12.4 Testing Game Rules with pytest

## On this page

- What unit tests can and cannot check in a game
- Installing and running pytest
- Test discovery and assertions
- Testing movement boundaries
- Testing fleet direction and descent
- Testing collision responses and score
- Fixtures and parameterised tests
- Designing code for testability

## Learning outcomes

By the end of this page, you should be able to:

- identify game rules suitable for automated unit tests;
- organise source and test files for pytest;
- write independent tests using plain assertions;
- parameterise boundary test cases;
- use fixtures to create fresh objects;
- test collision responses without running the full game loop;
- interpret passed and failed pytest results.

## Why test a game?

Playing the game is still necessary. Human observation is useful for feel, appearance, sound and overall experience. It is inefficient for repeatedly checking exact rules such as:

- the player never crosses the left or right boundary;
- the fleet reverses and descends at an edge;
- a projectile is removed after a collision;
- the correct point value is awarded;
- lives cannot remain above zero in a lost state.

Automated tests run the same checks after each refactor and feature change.

## What makes code testable?

Tests should import code without opening a window or entering the game loop. Therefore:

- place the loop inside `main()`;
- use the entry-point guard;
- keep rules in functions or methods;
- inject simple images or rectangles rather than requiring asset files;
- avoid unexplained global state;
- return meaningful results from collision functions.

## Install and run pytest

In the project environment:

```text
python -m pip install pytest
```

From the project root:

```text
python -m pytest -v
```

Pytest discovers files named `test_*.py` or `*_test.py`, and functions whose names begin with `test_`.

Use test parameters only when pytest supplies them through fixtures or parametrisation. This function is incomplete:

```python
def test_move_left(x):
    ...
```

Pytest interprets `x` as a requested fixture. If no fixture named `x` exists, collection fails. Supply the value explicitly through object setup, a fixture or `@pytest.mark.parametrize`.

## Suggested test layout

```text
space_game/
├── game_objects.py
├── game_rules.py
├── main.py
└── tests/
    ├── test_player.py
    ├── test_fleet.py
    └── test_collisions.py
```

## Test player boundaries

Create a tiny surface in memory rather than loading an asset:

```python
import pygame

from game_objects import Player


def test_player_stops_at_left_edge():
    image = pygame.Surface((35, 30))
    screen_rect = pygame.Rect(0, 0, 500, 500)
    player = Player(image, centre=(17, 450), speed=300)

    player.move(direction=-1, elapsed=1.0, screen_rect=screen_rect)

    assert player.rect.left == screen_rect.left
```

The test follows arrange, act, assert:

1. **Arrange:** create the image, screen and player.
2. **Act:** request a movement.
3. **Assert:** check the resulting boundary.

## Parameterise related cases

```python
import pytest


@pytest.mark.parametrize(
    "start_x,direction,expected_x",
    [
        (0, -1, 0),
        (100, 0, 100),
        (465, 1, 465),
    ],
    ids=["left edge", "stationary", "right edge"],
)
def test_player_horizontal_boundaries(
    start_x,
    direction,
    expected_x,
):
    image = pygame.Surface((35, 30))
    screen_rect = pygame.Rect(0, 0, 500, 500)
    player = Player(image, centre=(17, 450), speed=300)
    player.rect.x = start_x
    player._x = float(start_x)

    player.move(direction, elapsed=1.0, screen_rect=screen_rect)

    assert player.rect.x == expected_x
```

Parametrisation runs one test function with several named input sets. Each case is reported separately.

Directly changing `_x` in a test reveals that the class interface could be improved. A constructor accepting a rectangle position, or a public placement method, would reduce the test's knowledge of internals.

## Use a fixture for fresh objects

```python
@pytest.fixture
def screen_rect():
    return pygame.Rect(0, 0, 500, 500)


@pytest.fixture
def player(screen_rect):
    image = pygame.Surface((35, 30))
    return Player(image, centre=screen_rect.midbottom, speed=300)
```

Each test requesting `player` receives a newly created object. This prevents one test's movement or damage leaking into another.

Do not share one mutable player as a module-level global across tests.

## Test fleet reversal

```python
def test_fleet_reverses_and_descends_at_right_edge(screen_rect):
    image = pygame.Surface((30, 24))
    invader = Invader(image, position=(470, 80), points=10)
    invaders = pygame.sprite.Group(invader)
    fleet = FleetController(invaders, speed=70, drop=18)

    fleet.update(elapsed=1.0, screen_rect=screen_rect)

    assert fleet.direction == -1
    assert invader.rect.y == 98
```

Useful additional cases include:

- reversal at the left edge;
- normal horizontal movement away from an edge;
- an empty fleet;
- removal of the original outermost invader.

## Test collision responses

```python
from game_rules import resolve_player_hits


def test_hit_removes_objects_and_awards_points():
    invader_image = pygame.Surface((30, 24))
    projectile_image = pygame.Surface((4, 12))

    invader = Invader(invader_image, (100, 100), points=30)
    projectile = Projectile(
        projectile_image,
        midbottom=invader.rect.midbottom,
        vertical_speed=-420,
    )

    invaders = pygame.sprite.Group(invader)
    projectiles = pygame.sprite.Group(projectile)

    points = resolve_player_hits(invaders, projectiles)

    assert points == 30
    assert len(invaders) == 0
    assert len(projectiles) == 0
```

This test checks one rule through three observable outcomes. It does not need a visible window, keyboard or complete game loop.

## Test behaviour, not implementation trivia

Prefer:

```python
assert player.rect.left == 0
```

over asserting that a particular internal helper was called. A refactor should be allowed to change internal organisation while preserving the rule.

Similarly, avoid testing exact frame-by-frame positions unless the exact values are requirements. Boundary, direction, score and removal outcomes are usually more stable.

## Tests are not the whole answer

Unit tests will not establish that:

- movement feels satisfying;
- images are attractive and correctly aligned;
- sound levels are appropriate;
- instructions are understandable;
- the game is enjoyable;
- every platform displays and receives input identically.

Combine automated tests with playtesting and observation.

## Pause and design a test

Write arrange, act and assert statements for each rule:

1. an off-screen projectile removes itself;
2. an empty fleet does not raise an exception;
3. a ten-point invader adds ten points;
4. two simultaneous enemy hits remove only one life;
5. destroying the final invader changes the state to `WON`.

Decide whether each should be a unit test of one function or a larger integration test involving several objects.

## Common mistakes

- **Putting the game loop at module level:** importing the module starts the application.
- **Giving a test an unexplained parameter:** pytest treats it as a fixture request.
- **Calling test functions manually:** let pytest discover and report them.
- **Sharing mutable global objects:** one test contaminates another.
- **Loading real assets for every unit test:** small in-memory surfaces are faster and more reliable.
- **Opening a display unnecessarily:** most movement and rectangle collision rules need no window.
- **Returning `True` from a test:** pytest uses assertions; a non-`None` return does not define success.
- **Testing only the happy path:** boundaries and empty collections are particularly valuable.
- **Writing one enormous test:** focused failures are easier to interpret.
- **Assuming green tests prove the game is good:** playtesting remains essential.

## Check your understanding

1. How does pytest discover test files and functions?
2. Why would `def test_move_left(x)` fail without further setup?
3. What does a fixture provide?
4. When is parametrisation useful?
5. Why can collision rules be tested without displaying the game?
6. What important qualities still require human playtesting?

## Apply your learning

1. Make `main.py` safe to import.
2. Install pytest and create a `tests` folder.
3. Test player movement at both screen boundaries.
4. Parameterise normal, stationary and boundary movement cases.
5. Test fleet movement, reversal, descent and the empty-fleet case.
6. Test that a collision removes both objects and awards the correct points.
7. Test a life-loss rule and one win/loss transition.
8. Run `python -m pytest -v` after a refactor and interpret any regression.
9. Play the game and record two qualities that the automated tests cannot assess.

## Page summary

Pytest turns game requirements into repeatable checks. Import-safe modules, explicit state and focused rules allow movement, boundaries, fleet behaviour, collisions and scoring to be tested without running the complete game. Fixtures create fresh objects, parametrisation covers related cases, and clear assertions produce useful failure reports. Automated testing complements rather than replaces playtesting.

**Previous:** Return to **12.3 Collisions, Score, Lives and Game State**.  
**Next step:** Complete and test the Pygame prototype, then evaluate it against the assignment requirements and through human playtesting.

---

# Suggested lecture and VLE structure

Create one learning module titled **12 Pygame II: Objects, Collisions and Testing**, containing:

1. **12.1 From Prototype to Maintainable Design**
2. **12.2 Game Objects, the Fleet and Projectiles**
3. **12.3 Collisions, Score, Lives and Game State**
4. **12.4 Testing Game Rules with pytest**

This structure improves on a long requirements recap followed by separate “classes” and “collisions” topics. The recap becomes a short development checkpoint. Classes are introduced through the concrete need to preserve object identity and organise responsibilities. Testing follows the rules it verifies, but testability influences the refactoring from the beginning.

## Recommended scope

The core Lecture 12 outcome should be:

- persistent player, invader and projectile objects;
- coordinated fleet behaviour;
- multiple player projectiles;
- reliable projectile-invader collision handling;
- score and lives;
- basic win and loss states;
- pytest checks for boundaries, fleet behaviour and collision responses.

Enemy firing can be a guided extension. Barriers, animation, sound, increasing difficulty and leaderboards are valuable assignment enhancements rather than all being mandatory lecture outcomes.

## Further reading

- [Pygame sprite and group collision reference](https://www.pygame.org/docs/ref/sprite.html)
- [Pygame Rect reference](https://www.pygame.org/docs/ref/rect.html)
- [Pygame examples](https://www.pygame.org/docs/ref/examples.html)
- [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html)
- [pytest parametrisation](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [pytest assertions](https://docs.pytest.org/en/stable/how-to/assert.html)
