from brain_games.engine import startengine
from brain_games.constants import ROUNDS_COUNT
import random
import math


def gcd(x, y):
        return math.gcd(y, x)


def playgame():
    thepoint = 'Find the greatest common divisor of given numbers..'

    questions_answers = []
    for i in range(ROUNDS_COUNT):
        rand1 = random.randint(0, 50)
        rand2 = random.randint(0, 50)
        question = "{} {}".format(rand1, rand2)
        rightAnswer = str(gcd(rand1, rand2))
        questions_answers[i] = [question, rightAnswer]

    startengine(thepoint, questions_answers)
