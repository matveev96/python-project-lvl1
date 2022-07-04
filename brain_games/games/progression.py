from random import randint


def calculate():
    random_start = randint(0, 100)
    step = randint(1, 5)
    another_symb = randint(0, 9)
    next_num = random_start + step
    lst = [str(random_start)]
    for _ in range(0, 9):
        lst.append(str(next_num))
        next_num = next_num + step
    answer = lst[another_symb]
    lst[another_symb] = '..'
    delimiter = ' '
    print(f"Question: {delimiter.join(lst)}")
    return answer


def head():
    print('What number is missing in the progression?')
