# COM4008 Programming Concepts: Requirements and Design

This content is designed as five linked VLE information pages. Lecture 15 provides a compact introduction to the software development lifecycle, requirements analysis and design modelling, using the Space Invaders project and familiar software products as recurring examples.

---

# 15.1 Software Development Lifecycles: From Waterfall to Agile

## On this page

- Software engineering and the software development lifecycle
- Sequential and iterative development
- The Waterfall model
- Agile values and principles
- Sprints, feedback and increments
- Selecting practices to suit a project

## Learning outcomes

By the end of this page, you should be able to:

- explain why software development needs an organised lifecycle;
- distinguish sequential and iterative approaches;
- summarise the strengths and limitations of Waterfall;
- explain the purpose of short feedback cycles;
- distinguish Agile values from one particular framework;
- relate analysis, design, building and testing within an increment.

## Software development is more than programming

Programming turns ideas into executable instructions, but a successful product also depends on understanding the problem, agreeing what should be built, designing a coherent solution, checking its behaviour and maintaining it after release.

A simplified software development lifecycle (SDLC) contains:

```text
investigate → analyse → plan → design → build → test → deploy → review
```

Real projects do not always pass through these activities once in a straight line. The lifecycle gives us a vocabulary for the work and helps teams decide when feedback and decisions are needed.

## A sequential approach

A traditional Waterfall representation places major stages in sequence:

```text
Requirements → Design → Implementation → Testing → Deployment → Maintenance
```

This can be useful when:

- the problem and acceptance conditions are stable;
- changes are expensive or highly controlled;
- formal approvals and traceability are required;
- hardware, regulation or contracts constrain the process;
- the team needs substantial up-front coordination.

Its main risk is delayed feedback. If users see working software only near the end, a mistaken assumption made during requirements analysis may be expensive to correct.

Waterfall should not be presented as “never communicate and never revisit anything.” Nor is every planned or documented project automatically Waterfall. The important distinction is how work, approval and feedback are organised.

## Change is normal

Requirements can change because:

- users learn what they need after seeing a prototype;
- organisational priorities change;
- competitors or regulations alter the context;
- technical discoveries expose new constraints;
- team membership changes;
- an early assumption proves false.

A process therefore needs a deliberate way to receive, evaluate and prioritise change.

## Agile values

The 2001 Manifesto for Agile Software Development expresses four comparative values:

- individuals and interactions over processes and tools;
- working software over comprehensive documentation;
- customer collaboration over contract negotiation;
- responding to change over following a plan.

The items on the right still have value. Agile does not mean no planning, no documentation or no design. It places greater emphasis on collaboration, working results and adaptation.

The accompanying principles include early and continuous delivery, welcoming useful change, frequent working software, sustainable development, technical excellence, simplicity and regular reflection.

## Agile is not the same as Scrum

**Agile** is a broad set of values and principles. **Scrum** is one framework that teams may use for complex product work. **Extreme Programming (XP)** is a collection of development values and practices with a strong technical focus.

In Scrum, work happens within a time-boxed **Sprint**. A Sprint contains the other formal Scrum events and aims to create a useful product increment. The official framework also defines accountabilities, artifacts and commitments; simply dividing work into two-week periods does not by itself mean a team is practising Scrum.

For this introductory module, the transferable idea is the feedback loop:

```text
select valuable work
        ↓
analyse and design enough to begin
        ↓
build and test a small increment
        ↓
show it, learn and adapt
        └───────────────↺
```

## Design and testing happen throughout

An iterative process does not remove design or testing. It brings them into each increment:

```text
Analyse → Plan → Design ↔ Build ↔ Test → Review
```

Requirements provide a reason for the work. Design proposes a structure. Implementation realises it. Testing supplies evidence about whether it behaves as required. Feedback may change any of these.

## Compare approaches carefully

