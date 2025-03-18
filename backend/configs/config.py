import os
from typing import Optional

import yaml
from pydantic import BaseModel

from backend.core.board_controll.caffee_controller import logger


class LoggerConfig(BaseModel):
    logging_level: int


class ApiConfig(BaseModel):
    cors_allowed_origins: list[str]
    host: str
    port: int


class GlobalConfig(BaseModel):
    api: ApiConfig
    logger: LoggerConfig


DEFAULT_CONFIG_PATH = os.path.join("configs", "default_config.yaml")
_global_config: Optional[GlobalConfig] = None


def load_config() -> GlobalConfig:
    """
    load default config. returns the global config;

    :return: global config with the data from yaml
    """
    global _global_config
    if _global_config is None:

        with open(DEFAULT_CONFIG_PATH) as config_file:
            config = yaml.safe_load(config_file)

        _global_config = GlobalConfig.model_validate(config)
        logger.setLevel(_global_config.logger.logging_level)

        logger.info("loaded default config")
        return _global_config
