"""An brain_prime module."""

import random

THEPOINT = 'Answer "yes" if given number is prime. Otherwise answer "no"..'


def is_prime(number):
    """
    Run a code.

    Args:
        number: any number

    Returns:
        true or false
    """
    if number < 2:
        return False
    length = round(number / 2)
    for _ in range(2, length):
        if number % _ == 0:
            return False
    return True


def play_game():
    """
    Run a code.

    Returns:
        couple of question and answer
    """
    question = random.randint(0, 100)
    right_answer = 'yes' if is_prime(question) else 'no'
    return (question, right_answer)