| More sequential | More iterative |
|---|---|
| larger stages and formal handovers | smaller increments and frequent feedback |
| more decisions made before implementation | decisions refined as evidence emerges |
| change managed through formal control | change expected and reprioritised regularly |
| progress often measured through completed stages | progress demonstrated through working increments |
| can suit stable, constrained contexts | can suit uncertain or changing contexts |

Neither column guarantees success. A suitable process depends on risk, scale, regulation, uncertainty, stakeholders and team capability.

## Pause and choose a lifecycle

Compare two projects:

1. a small student game whose controls will be refined after play-testing;
2. software controlling a safety-critical medical device with formal regulatory evidence.

Which activities would both projects require? Where might the timing, approval and documentation differ?

## Common mistakes

- **Equating software engineering with coding:** requirements, design, testing, deployment and maintenance also matter.
- **Treating the lifecycle as one universal recipe:** adapt the process to the context.
- **Calling Agile unplanned:** planning occurs repeatedly and at different levels.
- **Calling Agile undocumented:** useful documentation remains valuable.
- **Assuming Scrum and Agile are synonyms:** Scrum is one framework aligned with Agile thinking.
- **Leaving testing until the end of an iteration:** test evidence should develop alongside the increment.
- **Using “working software” to excuse poor design:** technical excellence and good design support adaptability.
- **Choosing a process because it is fashionable:** justify it against project risks and constraints.

## Check your understanding

1. What activities commonly appear in an SDLC?
2. What risk arises when feedback is delayed?
3. Does Agile reject plans and documentation? Explain.
4. How does Scrum relate to Agile?
5. What is a product increment?
6. Why might a highly regulated project organise work differently from a student game?

## Apply your learning

1. Draw a sequential lifecycle and an iterative lifecycle for the same project.
2. Identify three likely sources of change in the Space Invaders assignment.
3. Define a one-week increment that produces demonstrable game behaviour.
4. State what requirements, design and test evidence that increment would need.
5. Choose an approach for a project you know and justify it using risk and uncertainty.
6. Write a short reflection on how feedback changed one of your earlier programs.

## Page summary

Software engineering organises more than implementation. Sequential approaches emphasise planned stages and controlled handovers, while iterative approaches create smaller feedback cycles. Agile values collaboration, working results and adaptation; frameworks such as Scrum provide more specific structures. Requirements, design and testing remain important in every approach.

**Next:** Continue to **15.2 Discovering and Managing Requirements**.

---

# 15.2 Discovering and Managing Requirements

## On this page

- Stakeholders, needs and constraints
- Functional and non-functional requirements
- Writing clear, testable requirements
- Acceptance criteria and traceability
- Prioritisation and changing requirements
- Requirements in GitHub
- Branches and forks

## Learning outcomes

By the end of this page, you should be able to:

- identify stakeholders and their different concerns;
- distinguish functional and non-functional requirements;
- rewrite ambiguous statements as testable requirements;
- add acceptance criteria to a requirement;
- prioritise and trace requirements through development;
- explain how branches and forks support different collaboration situations.

## Begin with stakeholders

A **stakeholder** is a person, group or organisation that affects the system or is affected by it. For a game, stakeholders might include players, developers, tutors, assessors, platform providers and asset creators.

Different stakeholders can want different things:

- a player wants responsive controls;
- an assessor needs evidence against the assignment criteria;
- a developer needs maintainable code;
- a platform provider imposes technical constraints;
- an asset creator expects licence conditions to be respected.

Requirements analysis makes these needs visible and resolves conflicts before they silently become code.

## Functional requirements

Functional requirements describe what the system must do. They normally contain an observable behaviour:

- The Defender shall move left while the left control is held.
- The Defender shall fire a projectile when the fire control is activated.
- Invaders shall reverse horizontal direction after the formation reaches a boundary.
- A collision between a player projectile and an Invader shall remove both objects and increase the score.

Use consistent language. **Shall** can identify a mandatory requirement; **should** may imply a recommendation and can create ambiguity if used accidentally.

## Non-functional requirements

Non-functional requirements describe qualities, constraints or conditions:

