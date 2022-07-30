from random import randint, choice


QUESTION = 'What is the result of the expression?'


def calculate():
    random_number_first = randint(1, 20)
    random_number_second = randint(1, 20)
    random_operator = choice(['+', '-', '*'])
    expression = (f"{random_number_first} \
{random_operator} {random_number_second}")
    print(f"Question: {expression}")
    if random_operator == "+":
        return str(random_number_first + random_number_second)
    elif random_operator == "-":
        return str(random_number_first - random_number_second)
    else:
        return str(random_number_first * random_number_second)
