import logging
from typing import Optional


_logger: Optional[logging.Logger] = None


def get_logger(name: str) -> logging.Logger:
    """
    get the global logger, that provides the modular logging
    once called, the function returns the same logger

    :param name: name of the module

    :return: logger for the specified module
    """
    global _logger
    if _logger is None:
        logging.addLevelName(0, "info")
        logging.addLevelName(1, "debug")
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=logging.DEBUG,
        )

        _logger = logging.getLogger(name)

    return _logger