- input should receive visible feedback within a defined time;
- the game must run in the supported environment;
- the source must follow the module's coding conventions;
- controls must be documented and usable without a mouse;
- saved data must not expose personal information.

“The game should be fast” is not testable. Replace vague qualities with a measure and operating condition appropriate to the project.

## Write requirements that can be checked

A useful requirement is:

- **necessary** — it contributes to a stakeholder need;
- **clear** — readers are likely to interpret it consistently;
- **specific** — its scope and conditions are understood;
- **feasible** — it can be delivered within constraints;
- **testable** — evidence can show whether it is satisfied;
- **traceable** — it can be connected to design, code and tests;
- **uniquely identified** — it can be discussed without copying its full text.

Example:

```text
FR-04: When no Invaders remain, the game shall display the next level
and create a new formation within two seconds.
```

## Add acceptance criteria

Acceptance criteria turn a broad item into concrete examples of success:

```text
Requirement: The Defender shall remain within the play area.

Given the Defender is at the left boundary
When the player holds the left control
Then the Defender's x-coordinate does not decrease.

Given the Defender is inside the play area
When the player holds the right control
Then the Defender moves right until it reaches the right boundary.
```

This Given-When-Then form is optional, but it encourages conditions, actions and observable results.

## Prioritise the work

Not every desired feature has equal value. A simple MoSCoW classification is:

- **Must have:** the increment cannot meet its purpose without it;
- **Should have:** important, but a temporary workaround exists;
- **Could have:** valuable if time and risk permit;
- **Won't have this time:** deliberately outside the current scope.

The final category is not “never.” It protects the current increment from uncontrolled scope growth.

## Trace rather than forget

A lightweight trace can connect development evidence:

| Requirement | Design element | Implementation | Test/evidence | Status |
|---|---|---|---|---|
| FR-01 Move Defender | `Defender` use case and class | `Defender.move()` | boundary movement checks | In progress |
| FR-02 Fire projectile | Shoot use case | `Projectile` creation | firing scenarios | Planned |

Traceability helps answer: Why does this code exist? Which requirement is untested? What is affected if the requirement changes?

## Store and discuss requirements collaboratively

For a small project, requirements can live in a README, project wiki or issue tracker. Issues are useful when a requirement needs discussion, ownership, status and links to code changes.

A **branch** is an alternative line of development inside one repository. It lets a contributor isolate a feature, fix or experiment before merging it.

A **fork** is a separate repository that begins as a copy of another repository and remains connected to that upstream project. It has its own branches, permissions and collaboration space. A local clone is the copy downloaded to a computer; it is not the same thing as a GitHub fork.

Use a branch when contributors work within the same repository. A fork is common when a contributor does not have direct write access or needs an independently controlled repository.

## Change requires a decision

When a requirement changes:

1. record the proposed change and reason;
2. identify affected stakeholders;
3. assess design, code, test, time and risk impacts;
4. decide whether and when to accept it;
5. update the requirement and linked artifacts;
6. communicate the decision.

Agility means responding intelligently to change, not accepting every request immediately.

## Pause and improve a requirement

Rewrite this statement:

> The Invaders should get faster and the game should be fun.

Separate the behaviour from the quality goal. Add at least two measurable acceptance criteria and state one question you would ask a player or product owner.

## Common mistakes

- **Writing implementation instead of need:** describe the required outcome before choosing code.
- **Using vague words:** “fast”, “easy”, “user-friendly” and “normally” require definitions.
- **Combining several behaviours in one requirement:** separate them so each can be traced and tested.
- **Ignoring non-functional requirements:** quality and constraints can determine whether functionality is usable.
- **Treating priorities as permanent:** revisit them as evidence and constraints change.
- **Confusing a fork with a local clone:** a GitHub fork is a separate repository; a clone is a local working copy.
- **Creating branches without integrating them:** plan review and merge work.
- **Accepting change without impact analysis:** determine what else must change.

## Check your understanding

