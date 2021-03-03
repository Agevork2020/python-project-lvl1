"""An engine module."""

import prompt


def start_engine(thepoint, questions_answers):
    """Run a code."""
    print('Welcome to the Brain Game!!')
    name = prompt.string('May I have your name?')
    print('Hello', name, '!!')
    print(thepoint)
    for question_answer in questions_answers:
        print('Question:', question_answer[0])
        player_answer = prompt.string('Your answer: ')
        if question_answer[1] != player_answer:
            print("'{}', 'is wrong answer ;(. Correct answer was '{}'. Let's try again, {}!".format(player_answer, question_answer[1], name))
            return False
        print("Correct!")
    print("Congratulations", name, "!")
    return True
