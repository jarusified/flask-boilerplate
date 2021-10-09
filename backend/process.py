from logger import get_logger

LOGGER = get_logger(__name__)


class Process:
    """
    Processing Class.
    """

    def __init__(self):

        LOGGER.info(f"{type(self).__name__} mode enabled.")
