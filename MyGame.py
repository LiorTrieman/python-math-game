# ---This is my first Python Project---#
# -------------------------------------#
# Last Modified 201990726
# Author: Lior Trieman
# Syntax reference link: https://www.youtube.com/watch?v=h4n_ByFuD90"


import random
import operator
# Initiate Game Variables

correct_answers = 0  # initial number of correct answers to the user:
wrong_answers_total = 0  # total wrong answers
wrong_answers_in_a_row = 0  # total wrong answers in a row
NUM_OF_QUESTIONS = 10  # total of 10 questions in a game

# each function generate a questions in a different level of difficulty
# level_1 = only real answers, number from 0-10 only (+) and (-)
# level_2 = numbers from 0-50
# level_3 = numbers from 0-100

MAX_ARG_LEVEL_1 = 10  # variable for max value for lever 1 arg


def question_level_1():                  # generate a new random math question
    arg_1 = random.randint(0, MAX_ARG_LEVEL_1)
    arg_2 = random.randint(0, MAX_ARG_LEVEL_1)
    operators = {"+": operator.add, "-": operator.sub}
    op = random.choice(list(operators.keys()))  # random operation
    current_answer = operators.get(op)(arg_1, arg_2)      # calc the answer
    current_question = ('{} {} {} ?\n'.format(arg_1, op, arg_2))
    return current_question, current_answer

MAX_ARG_LEVEL_2 = 50  # variable for max value for level 2 arg


def question_level_2():                  # generate a new random math question
    arg_1 = random.randint(0, MAX_ARG_LEVEL_2)
    arg_2 = random.randint(0, MAX_ARG_LEVEL_2)
    operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    op = random.choice(list(operators.keys()))  # random operation
    current_answer = operators.get(op)(arg_1, arg_2)      # calc the answer
    current_question = ('{} {} {} ?\n'.format(arg_1, op, arg_2))
    return current_question, current_answer

def rnd_correct_ans_reply():
    correct_reply_list = ["Good Job! :)","Very Good!:)","You nailed it;","You are a math master!", "way to go!!"]
    correct_reply = random.choice(correct_reply_list)  # random auto reply
    return correct_reply

def rnd_wrong_ans_reply():
    mistake_reply_list = ["Wrong answer! :(","That was a mistake...","Bad Answer, you will do better next one!",\
                          "Sorry, that's not the answer.."]
    mistake_reply = random.choice(mistake_reply_list)  # random auto reply
    return mistake_reply


# looping until getting a valid answer from user
start_game = input("Do you want to play? (Yes/No)")
while True:
    if start_game in ("Yes", "yes", "y", "Y"):
        print("Good Answer! Lets Start!")
        game_on = 1  # start game
        break
    elif start_game in ("No", "no", "n", "N"):
        print("OK, see you next time")
        game_on = 0
        quit()
    else:
        start_game = input("I didn't get that, Would you like to Play?")
        continue

# Checking if the user wants to play or leave
for a_question in range(0, NUM_OF_QUESTIONS):
    if wrong_answers_total < 5 and wrong_answers_in_a_row < 3:
        current_question, current_answer = question_level_1()
        user_answer = input(current_question)
        # check if answer is a number:
        while True:
            try:
                val = int(user_answer)
                break
            except ValueError:
                print("That's not a number, try again!")
                user_answer = input(current_question)
                continue
        if float(current_answer) == float(user_answer): # check if the answer is correct
            correct_answers += 1  # count as a correct answer
            print(rnd_correct_ans_reply())
            wrong_answers_in_a_row = 0  # last answer was correct
        else:
            print(rnd_wrong_ans_reply())
            wrong_answers_total += 1  # count wrong answers (up to 5 until Game-Over)
            wrong_answers_in_a_row += 1  # count wrong answers in a row (Up to 3 until Game-Over)
    else:
        game_on = 0
        print("Game over, you got ", correct_answers, "correct answers out of: ", a_question + 1)
        break
# End on game - give feedback to the user:
if game_on:
    print("Good job! you got ", correct_answers, "correct answers our of ", NUM_OF_QUESTIONS)
    print(" total wrong answers:", wrong_answers_total)


