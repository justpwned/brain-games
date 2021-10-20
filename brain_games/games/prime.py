from brain_games.games.utils import ask_question, play_round, welcome_user
import random
import math


def get_correct_answer(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def start():
    name = welcome_user(
        'Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_guesses = 0
    running = True
    while running:
        number = random.randint(1, 100)
        answer = ask_question(str(number))
        correct_answer = get_correct_answer(number)
        running, correct_guesses = play_round(
            name, answer, correct_answer, correct_guesses)
