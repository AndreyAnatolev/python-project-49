from random import randint
from math import sqrt

RULES_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_the_number_prime(number):
    if number in (0, 1):
        return False

    for i in range(2, int(sqrt(number))):
        if number % i == 0:
            return False

    return True


def create_the_task():
    task = randint(1, 100)
    answer_correct = ('no', 'yes')[is_the_number_prime(task)]
    return task, answer_correct