1. Who could be a stakeholder in the assignment?
2. How does a functional requirement differ from a non-functional one?
3. What makes a requirement testable?
4. What do acceptance criteria add?
5. What does “Won't have this time” achieve?
6. How do a branch, fork and clone differ?
7. Why is traceability useful after a change?

## Apply your learning

1. Identify at least five stakeholders and one concern for each.
2. Write six uniquely numbered game requirements, including two non-functional requirements.
3. Add Given-When-Then acceptance criteria to two requirements.
4. Prioritise the requirements using MoSCoW and justify one difficult choice.
5. Create a traceability table linking two requirements to classes and proposed tests.
6. Create a feature branch whose name refers to a requirement or issue.

## Page summary

Requirements translate stakeholder needs into clear, feasible and testable statements. Functional requirements describe behaviour; non-functional requirements capture qualities and constraints. Acceptance criteria, prioritisation and traceability make requirements actionable. Branches and forks support collaboration in different repository contexts, while change should be assessed and recorded deliberately.

**Previous:** Return to **15.1 Software Development Lifecycles: From Waterfall to Agile**.

**Next:** Continue to **15.3 Modelling Behaviour with Use Cases**.

---

# 15.3 Modelling Behaviour with Use Cases

## On this page

- The purpose and scope of use-case modelling
- Actors, system boundaries and use cases
- Naming behaviour from a user's perspective
- Associations between actors and use cases
- `«include»` and `«extend»`
- Building a Space Invaders use-case model
- Adding textual use-case descriptions

## Learning outcomes

By the end of this page, you should be able to:

- explain what a use-case diagram communicates;
- identify actors and goal-oriented use cases;
- draw a system boundary and associations;
- name use cases using clear verb phrases;
- distinguish `«include»` from `«extend»` accurately;
- supplement a diagram with a brief use-case description.

## Model the system from the outside

A UML use-case diagram shows how external **actors** interact with a system to achieve goals. It focuses on required behaviour rather than internal classes or source code.

An actor is a **role**, not necessarily one named person. It can be a human role, another system, a device or a time-based external trigger.

Examples include:

- Player;
- Administrator;
- Payment service;
- File system;
- Game controller.

An Invader inside the Space Invaders game is normally a domain object rather than an external user of the game system. If the model's subject were instead an individual Invader component, the boundary and actors could differ. Always state what system the diagram describes.

## Core notation

```text
          ┌──────── Space Invaders game ────────┐
Player ───┤ (Start game)                        │
       ├──┤ (Move Defender)                     │
       └──┤ (Fire projectile)                   │
          └─────────────────────────────────────┘
```

- the rectangle shows the system boundary;
- stick figures or labelled symbols show actors outside it;
- ovals show use cases inside it;
- solid lines show actor-use-case associations.

Name a use case with a goal-oriented verb phrase such as **Start game**, **Move Defender** or **View score**. Avoid vague nouns such as “Movement” when a clearer action is available.

## Derive use cases from requirements

Begin with the doing words in the requirements, but do not turn every method into a use case.

```text
Requirement: The player shall be able to fire a projectile.
Candidate use case: Fire projectile
Likely implementation methods: handleInput(), fire(), addProjectile()
```

The use case expresses an actor's goal. The methods are internal design decisions explored later.

## `«include»`: required reused behaviour

An `«include»` relationship extracts behaviour that the base use case incorporates. It is useful when several use cases share a required sub-flow.

```text
(Start new level) --«include»--> (Create Invader formation)
```

The dashed arrow points **from the including use case to the included use case**. “Include means mandatory” is an incomplete shortcut: the important idea is deliberate reuse of behaviour that forms part of the base use case.

## `«extend»`: conditional additional behaviour

An `«extend»` relationship adds behaviour to a base use case at a defined extension point, often under a condition. The base use case remains meaningful without the extension.

```text
(Award extra life) --«extend»--> (Update score)
condition: score reaches threshold
```

