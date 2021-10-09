import os
import sys

from logger import init_logger, get_logger
from argparser import ArgParser
from controller import Controller
from services import yourService

APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", 5000))
APP_NAME = "Flask - Backend"
APP_VERSION = "0.0.1.beta"

LOGGER = get_logger(__name__)


def main():
    """
    Entry point.
    Performs actions depending on the passed arguments
    :return None
    """

    # Start logging.
    log_level = 1 if "--verbose" in sys.argv else 2
    init_logger(level=log_level)

    LOGGER.info(f"Initialize {APP_NAME} - {APP_VERSION}")
    LOGGER.profile(f"Initialized {APP_NAME}")

    args = ArgParser(sys.argv)
    http = args.args["http"]

    if http:
        wip = Controller(yourService)
        wip.start(host=APP_HOST, port=APP_PORT)


if __name__ == "__main__":
    main()
