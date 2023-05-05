from random import randint
from random import choice

rules_of_game = 'What is the result of the expression?'


def body_of_games():
    a = randint(1, 99)
    b = randint(1, 99)
    list1 = ['+', '-', '*']
    operation = choice(list1)
    task = f'{a} {operation} {b}'
    answer_correct = ''

    if operation == '+':
        answer_correct = a + b
    elif operation == '-':
        answer_correct = a - b
    elif operation == '*':
        answer_correct = a * b
    return task, str(answer_correct)
