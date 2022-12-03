"""AoC 2022, Day {{day}}, Functional Code"""

from pathlib import Path
from typing import Optional, Any

PUZZLE_INPUT_FILENAME = Path("aoc2022/day{{day_full}}/puzzle_input.txt")


def parse_data(input_filename: str | Path):
    """Read a datafile and return the representative dataset"""

    with open(input_filename, "r", encoding="utf-8") as input_fh:
        for line in input_fh:
            line = line.strip()

    return ""


def solve_part_a(filename: str | Path = PUZZLE_INPUT_FILENAME):
    """Part A Solution"""

    dataset = parse_data(filename)
    return len(dataset)


def solve_part_b(filename: str | Path = PUZZLE_INPUT_FILENAME):
    """Part B Solution"""

    dataset = parse_data(filename)
    return len(dataset)
