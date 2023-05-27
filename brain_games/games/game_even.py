from random import randint

RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_the_number_even(number):
    return number % 2 == 0


def create_the_task():
    task = randint(1, 99)
    if is_the_number_even(task) is True:
        answer_correct = 'yes'
    else:
        answer_correct = 'no'
    return task, answer_correct
