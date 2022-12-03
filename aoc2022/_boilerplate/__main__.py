"""AoC 2022, Day {{day}}, CLI Code"""

import logging
import sys
from typing import Optional

import click

from aoc2022.utils import (
    CLICK_CONTEXT,
    setup_logging,
    print_day_header,
    print_part_solution,
)
from aoc2022.day{{day_full}} import solve_part_a, solve_part_b


@click.command(context_settings=CLICK_CONTEXT)
@click.argument(
    "PART", required=False, type=click.Choice(["A", "B"], case_sensitive=False)
)
@click.option("-v", "--verbose", count=True)
def cli(part: Optional[str] = None, verbose: int = 0):
    """Print AoC Day {{day}} Solutions

    Will output the solutions for the given day and PART. If PART is omitted,
    all parts' solutions for the day will be output."""

    args = locals().items()
    setup_logging(verbose)
    logger = logging.getLogger(__name__)
    logger.debug(
        "Running with options: %s", ", ".join(f"{k!s}={v!r}" for k, v in args)
    )

    show_output(part)

    return 0


def show_output(part: Optional[str] = None):
    """Print the day's output"""

    print_day_header({{day}})

    if part is None or part.lower() == "a":
        print_part_solution({{day}}, "A", solve_part_a())
    if part is None or part.lower() == "b":
        print_part_solution({{day}}, "B", solve_part_b())


if __name__ == "__main__":
    sys.exit(cli())
