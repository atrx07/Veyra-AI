# PROJECT.md — Veyra

## 1. Product Summary

**Veyra** is an offline, text-based virtual assistant built with Python fundamentals. It responds to a small set of user intents through explicit rule-based logic and demonstrates introductory AI, ML, and DL vocabulary without using trained models.

This repository implements the internship assignment formally titled **"Virtual AI Assistant (Mini Alexa)"** in the supplied PRD. "Veyra" is the repository/product name chosen for presentation; the assignment requirements remain unchanged.

---

## 2. Problem Being Solved

The internship assignment is designed to bridge the gap between knowing isolated Python concepts and building a complete, demonstrable application. The target deliverable should show:

- program structure
- functions with clear responsibilities
- loops and conditionals
- string processing
- state held during one process/session
- standard-library use
- basic exception handling
- manual testing discipline
- the ability to explain rule-based AI and simplified ML/DL analogies

The project is therefore primarily a structured Python application, not a real machine-learning system.

---

## 3. Product Vision

Create a compact terminal assistant that feels coherent, friendly, and reliable while remaining completely offline and technically faithful to the beginner-level PRD.

Veyra should demonstrate that a small rule-based system can still be engineered cleanly: predictable routing, explicit errors, modular feature ownership, testable logic, and honest documentation.

---

## 4. Primary Goals

1. Implement all 14 PRD functional requirements.
2. Support at least 10 meaningful user-input categories.
3. Run on standard Python 3 without third-party dependencies.
4. Remain fully offline.
5. Use modular, readable code with one main responsibility per function.
6. Handle invalid user input without terminating unexpectedly.
7. Demonstrate rule-based decision-making.
8. Demonstrate a fixed-weight perceptron calculation.
9. Provide documentation that clearly distinguishes analogy from real ML/DL.
10. Pass a manual acceptance suite of at least 20 inputs.

---

## 5. Non-Goals

Veyra is not intended to be:

- a natural-language model
- a chatbot powered by an API
- a trainable machine-learning application
- a persistent personal assistant
- a voice assistant
- a web application
- a desktop GUI
- a recommendation model
- a production automation platform

If an enhancement would move Veyra toward any of these areas, it belongs outside the current internship scope.

---

## 6. Target Users

### Intern developer

The primary developer who builds and explains the project.

### Program mentor

The reviewer who checks correctness, code structure, testing, and conceptual understanding.

### Simulated terminal user

A person using the app interactively to test its commands and behavior.

---

## 7. Supported Feature Groups

### Session
- greeting
- name capture
- in-session name reuse
- graceful goodbye

### Utilities
- current date
- current time
- calculator

### Entertainment
- motivational quotes
- jokes
- facts

### Interactive
- number-guessing game

### Discovery / control
- help menu
- exit aliases
- fallback handling

### Educational AI concepts
- rule-based activity recommendation
- simplified perceptron

---

## 8. Product Personality

The PRD asks for friendly conversational behavior, not a specific persona. Veyra should therefore use a light, helpful terminal tone without elaborate roleplay.

Example style:

```text
Veyra: Nice to meet you, Alex. Type 'help' to see what I can do.
You: time
Veyra: It's currently 06:42 PM.
```

Avoid claims such as:

- "I learned your preferences"
- "My neural network thinks..."
- "I searched..."
- "I remember you from last time"

Those claims would misrepresent the actual system.

---

## 9. Runtime Assumptions

- Python 3.x is installed.
- A terminal or command prompt is available.
- No internet connection is required.
- No environmental secrets or API keys are required.
- All state is lost when the process exits.

---

## 10. Delivery Shape

Expected application files:

```text
main.py
greetings.py
datetime_utils.py
calculator.py
content.py
game.py
ai_concepts.py
help_menu.py
README.md
```

Expected governance/reference files:

```text
AGENTS.md
PROJECT.md
REQUIREMENTS.md
ARCHITECTURE.md
COMMAND_SPEC.md
TESTING.md
STEPS.md
NEXTSTEPS.md
STATUS.md
DECISIONS.md
docs/PRD_TRACEABILITY.md
docs/AI_ML_DL_REFERENCE.md
```

---

## 11. Quality Bar

The implementation should feel deliberate rather than large.

Good Veyra code is:

- easy to read
- easy to explain
- easy to run
- explicit about errors
- deterministic where appropriate
- random only where the PRD requires variation
- honest about its AI limitations
- free of unnecessary dependencies

A smaller implementation that passes every requirement is preferable to a larger implementation with extra features.
