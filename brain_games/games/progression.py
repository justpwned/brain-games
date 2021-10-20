from brain_games.games.utils import ask_question, play_round, welcome_user
import random


def get_correct_answer(progression, missing_pos):
    return str(progression[missing_pos])


def generate_expr(progression, missing_pos):
    expr = ''
    for i in range(len(progression)):
        if i == missing_pos:
            expr += '.. '
        else:
            expr += str(progression[i]) + ' '
    return expr


def start():
    name = welcome_user('What number is missing in the progression?')
    correct_guesses = 0
    running = True
    while running:
        n1 = random.randint(0, 100)
        step = random.randint(1, 10)
        length = 10
        progression = [i for i in range(n1, n1 + step * length, step)]
        missing_pos = random.randint(0, length - 1)
        expr = generate_expr(progression, missing_pos)
        answer = ask_question(expr)
        correct_answer = get_correct_answer(progression, missing_pos)
        running, correct_guesses = play_round(
            name, answer, correct_answer, correct_guesses)