The dashed arrow points **from the extending use case to the base use case**. Extend does not simply mean “any optional feature.” Use it only when the conditional extension relationship genuinely clarifies the model.

## Keep diagrams readable

A use-case diagram is a communication tool, not a complete behavioural specification. Avoid:

- dozens of tiny use cases;
- implementation classes inside the boundary;
- arrows added without a clear semantic reason;
- use cases named as UI clicks rather than user goals;
- crossing lines and missing labels.

Split a large model by feature area or actor goal. Supply text for important flows.

## A short textual use case

```text
Use case: Fire projectile
Primary actor: Player
Precondition: A game is active and the Defender exists.
Trigger: The player activates the fire control.
Main success flow:
1. The game checks whether firing is currently allowed.
2. A projectile is created above the Defender.
3. The projectile begins moving upwards.
Postcondition: One new player projectile is active.
Alternative: If the firing limit has been reached, no projectile is created.
```

The diagram provides an overview; this description supplies sequence, conditions and outcomes.

## Pause and check the boundary

Consider these candidates: Player, Invader, Defender, keyboard, assessor, score and repository.

Which are actors for a use-case model of the running game? Which belong inside the game? Which may be irrelevant to this particular system boundary? Explain any assumption that changes your answer.

## Common mistakes

- **Calling every object an actor:** a UML actor is external to the system being modelled.
- **Omitting the system boundary:** readers cannot tell what is inside the subject.
- **Naming use cases with nouns:** use goal-oriented verb phrases.
- **Converting every method into a use case:** use cases describe external goals, not code structure.
- **Treating `«include»` only as “mandatory”:** it models incorporated, reusable behaviour.
- **Treating `«extend»` as a general optional label:** it adds behaviour to a meaningful base at an extension point.
- **Reversing dependency arrows:** check which use case includes or extends which.
- **Trying to show detailed order in a use-case diagram:** use a textual flow or sequence diagram when order matters.

## Check your understanding

1. What does a use-case diagram show?
2. Why is an actor a role rather than simply a person?
3. Where should the system boundary be drawn?
4. Why is **Fire projectile** better than **Projectile** as a use-case name?
5. How do `«include»` and `«extend»` differ?
6. Why supplement the diagram with text?

## Apply your learning

1. Draw a use-case diagram containing the Player and at least five goals.
2. Derive those goals from numbered requirements.
3. Add one justified `«include»` relationship.
4. Add one conditional extension only if the base remains meaningful without it.
5. Write a textual description for **Start game** or **Fire projectile**.
6. Review the diagram with a peer and record one ambiguity they found.

## Page summary

Use-case modelling describes a system's behaviour from the perspective of external roles. Actors remain outside the system boundary, while goal-oriented use cases appear inside it. Associations show participation; `«include»` supports required reused behaviour and `«extend»` describes conditional additions to a meaningful base. Textual descriptions provide detail that the overview diagram intentionally omits.

**Previous:** Return to **15.2 Discovering and Managing Requirements**.

**Next:** Continue to **15.4 Modelling Structure with Class Diagrams**.

---

# 15.4 Modelling Structure with Class Diagrams

## On this page

- Moving from requirements to structural design
- Classes, attributes and operations
- UML visibility and type notation
- Associations and multiplicity
- Generalisation and inheritance
- Identifying candidate game classes
- Keeping models useful and proportionate

## Learning outcomes

By the end of this page, you should be able to:

- identify candidate classes from a problem description;
- represent attributes and operations in UML notation;
- interpret visibility, parameter and return-type notation;
- show associations and multiplicities;
- model a justified inheritance relationship;
- compare a conceptual class model with Java implementation classes.

## Model the static structure

A class diagram describes types of object and relationships between them. Unlike a use-case diagram, it looks inside the system.

A class is commonly shown in compartments:

```text
┌──────────────────────────┐
│ Defender                 │
├──────────────────────────┤
│ - lives : int            │
│ - speed : int            │
├──────────────────────────┤
│ + move(direction : int)  │
│ + fire() : Projectile    │
└──────────────────────────┘
```

