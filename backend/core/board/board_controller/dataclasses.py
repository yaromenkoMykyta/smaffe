"""
This module defines the data structures and enumerations used for the board controller.

It includes:
- An enumeration (`OutputsBoard`) to represent the output types for the board.
"""

from enum import Enum


class OutputsBoard(Enum):
    """
    Enum representing the output types for the board.

    Attributes:
        ESPRESSO (int): Represents the espresso output, with a value of 0.
        CREAM (int): Represents the cream output, with a value of 1.
    """
    ESPRESSO = 0
    CREAM = 1
