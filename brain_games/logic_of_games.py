import prompt


def logic_games(game_variants):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_variants.rules_of_game)

    count = 0
    for _ in range(3):
        answer_correct, answer_user = game_variants.body_of_games()
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