- the first compartment names the class;
- the second lists attributes;
- the third lists operations.

## Visibility and types

Common UML visibility symbols are:

- `+` public;
- `-` private;
- `#` protected;
- `~` package visibility.

Attribute notation normally follows:

```text
visibility name : Type
```

Operation notation normally follows:

```text
visibility name(parameter : Type) : ReturnType
```

UML is language-independent, although the model may be designed with Java in mind. A diagram should communicate decisions rather than reproduce every line of code automatically.

## Find candidate classes

Nouns in requirements can suggest candidate entities:

- Defender;
- Invader;
- Projectile;
- Shield;
- Game;
- Level;
- Score.

This is a starting heuristic, not a rule. Some nouns are attributes, external actors, values or irrelevant details. Ask whether each candidate has identity, state, behaviour or meaningful relationships.

Verbs can suggest operations:

- move;
- fire;
- collide;
- update score;
- start level.

Place behaviour with the class that has the information and responsibility needed to perform it. Avoid creating one “god class” that knows and does everything.

## Associations and multiplicity

An association shows a meaningful structural relationship. Multiplicity states how many objects can participate:

```text
Game 1 ───────── 1 Defender
Game 1 ───────── 1..* Invader
Defender 1 ───── 0..* Projectile
```

Common multiplicities include:

- `1` exactly one;
- `0..1` zero or one;
- `*` or `0..*` zero or many;
- `1..*` one or many.

Do not add an association merely because two classes call each other once. Model relationships that help explain the design.

## Generalisation and inheritance

If several classes share genuine state and behaviour, a general superclass may be useful:

```text
              Sprite
             △      △
            /        \
      Defender      Invader
                       △
                 ┌─────┼─────┐
               Squid  Crab  Octopus
```

The hollow triangular arrow points to the more general class. This represents an “is a kind of” relationship:

- a Defender is a kind of Sprite;
- an Invader is a kind of Sprite;
- a Squid is a kind of Invader.

Inheritance should express substitutable specialisation, not merely reduce duplicated fields. Prefer a clear association or composition when the relationship is “has a” rather than “is a.”

## Connect the diagram to Java

```java
public abstract class Sprite {
    private int x;
    private int y;

    public abstract void move();
}

public class Invader extends Sprite {
    @Override
    public void move() {
        // Invader movement rule
    }
}
```

The UML model guides implementation, but code will contain additional details such as constructors, framework methods and helper operations. The model may also change when implementation exposes a better design.

BlueJ and Greenfoot show classes and inheritance visually, providing a useful class overview. A deliberate UML class diagram adds attributes, operations, multiplicities and relationships that an environment's class view may not communicate fully.

## Pause and allocate responsibilities

Given `Game`, `Defender`, `Invader`, `Projectile` and `Score`, decide which class should:

- interpret player movement;
- create a player projectile;
- know whether a projectile hit an Invader;
- maintain the current score;
- decide that the level is complete.

There can be more than one defensible design. Justify each choice using the information the class possesses.

## Common mistakes

- **Treating every noun as a class:** distinguish entities from values, actors and incidental language.
- **Giving every attribute public visibility:** protect internal state and provide intentional operations.
- **Forgetting types and return values:** they communicate important design constraints.
- **Using inheritance for “has a”:** generalisation means “is a kind of.”
- **Adding a superclass solely to remove one repeated line:** inheritance carries conceptual and behavioural meaning.
- **Omitting multiplicity:** readers cannot see whether a relationship is optional or many-valued.
- **Copying all implementation details into the model:** select the details needed for the design conversation.
- **Assuming the first diagram is final:** refine it as requirements and implementation knowledge develop.

## Check your understanding

1. How does a class diagram differ from a use-case diagram?
2. What do the three class compartments contain?
3. What do `+`, `-` and `#` mean?
4. What does `0..*` express?
5. In which direction does a generalisation arrow point?
6. Why might `Squid` extend `Invader`?
7. When is composition more suitable than inheritance?

