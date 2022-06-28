from random import randint


def calculate():
    random_number = randint(1, 100)
    print(f"Question: {random_number}")
    if random_number % 2 == 0:
        return "yes"
    else:
        return "no"


def head():
    print('Answer "yes" if the number is even, otherwise answer "no".')
