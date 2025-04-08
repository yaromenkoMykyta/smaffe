from backend.tools.logger import get_logger
from backend.configs.config import load_config
from backend.core.board.board_controller.board_controller_raspberry import (
    BoardControllerRaspberry,
)
from backend.core.board.board_controller.dataclasses import OutputsBoard

logger = get_logger(__name__)


def make_espresso():
    cfg = load_config()
    with BoardControllerRaspberry(cfg.board_config) as board:
        board.set_output_high(OutputsBoard.Espresso)
    logger.info("started make caffe espresso")


def make_cream_caffe():
    cfg = load_config()
    board = BoardControllerRaspberry(cfg.board_config)
    with board:
        board.set_output_high(OutputsBoard.Cream)
    logger.info("started make cream caffe")
