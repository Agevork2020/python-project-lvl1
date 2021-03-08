#!/usr/bin/env python3
"""An brain_prime script."""

from brain_games.engine import start_engine
from brain_games.games import brain_prime


def main():
    """Run a code."""
    start_engine(brain_prime)


if __name__ == '__main__':
    main()
