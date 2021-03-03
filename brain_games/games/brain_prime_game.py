import random
from brain_games.games.constants import ROUNDS_COUNT
from brain_games.games.engine import startengine


def isPrime(var):
    if var < 2:
        return False
    length = round(var / 2)
    for num in range(2, length):
        if var % num == 0:
            return False
    return True


def playgame():
    thepoint = 'Answer "yes" if given number is prime. Otherwise answer "no"..'
    questions_answers = []
    for num in range(ROUNDS_COUNT):
        question = random.randint(0, 100)
        right_answer = 'yes' if isPrime(question) else 'no'
        questions_answers.append([question, right_answer])
    startengine(thepoint, questions_answers)
