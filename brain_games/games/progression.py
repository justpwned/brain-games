from brain_games.games.common import ask_question, play_round, welcome_user
import random


def get_correct_answer(progression, missing_pos):
    return str(progression[missing_pos])


def generate_expr(progression, missing_pos):
    return ''.join(
        '.. ' if i == missing_pos else f'{progression[i]} '
        for i in range(len(progression))
    )


def start():
    name = welcome_user('What number is missing in the progression?')
    correct_guesses = 0
    running = True
    length = 10
    while running:
        n1 = random.randint(0, 100)
        step = random.randint(1, 10)
        progression = [i for i in range(n1, n1 + step * length, step)]
        missing_pos = random.randint(0, length - 1)
        expr = generate_expr(progression, missing_pos)
        answer = ask_question(expr)
        correct_answer = get_correct_answer(progression, missing_pos)
        running, correct_guesses = play_round(
            name, answer, correct_answer, correct_guesses)
