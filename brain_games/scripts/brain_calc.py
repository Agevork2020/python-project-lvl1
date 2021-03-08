#!/usr/bin/env python3
"""An brain_calc script."""

from brain_games.engine import start_engine
from brain_games.games import brain_calc


def main():
    """Run a code."""
    start_engine(brain_calc)


if __name__ == '__main__':
    main()
