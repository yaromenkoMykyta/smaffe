"""
This module contains the configuration management for the application.

It defines configuration models using Pydantic and provides a function
to load the configuration from a YAML file.
"""

import os
from typing import Optional

import pydantic.v1.utils
import yaml
from pydantic import BaseModel

from backend.tools.logger import Logger


class BoardConfig(BaseModel):
    """
    Configuration for the board, including output settings for cream and espresso.
    """

    output_cream: int
    output_espresso: int


class LoggerConfig(BaseModel):
    """
    Configuration for the logger, including the logging level.
    """

    logging_level: int


class ApiConfig(BaseModel):
    """
    Configuration for the API, including CORS settings, host, and port.
    """

    cors_allowed_origins: list[str]
    host: str
    port: int


class GlobalConfig(BaseModel):
    """
    Global configuration that combines API, logger, and board configurations.
    """

    api: ApiConfig
    logger: LoggerConfig
    board_config: BoardConfig


class ConfigLoader:
    """
    Singleton class to manage the configuration instance.
    """

    _DEFAULT_CONFIG_PATHS = [
            os.path.join("configs", "app_configs", "default_config.yaml"),
            os.path.join("configs", "app_configs", "local_config.yaml")
        ]

    _instance: Optional[GlobalConfig] = None

    @classmethod
    def load_config(cls) -> GlobalConfig:
        """
        Load the configuration data from the default YAML file and return a GlobalConfig object.

        This method ensures the configuration is loaded only once.

        :return: GlobalConfig object
        """
        logger = Logger.get_logger(__name__)

        config_data: dict[str, any] = {}

        if cls._instance is None:
            for path in cls._DEFAULT_CONFIG_PATHS:
                if os.path.isfile(path):
                    logger.info("load_config %s ", path)
                    with open(path) as file:
                        current_config_data: dict[str, any] = yaml.safe_load(file)
                        if current_config_data is None:
                            continue
                        config_data = pydantic.v1.utils.deep_update(config_data, current_config_data)

                else:
                    logger.warning("Path %s doesn't exist", path)
            cls._instance = GlobalConfig.model_validate(config_data)
            logger.setLevel(cls._instance.logger.logging_level)

            logger.info("Config loaded")

        return cls._instance
