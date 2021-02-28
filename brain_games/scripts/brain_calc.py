from brain_games.engine import startengine
from brain_games.constants import ROUNDS_COUNT
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
    thepoint = 'What is the result of the expression?'

    operators = ['*', '-', '+']
    questions_answers = []
    for i in range(ROUNDS_COUNT):
        x = random.randint(-30, 30)
        y = random.randint(-30, 30)
        randKey = random.choice(operators)
        operator = operators[randKey]
        question = "{} {} {}".format(x, operator, y)
        rightAnswer = str(solving(x, y, operator))
        questions_answers[i] = [question, rightAnswer]

    startengine(thepoint, questions_answers)