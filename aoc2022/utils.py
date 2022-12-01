"""AoC 2022 CLI Utility Functions"""

from importlib.resources import contents
import logging
from typing import Iterator

from rich import print as rprint
from rich.logging import RichHandler


PACKAGE_NAME = "aoc2022"
CLICK_CONTEXT = {"help_option_names": ["-h", "--help"]}


def setup_logging(verbosity: int = 0):
    """Setup a root logger with console output

    Args:
        verbosity (int, optional): The logging level; 0=Error, 1=Warning,
            2=Info, 3+=Debug. Defaults to 0.
    """

    logging_level = logging.ERROR
    if verbosity == 1:
        logging_level = logging.WARNING
    elif verbosity == 2:
        logging_level = logging.INFO
    elif verbosity >= 3:
        logging_level = logging.DEBUG

    logging.basicConfig(
        level=logging_level,
        format="%(message)s",
        datefmt="[%x]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )


def day_module_name(d: int) -> str:
    """Format a day index into a module name"""

    return f"day{d:02d}"


def find_available_days() -> Iterator[int]:
    """Identify the days which have solutions"""

    logger = logging.getLogger(__name__)

    top_modules = contents(PACKAGE_NAME)
    logger.debug("Top-level modules: %s", repr(top_modules))

    possible_days = list(range(1, 25 + 1))
    for d in possible_days:
        day_module = day_module_name(d)
        if day_module in top_modules:

            day_modules = contents(f"{PACKAGE_NAME}.{day_module}")
            logger.debug("Day %d modules: %s", d, repr(day_modules))

            if "__main__.py" in day_modules:
                yield d
            else:
                logger.debug(
                    "Day %d package does not have __MAIN__ resource", d
                )
        else:
            logger.debug("Day %d package does not exist", d)


def print_aoc_header():
    """Print a top-level output banner"""

    rprint("[bold white]=== AoC 2022 Solutions ===[/bold white]")


def print_day_header(day: int):
    """Print a day output banner"""

    rprint(f"[bold blue]--- AoC 2022, Day {day:2} ---[/bold blue]")


def print_part_solution(day: int, part: str, solution: int):
    """Print a part's solution"""

    rprint(
        f"  Day [blue]{day:02d}[/blue], "
        f"Part [green]{part:1s}[/green] "
        f"Solution: [red]{solution:6d}[/red]"
    )
