# same as game 1 but with random questions

# game syntax  from the link: https://www.youtube.com/watch?v=h4n_ByFuD90"

# all options for the questions are defined in this dict:

import random
import operator
# initiate game variables
Correct_answers = 0  # initial number of correct answers to the user:


def question():  # generate a new random math question
    arg_1 = random.randint(0, 10)
    arg_2 = random.randint(1, 10)
    operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    op = random.choice(list(operators.keys()))  # random operation
    current_answer = operators.get(op)(arg_1, arg_2)      # calc the answer
    current_question = ('{} {} {} ?\n'.format(arg_1, op, arg_2))
    return current_question, current_answer


# looping until getting a valid answer from user
start_game = input("Do you want to play? (Yes/No)")
while True:
    if start_game in ("Yes", "yes", "y", "Y"):
        print("Good Answer! Lets Start!")
        Game_On = 1  # start game
        break
    elif start_game in ("No", "no", "n", "N"):
        print("OK, see you next time")
        Game_On = 0
        quit()
    else:
        start_game = input("I didn't get that, Would you like to Play?")
        continue
number_of_questions = 10  # total of 10 questions in a game
for no_questions in range(1, number_of_questions):
    current_question, current_answer = question()
    if Game_On:  # the user wants to play
        user_answer = input(current_question)

        Bool = random.choice([True, False])  # to give multiple relpys to user so it wont be boring...
        # check if answer is an int:
        while True:
            try:
                val = float(user_answer)
                break
            except ValueError:
                print("That's not a number, try again!")
                user_answer = input(current_question)
                continue
        if float(current_answer) == float(user_answer): # check if the answer is correct
            Correct_answers += 1  # count as a correct answer
            if Bool == 1:
                print("Good Job! :)")
            else:
                print("Very Good! :)")
        else:
            if Bool == 1:
                print("Wrong answer! :(")
            else:
                print("Bad Answer, you will succeed next time!")

# End on game - give feedback to the user:
print("Good job! you got ", Correct_answers, "correct answers our of ", number_of_questions)


# Add to this game:
# GUI
# TRY EXEPT
# Random Qs?
# Else
