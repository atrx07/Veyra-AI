# Veyra

Veyra is an offline, rule-based Python terminal assistant for the internship
assignment **Virtual AI Assistant (Mini Alexa)**.

## Requirements

- Python 3.x
- No third-party packages
- No internet connection

## Current status

Phase 9 name reuse and UX polish is complete. Veyra greets the user,
captures a session-only name, reports the machine's local date and time,
performs safe basic arithmetic, selects local quotes, jokes, and facts, runs a
bounded guessing game, recommends an activity through explicit time rules,
demonstrates a fixed perceptron calculation, lists every required feature,
handles invalid input, and exits cleanly with a personalized goodbye. Final
README completion and acceptance remain pending.

## Roadmap

| Phase | Scope | Status |
|---:|---|---|
| 0 | Repository bootstrap | Complete |
| 1 | Session startup, fallback, and exit | Complete |
| 2 | Current local date and time | Complete |
| 3 | Safe four-operator calculator | Complete |
| 4 | Random quotes, jokes, and facts | Complete |
| 5 | Number-guessing game | Complete |
| 6 | Complete help menu | Complete |
| 7 | Rule-based activity recommendation | Complete |
| 8 | Fixed-weight perceptron demonstration | Complete |
| 9 | Name reuse and UX polish | Complete |
| 10 | Final README documentation | Pending |
| 11 | Full acceptance and scope audit | Pending |

## Run

```bash
python main.py
```

## Current commands

- `date`, `current date`, `what is the date`, `today's date`
- `time`, `current time`, `what time is it`
- `calculate <number> <+|-|*|/> <number>`
- `quote`, `motivate me`
- `joke`, `tell me a joke`
- `fact`, `random fact`
- `game`, `guess`, `number game`
- `activity`, `recommend`
- `perceptron`, `neuron`
- `help`, `commands`, `what can you do`
- `exit`, `quit`, `bye`

Calculator example:

```text
calculate 12 + 8
```

The calculator accepts signed integers and decimals. It does not use Python
`eval()` or `exec()`.

Quotes, jokes, and facts are selected randomly from predefined local
collections. No network lookup is performed.

The guessing game chooses a random whole number from 1 through 20 and allows
five valid attempts. Non-numeric and out-of-range guesses do not consume an
attempt.

The activity command uses handwritten time-of-day conditions. It does not use
a trained recommendation model or retain user preferences.

The perceptron demo accepts two numeric inputs, applies fixed weights
`(0.6, -0.4)` and bias `-0.1`, then uses a step activation to return `0` or
`1`. It does not train or update its values.

Other commands receive a friendly fallback until their documented
implementation phase is complete.

## Module layout

- `main.py`: startup and command-loop coordination
- `greetings.py`: greeting and session-only name handling
- `datetime_utils.py`: local date and time helpers
- `calculator.py`: safe arithmetic parsing and calculation
- `content.py`: predefined quotes, jokes, and facts
- `game.py`: number-guessing game
- `ai_concepts.py`: rule-based recommendation and perceptron demonstrations
- `help_menu.py`: supported-command help text

The README will be completed with commands, examples, concept explanations,
limitations, and final testing evidence during the documentation phase.
