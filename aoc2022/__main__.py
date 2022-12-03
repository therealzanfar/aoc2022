#! /usr/bin/env python3

"""Console script for aoc2022."""

from importlib import import_module
import logging
import sys
from typing import Optional

import click

from aoc2022.utils import (
    CLICK_CONTEXT,
    PACKAGE_NAME,
    setup_logging,
    find_available_days,
    day_module_name,
    print_aoc_header,
)


@click.command(context_settings=CLICK_CONTEXT)
@click.argument("DAY", required=False, type=int)
@click.argument(
    "PART", required=False, type=click.Choice(["A", "B"], case_sensitive=False)
)
@click.option("-v", "--verbose", count=True)
def cli(
    day: Optional[int] = None, part: Optional[str] = None, verbose: int = 0
) -> int:
    """Main entry point for aoc2022

    Will output the solutions for the given DAY and PART. If PART is omitted,
    all parts' solutions for the day will be output. If DAY is omitted, all
    days' solutions available will be output."""

    args = locals().items()
    setup_logging(verbose)
    logger = logging.getLogger(__name__)
    logger.debug(
        "Running with options: %s", ", ".join(f"{k!s}={v!r}" for k, v in args)
    )

    available_days = list(find_available_days())
    logger.debug("Available days: %s", repr(available_days))

    print_aoc_header()

    for d in available_days:
        if day is None or day == d:
            day_module = import_module(
                f"{PACKAGE_NAME}.{day_module_name(d)}.__main__"
            )
            day_module.show_output(part)

        else:
            logger.info("Day %d was not selected for output", d)

    return 0


if __name__ == "__main__":
    sys.exit(cli())
