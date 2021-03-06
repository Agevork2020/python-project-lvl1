#!/usr/bin/env python3
"""An brain_prime script."""

from brain_games.games.brain_prime_game import THEPOINT, play_game
from brain_games.games.engine import start_engine


def main():
    """Run a code."""
    start_engine(THEPOINT, play_game)


if __name__ == '__main__':
    main()
