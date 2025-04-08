import os
from typing import Optional

import yaml
from pydantic import BaseModel

from backend.tools.logger import get_logger


class BoardConfig(BaseModel):
    output_cream: int
    output_espresso: int


class LoggerConfig(BaseModel):
    logging_level: int


class ApiConfig(BaseModel):
    cors_allowed_origins: list[str]
    host: str
    port: int


class GlobalConfig(BaseModel):
    api: ApiConfig
    logger: LoggerConfig
    board_config: BoardConfig


DEFAULT_CONFIG_PATH = os.path.join("configs", "default_config.yaml")
_global_config: Optional[GlobalConfig] = None


def load_config() -> GlobalConfig:
    """
    load the config data and return GlobalConfig object

    :return: GlobalConfig object
    """
    global _global_config
    logger = get_logger(__name__)
    if _global_config is None:

        with open(DEFAULT_CONFIG_PATH) as config_file:
            config = yaml.safe_load(config_file)

        _global_config = GlobalConfig.model_validate(config)
        logger.setLevel(_global_config.logger.logging_level)

        logger.info("loaded default config")
    return _global_config
