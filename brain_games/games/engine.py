"""An engine module."""

import prompt
from brain_games.games.constants import ROUNDS_COUNT

WR_AN = """'{0}', 'is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!"""


def start_engine(thepoint, func):
    """
    Run a code.

    Args:
        thepoint: question
        func: return couple of questions and answers

    Returns:
        true or false answer
    """
    print('Welcome to the Brain Game!!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!!'.format(name))
    print(thepoint)
    for _ in range(ROUNDS_COUNT):
        question_answer = func()
        print('Question:', question_answer[0])
        player_answer = prompt.string('Your answer: ')
        if question_answer[1] != player_answer:
            print(WR_AN.format(player_answer, question_answer[1], name))
            return False
        print('Correct!')
    print('Congratulations,', name, '!')
    return True
