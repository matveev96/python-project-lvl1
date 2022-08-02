"""The progression game logic."""
import random


QUESTION = 'What number is missing in the progression?'


def calculate():
    first_term = random.randint(0, 100)
    step = random.randint(1, 5)
    missing_term = random.randint(0, 9)
    term = first_term
    lst_progression = []
    for _ in range(10):
        lst_progression.append(str(term))
        term += step
    correct_answer = lst_progression[missing_term]
    lst_progression[missing_term] = '..'
    task = ' '.join(lst_progression)
    return task, correct_answer
