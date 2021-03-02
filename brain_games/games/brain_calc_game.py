from brain_games.games.engine import startengine
from brain_games.games.constants import ROUNDS_COUNT
import random


def solving(x, y, operator):
    if operator == '*':
        return x * y
    if operator == '-':
        return x - y
    if operator == '+':
        return x + y
    raise ValueError("Unknown operator: ", operator, "!")


def playgame():
    thepoint = 'What is the result of the expression??'

    operators = ['*', '-', '+']
    questions_answers = []
    for i in range(ROUNDS_COUNT):
        x = random.randint(-30, 30)
        y = random.randint(-30, 30)
        operator = random.choice(operators)
        question = "{} {} {}".format(x, operator, y)
        right_answer = '{}'.format(solving(x, y, operator))
        questions_answers.append([question, right_answer])

    startengine(thepoint, questions_answers)