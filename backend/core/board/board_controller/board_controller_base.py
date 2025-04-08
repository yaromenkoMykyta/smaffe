from abc import ABC, abstractmethod
from typing import Sequence, TypeVar
from backend.core.board.board_controller.dataclasses import OutputsBoard

T = TypeVar("T")


class BoardControllerBase(ABC):

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    def set_output_high(self, output: OutputsBoard):
        pass
