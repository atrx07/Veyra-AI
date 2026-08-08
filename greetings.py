"""Provide Veyra's startup greeting and session-only name handling."""


def get_user_name():
    """Greet the user and return the first non-blank name they enter."""
    print("Veyra: Hello! I'm Veyra. What's your name?")

    while True:
        user_name = input("You: ").strip()
        if user_name:
            return user_name

        print("Veyra: Please enter a name so I know what to call you.")


def create_welcome_message(user_name):
    """Return a friendly welcome that uses the current session name."""
    return f"Veyra: Nice to meet you, {user_name}."


def create_goodbye_message(user_name):
    """Return a personalized goodbye for the current session."""
    return f"Veyra: Goodbye, {user_name}!"
