"""The great common divisor logic."""
import random


QUESTION = 'Find the greatest common divisor of given numbers.'


def calculate():
    number_1 = random.randint(0, 50)
    number_2 = random.randint(0, 50)
    task = f'{number_1} {number_2}'
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 %= number_2
        else:
            number_2 %= number_1
    correct_answer = str(number_1 + number_2)
    return task, correct_answer
