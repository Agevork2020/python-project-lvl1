"""An brain_gcd module."""

import math
import random

from brain_games.games.constants import ROUNDS_COUNT
from brain_games.games.engine import start_engine

THEPOINT = 'Find the greatest common divisor of given numbers..'
SPAN_START = 0
SPAN_END = 50


def gcd(variable1, variable2):
    """
    Run a code.

    Args:
        variable1: x
        variable2: y

    Returns:
        gcd
    """
    return math.gcd(variable1, variable2)


def play_game():
    """Run a code."""
    questions_answers = []
    for _ in range(ROUNDS_COUNT):
        rand1 = random.randint(SPAN_START, SPAN_END)
        rand2 = random.randint(SPAN_START, SPAN_END)
        question = '{0} {1}'.format(rand1, rand2)
        right_answer = '{0}'.format(gcd(rand1, rand2))
        questions_answers.append([question, right_answer])
    start_engine(THEPOINT, questions_answers)
