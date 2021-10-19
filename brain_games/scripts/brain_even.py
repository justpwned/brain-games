from brain_games.cli import welcome_user, prompt_answer
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_guesses = 0
    while correct_guesses != 3:
        question_number = randint(0, 1000)
        correct_answer = 'yes' if question_number % 2 == 0 else 'no'

        print(f'Question: {question_number}')
        guess = prompt_answer(['yes', 'no'], 'Your answer: ').string
        if guess == correct_answer:
            print('Correct!')
            correct_guesses += 1
        else:
            print(f'"{guess}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}"')

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
