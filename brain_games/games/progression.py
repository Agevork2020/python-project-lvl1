"""A progression module."""

import random

RULE = 'What number is missing in the progression?'
SPAN_LENGTH_START = 7
SPAN_LENGTH_END = 15
SPAN_MAX_START = 30
SPAN_STEP_START = 2
SPAN_STEP_END = 10


def make_question(length, hidden, first, step):
    """
    Run a code.

    Args:
        length: length of кщц
        hidden: index of hidden number
        first: first number
        step: step of the progression

    Returns:
        row
    """
    result1 = ''
    for num in range(length):
        number = '{0} '.format(first + step * num)
        if num == hidden:
            number = '.. '
        result1 += number
    return str(result1)


def generate_question_answer():
    """
    Run a code.

    Returns:
        couple of question and answer
    """
    length = random.randint(SPAN_LENGTH_START, SPAN_LENGTH_END)
    hidden_index = random.randint(1, length - 1)
    first = random.randint(0, SPAN_MAX_START)
    step = random.randint(SPAN_STEP_START, SPAN_STEP_END)
    question = make_question(length, hidden_index, first, step)
    right_answer = '{0}'.format(first + step * hidden_index)
    return question, right_answer
