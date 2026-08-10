# Veyra

Veyra is a small, offline, rule-based Python terminal assistant. It implements
the internship assignment **Virtual AI Assistant (Mini Alexa)**, project code
**AI-INT-P1-VAA**, while using Veyra as its application name.

This project was created by **Arppith Andrews**
([@atrx07](https://github.com/atrx07)) as part of the **AI internship by
Internmo**.

The project demonstrates Python fundamentals, explicit command routing, input
validation, and beginner-level AI/ML/DL concepts without using a trained model
or external service.

## Author and internship

- **Author:** Arppith Andrews
- **GitHub:** [@atrx07](https://github.com/atrx07)
- **Program:** AI internship by Internmo
- **Submission:** Virtual AI Assistant (Mini Alexa), project AI-INT-P1-VAA

Veyra is Arppith's implementation and presentation name for this
Internmo AI internship assignment.

## Requirements

- Python 3.x
- A terminal or command prompt
- No third-party packages
- No internet connection, API key, account, or environment variable

All runtime functionality uses only the Python standard library.

## Run

Open a terminal in the repository directory and run:

```bash
python main.py
```

On systems where Python 3 uses a separate command, run:

```bash
python3 main.py
```

Veyra will greet you, ask for your name, and then wait for commands. The name
is kept only in memory and is discarded when the process exits.

## Features and commands

| Feature | Commands | Behavior |
|---|---|---|
| Current date | `date`, `current date`, `what is the date`, `today's date` | Shows the machine's local date. |
| Current time | `time`, `current time`, `what time is it` | Shows the machine's local time. |
| Calculator | `calculate <number> <operator> <number>` | Supports `+`, `-`, `*`, and `/`. |
| Motivation | `quote`, `motivate me` | Selects a random local quote. |
| Joke | `joke`, `tell me a joke` | Selects a random local joke. |
| Fact | `fact`, `random fact` | Selects a random local fact. |
| Guessing game | `game`, `guess`, `number game` | Starts a five-attempt game using numbers 1 through 20. |
| Activity suggestion | `activity`, `recommend` | Uses explicit time-of-day rules to suggest an activity. |
| Perceptron demo | `perceptron`, `neuron` | Runs a fixed-weight educational calculation. |
| Help | `help`, `commands`, `what can you do` | Lists the supported features. |
| Exit | `exit`, `quit`, `bye` | Ends the session with a personalized goodbye. |

Unknown or blank commands produce a friendly message and leave the assistant
running.

### Calculator example

```text
You: calculate 12 + 8
Veyra: The result is 20.
```

The calculator accepts signed integers and decimals in the documented
space-delimited format. It parses the supported operators directly and never
uses Python `eval()` or `exec()`. Invalid numbers, malformed expressions,
unsupported operators, and division by zero are handled without ending the
session.

### Guessing-game rules

The game chooses a random whole number from 1 through 20 and permits five valid
guesses. It gives higher/lower hints after wrong guesses. Non-numeric and
out-of-range entries display guidance and do not consume an attempt.

### Perceptron calculation

The demo asks for two numeric inputs, applies fixed weights `(0.6, -0.4)` and
bias `-0.1`, and returns `1` when the weighted sum is greater than zero or `0`
otherwise. The values never train or update.

## How the AI, ML, and DL ideas map to Veyra

### Artificial intelligence: explicit rules

Veyra normalizes each command and checks it against rules written by the
developer. For example, `time` routes to the time helper and `joke` routes to
the joke helper. This demonstrates rule-based intent routing, not natural
language understanding.

The activity feature is another rule-based example: the current hour is placed
into a handwritten morning, afternoon, evening, or night branch. The selected
suggestion is deterministic for that time band.

### Machine learning: analogy only

Some behavior resembles the role of ML systems without using ML. Mapping an
hour to an activity resembles classification, and selecting predefined content
resembles recommendation. In Veyra those choices come from fixed conditions or
Python's local random selection; no examples, dataset, or parameters are
learned. The user's name is simply a session variable, not learned memory.

### Deep learning: arithmetic demonstration only

The perceptron demonstrates inputs, weights, bias, a weighted sum, and a step
activation. This is a tiny one-way calculation inspired by an artificial
neuron. It has no dataset, loss function, backpropagation, optimizer, epochs,
or training loop, so it is not a trained neural network.

## Module layout

- `main.py`: startup, command normalization, routing, and loop coordination
- `greetings.py`: greeting, session-only name capture, and goodbye text
- `datetime_utils.py`: machine-local date and time formatting
- `calculator.py`: safe expression parsing and four arithmetic operations
- `content.py`: predefined quotes, jokes, facts, and random selection
- `game.py`: bounded number-guessing game and input validation
- `ai_concepts.py`: activity rules and fixed perceptron calculation
- `help_menu.py`: complete user-facing command list

The modules remain deliberately small and use only Python's standard library.

## Limitations and non-capabilities

Veyra deliberately:

- recognizes only documented commands and modest aliases
- does not understand unrestricted natural language
- does not use an LLM, trained ML model, external AI service, or external data
- does not access the network, browse the web, or call APIs
- does not save names, preferences, or conversation history between sessions
- does not provide voice, audio, GUI, web, mobile, database, or multi-user features
- does not train or improve from user input

These limits keep the program faithful to the beginner-level offline PRD.

## Testing

All 14 functional requirements passed the final 32-case manual matrix on
2026-08-08 using Python 3.14.6 on Windows 11. Coverage included invalid
calculator, game, perceptron, blank, and unknown inputs; content variation;
name reuse; date/time; help; fallback; and all exit aliases.

The final module-import, dependency, scope, portability, maintainability,
performance, help, documentation, and clean-terminal run audits also passed.
The final acceptance summary is included here so the submitted documentation
remains self-contained.

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
| 10 | Final README documentation | Complete |
| 11 | Full acceptance and scope audit | Complete |
