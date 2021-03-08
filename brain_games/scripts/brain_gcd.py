#!/usr/bin/env python3
"""An brain_gcd script."""

from brain_games.engine import start_engine
from brain_games.games import brain_gcd


def main():
    """Run a code."""
    start_engine(brain_gcd)


if __name__ == '__main__':
    main()
