from backend.core.board.board_controller.dataclasses import OutputsBoard

try:
    import RPi.GPIO as GPIO
except ImportError:
    import Mock.GPIO as GPIO

from backend.configs.config import BoardConfig
from backend.core.board.board_controller.board_controller_base import (
    BoardControllerBase,
)


class BoardControllerRaspberry(BoardControllerBase):
    def __init__(self, board_config: BoardConfig):
        self.config = board_config

    def __enter__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.config.output_espresso, GPIO.OUT)
        GPIO.setup(self.config.output_cream, GPIO.OUT)

    def __exit__(self, exc_type, exc_val, exc_tb):
        GPIO.cleanup()

    def set_output_high(self, output: OutputsBoard):
        """

        :param output: the output pin on the board

        :return: None
        """
        if output == OutputsBoard.Cream:
            GPIO.output(self.config.output_cream, GPIO.HIGH)
        elif output == OutputsBoard.Espresso:
            GPIO.output(self.config.output_espresso, GPIO.HIGH)
