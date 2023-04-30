from random import randint

rules_of_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def body_of_games():
    n = randint(1, 99)
    print('Question:', n)
    print('Your answer: ', end='')
    answer_user = input()
    if n % 2 == 0:
        answer_correct = 'yes'
    else:
        answer_correct = 'no'
    return answer_correct, answer_user
