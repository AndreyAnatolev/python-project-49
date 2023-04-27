from random import randint

rules_of_game = 'Answer "yes" if the number is even, otherwise answer "no".'

def games_even():
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
