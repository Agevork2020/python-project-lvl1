from brain_games.games.engine import startengine
from brain_games.games.constants import ROUNDS_COUNT
import random


def isPrime(x):
    if x < 2:
        return False
    length = x / 2
    for i in range(2, length):
        if x % i == 0:
            return False
    return True


def playgame():
    thepoint = 'Answer "yes" if given number is prime. Otherwise answer "no"..'

    questions_answers = []
    for i in range(ROUNDS_COUNT):
        question = random.randint(0, 100)
        right_answer = 'yes' if isPrime(question) else 'no'
        questions_answers.append([question, right_answer])

    startengine(thepoint, questions_answers)