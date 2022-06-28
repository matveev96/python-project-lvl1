

def game_engine(calculate, head, greet):
    user_name = greet()
    head()
    for i in range(0, 3):
        correct_answer = calculate()
        answer = input('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {user_name}!")
            break
        if i == 2:
            print(f"Congratulations, {user_name}!")
