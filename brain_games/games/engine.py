import prompt

def startengine(thepoint, questions_answers):
    print('Welcome to the Brain Game!!')
    name = prompt.string('May I have your name?')
    print('Hello', name, '!!')
    print(thepoint)
    i = 0
    while i < count(questions_answers): 
        print('Question:', questions_answers[i][0])
        player_answer = prompt.string('Your answer')
        if questions_answers[i][1] != player_answer:
            print(player_answer, "is wrong answer ;(. Correct answer was ", questions_answers[i][1],
"Let's try again,", name, "!")
            return False
        else:
            print("Correct!")
            i += 1
            print("Congratulations", name, "!")