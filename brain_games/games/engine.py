"""An engine module."""

import prompt

WRONG_MSG = """
    '{0}', 'is wrong answer ;(. Correct answer was '{1}'.
    Let's try again, {2}!
"""


def start_engine(thepoint, questions_answers):
    """
    Run a code.

    Args:
        thepoint: question
        questions_answers: list of couples of questions and answers

    Returns:
        true or false answer
    """
    print('Welcome to the Brain Game!!')
    name = prompt.string('May I have your name?')
    print('Hello', name, '!!')
    print(thepoint)
    for question_answer in questions_answers:
        print('Question:', question_answer[0])
        player_answer = prompt.string('Your answer: ')
        if question_answer[1] != player_answer:
            print(WRONG_MSG.format(player_answer, question_answer[1], name))
            return False
        print('Correct!')
    print('Congratulations', name, '!')
    return True
