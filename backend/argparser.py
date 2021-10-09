import argparse
from logger import get_logger

LOGGER = get_logger(__name__)


class ArgParser:
    """
    Argparser class decodes the arguments passed to
    """

    def __init__(self, args_string):

        assert isinstance(args_string, list)

        # Parse the arguments passed.
        self.parser = ArgParser._create_parser()
        self.args = vars(self.parser.parse_args())

        # Verify if only valid things are passed.
        self.mode = self._verify_parser()
        LOGGER.info(f"Mode: {self.mode}")

    def __str__(self):
        items = ("%s = %r" % (k, v) for k, v in self.__dict__.items())
        return "<%s: {%s}> \n" % (self.__class__.__name__, ", ".join(items))

    def __repr__(self):
        return self.__str__()

    # --------------------------------------------------------------------------
    # Private methods.
    @staticmethod
    def _create_parser():
        """
        Parse the input arguments.
        """
        parser = argparse.ArgumentParser(prefix_chars="--")
        parser.add_argument("--process", action="store_true", help="Process mode. ")
        parser.add_argument(
            "--http",
            action="store_true",
            help="Server mode." "Spawns a http server to render the views.",
        )
        return parser

    def _verify_parser(self):
        """
        Verify the input arguments.

        Raises expections if something is not provided
        Check if the config file is provided and exists!

        :pargs : argparse.Namespace
            Arguments passed by the user.

        Returns
        -------
        """

        _has_process = self.args["process"] is not None
        _has_http = self.args["http"] is not None

        if not _has_process and not _has_http:
            s = "Please choose an option: --process or --http."
            LOGGER.error(s)
            self.parser.print_help()
            exit(1)

        if _has_http:
            mode = "HTTP"

        if _has_process:
            mode = "PROCESS"

        return mode
