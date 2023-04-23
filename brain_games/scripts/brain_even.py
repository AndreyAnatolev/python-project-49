#!/usr/bin/env python3

import brain_games.games_even
import brain_games.greeting


def main():
    user_name = brain_games.greeting.greeting()
    brain_games.games_even.games_even(user_name)


if __name__ == '__main__':
    main()
