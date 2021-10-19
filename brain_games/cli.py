import prompt


def welcome_user():
    name = prompt.string('May i have your name? ')
    print(f'Hello, {name}!')
    return name


def prompt_answer(allowed_answers=[], question=''):
    pattern = '(.*?)'
    if len(allowed_answers) != 0:
        pattern = '|'.join(allowed_answers)

    answer = prompt.regex(pattern, question)
    return answer
