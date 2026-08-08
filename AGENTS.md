# AGENTS.md — Veyra Agent Governance

## 1. Purpose

This file is the primary execution contract for any coding agent working on **Veyra**. It converts the internship Product Requirements Document (PRD) into implementation constraints, delivery rules, and agent behavior.

The agent must read this file before making changes. It must then read, in order:

1. `PROJECT.md`
2. `REQUIREMENTS.md`
3. `ARCHITECTURE.md`
4. `COMMAND_SPEC.md`
5. `TESTING.md`
6. `STEPS.md`
7. `STATUS.md`
8. `NEXTSTEPS.md`
9. `DECISIONS.md`
10. `docs/PRD_TRACEABILITY.md`
11. `docs/AI_ML_DL_REFERENCE.md`

If documents appear to conflict, use this precedence order:

1. The internship PRD supplied by the project owner
2. `AGENTS.md`
3. `REQUIREMENTS.md`
4. `ARCHITECTURE.md`
5. Other project governance files
6. Existing code

Never silently resolve a true ambiguity by inventing a new product requirement. Record the choice in `DECISIONS.md` and keep it within the PRD's allowed scope.

---

## 2. Project Identity

- Product name: **Veyra**
- Assignment reference: **Virtual AI Assistant (Mini Alexa)**
- Assignment project code in source PRD: **AI-INT-P1-VAA**
- Application type: Offline Python command-line assistant
- Runtime: Python 3.x
- Network requirement: None
- Persistence: None
- GUI: None
- Voice/audio: None
- Real ML model: None
- External AI service: None

The assignment title may be referenced in documentation for traceability, but the application and repository-facing product name is **Veyra**.

---

## 3. Scope Lock — Non-Negotiable

Veyra is intentionally a beginner-level, rule-based terminal assistant. Do **not** turn it into a modern LLM assistant.

### The agent MUST NOT add

- OpenAI, Gemini, Anthropic, Hugging Face, or any other external AI/API integration
- HTTP/network calls of any kind
- Real machine-learning training or inference
- TensorFlow, PyTorch, Keras, scikit-learn, NumPy, pandas, OpenCV, or similar third-party data/AI libraries
- A database
- File-backed persistence or saved user profiles
- Conversation history saved across runs
- Speech recognition
- Text-to-speech
- Audio input/output
- GUI, web UI, Streamlit, Flask, FastAPI, Django, Electron, or mobile UI
- Multi-user behavior
- Threads/process-based concurrency
- Cloud services
- Telemetry or analytics that requires network or persistent storage
- Package dependencies merely for convenience
- Artificial delays, typing animations, sleeps, or blocking decorative behavior

### The agent MAY use

Only Python standard-library facilities appropriate to the specification, including examples such as:

- `datetime`
- `random`
- `re` if useful for safe local parsing
- standard exceptions
- `unittest` for optional automated checks

The finished program must remain usable completely offline with a normal Python 3 installation.

---

## 4. Required Functional Surface

All PRD functional requirements FR-01 through FR-14 are required for the final submission, even where the PRD labels FR-13 and FR-14 as "Should". The PRD success criteria explicitly require all 14 functional requirements to be demonstrable.

The final program must implement:

1. Startup greeting
2. User-name capture
3. Session-only use of the user's name
4. Current date
5. Current time
6. Basic arithmetic: add, subtract, multiply, divide
7. Random motivational quote
8. Random joke
9. Random fact
10. Number-guessing game with limited attempts and higher/lower hints
11. Help menu
12. Graceful exit
13. Friendly fallback for unrecognized input
14. Rule-based recommendation demo
15. Simplified perceptron demo using fixed weights and bias

The distinction between items 1 and 2 above comes from the same startup/name requirements; all PRD IDs remain authoritative in `REQUIREMENTS.md`.

---

## 5. Implementation Philosophy

### 5.1 Keep it small, explicit, teachable

The mentor should be able to understand the project by reading the files in a few minutes. Prefer clear functions over abstractions.

Avoid:

- class hierarchies when functions are sufficient
- dependency injection frameworks
- service/repository/controller layers
- plugin systems
- command registries requiring metaprogramming
- decorators used only for cleverness
- abstract factories
- elaborate configuration systems

This is not a production SaaS application. Code quality matters; architectural ceremony does not.

### 5.2 Modular, not monolithic

Use the PRD-recommended module layout unless a documented, simpler equivalent is justified:

