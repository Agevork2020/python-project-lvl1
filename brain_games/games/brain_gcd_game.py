"""An brain_gcd module."""

import math
import random

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
    """
    Run a code.

    Returns:
        couple of question and answer
    """
    rand1 = random.randint(SPAN_START, SPAN_END)
    rand2 = random.randint(SPAN_START, SPAN_END)
    question = '{0} {1}'.format(rand1, rand2)
    right_answer = '{0}'.format(gcd(rand1, rand2))
    return (question, right_answer)
