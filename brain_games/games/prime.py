"""A prime module."""

import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no"..'


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
    length = round(number / 2) + 1
    for num in range(2, length):
        if number % num == 0:
            return False
    return True


def generate_question_answer():
    """
    Run a code.

    Returns:
        couple of question and answer
    """
    question = random.randint(0, 100)
    right_answer = 'yes' if is_prime(question) else 'no'
    return question, right_answer
