"""AoC 2022, Day 3, Functional Code"""

from pathlib import Path
from typing import Iterable, Iterator, Optional, Any, TypeVar

PUZZLE_INPUT_FILENAME = Path("aoc2022/day03/puzzle_input.txt")


def parse_data(input_filename: str | Path) -> list[str]:
    """Read a datafile and return the representative dataset"""

    with open(input_filename, "r", encoding="utf-8") as input_fh:
        return [line.strip() for line in input_fh]


def split_compartments(pack: str) -> tuple[str, str]:
    """Split a pack representation into it's two compartments"""

    half = len(pack) // 2
    return pack[:half], pack[half:]


def item_in_common(a: str, *other: str) -> str:
    """Find the item in common between two compartments"""

    common = set(a)
    for b in other:
        common.intersection_update(set(b))

    return common.pop()


def priority(item: str) -> int:
    """Get the priority of an item"""

    if item.islower():
        return ord(item) - ord("a") + 1

    if item.isupper():
        return ord(item) - ord("A") + 27

    return 0


GT = TypeVar("GT")


def group_by(i: Iterable[GT], size: int = 2) -> Iterator[tuple[GT, ...]]:
    """Break an iterable up into size pieces"""

    it = iter(i)
    ret = []

    try:
        while True:
            for _ in range(size):
                ret.append(next(it))
            yield tuple(ret)
            ret = []
    except StopIteration:
        if ret:
            yield tuple(ret)


def solve_part_a(filename: str | Path = PUZZLE_INPUT_FILENAME):
    """Part A Solution"""

    dataset = parse_data(filename)
    total_priority = 0

    for pack in dataset:
        a, b = split_compartments(pack)
        common = item_in_common(a, b)
        total_priority += priority(common)

    return total_priority


def solve_part_b(filename: str | Path = PUZZLE_INPUT_FILENAME):
    """Part B Solution"""

    dataset = parse_data(filename)
    total_priority = 0

    for group in group_by(dataset, 3):
        common = item_in_common(*group)
        total_priority += priority(common)

    return total_priority
