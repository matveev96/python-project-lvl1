"""The brain prime game logic."""
import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculate():
    task = random.randint(0, 100)
    flag = False # define a flag variable
    if task < 2:
        flag = True
    else:
        for i in range(2, int(task ** 0.5 + 1)):
            if (task % i) == 0:
                flag = True
                break
    correct_answer = 'no' if flag else 'yes'
    return task, correct_answer
