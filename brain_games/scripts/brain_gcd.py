#!/usr/bin/env python3

from brain_games import logic_of_games as engine
from brain_games.games import game_gcd


def main():
    engine.run(game_gcd)


if __name__ == '__main__':
    main()
