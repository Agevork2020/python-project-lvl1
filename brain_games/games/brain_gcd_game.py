from brain_games.games.engine import startengine
from brain_games.games.constants import ROUNDS_COUNT
import random
import math


def gcd(variable1, variable2):
    return math.gcd(variable1, variable2)


def playgame():
    thepoint = 'Find the greatest common divisor of given numbers..'
    questions_answers = []
    for num in range(ROUNDS_COUNT):
        span_start = 0
        span_end = 50
        rand1 = random.randint(span_start, span_end)
        rand2 = random.randint(span_start, span_end)
        question = "{} {}".format(rand1, rand2)
        right_answer = '{}'.format(gcd(rand1, rand2))
        questions_answers.append([question, right_answer])
    startengine(thepoint, questions_answers)
