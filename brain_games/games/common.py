import prompt
import brain_games.cli


def ask_question(question):
    print(f'Question: {question}')
    return prompt.string('Your answer: ')


def welcome_user(game_rules):
    name = brain_games.cli.welcome_user()
    print(game_rules)
    return name


def game_won(name):
    print(f'Congratulations, {name}!')


def game_lost(name, wrong_answer, correct_answer):
    print(f'"{wrong_answer}" is wrong answer ;(. '
          f'Correct answer was "{correct_answer}".')
    print(f'Let\'s try again, {name}!')


def play_round(name, answer, correct_answer, correct_guesses):
    if answer == correct_answer:
        correct_guesses += 1
        print('Correct!')
        if correct_guesses == 3:
            game_won(name)
            return False, correct_guesses

        return True, correct_guesses

    game_lost(name, answer, correct_answer)
    return False, correct_guesses