## Apply your learning

1. Extract candidate classes, attributes and operations from four requirements.
2. Draw a class diagram for the core Space Invaders prototype.
3. Add types, visibility and return values.
4. Add associations and justified multiplicities.
5. Model one inheritance hierarchy and challenge whether it is truly an “is a” relationship.
6. Compare your diagram with the classes visible in Greenfoot or your Python implementation.

## Page summary

Class diagrams model the system's static structure through classes, attributes, operations and relationships. Candidate classes emerge from domain concepts but require judgement. Visibility, types and multiplicity make decisions explicit. Generalisation represents genuine “is a kind of” relationships and should be used more carefully than simple code reuse suggests.

**Previous:** Return to **15.3 Modelling Behaviour with Use Cases**.

**Next:** Continue to **15.5 Designing the User Experience**.

---

# 15.5 Designing the User Experience

## On this page

- User experience and user interface design
- Design principles and consistency
- Level design as rule and experience design
- Sketching and paper prototypes
- Wireframes and interactive prototypes
- Storyboards, personas and scenarios
- Moving from low to higher fidelity

## Learning outcomes

By the end of this page, you should be able to:

- distinguish user experience from user interface;
- explain the value of low-fidelity design;
- create an annotated level sketch;
- produce a wireframe focused on structure and interaction;
- use a persona, scenario and storyboard to explore context;
- select an appropriate prototype fidelity;
- connect a design artifact to requirements and evaluation.

## UX is broader than appearance

The **user interface (UI)** is the part of a system through which a person interacts: controls, screens, information and feedback.

The **user experience (UX)** includes the wider experience of trying to achieve a goal: usefulness, learnability, efficiency, accessibility, confidence, emotion and recovery from mistakes.

A polished screen can still produce a poor experience if the user cannot understand the next action, receives no feedback or loses work unexpectedly.

## Useful interface principles

Effective interfaces commonly aim for:

- **visibility:** important state and available actions can be found;
- **feedback:** the system responds clearly to an action;
- **consistency:** similar things look and behave similarly;
- **mapping:** controls relate naturally to their effects;
- **constraints:** invalid actions are prevented or discouraged;
- **error recovery:** mistakes can be understood and corrected;
- **accessibility:** different users and interaction needs are considered;
- **simplicity:** unnecessary choices and decoration do not obscure the goal.

These are design questions, not merely styling choices.

## Level design

A game level combines spatial structure, rules, challenge and pacing. A sketch can show:

- the player's starting position;
- obstacles and safe areas;
- enemies, resources and goals;
- the intended route;
- where a new mechanic is introduced;
- transitions between worlds or levels;
- changes in difficulty.

Annotate why each element exists. “Platform here” is weaker than “safe platform lets the player observe the moving obstacle before attempting the jump.”

Classic games were often designed using grids and paper planning sheets because the level had to fit precise tile and memory constraints. The same practice remains useful: a cheap sketch reveals layout problems before assets and code make change expensive.

## Wireframes

A wireframe represents the structure and interaction of a screen without committing to final visual styling. It can show:

- information hierarchy;
- navigation;
- controls and input fields;
- expected content;
- transitions between screens;
- feedback, validation and error states.

Begin with paper or simple blocks. High visual polish too early can make a weak structure appear finished and discourage useful change.

```text
┌─────────────────────────────────┐
│ Game title              Score 0 │
├─────────────────────────────────┤
│                                 │
│          play area              │
│                                 │
├─────────────────────────────────┤
│ [Pause]     Lives: 3     [Help] │
└─────────────────────────────────┘
```

Tools such as Figma can connect multiple frames into a clickable prototype, but the design reasoning matters more than the tool.

## Fidelity should match the question

| Fidelity | Suitable questions |
|---|---|
| paper sketch | Is the concept understandable? What is missing? |
| low-fidelity wireframe | Is the structure and flow sensible? |
| clickable prototype | Can users navigate and complete a task? |
| coded prototype | Does the interaction work under technical constraints? |
| polished product | Does the complete experience meet its requirements? |

