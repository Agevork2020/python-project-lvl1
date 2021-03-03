import random
from brain_games.games.constants import ROUNDS_COUNT
from brain_games.games.engine import startengine


def solving(variable1, variable2, operator):
    if operator == '*':
        return variable1 * variable2
    if operator == '-':
        return variable1 - variable2
    if operator == '+':
        return variable1 + variable2
    raise ValueError("Unknown operator: ", operator, "!")


def playgame():
    thepoint = 'What is the result of the expression??'
    span_start = -30
    span_end = 30
    operators = ['*', '-', '+']
    questions_answers = []
    for num in range(ROUNDS_COUNT):
        variable1 = random.randint(span_start, span_end)
        variable2 = random.randint(span_start, span_end)
        operator = random.choice(operators)
        question = "{} {} {}".format(variable1, operator, variable2)
        right_answer = '{}'.format(solving(variable1, variable2, operator))
        questions_answers.append([question, right_answer])
    startengine(thepoint, questions_answers)
