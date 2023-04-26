import brain_games.games.games_even
import brain_games.greeting
import brain_games.wrong_answer
import brain_games.rules_of_even
import brain_games.congrat


def logic_games():
    user_name = brain_games.greeting.greeting()
    brain_games.rules_of_even.ruls_of_games_even()
    count = 0
    for _ in range(3):
        answer_correct, answer_user = brain_games.games.games_even.games_even_question()
        if answer_correct == answer_user:
            count += 1
            print('Correct!')
        else:
            brain_games.wrong_answer.wrong_answer(user_name, answer_user, answer_correct)
            break
    if count == 3:
        brain_games.congrat.congratulation(user_name)
