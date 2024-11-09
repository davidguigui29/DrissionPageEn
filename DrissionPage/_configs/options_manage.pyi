# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from configparser import RawConfigParser
from pathlib import Path
from typing import Any, Optional, Union


class OptionsManager(object):
    ini_path: Optional[Path] = ...
    file_exists: bool = ...
    _conf: RawConfigParser = ...

    def __init__(self, path: Union[Path, str] = None):
        """Initialize and read the configuration file.
        If no temporary folder is set, it will create one.
        :param path: Path to the ini file. If None, it will look in the project folder.
                     If not found, it will read from the module folder.
        """
        ...

    def __getattr__(self, item) -> dict:
        """Return information from a major section in dictionary format.
        :param item: Name of the section
        :return: None
        """
        ...

    def get_value(self, section: str, item: str) -> Any:
        """Get the value from the configuration.
        :param section: Name of the section
        :param item: Name of the item
        :return: Value of the item
        """
        ...

    def get_option(self, section: str) -> dict:
        """Return the content of the section as a dictionary.
        :param section: Name of the section
        :return: Dictionary generated from the section's content
        """
        ...

    def set_item(self, section: str, item: str, value: Any) -> None:
        """Set a configuration value.
        :param section: Name of the section
        :param item: Name of the item
        :param value: Value of the item
        :return: None
        """
        ...

    def remove_item(self, section: str, item: str) -> None:
        """Remove a configuration value.
        :param section: Name of the section
        :param item: Name of the item
        :return: None
        """
        ...

    def save(self, path: str = None) -> str:
        """Save the configuration file.
        :param path: Path to the ini file. Pass 'default' to save to the default ini file.
        :return: Path where the configuration was saved
        """
        ...

    def save_to_default(self) -> str:
        """Save the current configuration to the default ini file."""
        ...

    def show(self) -> None:
        """Print all settings information."""
        ...
