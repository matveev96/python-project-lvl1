"""The calculator game logic."""
import random
import operator


QUESTION = 'What is the result of the expression?'


def calculate():
    number_1 = random.randint(0, 10)
    number_2 = random.randint(0, 10)
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    operation = random.choice(list(operators.keys()))
    correct_answer = str(operators[operation] (number_1, number_2))
    task = f'{number_1} {operation} {number_2}'
    return task, correct_answer
