"""
This module provides functions to control the preparation of espresso and cream caffe.

It utilizes the `BoardControllerRaspberry` class to manage GPIO pins for controlling
the outputs of the board. The module includes functions to prepare espresso and cream
caffe by setting the respective output pins to HIGH.
"""

from backend.tools.logger import Logger
from backend.configs.config import ConfigLoader
from backend.core.board.board_controller.board_controller_raspberry import (
    BoardControllerRaspberry,
)
from backend.core.board.board_controller.dataclasses import OutputsBoard

# Initialize a logger for the module
LOGGER = Logger.get_logger(__name__)
CONFIG = ConfigLoader.load_config()


def make_espresso():
    """
    Prepares an espresso by setting the corresponding output pin to HIGH.

    :return: None
    """
    board_config = CONFIG.board_config  # Load the configuration for the board

    board = BoardControllerRaspberry(board_config)  # Initialize the board controller

    LOGGER.info("started of making caffe espresso")  # Log the action

    with board:
        board.set_output_high(OutputsBoard.ESPRESSO)  # Set the espresso output to HIGH


def make_cream_caffe():
    """
    Prepares a cream caffe by setting the corresponding output pin to HIGH.

    :return: None
    """
    board_config = CONFIG.board_config  # Load the configuration for the board

    board = BoardControllerRaspberry(board_config)  # Initialize the board controller

    LOGGER.info("started of making cream caffe")  # Log the action

    with board:
        board.set_output_high(OutputsBoard.CREAM)  # Set the cream caffe output to HIGH
