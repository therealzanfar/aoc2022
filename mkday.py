#! /usr/bin/env python3

from typing import Optional
import logging
from pathlib import Path
import sys

import click
from jinja2 import PackageLoader, Environment

from aoc2022.utils import (
    CLICK_CONTEXT,
    setup_logging,
)

PACKAGE_NAME = "aoc2022"


@click.command(context_settings=CLICK_CONTEXT)
@click.argument("DAY", required=True, type=int)
@click.option("-v", "--verbose", count=True)
def main(day: Optional[int] = None, verbose: int = 0):
    """Generate boilerplate for a new challenge day"""

    args = locals().items()
    setup_logging(verbose)
    logger = logging.getLogger(__name__)
    logger.debug(
        "Running with options: %s", ", ".join(f"{k!s}={v!r}" for k, v in args)
    )

    if day is None:
        logger.error("No day number specified")
        return 1

    context = {
        "day": day,
        "day_full": f"{day:02d}",
    }
    output_path = Path(f"{PACKAGE_NAME}/day{context['day_full']}")
    template_path = Path(f"{PACKAGE_NAME}/_boilerplate")

    if output_path.exists():
        logger.error("Output path ('%s') already exists", output_path)
        return 1

    if not template_path.exists():
        logger.error("Template path ('%s') cannot be found", template_path)
        return 1

    logger.info("Creating output path: %s", output_path)
    output_path.mkdir()

    jinja_env = Environment(
        loader=PackageLoader(PACKAGE_NAME, template_path.name)
    )

    for template_file in template_path.iterdir():
        if not template_file.is_file():
            logger.debug("Skipping non-file '%s'", template_file.name)
            continue

        logger.info("Generating file from '%s' template", template_file.name)

        output_file = output_path / template_file.name

        jinja_template = jinja_env.get_template(template_file.name)
        with open(output_file, "w", encoding="utf-8") as output_fh:
            output_fh.write(jinja_template.render(**context))


if __name__ == "__main__":
    sys.exit(main())
