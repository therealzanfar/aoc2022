"""AoC 2022, Day 01, Unit Tests"""

from pathlib import Path

from aoc2022.day01 import parse_data, most_calorie_elf, sort_elves

TEST_INPUT_FILENAME = Path("aoc2022/day01/test_input.txt")


def test_import_and_parse():
    dataset = parse_data(TEST_INPUT_FILENAME)

    assert len(dataset) == 5
    assert len(dataset[0]) == 3
    assert sum(dataset[0]) == 6000


def test_largest_selector():
    dataset = parse_data(TEST_INPUT_FILENAME)

    assert most_calorie_elf(dataset) is dataset[3]


def test_sort_elves():
    dataset = parse_data(TEST_INPUT_FILENAME)
    sorted_ds = sort_elves(dataset)

    assert sorted_ds[0] is dataset[3]
    assert sorted_ds[1] is dataset[2]
    assert sorted_ds[2] is dataset[4]
