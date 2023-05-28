from random import randint

RULES_OF_GAME = 'What number is missing in the progression?'
MIN_INITIAL_TERM_OF_PROG = 1
MAX_INITIAL_TERM_OF_PROG = 20
MIN_DIFFERENCE_OF_ARITH_PROG = 3
MAX_DIFFERENCE_OF_ARITH_PROG = 7
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10


def create_the_arithmetic_progression(first_number, length, step):
    last_num_of_progression = first_number + ((length - 1) * step)
    progression = [
        number for number in range(
            first_number, last_num_of_progression + 1, step)]

    return progression


def create_the_question_and_hidden_element(progression, index_random):
    hidden_num = progression[index_random]
    answer_correct = str(hidden_num)
    progression[index_random] = '..'
    task = ' '.join([str(number) for number in progression])

    return task, answer_correct


def create_the_task():
    initial_term = randint(
        MIN_INITIAL_TERM_OF_PROG, MAX_INITIAL_TERM_OF_PROG)
    difference_of_arith_prog = randint(
        MIN_DIFFERENCE_OF_ARITH_PROG, MAX_DIFFERENCE_OF_ARITH_PROG)
    progression_length = randint(
        MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    progression = create_the_arithmetic_progression(
        initial_term, progression_length, difference_of_arith_prog)
    index_random = randint(1, len(progression) - 1)
    task, answer_correct = create_the_question_and_hidden_element(
        progression, index_random)

    return task, answer_correct
