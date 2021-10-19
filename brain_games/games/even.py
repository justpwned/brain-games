from brain_games.games.utils import ask_question, play_round, welcome_user
from random import randint


def get_correct_answer(answer):
    correct_answer = 'yes' if answer % 2 == 0 else 'no'
    return correct_answer


def is_game_over(correct_guesss):
    return correct_guesss == 3


def start():
    name = welcome_user(
        'Answer "yes" if the number is even, otherwise answer "no".')

    correct_guesses = 0
    running = True
    while running:
        guessed_number = randint(0, 100)
        answer = ask_question(guessed_number)
        correct_answer = get_correct_answer(guessed_number)
        running, correct_guesses = play_round(
            name, answer, correct_answer, correct_guesses)
