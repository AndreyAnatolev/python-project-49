#!/usr/bin/env python3

import brain_games.greeting
import brain_games.games_calc


def main():
    user_name = brain_games.greeting.greeting()
    brain_games.games_calc.calc(user_name)

if __name__ == '__main__':
    main()
