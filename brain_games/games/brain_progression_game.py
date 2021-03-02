from brain_games.games.engine import startengine
from brain_games.games.constants import ROUNDS_COUNT
import random


def makeQuestion(randLength, randHidden, randFirst, randStep):
    result1 = ''
    for i in range(randLength):
        x = randFirst + randStep * i
        if i == randHidden:
            x = "..."
        result1 .= " {}".format(x)
    return "{}{}".format(randFirst, result1)


def playgame():
    thepoint = 'What number is missing in the progression??'

    questions_answers = []
    for i in range(ROUNDS_COUNT):
        randLength = random.randint(5, 15)
        randHidden = random.randint(1, randLength - 1)
        randFirst = random.randint(0, 30)
        randStep = random.randint(2, 10)
        question = makeQuestion(randLength, randHidden, randFirst, randStep)
        right_answer = str(randFirst + randStep * randHidden)
        questions_answers.append([question, right_answer])

    startengine(thepoint, questions_answers)