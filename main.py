"""Coordinate Veyra's startup and command loop."""

from ai_concepts import perceptron_demo, recommend_activity
from calculator import get_calculation_response
from content import get_random_fact, get_random_joke, get_random_quote
from datetime_utils import get_current_date, get_current_time
from game import play_guessing_game
from greetings import (
    create_goodbye_message,
    create_welcome_message,
    get_user_name,
)
from help_menu import print_help


BANNER = "=== Veyra ==="
EXIT_COMMANDS = {"exit", "quit", "bye"}
TIME_COMMANDS = {"time", "current time", "what time is it"}
DATE_COMMANDS = {"date", "current date", "what is the date", "today's date"}
QUOTE_COMMANDS = {"quote", "motivate me"}
JOKE_COMMANDS = {"joke", "tell me a joke"}
FACT_COMMANDS = {"fact", "random fact"}
GAME_COMMANDS = {"game", "guess", "number game"}
HELP_COMMANDS = {"help", "commands", "what can you do"}
ACTIVITY_COMMANDS = {"activity", "recommend"}
PERCEPTRON_COMMANDS = {"perceptron", "neuron"}


def normalize_command(raw_command):
    """Normalize top-level input for Veyra's explicit routing rules."""
    return raw_command.strip().lower()


def run_assistant():
    """Run Veyra's startup sequence and main command loop."""
    print(BANNER)
    user_name = get_user_name()
    print(create_welcome_message(user_name))

    while True:
        command = normalize_command(input("You: "))

        if command in EXIT_COMMANDS:
            print(create_goodbye_message(user_name))
            break

        if not command:
            print("Veyra: I didn't get a command. Please type something.")
            continue

        if command in HELP_COMMANDS:
            print_help()
            continue

        if command == "calculate" or command.startswith("calculate "):
            print(get_calculation_response(command))
            continue

        if command in GAME_COMMANDS:
            play_guessing_game()
            continue

        if command in PERCEPTRON_COMMANDS:
            perceptron_demo()
            continue

        if command in ACTIVITY_COMMANDS:
            print(f"Veyra: {recommend_activity()}")
            continue

        if command in TIME_COMMANDS:
            print(f"Veyra: It's currently {get_current_time()}.")
            continue

        if command in DATE_COMMANDS:
            print(f"Veyra: Today is {get_current_date()}.")
            continue

        if command in QUOTE_COMMANDS:
            print(f"Veyra: {get_random_quote()}")
            continue

        if command in JOKE_COMMANDS:
            print(f"Veyra: {get_random_joke()}")
            continue

        if command in FACT_COMMANDS:
            print(f"Veyra: {get_random_fact()}")
            continue

        print(
            f"Veyra: {user_name}, I'm not sure I understood that command."
        )


if __name__ == "__main__":
    run_assistant()
