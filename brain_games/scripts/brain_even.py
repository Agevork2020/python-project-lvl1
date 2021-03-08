#!/usr/bin/env python3
"""An brain_even script."""

from brain_games.engine import start_engine
from brain_games.games import brain_even


def main():
    """Run a code."""
    start_engine(brain_even)


if __name__ == '__main__':
    main()
