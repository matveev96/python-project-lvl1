#!/usr/bin/env python

from brain_games import engine
from brain_games.games.gcd import calculate, QUESTION


def main():
    engine.game_engine(calculate, QUESTION)


if __name__ == '__main__':
    main()
