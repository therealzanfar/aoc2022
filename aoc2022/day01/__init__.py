"""AoC 2022, Day 01, Part A Functional Code"""

from pathlib import Path
from typing import Optional

CalorieRecord = list[int]
CalorieRecords = list[CalorieRecord]


def parse_data(input_filename: str | Path) -> CalorieRecords:
    """Read a datafile and return the representative dataset"""

    with open(input_filename, "r", encoding="utf-8") as input_fh:
        all_elves: CalorieRecords = []
        current_elf: CalorieRecord = []

        for line in input_fh:
            line = line.strip()

            if line == "":
                if len(current_elf) != 0:
                    all_elves.append(current_elf)
                    current_elf = []
                continue

            value = int(line)
            current_elf.append(value)

        if len(current_elf) != 0:
            all_elves.append(current_elf)
            current_elf = []

        return all_elves


def most_calorie_elf(dataset: CalorieRecords) -> CalorieRecord:
    """Find and return the elf with the largest calorie count in the dataset"""

    largest_total = 0
    largest_elf: Optional[CalorieRecord] = None

    for elf in dataset:
        total = sum(elf)

        if largest_elf is None or total > largest_total:
            largest_total = total
            largest_elf = elf

    assert largest_elf is not None
    return largest_elf


def sort_elves(dataset: CalorieRecords) -> CalorieRecords:
    """Sort the dataset by each elf's total calories"""

    return list(sorted(dataset, key=sum, reverse=True))


def solve_part_a():
    """Part A Solution"""

    dataset = parse_data("aoc2022/day01/puzzle_input.txt")
    return sum(most_calorie_elf(dataset))


def solve_part_b():
    """Part B Solution"""

    dataset = parse_data("aoc2022/day01/puzzle_input.txt")
    return sum(sum(elf) for elf in sort_elves(dataset)[:3])
