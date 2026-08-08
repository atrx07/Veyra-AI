"""Coordinate Veyra's startup and command loop."""

from greetings import (
    create_goodbye_message,
    create_welcome_message,
    get_user_name,
)


BANNER = "=== Veyra ==="
EXIT_COMMANDS = {"exit", "quit", "bye"}


def normalize_command(raw_command):
    """Normalize top-level input for Veyra's explicit routing rules."""
    return raw_command.strip().lower()


def run_assistant():
    """Run Veyra's startup sequence and Phase 1 command loop."""
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

        print(
            f"Veyra: {user_name}, I'm not sure I understood that command."
        )


if __name__ == "__main__":
    run_assistant()
