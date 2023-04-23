#!/usr/bin/env python3

from random import randint
import brain_games.games_even
import brain_games.greeting

def main():
    brain_games.greeting.greeting()
    brain_games.games_even.games_even()


if __name__ == '__main__':
    main()
