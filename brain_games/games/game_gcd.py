from random import randint
from math import gcd

RULES_OF_GAME = 'Find the greatest common divisor of given numbers.'


def body_of_games():
    n = randint(1, 100)
    m = randint(1, 100)
    task = f'{n} {m}'
    answer_correct = str(gcd(n, m))
    return task, answer_correct
