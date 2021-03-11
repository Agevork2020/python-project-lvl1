"""An even module."""

import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no"..'


def generate_question_answer():
    """
    Run a code.

    Returns:
        couple of question and answer
    """
    question = random.randint(-100, 100)
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return question, right_answer
