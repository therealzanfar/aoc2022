"""AoC 2022, Day 3, Unit Tests"""

from pathlib import Path

from aoc2022.day03 import (
    parse_data,
    split_compartments,
    item_in_common,
    priority,
    group_by,
    solve_part_a,
    solve_part_b,
)

TEST_INPUT_FILENAME = Path("aoc2022/day03/test_input.txt")


def test_import_and_parse():
    dataset = parse_data(TEST_INPUT_FILENAME)
    assert len(dataset) == 6


def test_split():
    pack = "PmmdzqPrVvPwwTWBwg"

    a, b = split_compartments(pack)
    assert len(a) == len(b)
    assert len(a) + len(b) == len(pack)


def test_in_common():
    a, b = "vJrwpWtwJgWr", "hcsFMMfFFhFp"

    assert item_in_common(a, b) == "p"


def test_priority():
    assert priority("L") == 38
    assert priority("t") == 20


def test_group_by():
    assert list(group_by([1, 2, 3, 4, 5, 6], 2)) == [(1, 2), (3, 4), (5, 6)]


def test_solution_a():
    assert solve_part_a(TEST_INPUT_FILENAME) == 157


def test_solution_b():
    assert solve_part_b(TEST_INPUT_FILENAME) == 70
