"""AoC 2022, Day {{day}}, Unit Tests"""

from pathlib import Path

from aoc2022.day{{day_full}} import parse_data, solve_part_a, solve_part_b

TEST_INPUT_FILENAME = Path("aoc2022/day{{day_full}}/test_input.txt")


def test_import_and_parse():
    dataset = parse_data(TEST_INPUT_FILENAME)
    assert dataset


def test_solution_a():
    assert solve_part_a(TEST_INPUT_FILENAME) == 0


def test_solution_b():
    assert solve_part_b(TEST_INPUT_FILENAME) == 0
