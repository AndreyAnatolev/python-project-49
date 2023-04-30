from random import randint

rules_of_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def body_of_games():
    number = randint(1, 100)
    print('Question:', number)
    print('Your answer: ', end='')
    answer_user = input()
    answer_correct = 'yes'
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count > 2:
        answer_correct = 'no'
    return answer_correct, answer_user
