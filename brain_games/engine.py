"""An engine module."""

import prompt

WRONG_ANSWER = """'{0}', 'is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!"""
ROUNDS_COUNT = 3


def start_engine(game_module):
    """
    Run a code.

    Args:
        game_module: game atributes

    Returns:
        true or false answer
    """
    print('Welcome to the Brain Game!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game_module.RULES)
    for _ in range(ROUNDS_COUNT):
        question, answer = game_module.game_question_answer()
        print('Question:', question)
        player_answer = prompt.string('Your answer: ')
        if answer != player_answer:
            print(WRONG_ANSWER.format(player_answer, answer, name))
            return False
        print('Correct!')
    print('Congratulations, {0}!'.format(name))
