#!/usr/bin/env python3
"""An brain_progression script."""

from brain_games.engine import start_engine
from brain_games.games import brain_progression


def main():
    """Run a code."""
    start_engine(brain_progression)


if __name__ == '__main__':
    main()
