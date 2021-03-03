"""An brain_calc module."""

import random

from brain_games.games.constants import ROUNDS_COUNT
from brain_games.games.engine import start_engine

THEPOINT = 'What is the result of the expression??'
SPAN_START = -30
SPAN_END = 30
OPERATORS = ('*', '-', '+')


def solving(variable1, variable2, operator):
    """Run a code."""
    if operator == '*':
        return variable1 * variable2
    if operator == '-':
        return variable1 - variable2
    if operator == '+':
        return variable1 + variable2
    raise ValueError("Unknown operator: ", operator, "!")


def play_game():
    """Run a code."""
    questions_answers = []
    for _ in range(ROUNDS_COUNT):
        variable1 = random.randint(SPAN_START, SPAN_END)
        variable2 = random.randint(SPAN_START, SPAN_END)
        operator = random.choice(OPERATORS)
        question = "{} {} {}".format(variable1, operator, variable2)
        right_answer = '{}'.format(solving(variable1, variable2, operator))
        questions_answers.append([question, right_answer])
    start_engine(THEPOINT, questions_answers)
