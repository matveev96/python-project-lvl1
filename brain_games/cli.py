import prompt

def get_user_name():
    return prompt.string('May I have your name? ')


def welcome_user():
    print(f'Hello, {get_user_name()}!')

