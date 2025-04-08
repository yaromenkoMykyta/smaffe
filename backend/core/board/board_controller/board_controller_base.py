"""
This module defines the base class for board controllers.

It provides an abstract base class (`BoardControllerBase`) that outlines the
required methods for implementing a board controller, such as setting outputs
to high values and managing context.
"""

from abc import ABC, abstractmethod
from typing import TypeVar
from backend.core.board.board_controller.dataclasses import OutputsBoard

T = TypeVar("T")


class BoardControllerBase(ABC):
    """
    Abstract base class for board controllers.

    This class defines the interface for board controllers, including methods
    for setting outputs and managing context.
    """

    @abstractmethod
    def __enter__(self):
        """
        Enter the runtime context related to this object.

        :return: The object itself.
        """

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the runtime context related to this object.

        :param exc_type: The exception type, if an exception occurred.
        :param exc_val: The exception value, if an exception occurred.
        :param exc_tb: The traceback object, if an exception occurred.
        :return: None
        """

    @abstractmethod
    def set_output_high(self, output: OutputsBoard) -> None:
        """
        Set a specific output of the board to a HIGH value.

        :param output: The output pin to set to HIGH.
        :return: None
        """