Do not use a costly prototype to answer a question that paper could resolve.

## Personas and scenarios

A **persona** is an evidence-informed representation of a relevant user group. It should capture behaviours, goals, context and constraints rather than stereotypes or irrelevant biography.

A **scenario** describes the persona trying to achieve a goal in context:

```text
James is replenishing office supplies between meetings. He needs to
repeat a previous order quickly, confirm the delivery date and retain
evidence for expenses.
```

This exposes requirements that a generic “user places an order” statement may miss.

## Storyboards

A storyboard shows a sequence of moments in the experience:

1. context or trigger;
2. the user's goal;
3. interactions with the system;
4. feedback and decisions;
5. outcome and emotional response.

It can include events beyond the screen. For example, a player sees instructions, tries a control, misinterprets feedback, learns the rule and succeeds. That sequence suggests interface and onboarding requirements.

Storyboards are particularly useful when multiple touchpoints, environmental constraints or human emotions matter. Artistic skill is not required; clarity is.

## Connect designs to evidence

Every important design choice should relate to a need or hypothesis:

| Requirement/need | Design response | Evaluation |
|---|---|---|
| player must recognise remaining lives | lives displayed consistently near score | ask players to locate status; observe play-test |
| first-time player needs controls | short instruction panel before play | test whether new player can start unaided |
| level must introduce challenge gradually | safe demonstration before hazard | observe failure points and completion rate |

A design artifact is not proof that the design works. It is something that can be reviewed and tested.

## Pause and choose a prototype

For each question, select the cheapest useful artifact:

- Do players understand the purpose of a power-up?
- Can users navigate from a start screen to accessibility settings?
- Is the jump mechanic technically possible in Greenfoot?
- Does a level's difficulty increase at an appropriate pace?

Explain when a sketch, wireframe, storyboard, clickable prototype or coded prototype is most suitable.

## Common mistakes

- **Equating UX with visual decoration:** UX concerns the whole experience of achieving a goal.
- **Designing for yourself alone:** investigate relevant users and contexts.
- **Starting at high fidelity:** cheap early artifacts invite change.
- **Creating a persona from stereotypes:** base it on relevant behaviours and needs.
- **Drawing screens without transitions:** show how the user moves between states.
- **Showing only the happy path:** include validation, failure and recovery.
- **Designing a level as decoration:** connect layout to mechanics, learning and pacing.
- **Treating a prototype as validation:** evaluate it with users or explicit criteria.
- **Using a tool because it is fashionable:** choose fidelity according to the question.

## Check your understanding

1. How do UI and UX differ?
2. What can a paper level design reveal before coding?
3. What is the purpose of a wireframe?
4. Why can high fidelity be harmful too early?
5. How do persona, scenario and storyboard differ?
6. Why should a storyboard include context beyond the screen?
7. How can a design choice be traced to evaluation evidence?

## Apply your learning

1. Create an annotated paper design for one Space Invaders or platform-game level.
2. Produce a low-fidelity start, play, pause and game-over flow.
3. Include one validation or error state, not only the happy path.
4. Create one short persona grounded in a relevant player need.
5. Storyboard that persona learning one game mechanic.
6. Link each frame or design decision to a numbered requirement.
7. Ask another learner to complete a task using the prototype and record one resulting change.

## Page summary

User experience design addresses how effectively and confidently people achieve goals, not only how an interface looks. Level sketches, wireframes and storyboards make ideas visible before expensive implementation. Personas and scenarios add user context, while different fidelity levels answer different questions. Designs should remain traceable to requirements and be evaluated rather than merely admired.

**Previous:** Return to **15.4 Modelling Structure with Class Diagrams**.

**End of Lecture 15.** You should now be able to move from stakeholder needs and requirements into behavioural, structural and experiential design artifacts that can guide implementation and testing.

