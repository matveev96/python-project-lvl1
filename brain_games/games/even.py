from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculate():
    task = randint(0, 100)
    correct_answer = 'no' if task % 2 else 'yes'
    return task, correct_answer
