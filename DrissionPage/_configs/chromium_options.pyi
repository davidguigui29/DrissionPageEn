# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from pathlib import Path
from typing import Union, Any, Literal, Optional, Tuple


class ChromiumOptions(object):
    ini_path: Optional[str] = ...
    _driver_path: str = ...
    _user_data_path: Optional[str] = ...
    _download_path: str = ...
    _tmp_path: str = ...
    _arguments: list = ...
    _browser_path: str = ...
    _user: str = ...
    _load_mode: str = ...
    _timeouts: dict = ...
    _proxy: str = ...
    _address: str = ...
    _extensions: list = ...
    _prefs: dict = ...
    _flags: dict = ...
    _prefs_to_del: list = ...
    _new_env: bool = ...
    clear_file_flags: bool = ...
    _auto_port: Union[Tuple[int, int], False] = ...
    _system_user_path: bool = ...
    _existing_only: bool = ...
    _retry_times: int = ...
    _retry_interval: float = ...
    _is_headless: bool = ...
    _ua_set: bool = ...

    def __init__(self,
                 read_file: [bool, None] = True,
                 ini_path: Union[str, Path] = None):
        """
        :param read_file: whether to read configuration information from the default ini file
        :param ini_path: ini file path, if None, read the default ini file
        """
        ...

    @property
    def download_path(self) -> str:
        """Default download path file path"""
        ...

    @property
    def browser_path(self) -> str:
        """Browser startup file path"""
        ...

    @property
    def user_data_path(self) -> str:
        """Returns the path to the user data folder"""
        ...

    @property
    def tmp_path(self) -> Optional[str]:
        """Returns the temporary folder path"""
        ...

    @property
    def user(self) -> str:
        """Returns the user configuration folder name"""
        ...

    @property
    def load_mode(self) -> str:
        """Returns the page loading strategy, 'normal', 'eager', 'none'"""
        ...

    @property
    def timeouts(self) -> dict:
        """Returns the timeouts settings"""
        ...

    @property
    def proxy(self) -> str:
        """Returns the proxy settings"""
        ...

    @property
    def address(self) -> str:
        """Returns the browser address in the format 'ip:port'"""
        ...

    @property
    def arguments(self) -> list:
        """Returns a list of command-line arguments for the browser"""
        ...

    @property
    def extensions(self) -> list:
        """Returns a list of plugin paths to be loaded"""
        ...

    @property
    def preferences(self) -> dict:
        """Returns the user preferences configuration"""
        ...

    @property
    def flags(self) -> dict:
        """Returns the experimental feature settings"""
        ...

    @property
    def system_user_path(self) -> bool:
        """Returns whether the system-installed browser's user data folder is used"""
        ...

    @property
    def is_existing_only(self) -> bool:
        """Returns whether only an existing browser is taken over"""
        ...

    @property
    def is_auto_port(self) -> Union[bool, Tuple[int, int]]:
        """Returns whether an automatic port and user file is used, or a range tuple if specified"""
        ...

    @property
    def retry_times(self) -> int:
        """Returns the number of retry attempts on connection failure"""
        ...

    @property
    def retry_interval(self) -> float:
        """Returns the retry interval in seconds on connection failure"""
        ...

    @property
    def is_headless(self) -> bool:
        """Returns whether the browser is in headless mode"""
        ...

    def set_retry(self, times: int = None, interval: float = None) -> ChromiumOptions:
        """Sets the retry behavior on connection failure
        :param times: Number of retry attempts
        :param interval: Retry interval in seconds
        :return: Current object
        """
        ...

    def set_argument(self, arg: str, value: Union[str, None, bool] = None) -> ChromiumOptions:
        """Sets an argument for the browser configuration
        :param arg: Argument name
        :param value: Argument value; if None, it's an argument without a value. If False, the argument is removed
        :return: Current object
        """
        ...

    def remove_argument(self, value: str) -> ChromiumOptions:
        """Removes an argument from the configuration
        :param value: Argument name
        :return: Current object
        """
        ...

    def add_extension(self, path: Union[str, Path]) -> ChromiumOptions:
        """Adds a plugin
        :param path: Path to the plugin, can point to a folder
        :return: Current object
        """
        ...

    def remove_extensions(self) -> ChromiumOptions:
        """Removes all plugins
        :return: Current object
        """
        ...

    def set_pref(self, arg: str, value: Any) -> ChromiumOptions:
        """Sets a user preference in the Preferences file
        :param arg: Preference name
        :param value: Preference value
        :return: Current object
        """
        ...

    def remove_pref(self, arg: str) -> ChromiumOptions:
        """Removes a user preference; cannot remove already saved preferences
        :param arg: Preference name
        :return: Current object
        """
        ...

    def remove_pref_from_file(self, arg: str) -> ChromiumOptions:
        """Removes a preference from the user configuration file
        :param arg: Preference name
        :return: Current object
        """
        ...

    def set_flag(self, flag: str, value: Union[int, str, bool] = None) -> ChromiumOptions:
        """Sets an experimental feature flag
        :param flag: Flag name
        :param value: Flag value; if False, the flag is removed
        :return: Current object
        """
        ...

    def clear_flags_in_file(self) -> ChromiumOptions:
        """Removes all experimental flags from the browser configuration file"""
        ...

    def clear_flags(self) -> ChromiumOptions:
        """Clears all flags set in this object"""
        ...

    def clear_arguments(self) -> ChromiumOptions:
        """Clears all arguments set in this object"""
        ...

    def clear_prefs(self) -> ChromiumOptions:
        """Clears all preferences set in this object"""
        ...

    def set_timeouts(self, base: float = None, page_load: float = None, script: float = None) -> ChromiumOptions:
        """Sets timeouts in seconds
        :param base: Default timeout
        :param page_load: Page load timeout
        :param script: Script execution timeout
        :return: Current object
        """
        ...

    def set_user(self, user: str = 'Default') -> ChromiumOptions:
        """Sets the user profile folder to use
        :param user: User profile folder name
        :return: Current object
        """
        ...

    def headless(self, on_off: bool = True) -> ChromiumOptions:
        """Sets whether the browser runs in headless mode
        :param on_off: True to enable, False to disable
        :return: Current object
        """
        ...

    def no_imgs(self, on_off: bool = True) -> ChromiumOptions:
        """Sets whether to load images
        :param on_off: True to disable image loading, False to enable
        :return: Current object
        """
        ...

    def no_js(self, on_off: bool = True) -> ChromiumOptions:
        """Sets whether to disable JavaScript
        :param on_off: True to disable, False to enable
        :return: Current object
        """
        ...

    def mute(self, on_off: bool = True) -> ChromiumOptions:
        """Sets whether to mute the browser
        :param on_off: True to mute, False to unmute
        :return: Current object
        """
        ...

    def incognito(self, on_off: bool = True) -> ChromiumOptions:
        """Sets whether to launch in incognito mode
        :param on_off: True to enable, False to disable
        :return: Current object
        """
        ...

    def new_env(self, on_off: bool = True) -> ChromiumOptions:
        """Sets whether to use a fresh browser environment
        :param on_off: True to enable, False to disable
        :return: Current object
        """
        ...

    def ignore_certificate_errors(self, on_off=True) -> ChromiumOptions:
        """Sets whether to ignore certificate errors
        :param on_off: True to ignore, False to enforce
        :return: Current object
        """
        ...

    def set_user_agent(self, user_agent: str) -> ChromiumOptions:
        """Sets the User-Agent string
        :param user_agent: User-Agent text
        :return: Current object
        """
        ...

    def set_proxy(self, proxy: str) -> ChromiumOptions:
        """Sets the proxy
        :param proxy: Proxy URL and port
        :return: Current object
        """
        ...

    def set_load_mode(self, value: Literal['normal', 'eager', 'none']) -> ChromiumOptions:
        """Sets the load mode, accepts 'normal', 'eager', 'none'
        normal: Waits for all resources to load
        eager: DOM is ready, but resources like images may still be loading
        none: Does not block at all
        :param value: Load mode
        :return: Current object
        """
        ...

    def set_local_port(self, port: Union[str, int]) -> ChromiumOptions:
        """Sets the local port
        :param port: Port number
        :return: Current object
        """
        ...

    def set_address(self, address: str) -> ChromiumOptions:
        """Sets the browser address, format 'ip:port'
        :param address: Browser address
        :return: Current object
        """
        ...

    def set_browser_path(self, path: Union[str, Path]) -> ChromiumOptions:
        """Sets the browser executable path
        :param path: Browser path
        :return: Current object
        """
        ...

    def set_download_path(self, path: Union[str, Path]) -> ChromiumOptions:
        """Sets the download path
        :param path: Download path
        :return: Current object
        """
        ...

    def set_tmp_path(self, path: Union[str, Path]) -> ChromiumOptions:
        """Sets the temporary files path
        :param path: Temporary files path
        :return: Current object
        """
        ...

    def set_user_data_path(self, path: Union[str, Path]) -> ChromiumOptions:
        """Sets the user data folder path
        :param path: User data folder path
        :return: Current object
        """
        ...

    def set_cache_path(self, path: Union[str, Path]) -> ChromiumOptions:
        """Sets the cache path
        :param path: Cache path
        :return: Current object
        """
        ...

    def set_paths(self, browser_path: Union[str, Path] = None, local_port: Union[int, str] = None,
                address: str = None, download_path: Union[str, Path] = None, user_data_path: Union[str, Path] = None,
                cache_path: Union[str, Path] = None) -> ChromiumOptions: ...

    def use_system_user_path(self, on_off: bool = True) -> ChromiumOptions:
        """Sets whether to use the system-installed browser's default user folder
        :param on_off: True to enable, False to disable
        :return: Current object
        """
        ...

    def auto_port(self, on_off: bool = True, scope: Tuple[int, int] = None) -> ChromiumOptions:
        """Automatically acquire an available port
        :param on_off: Enable or disable automatic port selection
        :param scope: Specify port range, default is [9600-59600) if None
        :return: Current object
        """
        ...

    def existing_only(self, on_off: bool = True) -> ChromiumOptions:
        """Only take over an existing browser session
        :param on_off: True to enable, False to disable
        :return: Current object
        """
        ...

    def as_freezer(self) -> ChromiumOptions:
        """Creates a deep copy of the current object to avoid modifying the original"""
        ...

    def save(self, path: Union[str, Path] = None) -> str:
        """Save settings to a file
        :param path: Path to the ini file. If None, saves to the currently loaded configuration file.
                    Pass 'default' to save to the default ini file.
        :return: Absolute path of the saved file
        """
        ...

    def save_to_default(self) -> str:
        """Save the current configuration to the default ini file"""
        ...
