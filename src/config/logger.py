import logging

from rich.logging import RichHandler

from .settings import settings

FORMAT = "(%(filename)s: %(lineno)d) | %(message)s"


def setup_logging():
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format=FORMAT,
        datefmt="[%X]",
        handlers=[RichHandler()],
    )


setup_logging()
logger = logging.getLogger("backend")
