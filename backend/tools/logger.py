"""
This module provides a utility class to retrieve or initialize a global logger.

The `Logger` class ensures that a single logger instance is used globally
throughout the application. It configures the logging format and levels if the
logger is not already initialized.
"""

import logging


class Logger:
    """
    Singleton class to manage the logger instance.
    """

    _instance: logging.Logger = None


    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        """
        Retrieve or initialize a global logger for the specified module.

        This method ensures that a single logger instance is used globally
        throughout the application. If the logger is not already initialized,
        it sets up the logging configuration and creates a new logger.

        :param name: The name of the module requesting the logger.
        :return: A logger instance configured for the specified module.
        """
        if cls._instance is None:
            logging.addLevelName(0, "info")
            logging.addLevelName(1, "debug")
            name = name.split(".")[-1]

            logging.basicConfig(
                format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=logging.DEBUG,
            )
            cls._instance = logging.getLogger(name)

        return cls._instance
