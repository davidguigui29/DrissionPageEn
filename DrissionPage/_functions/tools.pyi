# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from os import popen
from pathlib import Path
from threading import Lock
from typing import Union, Tuple

from .._pages.chromium_base import ChromiumBase


class PortFinder(object):
    used_port: set = ...
    prev_time: float = ...
    lock: Lock = ...
    tmp_dir: Path = ...
    checked_paths: set = ...

    def __init__(self, path: Union[str, Path] = None):
        """
        :param path: temporary file storage path, use the system temporary folder when None
        """
        ...

    @staticmethod
    def get_port(scope: Tuple[int, int] = None) -> Tuple[int, str]:
        """Find an available port
        :param scope: specifies the port range, excluding the last number, if None, use [9600-59600)
        :return: A tuple consisting of an available port and a user folder path
        """
        ...


def port_is_using(ip: str, port: Union[str, int]) -> bool:
    """Check if the port is occupied
    :param ip: browser address
    :param port: browser port
    :return: bool
    """
    ...


def clean_folder(folder_path: Union[str, Path], ignore: Union[tuple, list] = None) -> None:
    """Clear a folder, except for the files and folders in ignore
    :param folder_path: the folder path to be cleared
    :param ignore: ignore list
    :return: None
    """
    ...


def show_or_hide_browser(page: ChromiumBase, hide: bool = True) -> None:
    """Executes showing or hiding the browser window
    :param page: ChromePage object
    :param hide: whether to hide
    :return: None
    """
    ...


def get_browser_progress_id(progress: Union[popen, None], address: str) -> Union[str, None]:
    """Get the browser process id
    :param progress: known process object, pass None if none
    :param address: browser management address, including port
    :return: process id or None
    """
    ...


def get_hwnds_from_pid(pid: Union[str, int], title: str) -> list:
    """Query handle ID by PID
    :param pid: process id
    :param title: window title
    :return: list of process handles
    """
    ...


def wait_until(function: callable, kwargs: dict = None, timeout: float = 10):
    """Wait for the returned value of the passed method to be not false
    :param function: method to be executed
    :param kwargs: method parameters
    :param timeout: timeout (seconds)
    :return: execution result, throw TimeoutError if timeout
    """
    ...


def configs_to_here(save_name: Union[Path, str] = None) -> None:
    """Copy the default ini file to the current directory
    :param save_name: specifies the file name, if None, it will be named 'dp_configs.ini'
    :return: None
    """
    ...


def raise_error(result: dict, ignore=None, user: bool = False) -> None:
    """Throw error and report the corresponding error
    :param result: dict containing error
    :param ignore: errors to be ignored
    :param user: whether it is called by the user
    :return: None
    """
    ...
