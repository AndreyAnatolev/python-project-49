from random import randint

rules_of_game = 'What number is missing in the progression?'


def body_of_games():
    n = randint(1, 20)
    m = randint(1, 7)
    progression = []
    index_random = randint(1, 9)
    for i in range(10):
        n += m
        progression.append(str(n))
    answer_correct = progression[index_random]
    progression.pop(index_random)
    progression.insert(index_random, '..')
    print('Question: ', *progression)
    print('Your answer: ', end='')
    answer_user = input()
    return answer_correct, answer_user
