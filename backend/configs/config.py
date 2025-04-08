"""
This module contains the configuration management for the application.

It defines configuration models using Pydantic and provides a function
to load the configuration from a YAML file.
"""

import os
from typing import Optional

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

    _DEFAULT_CONFIG_PATH = os.path.join("configs", "default_config.yaml")

    _instance: Optional[GlobalConfig] = None

    @classmethod
    def load_config(cls) -> GlobalConfig:
        """
        Load the configuration data from the default YAML file and return a GlobalConfig object.

        This method ensures the configuration is loaded only once.

        :return: GlobalConfig object
        """
        logger = Logger.get_logger(__name__)
        if cls._instance is None:
            with open(cls._DEFAULT_CONFIG_PATH, encoding="utf-8") as config_file:
                config = yaml.safe_load(config_file)

            cls._instance = GlobalConfig.model_validate(config)
            logger.setLevel(cls._instance.logger.logging_level)

            logger.info("Loaded default config")
        return cls._instance
