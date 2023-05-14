from random import randint

RULES_OF_GAME = 'What number is missing in the progression?'


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
    task = ''
    for index, i in enumerate(progression):
        if index < 9:
            task += f'{i} '
        else:
            task += f'{i}'

    return task, answer_correct
