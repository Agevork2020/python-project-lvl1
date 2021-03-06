"""An cli module."""

import prompt


# cпрашивает имя и здоровается
def welcome_user():
    """Run a code."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
