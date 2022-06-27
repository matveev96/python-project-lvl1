from random import randint
import prompt


def brain_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(1, 4):
        random_number = randint(1, 100)
        print(f"Question: {random_number}")
        answer = input('Your answer: ')
        if random_number % 2 == 0:
            right_answer = str("yes")
        else:
            right_answer = str("no")
        if right_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
        print(f"Congratulations, {name}!")
