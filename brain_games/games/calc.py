from random import randint, choice


def calculate():
    random_number_first = randint(1, 20)
    random_number_second = randint(1, 20)
    random_operator = choice(['+', '-', '*'])
    expression = (f"{random_number_first} \
{random_operator} {random_number_second}")
    print(f"Question: {expression}")
    if random_operator == "+":
        result = random_number_first + random_number_second
        return str(result)
    elif random_operator == "-":
        result = random_number_first - random_number_second
        return str(result)
    else:
        result = random_number_first * random_number_second
        return str(result)


def head():
    print('What is the result of the expression?')
