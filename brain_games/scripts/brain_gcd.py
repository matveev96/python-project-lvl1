#!/usr/bin/env python
""""Main programm."""
from brain_games.engine import game_engine
from brain_games.games.gcd import calculate, QUESTION


def main():
    """Run great common division game logic."""
    game_engine(calculate, QUESTION)


if __name__ == '__main__':
    main()