```text
veyra/
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

Governance files remain at repository root. Do not create a package hierarchy unless the existing repository structure requires it.

### 5.3 Safe arithmetic

Never use Python `eval()` or `exec()` for calculator input. Parse the supported expression deliberately and handle invalid values explicitly.

### 5.4 Session state only

The user name may live in a local variable and be passed to functions. Restarting the process must reset it.

### 5.5 Explicit rule-based intent routing

The main interaction loop should follow:

`input -> normalize -> identify intent -> call feature -> print response -> repeat`

The routing logic should be visible and explainable. A direct `if/elif` chain is acceptable and aligned with the PRD.

---

## 6. User Experience Rules

Veyra should be friendly and readable without pretending to possess capabilities it does not have.

- Prefix assistant output consistently with `Veyra:` where practical.
- Use the user's name naturally in at least two later responses, satisfying the acceptance criterion.
- Keep prompts concise.
- Help output must list every supported user-facing feature.
- Unknown commands must never crash the loop.
- Invalid calculator/game/perceptron inputs must be recoverable.
- Exit aliases should include at least `exit`, `quit`, and `bye`.
- Do not claim Veyra "learned" the user name. Documentation may explain the PRD's learning analogy, but UI copy should remain truthful.

---

## 7. Error-Handling Rules

The program must survive foreseeable bad input.

Mandatory cases:

- non-numeric calculator operands
- unsupported arithmetic operator
- malformed calculator expression
- division by zero
- non-numeric guessing-game input
- guesses outside the documented range
- non-numeric perceptron input
- blank top-level command
- unrecognized command

Errors should be handled closest to the feature that owns them. `main.py` may include a defensive top-level exception boundary, but it must not be used to hide poor feature-level handling.

Do not write bare `except:` blocks.

---

## 8. Source-of-Truth Rules for Content

The PRD requires predefined lists for quotes, jokes, and facts but does not prescribe exact entries.

Implementation-selected content must:

- be safe for general audiences
- be short enough for terminal output
- not require attribution unless the README provides it
- avoid fabricated scientific claims presented as facts

Where an exact value is not specified by the PRD (for example guessing-game range, attempt limit, perceptron weights, or activity time bands), the agent may use a reasonable value only if it is:

1. centralized as a named constant when appropriate,
2. explained in code or documentation, and
3. recorded in `DECISIONS.md` if it meaningfully affects behavior.

The PRD sample uses a guessing range of 1–20 and 5 attempts. Prefer those sample values for consistency unless the owner directs otherwise.

---

## 9. Testing Contract

Before marking implementation complete:

- run the program successfully
- execute every FR path manually
- complete at least 20 documented manual test inputs
- include invalid-input tests
- verify content randomness by repeated requests
- verify user-name reuse in at least two later responses
- verify date and time are based on the running machine
- verify divide-by-zero is non-fatal
- verify guessing-game higher/lower feedback
- verify attempt limit
- verify help contains every supported command
- verify fallback keeps the program alive
- verify exit terminates cleanly
- verify recommendation output can differ by time condition
- verify perceptron output is binary (`0` or `1`)

`TESTING.md` defines the canonical test matrix.

Automated tests are optional. If added, use the standard library unless the project owner explicitly changes scope. Automated tests do not replace the manual acceptance pass required by the PRD.

---

## 10. Documentation Contract

The final repository must have a `README.md` that includes at minimum:

- Veyra name and one-line description
- note that it implements the internship "Virtual AI Assistant (Mini Alexa)" assignment
- requirements: Python 3.x only
- offline/no-dependency statement
- run command
- supported commands/features
- module overview
- AI/ML/DL concept explanation at an appropriate beginner level
- limitations / explicit non-capabilities
- testing summary

Major functions should use clear docstrings or comments where they explain an assignment concept. Avoid comment spam that merely repeats obvious code.

---

## 11. Change Discipline

For each meaningful implementation step:

1. Read `NEXTSTEPS.md`.
2. Implement one coherent slice.
3. Run relevant tests.
4. Update `STATUS.md`.
5. Update `NEXTSTEPS.md` with the next concrete action.
6. If behavior or architecture changed, update the relevant governance file.
7. If a new non-trivial decision was made, append it to `DECISIONS.md`.

Do not mark a requirement complete because code exists. Mark it complete only after its acceptance path has been exercised.

---

## 12. Definition of Done

Veyra is done only when all of the following are true:

- FR-01 through FR-14 are implemented
- all non-functional requirements are respected
- no forbidden technology has been introduced
- at least 20 manual test inputs have passed
- invalid inputs do not crash the program
- README is complete
- `STATUS.md` shows all required items verified
- the project can be explained verbally without relying on jargon or pretending its rule-based logic is trained ML
- a clean Python 3 environment can run it offline

Until those conditions are met, the agent must leave the project status as incomplete.
