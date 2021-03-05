"""An brain_prime module."""

import random

from brain_games.games.constants import ROUNDS_COUNT
from brain_games.games.engine import start_engine


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
    """Run a code."""
    thepoint = 'Answer "yes" if given number is prime. Otherwise answer "no"..'
    questions_answers = []
    for _ in range(ROUNDS_COUNT):
        question = random.randint(0, 100)
        right_answer = 'yes' if is_prime(question) else 'no'
        questions_answers.append([question, right_answer])
    start_engine(thepoint, questions_answers)
