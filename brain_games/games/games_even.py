from random import randint


def games_even_question():
    n = randint(1, 99)
    print('Question:', n)
    answer_user = ''
    while answer_user == '':
        print('Your answer: ', end='')
        answer_user = input()
        answer_correct = 'no'
        if n % 2 == 0:
            answer_correct = 'yes'
    return answer_correct, answer_user
