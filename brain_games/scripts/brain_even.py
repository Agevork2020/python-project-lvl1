from brain_games.engine import startengine
from brain_games.constants import ROUNDS_COUNT
import random


def playGame():
    thepoint = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions_answers = []
    for i in range(ROUNDS_COUNT):
        question = random.randint(-100, 100)
        rightAnswer = 'yes' if question % 2 == 0 else 'no'
        questions_answers[i] = [question, rightAnswer]

    startengine(thepoint, questions_answers)