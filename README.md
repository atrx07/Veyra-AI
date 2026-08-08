# Veyra

Veyra is an offline, rule-based Python terminal assistant for the internship
assignment **Virtual AI Assistant (Mini Alexa)**.

## Requirements

- Python 3.x
- No third-party packages
- No internet connection

## Current status

Phase 2 date and time reporting is complete. Veyra greets the user, captures a
session-only name, reports the machine's local date and time, handles blank or
unknown commands, and exits cleanly with a personalized goodbye. Later feature
commands are not implemented yet.

## Run

```bash
python main.py
```

## Current commands

- `date`, `current date`, `what is the date`, `today's date`
- `time`, `current time`, `what time is it`
- `exit`, `quit`, `bye`

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
