from amsdualit import cli
import sys
from logging import INFO, DEBUG, basicConfig, info


def _setup_logging(verbose: bool = False) -> None:
    """setting up default logging levels
    Args:
        verbose (bool, optional): True sets logging level to DEBUG. False sets logging level to INFO. Defaults to False.
    """
    level = DEBUG if verbose else INFO
    basicConfig(
        format="%(asctime)s - %(levelname)s: %(message)s",
        level=level,
        datefmt="%Y-%m-%d %I:%M:%S %p",
    )


def run(argv: list[str]):
    """entry point
    Args:
        argv (list[str]): raw command line arguments
    """
    # parse command line args
    opts, _ = cli.parse(argv)

    # setting the proper logging level
    _setup_logging(opts.verbose)

    info("Start sending requests ...")

    # run all checks
    print(opts)


if __name__ == "__main__":
    run(sys.argv[1:])
