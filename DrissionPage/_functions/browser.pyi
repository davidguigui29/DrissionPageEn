# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from typing import Union

from .._configs.chromium_options import ChromiumOptions


def connect_browser(option: ChromiumOptions) -> bool:
    """Connect or start the browser
    :param option: ChromiumOptions object
    :return: Returns whether the browser is taken over
    """
    ...


def get_launch_args(opt: ChromiumOptions) -> list:
    """Get command line startup parameters from ChromiumOptions
    :param opt: ChromiumOptions
    :return: startup parameter list
    """
    ...


def set_prefs(opt: ChromiumOptions) -> None:
    """Process the prefs item in the startup configuration. Currently, only existing folders can be configured.
    :param opt: ChromiumOptions
    :return: None
    """
    ...


def set_flags(opt: ChromiumOptions) -> None:
    """Process the flags item in the launch configuration
    :param opt: ChromiumOptions
    :return: None
    """
    ...


def test_connect(ip: str, port: Union[int, str], timeout: float = 30) -> bool:
    """Test whether the browser is available
    :param ip: browser ip
    :param port: browser port
    :param timeout: timeout (seconds)
    :return: None
    """
    ...


def get_chrome_path(ini_path: str) -> Union[str, None]:
    """Get the path of the chrome executable file from the ini file or system variables
    :param ini_path: ini file path
    :return: file path
    """
    ...
