"""A calc module."""

import random

RULE = 'What is the result of the expression?'
SPAN_START = -30
SPAN_END = 30
OPERATORS = ('*', '-', '+')


def solve(variable1, variable2, operator):
    """
    Run a code.

    Args:
        variable1: x
        variable2: y
        operator: math operator

    Returns:
        result of operation
    """
    if operator == '*':
        return variable1 * variable2
    if operator == '-':
        return variable1 - variable2
    return variable1 + variable2


def generate_question_answer():
    """
    Run a code.

    Returns:
        couple of question and answer
    """
    variable1 = random.randint(SPAN_START, SPAN_END)
    variable2 = random.randint(SPAN_START, SPAN_END)
    operator = random.choice(OPERATORS)
    question = '{0} {1} {2}'.format(variable1, operator, variable2)
    right_answer = '{0}'.format(solve(variable1, variable2, operator))
    return question, right_answer
