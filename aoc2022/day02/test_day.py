"""AoC 2022, Day 2, Unit Tests"""

from pathlib import Path

from aoc2022.day02 import (
    parse_data_a,
    parse_data_b,
    is_win,
    score,
    correct_response,
    solve_part_a,
    solve_part_b,
    Shape,
    Result,
)

TEST_INPUT_FILENAME = Path("aoc2022/day02/test_input.txt")


def test_import_and_parse_a():
    dataset = parse_data_a(TEST_INPUT_FILENAME)

    assert len(dataset) == 3
    assert dataset[0].you is Shape.P
    assert dataset[0].opp is Shape.R


def test_win():
    assert is_win(Shape.R, Shape.P) is True
    assert is_win(Shape.R, Shape.S) is False
    assert is_win(Shape.R, Shape.R) is None


def test_score():
    assert score(Shape.R, Shape.P) == 6 + 2
    assert score(Shape.R, Shape.S) == 0 + 3
    assert score(Shape.R, Shape.R) == 3 + 1


def test_solution_a():
    assert solve_part_a(TEST_INPUT_FILENAME) == 15


def test_import_and_parse_b():
    dataset = parse_data_b(TEST_INPUT_FILENAME)

    assert len(dataset) == 3
    assert dataset[0].opp is Shape.R
    assert dataset[0].res is Result.DRAW


def test_response():
    assert correct_response(Shape.R, Result.WIN) == Shape.P
    assert correct_response(Shape.R, Result.LOSE) == Shape.S
    assert correct_response(Shape.R, Result.DRAW) == Shape.R


def test_solution_b():
    assert solve_part_b(TEST_INPUT_FILENAME) == 12
