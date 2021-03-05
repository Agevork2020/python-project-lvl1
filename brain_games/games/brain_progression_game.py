"""An brain_progression module."""

import random

from brain_games.games.constants import ROUNDS_COUNT
from brain_games.games.engine import start_engine

THEPOINT = 'What number is missing in the progression??'
SPAN_LENGTH_START = 5
SPAN_LENGTH_END = 15
SPAN_MAX_START = 30
SPAN_STEP_START = 2
SPAN_STEP_END = 10


def mk_question(rand_length, rand_hidden, rand_first, rand_step):
    """
    Run a code.

    Args:
        rand_length: length of кщц
        rand_hidden: index of hidden number
        rand_first: first number
        rand_step: step of the progression

    Returns:
        row
    """
    result1 = ''
    for _ in range(rand_length):
        number = '{0} '.format(rand_first + rand_step * _)
        if _ == rand_hidden:
            number = '... '
        result1 += number
    return str(result1)


def play_game():
    """Run a code."""
    questions_answers = []
    for _ in range(ROUNDS_COUNT):
        rand_length = random.randint(SPAN_LENGTH_START, SPAN_LENGTH_END)
        rand_hidden = random.randint(1, rand_length - 1)
        rand_first = random.randint(0, SPAN_MAX_START)
        rand_step = random.randint(SPAN_STEP_START, SPAN_STEP_END)
        question = mk_question(rand_length, rand_hidden, rand_first, rand_step)
        right_answer = '{0}'.format(rand_first + rand_step * rand_hidden)
        questions_answers.append([question, right_answer])
    start_engine(THEPOINT, questions_answers)
