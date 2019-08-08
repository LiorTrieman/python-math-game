# same as game 2 just trying to do it OOP
import random
import operator


def question():  # generate a new random math question
    rand_ind = random.randint(0, 3) # generate a random number between 0-3
    arg_1 = random.randint(0, 20)
    arg_2 = random.randint(0, 20)
    operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    op = random.choice(list(operators.keys()))  # random operation
    answer = operators.get(op)(arg_1, arg_2)      # calc the answer
    new_question = ('{} {} {} ?\n'.format(arg_1, op, arg_2))
    print(new_question)
    return answer


print(question())  # print the new questions
