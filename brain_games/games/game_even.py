from random import randint

RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_for_even(number):
    return number % 2 == 0


def create_the_task():
    task = randint(1, 99)
    if check_for_even(task) is True:
        answer_correct = 'yes'
    else:
        answer_correct = 'no'
    return task, answer_correct
