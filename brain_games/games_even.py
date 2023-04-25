from random import randint


def games_even(user_name):
    n = randint(1, 99)
    print('Question:', n)
    answer_user = ''
    while answer_user == '':
        print('Your answer: ', end='')
        answer_user = input()
        answer_random = 'no'
        if n % 2 == 0:
            answer_random = 'yes'
    return answer_random, answer_user
