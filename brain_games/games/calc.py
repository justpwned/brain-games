from brain_games.games.common import ask_question, play_round, welcome_user
import operator
import random

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}
OP_LIST = list(OPERATORS)


def get_correct_answer(op1, op, op2):
    result = OPERATORS[op](op1, op2)
    return str(result)


def start():
    name = welcome_user('What is the result of the expression?')
    correct_guesses = 0
    running = True

    while running:
        first_operand = random.randint(0, 100)
        second_operand = random.randint(0, 100)
        op = random.choice(OP_LIST)
        expr = f'{first_operand} {op} {second_operand}'

        answer = ask_question(expr)
        correct_answer = get_correct_answer(first_operand, op, second_operand)
        running, correct_guesses = play_round(
            name, answer, correct_answer, correct_guesses)
