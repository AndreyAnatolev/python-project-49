from random import randint
from math import gcd

RULES_OF_GAME = 'Find the greatest common divisor of given numbers.'
MIN_VALUE_FOR_RANDOM = 1
MAX_VALUE_FOR_RANDOM = 100


def create_the_task():
    first_random_number = randint(MIN_VALUE_FOR_RANDOM, MAX_VALUE_FOR_RANDOM)
    second_random_number = randint(MIN_VALUE_FOR_RANDOM, MAX_VALUE_FOR_RANDOM)
    task = f'{first_random_number} {second_random_number}'
    answer_correct = str(gcd(first_random_number, second_random_number))

    return task, answer_correct
