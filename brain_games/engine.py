"""The game engine."""
import prompt

def game_engine(calculate, QUESTION):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(QUESTION)
    STEP_COUNT = 3
    for _ in range(STEP_COUNT):
        correct_answer = calculate()
        answer = input('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
