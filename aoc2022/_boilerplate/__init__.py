"""AoC 2022, Day {{day}}, Functional Code"""

from pathlib import Path
from typing import Optional, Any


def parse_data(input_filename: str | Path):
    """Read a datafile and return the representative dataset"""

    with open(input_filename, "r", encoding="utf-8") as input_fh:
        for line in input_fh:
            line = line.strip()

    return ""


def solve_part_a():
    """Part A Solution"""

    dataset = parse_data("aoc2022/day{{day_full}}/puzzle_input.txt")
    return len(dataset)


def solve_part_b():
    """Part B Solution"""

    dataset = parse_data("aoc2022/day{{day_full}}/puzzle_input.txt")
    return len(dataset)
