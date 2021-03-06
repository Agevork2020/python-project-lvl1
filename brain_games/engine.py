"""An engine module."""

import prompt

ROUNDS_COUNT = 3


def engine(game):
    """
    Run a code.

    Args:
        game: game atributes
    """
    print('Welcome to the Brain Game!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game.RULE)
    for _ in range(ROUNDS_COUNT):
        question, answer = game.generate_question_answer()
        print('Question:', question)
        player_answer = prompt.string('Your answer: ')
        if answer != player_answer:
            print(
                "'{0}', 'is wrong answer ;(. Correct answer was '{1}'.".format(
                    player_answer, answer,
                ),
            )
            print("Let's try again, {0}!".format(name))
            return
        print('Correct!')
    print('Congratulations, {0}!'.format(name))
