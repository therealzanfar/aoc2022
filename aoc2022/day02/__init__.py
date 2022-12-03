"""AoC 2022, Day 2, Functional Code"""

from enum import Enum, auto
from pathlib import Path
from typing import NamedTuple, Optional, cast


class ShapeDef(NamedTuple):
    """Shape Definition"""

    name: str
    score: int


class Shape(ShapeDef, Enum):
    """Shape Enumeration"""

    R = ("Rock", 1)
    P = ("Paper", 2)
    S = ("Scissors", 3)


class Result(Enum):
    """Result Enumeration"""

    WIN = auto()
    LOSE = auto()
    DRAW = auto()


class Round(NamedTuple):
    """Round Object"""

    opp: Shape
    you: Optional[Shape] = None
    res: Optional[Result] = None


GUIDE_MAPPING_A: dict[str, Shape] = {
    "A": Shape.R,
    "B": Shape.P,
    "C": Shape.S,
    "X": Shape.R,
    "Y": Shape.P,
    "Z": Shape.S,
}


GUIDE_MAPPING_B: dict[str, Result] = {
    "X": Result.LOSE,
    "Y": Result.DRAW,
    "Z": Result.WIN,
}


def parse_data_a(input_filename: str | Path) -> list[Round]:
    """Read a datafile and return the representative dataset"""

    rounds: list[Round] = []

    with open(input_filename, "r", encoding="utf-8") as input_fh:
        for line in input_fh:
            a, b = line.strip().split(" ")

            rounds.append(
                Round(
                    opp=GUIDE_MAPPING_A[a],
                    you=GUIDE_MAPPING_A[b],
                )
            )

    return rounds


def parse_data_b(input_filename: str | Path) -> list[Round]:
    """Read a datafile and return the representative dataset"""

    rounds: list[Round] = []

    with open(input_filename, "r", encoding="utf-8") as input_fh:
        for line in input_fh:
            a, b = line.strip().split(" ")

            rounds.append(
                Round(
                    opp=GUIDE_MAPPING_A[a],
                    res=GUIDE_MAPPING_B[b],
                )
            )

    return rounds


def is_win(opp: Shape, you: Shape) -> Optional[bool]:
    """Returns True if you beats opp, False if opp beats you, and None if
    the game is a draw"""

    if opp is you:
        return None

    if (
        (opp is Shape.R and you is Shape.P)
        or (opp is Shape.P and you is Shape.S)
        or (opp is Shape.S and you is Shape.R)
    ):
        return True

    return False


def score(opp: Shape, you: Shape) -> int:
    """Returns the points won in a round"""

    round_score = you.score
    result = is_win(opp, you)

    if result is True:
        round_score += 6
    elif result is None:
        round_score += 3

    return round_score


def correct_response(opp: Shape, res: Result) -> Shape:
    """Determine the correct response to force the result"""

    if (
        (opp is Shape.S and res is Result.WIN)
        or (opp is Shape.P and res is Result.LOSE)
        or (opp is Shape.R and res is Result.DRAW)
    ):
        return Shape.R

    if (
        (opp is Shape.R and res is Result.WIN)
        or (opp is Shape.S and res is Result.LOSE)
        or (opp is Shape.P and res is Result.DRAW)
    ):
        return Shape.P

    return Shape.S


def solve_part_a(filename: str = "aoc2022/day02/puzzle_input.txt"):
    """Part A Solution"""

    dataset = parse_data_a(filename)
    return sum(score(r.opp, cast(Shape, r.you)) for r in dataset)


def solve_part_b(filename: str = "aoc2022/day02/puzzle_input.txt"):
    """Part B Solution"""

    dataset = parse_data_b(filename)
    total_score = 0

    for r in dataset:
        assert r.res is not None

        you = correct_response(r.opp, r.res)
        total_score += score(r.opp, you)

    return total_score
