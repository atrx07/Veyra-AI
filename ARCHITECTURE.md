# ARCHITECTURE.md — Veyra Technical Architecture

## 1. Architectural Style

Veyra uses a deliberately flat, procedural, single-process architecture aligned with the internship PRD.

There is:

- no client/server split
- no database layer
- no service layer
- no network layer
- no persistence layer
- no background worker
- no trained model

The application is coordinated by one terminal interaction loop.

---

## 2. High-Level Flow

```text
┌───────────────────────────────────────────────────────┐
│                     main.py                           │
│                                                       │
│  startup -> capture name -> command loop              │
│                                                       │
│  input -> normalize -> classify by rules -> dispatch  │
└───────────────────────┬───────────────────────────────┘
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          v             v             v
     greetings      utilities      interaction
          │             │             │
          v             v             v
   greetings.py   datetime_utils  calculator.py
                  content.py      game.py
                                  ai_concepts.py
                        │
                        v
                   help_menu.py
```

The exact imports may be flatter than the diagram; the key principle is feature ownership by small modules.

---

## 3. Recommended Repository Layout

```text
Veyra/
├── AGENTS.md
├── PROJECT.md
├── REQUIREMENTS.md
├── ARCHITECTURE.md
├── COMMAND_SPEC.md
├── TESTING.md
├── STEPS.md
├── NEXTSTEPS.md
├── STATUS.md
├── DECISIONS.md
├── docs/
│   ├── PRD_TRACEABILITY.md
│   └── AI_ML_DL_REFERENCE.md
├── main.py
├── greetings.py
├── datetime_utils.py
├── calculator.py
├── content.py
├── game.py
├── ai_concepts.py
├── help_menu.py
└── README.md
```

Do not add directories such as `services/`, `repositories/`, `models/`, or `api/` unless scope is explicitly changed by the owner.

---

## 4. Module Responsibilities

### `main.py`

Owns:
- process entry point
- startup sequence
- user-name acquisition call
- main command loop
- command normalization
- top-level rule routing
- graceful loop termination
- defensive top-level exception boundary if needed

Must not own:
- calculator arithmetic details
- content lists
- guessing-game internals
- perceptron math details

---

### `greetings.py`

Owns:
- `get_user_name()` or equivalent
- startup greeting construction
- reusable personalized response helpers if useful

Behavior notes:
- A blank name should be handled sensibly without crashing.
- Do not persist the name.

---

### `datetime_utils.py`

Owns:
- current local date formatting
- current local time formatting

Suggested functions:

```python
get_current_date() -> str
get_current_time() -> str
```

Use only Python standard-library date/time facilities.

---

### `calculator.py`

Owns:
- calculator expression parsing
- arithmetic execution
- operator validation
- division-by-zero handling
- user-facing calculator error results where appropriate

Suggested pure core:

```python
calculate(left: float, operator: str, right: float) -> float
```

Suggested parser boundary:

```python
parse_expression(command: str)
```

Never use `eval()`.

---

### `content.py`

Owns:
- predefined quotes
- predefined jokes
- predefined facts
- random selection functions

Suggested functions:

```python
get_random_quote() -> str
get_random_joke() -> str
get_random_fact() -> str
```

The lists should contain enough entries that repeated requests visibly vary.

---

### `game.py`

Owns:
- target number generation
- attempt loop
- guess validation
- higher/lower feedback
- success/failure result

Preferred defaults based on PRD sample:

```text
MIN_NUMBER = 1
MAX_NUMBER = 20
MAX_ATTEMPTS = 5
```

Use named constants, not unexplained literals scattered through the function.

---

### `ai_concepts.py`

Owns both educational concept demonstrations.

#### Rule-based recommendation

Suggested API:

```python
recommend_activity(hour: int | None = None) -> str
```

If `hour` is omitted, use current local hour. Accepting an explicit hour makes the rule testable without changing user-facing behavior.

Rules should remain an ordinary visible `if/elif/else` chain.

#### Perceptron demo

Suggested split:

```python
perceptron(inputs: list[float]) -> int
perceptron_demo() -> None
```

The calculation should conceptually perform:

```text
weighted_sum = Σ(input_i × weight_i) + bias
output = 1 if weighted_sum > threshold else 0
```

The PRD specifically describes a step activation such as output 1 when the sum is greater than 0, otherwise 0. No training occurs.

Fixed values must be named and documented.

---

### `help_menu.py`

Owns:
- formatted supported-command list
- one-line descriptions
- syntax example for calculator if useful

Suggested function:

```python
print_help() -> None
```

All user-facing features must be discoverable here.

---

## 5. Main Loop Contract

Conceptual pseudocode:

```text
print startup banner
greet user
name = get user name
print personalized welcome

while true:
    raw = input("You: ")
    command = normalize(raw)

    if exit intent:
        print goodbye using name
        break
    elif help intent:
        help
    elif calculator intent:
        calculator
    elif game intent:
        game
    elif perceptron intent:
        perceptron demo
    elif recommendation intent:
        recommendation
    elif time intent:
        time
    elif date intent:
        date
    elif quote intent:
        quote
    elif joke intent:
        joke
    elif fact intent:
        fact
    elif greeting intent if implemented:
        greeting
    else:
        fallback
```

Exact precedence is defined in `COMMAND_SPEC.md`.

---

## 6. Data and State

Persistent storage is forbidden.

Allowed in-memory state:
- current user's name
- current command
- local game target/attempt count
- temporary perceptron inputs

State lifetime must not exceed the current process.

---

## 7. Dependency Boundary

Runtime dependency graph should terminate at the Python standard library.

```text
Veyra modules
   └── Python standard library
```

There should be no `requirements.txt` unless it intentionally documents that there are no third-party dependencies. Prefer simply stating this in README.

---

## 8. Testability Design

Where convenient, separate pure calculations from input/output wrappers:

- calculator arithmetic separated from terminal prompting
- recommendation accepts a test hour
- perceptron calculation separated from prompting

This is allowed because it preserves the simple architecture while improving confidence and explanation.

Do not redesign the whole program around test infrastructure.

---

## 9. Failure Model

Expected user errors should produce friendly messages and return control to the relevant loop.

Unexpected internal errors should not be swallowed silently. During development they should be visible enough to diagnose. Final user-facing behavior should remain stable for known invalid inputs.

---

## 10. Performance Model

All feature execution is local and small. The expected response time is effectively immediate. Do not introduce delays for aesthetics.
