"""Provide Veyra's number-guessing game logic."""

import random


MIN_NUMBER = 1
MAX_NUMBER = 20
MAX_ATTEMPTS = 5


def generate_target():
    """Return a random target within Veyra's documented game range."""
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def play_guessing_game(target=None):
    """Run one bounded guessing game and then return to the main loop."""
    if target is None:
        target = generate_target()

    print(
        f"Veyra: Guess a whole number from {MIN_NUMBER} to {MAX_NUMBER}."
    )
    print(f"Veyra: You have {MAX_ATTEMPTS} attempts.")

    attempts_used = 0
    while attempts_used < MAX_ATTEMPTS:
        raw_guess = input(
            f"You (attempt {attempts_used + 1}/{MAX_ATTEMPTS}): "
        ).strip()

        try:
            guess = int(raw_guess)
        except ValueError:
            print(
                "Veyra: Please enter a whole number. "
                "That did not use an attempt."
            )
            continue

        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print(
                f"Veyra: Enter a number from {MIN_NUMBER} to {MAX_NUMBER}. "
                "That did not use an attempt."
            )
            continue

        attempts_used += 1

        if guess == target:
            print(
                f"Veyra: Correct! You guessed it in {attempts_used} "
                f"attempt{'s' if attempts_used != 1 else ''}."
            )
            return

        if guess < target:
            print("Veyra: Try higher.")
        else:
            print("Veyra: Try lower.")

    print(f"Veyra: You're out of attempts. The number was {target}.")
