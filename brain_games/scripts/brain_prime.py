from brain_games.engine import startengine
from brain_games.constants import ROUNDS_COUNT
import random


def isPrime(x):
    if x < 2:
        return False
    length = x / 2
    lis = [2:length]
    for i in range(lis):
        if x % i == 0:
            return False
    return True


def playgame():
    thepoint = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    questions_answers = []
    for i in range(ROUNDS_COUNT):
        question = random.randint(0, 100)
        rightAnswer = 'yes' if isPrime(question) else 'no'
        questions_answers[i] = [question, rightAnswer]

    startengine(thepoint, questions_answers)
