"""Provide help text for Veyra's supported commands."""


HELP_ITEMS = (
    ("time", "Show the current local time."),
    ("date", "Show the current local date."),
    ("calculate 12 + 8", "Add, subtract, multiply, or divide."),
    ("quote", "Show a random motivational quote."),
    ("joke", "Tell a random general-audience joke."),
    ("fact", "Show a random fact."),
    ("game", "Play the five-attempt number-guessing game."),
    ("activity / recommend", "Get a rule-based activity suggestion."),
    ("perceptron / neuron", "Run the fixed-weight perceptron demo."),
    ("help", "Show this command list."),
    ("exit / quit / bye", "End the current Veyra session."),
)


def get_help_text(user_name=None):
    """Return the complete formatted help menu."""
    if user_name:
        heading = f"Veyra: {user_name}, here's what I can do:"
    else:
        heading = "Veyra: Here's what I can do:"

    lines = [heading]
    for command, description in HELP_ITEMS:
        lines.append(f"  {command:<24} - {description}")
    return "\n".join(lines)


def print_help(user_name=None):
    """Print every supported user-facing command and its description."""
    print(get_help_text(user_name))
