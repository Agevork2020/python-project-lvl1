from brain_games.games.engine import startengine
from brain_games.games.constants import ROUNDS_COUNT
import random


def make_question(rand_length, rand_hidden, rand_first, rand_step):
    result1 = ''
    for i in range(rand_length):
        x = '{} '.format(rand_first + rand_step * i)
        if i == rand_hidden:
            x = "... "
        result1 += x
    return str(result1)


def playgame():
    thepoint = 'What number is missing in the progression??'
    questions_answers = []
    for num in range(ROUNDS_COUNT):
        rand_length = random.randint(5, 15)
        rand_hidden = random.randint(1, rand_length - 1)
        rand_first = random.randint(0, 30)
        rand_step = random.randint(2, 10)
        question = make_question(rand_length, rand_hidden, rand_first, rand_step)
        right_answer = '{}'.format(rand_first + rand_step * rand_hidden)
        questions_answers.append([question, right_answer])
    startengine(thepoint, questions_answers)
