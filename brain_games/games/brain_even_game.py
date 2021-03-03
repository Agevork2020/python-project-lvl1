import random
from brain_games.games.constants import ROUNDS_COUNT
from brain_games.games.engine import startengine


def playgame():
    thepoint = 'Answer "yes" if the number is even, otherwise answer "no"..'
    questions_answers = []
    for num in range(ROUNDS_COUNT):
        question = random.randint(-100, 100)
        right_answer = 'yes' if question % 2 == 0 else 'no'
        questions_answers.append([question, right_answer])
    startengine(thepoint, questions_answers)
