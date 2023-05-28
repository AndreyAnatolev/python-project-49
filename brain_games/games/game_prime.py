from random import randint

RULES_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_the_number_prime(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    return count == 2


def create_the_task():
    task = randint(1, 100)
    answer_correct = ('no', 'yes')[is_the_number_prime(task)]
    return task, answer_correct
