# initial try for a math game,
# bank of 8 qustions
# flow of code:
# 1. ask the user if she owuld like to play -Yes/No
# 2. if Y - start asking math questions
# 3. count number of correct answers and gives a feedback at the end of the game.

import random

# initiate game variables
Correct_answers = 0  # initial number of correct answers to the user:
questions = {"1*5= ": "5", "2*3= ": "6", "4*2= ": "8", "4*4= ": "16", "3*4= ": "12", "15*2= ": "30", "33*3= ": "99"
    , "5+15= ": "20"}
# looping until getting a valid answer from user
start_game = input("Do you want to play? (Yes/No)")
while True:
    if start_game in ("Yes", "yes", "y", "Y"):
        print("Good Answer! Lets Start!")
        Game_On = 1  # start game
        break
    elif start_game in ("No", "no","n", "N"):
        print("OK, see you next time")
        Game_On = 0
        quit()
    else:
        start_game = input("I didn't get that, Would you like to Play?")
        continue
if Game_On:  # the user wants to play
    for q in questions:
        answer = input(q)
        Bool = random.choice([True, False])
        # check if answer is an int:
        while True:
            try:
                val = int(answer)
                break
            except ValueError:
                print("That's not a number, try again!")
                answer = input(q)
                continue
        if answer == questions.get(q):
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
print("Good job! you got ", Correct_answers, "correct answers our of ", len(questions))



