#!/usr/bin/env python

from brain_games import engine
from brain_games.games.gcd import calculate, head
from brain_games.greeting import greet


def main():
    engine.game_engine(calculate, head, greet)


if __name__ == '__main__':
    main()
