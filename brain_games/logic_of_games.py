import prompt

NUMBER_OF_ROUNDS = 3


def run(game_variants):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_variants.RULES_OF_GAME)

    count = 0
    for _ in range(NUMBER_OF_ROUNDS):
        task, answer_correct = game_variants.task_and_answer_correct()
        print('Question:', task)
        answer_user = input('Your_answer: ')

        if answer_correct == answer_user:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer_user}' is wrong answer ;(. "
                  f"Correct answer was '{answer_correct}'. "
                  f"Let's try again, {user_name}!")
            break
    if count == 3:
        print(f'Congratulations, {user_name}!')
