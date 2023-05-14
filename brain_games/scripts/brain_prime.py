#!/usr/bin/env python3

from brain_games import logic_of_games as engine
from brain_games.games import game_prime


def main():
    engine.run(game_prime)


if __name__ == '__main__':
    main()
