"""An brain_even module."""

import random

from brain_games.games.constants import ROUNDS_COUNT
from brain_games.games.engine import start_engine

THEPOINT = 'Answer "yes" if the number is even, otherwise answer "no"..'


def play_game():
    """Run a code."""
    questions_answers = []
    for _ in range(ROUNDS_COUNT):
        question = random.randint(-100, 100)
        right_answer = 'yes' if question % 2 == 0 else 'no'
        questions_answers.append([question, right_answer])
    start_engine(THEPOINT, questions_answers)
