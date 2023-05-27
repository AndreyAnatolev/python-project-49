from random import randint

RULES_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_for_prime(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    return count == 2


def create_the_task():
    task = randint(1, 100)
    if check_for_prime(task) is True:
        answer_correct = 'yes'
    else:
        answer_correct = 'no'
    return task, answer_correct
