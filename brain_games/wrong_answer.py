import brain_games.greeting
import brain_games.games.games_even


def wrong_answer(user_name, answer_user, answer_correct):
    print(f"'{answer_user}' is wrong answer ;(. "
          f"Correct answer was '{answer_correct}'. "
          f"Let's try again, {user_name}!")
