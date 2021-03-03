"""An brain_prime module."""

import random

from brain_games.games.constants import ROUNDS_COUNT
from brain_games.games.engine import start_engine


def is_prime(var):
    """Run a code."""
    if var < 2:
        return False
    length = round(var / 2)
    for num in range(2, length):
        if var % num == 0:
            return False
    return True


def play_game():
    """Run a code."""
    thepoint = 'Answer "yes" if given number is prime. Otherwise answer "no"..'
    questions_answers = []
    for num in range(ROUNDS_COUNT):
        question = random.randint(0, 100)
        right_answer = 'yes' if is_prime(question) else 'no'
        questions_answers.append([question, right_answer])
    start_engine(thepoint, questions_answers)
