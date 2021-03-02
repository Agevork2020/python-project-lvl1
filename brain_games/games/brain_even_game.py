from brain_games.games.engine import startengine
from brain_games.games.constants import ROUNDS_COUNT
import random


def playgame():
    thepoint = 'Answer "yes" if the number is even, otherwise answer "no"..'
    questions_answers = []
    for i in range(1, ROUNDS_COUNT):
        question = random.randint(-100, 100)
        right_answer = 'yes' if question % 2 == 0 else 'no'
        questions_answers[i] = [question, right_answer]

    startengine(thepoint, questions_answers)