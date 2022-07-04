from random import randint


def calculate():
    random_number = randint(1, 500)
    print(f"Question: {random_number}")
    counter = 0
    for i in range(2, random_number // 2 + 1):
        if random_number % i == 0:
            counter += 1
    if counter <= 0:
        return "yes"
    else:
        return "no"


def head():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
