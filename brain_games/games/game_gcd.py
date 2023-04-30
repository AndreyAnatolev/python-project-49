from random import randint
from math import gcd

rules_of_game = 'Find the greatest common divisor of given numbers.'


def body_of_games():
    n = randint(1, 100)
    m = randint(1, 100)
    print('Question:', n, m)
    print('Your answer: ', end='')
    answer_user = input()
    answer_correct = str(gcd(n, m))
    return answer_correct, answer_user
