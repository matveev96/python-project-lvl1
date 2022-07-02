from random import randint


def calculate():
    random_number_first = randint(1, 100)
    random_number_second = randint(1, 100)
    print(f"Question: {random_number_first} {random_number_second}")
    while random_number_first != 0 and random_number_second != 0:
        if random_number_first > random_number_second:
            random_number_first %= random_number_second
        else:
            random_number_second %= random_number_first
    return str(random_number_first + random_number_second)


def head():
    print('Find the greatest common divisor of given numbers.')
