from random import randint
from random import choice

RULES_OF_GAME = 'What is the result of the expression?'
MIN_VALUE_FOR_RANDOM = 1
MAX_VALUE_FOR_RANDOM = 99
LIST_OF_OPERATION = ['+', '-', '*']


def solve_the_task(first_num, operation, second_num):
    if operation == '+':
        return first_num + second_num
    elif operation == '-':
        return first_num - second_num
    elif operation == '*':
        return first_num * second_num


def create_the_task():
    first_number = randint(MIN_VALUE_FOR_RANDOM, MAX_VALUE_FOR_RANDOM)
    second_number = randint(MIN_VALUE_FOR_RANDOM, MAX_VALUE_FOR_RANDOM)
    operation = choice(LIST_OF_OPERATION)
    task = f'{first_number} {operation} {second_number}'
    answer_correct = solve_the_task(first_number, operation, second_number)

    return task, str(answer_correct)
