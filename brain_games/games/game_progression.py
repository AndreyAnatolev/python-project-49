from random import randint

RULES_OF_GAME = 'What number is missing in the progression?'
MIN_NUM_START_OF_PROG = 1
MAX_NUM_START_OF_PROG = 20
MIN_RANGE_OF_STEP = 3
MAX_RANGE_OF_STEP = 7
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10


def arithmetic_progression(first_number, length, step):
    last_num_of_progression = first_number + ((length - 1) * step)
    progression = [
        str(number) for number in range(
            first_number, last_num_of_progression + 1, step)]

    return progression


def question_and_hidden_element(progression, index_random):
    hidden_num = progression[index_random]
    answer_correct = str(hidden_num)
    progression[index_random] = '..'
    task = ' '.join(progression)

    return task, answer_correct


def task_and_answer_correct():
    start_num_of_progression = randint(
        MIN_NUM_START_OF_PROG, MAX_NUM_START_OF_PROG)
    range_of_step = randint(
        MIN_RANGE_OF_STEP, MAX_RANGE_OF_STEP)
    progression_length = randint(
        MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    progression = arithmetic_progression(
        start_num_of_progression, progression_length, range_of_step)
    index_random = randint(1, len(progression) - 1)
    task, answer_correct = question_and_hidden_element(
        progression, index_random)

    return task, answer_correct
