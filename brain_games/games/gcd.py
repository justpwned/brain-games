from brain_games.games.utils import ask_question, play_round, welcome_user
import random
import math


def get_correct_answer(n1, n2):
    result = math.gcd(n1, n2)
    return str(result)


def start():
    name = welcome_user('Find the greatest common divisor of given numbers.')
    correct_guesses = 0
    running = True
    while running:
        n1 = random.randint(0, 100)
        n2 = random.randint(0, 100)
        expr = f'{n1} {n2}'
        answer = ask_question(expr)
        correct_answer = get_correct_answer(n1, n2)
        running, correct_guesses = play_round(
            name, answer, correct_answer, correct_guesses)
