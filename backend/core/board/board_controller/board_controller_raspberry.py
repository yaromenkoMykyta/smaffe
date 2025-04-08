"""
This module implements the Raspberry Pi-specific board controller.

It provides the `BoardControllerRaspberry` class, which extends the
`BoardControllerBase` to control board outputs using GPIO pins.
"""

try:
    from RPi import GPIO
except ImportError:
    from Mock import GPIO

from backend.configs.config import BoardConfig
from backend.core.board.board_controller.board_controller_base import (
    BoardControllerBase,
)
from backend.core.board.board_controller.dataclasses import OutputsBoard


class BoardControllerRaspberry(BoardControllerBase):
    """
    Raspberry Pi-specific implementation of the `BoardControllerBase`.

    This class manages GPIO pins to control board outputs for espresso and cream.
    """

    def __init__(self, board_config: BoardConfig):
        """
        Initialize the board controller with the given configuration.

        :param board_config: The configuration object containing GPIO pin mappings.
        """
        self.config = board_config

    def __enter__(self):
        """
        Set up the GPIO pins for the board outputs.

        :return: None
        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.config.output_espresso, GPIO.OUT)
        GPIO.setup(self.config.output_cream, GPIO.OUT)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Clean up the GPIO pins when exiting the context.

        :param exc_type: The exception type, if an exception occurred.
        :param exc_val: The exception value, if an exception occurred.
        :param exc_tb: The traceback object, if an exception occurred.
        :return: None
        """
        GPIO.cleanup()

    def set_output_high(self, output: OutputsBoard):
        """
        Set a specific output of the board to a HIGH value.

        :param output: The output pin to set to HIGH (either CREAM or ESPRESSO).
        :return: None
        """
        if output == OutputsBoard.CREAM:
            GPIO.output(self.config.output_cream, GPIO.HIGH)
        elif output == OutputsBoard.ESPRESSO:
            GPIO.output(self.config.output_espresso, GPIO.HIGH)
