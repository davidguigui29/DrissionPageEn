# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from threading import Lock
from typing import List, Optional, Set, Dict, Union, Tuple, Literal

from .driver import BrowserDriver, Driver
from .._configs.chromium_options import ChromiumOptions
from .._configs.session_options import SessionOptions
from .._functions.cookies import CookiesList
from .._pages.chromium_base import Timeout
from .._pages.chromium_tab import ChromiumTab
from .._pages.mix_tab import MixTab
from .._units.downloader import DownloadManager
from .._units.setter import BrowserSetter
from .._units.states import BrowserStates
from .._units.waiter import BrowserWaiter


class Chromium(object):
    _BROWSERS: dict = ...
    _lock: Lock = ...

    id: str = ...
    address: str = ...
    version: str = ...
    retry_times: int = ...
    retry_interval: float = ...

    _set: Optional[BrowserSetter] = ...
    _wait: Optional[BrowserWaiter] = ...
    _states: Optional[BrowserStates] = ...
    _chromium_options: ChromiumOptions = ...
    _session_options: SessionOptions = ...
    _driver: BrowserDriver = ...
    _frames: dict = ...
    _drivers: Dict[str, Driver] = ...
    _all_drivers: Dict[str, Set[Driver]] = ...
    _process_id: Optional[int] = ...
    _dl_mgr: DownloadManager = ...
    _timeouts: Timeout = ...
    _load_mode: str = ...
    _download_path: str = ...
    _auto_handle_alert: Optional[bool] = ...
    _is_exists: bool = ...
    _is_headless: bool = ...
    _disconnect_flag: bool = ...

    def __new__(cls,
                addr_or_opts: Union[str, int, ChromiumOptions] = None,
                session_options: Union[SessionOptions, None, False] = None):
        """

        :param addr_or_opts: browser address: port, ChromiumOptions object or port number (int)
        :param session_options: default session configuration used when using dual-mode Tab, None uses ini file configuration, False does not read from ini
        """
        ...

    def __init__(self, addr_or_opts: Union[str, int, ChromiumOptions] = None,
                 session_options: Union[SessionOptions, None, False] = None):
        """
        :param addr_or_opts: browser address: port, ChromiumOptions object or port number (int)
        :param session_options: default session configuration used when using dual-mode Tab, None uses ini file configuration, False does not read from ini
        """
        ...

    @property
    def user_data_path(self) -> str:
        """Returns the user folder path"""
        ...

    @property
    def process_id(self) -> Optional[int]:
        """Return the browser process id"""
        ...

    @property
    def timeout(self) -> float:
        """Return the base timeout setting"""
        ...

    @property
    def timeouts(self) -> Timeout:
        """Return all timeout settings"""
        ...

    @property
    def load_mode(self) -> Literal['none', 'normal', 'eager']:
        """Returns the page loading mode, including 'none', 'normal', 'eager'"""
        ...

    @property
    def download_path(self) -> str:
        """Return to the default download path"""
        ...

    @property
    def set(self) -> BrowserSetter:
        """Returns the object used for settings"""
        ...

    @property
    def states(self) -> BrowserStates:
        """Returns an object for getting status"""
        ...

    @property
    def wait(self) -> BrowserWaiter:
        """返回用于等待的对象"""
        ...

    @property
    def tabs_count(self) -> int:
        """Return the number of tabs, only count page and webview types"""
        ...

    @property
    def tab_ids(self) -> List[str]:
        """Returns a list of all tab ids, only counting page and webview types"""
        ...

    @property
    def latest_tab(self) -> Union[MixTab, str]:
        """Returns the latest tab page, which is the last created or last activated tab page.
        When Settings.singleton_tab_obj==True, it returns the Tab object, otherwise it returns the tab id
        """
        ...

    def cookies(self, all_info: bool = False) -> CookiesList:
        """以list格式返回所有域名的cookies
        :param all_info: 是否返回所有内容，False则只返回name, value, domain
        :return: cookies组成的列表
        """
        ...

    def new_tab(self,
                url: str = None,
                new_window: bool = False,
                background: bool = False,
                new_context: bool = False) -> MixTab:
        """Create a new tab
        :param url: URL to which the new tab jumps, create a new empty tab when None
        :param new_window: whether to open the tab in a new window, invalid in incognito mode
        :param background: whether to disable the new tab, invalid in incognito mode, guest mode and when new_window is True
        :param new_context: whether to create an independent environment, invalid in incognito mode and guest mode
        :return: new tab object
        """
        ...

    def get_tab(self,
                id_or_num: Union[str, int] = None,
                title: str = None,
                url: str = None,
                tab_type: Union[str, list, tuple] = 'page',
                as_id: bool = False) -> Union[MixTab, str]:
        """Get a tab object. When id_or_num is not None, the following parameters are invalid
        :param id_or_num: The tab id or serial number to be obtained. The serial number starts from 1. You can pass in a negative number to get the last one. It is not the visual order, but the activation order
        :param title: The text to match the title, fuzzy matching, if None, it matches all
        :param url: The text to match the url, fuzzy matching, if None, it matches all
        :param tab_type: Tab type, you can enter multiple in a list, such as 'page', 'iframe', etc., if None, it matches all
        :param as_id: Whether to return the tab id instead of the tab object
        :return: Tab object
        """
        ...

    def get_tabs(self,
                 title: str = None,
                 url: str = None,
                 tab_type: Union[str, list, tuple] = 'page',
                 as_id: bool = False) -> List[MixTab, str]:
        """Find the tabs that meet the conditions and return a list of them. Title and url are in relation
        :param title: The text to match the title
        :param url: The text to match the url
        :param tab_type: The tab type, multiple can be entered as a list
        :param as_id: Whether to return the tab id instead of the tab object
        :return: Tab object list
        """
        ...

    def close_tabs(self,
                   tabs_or_ids: Union[str, ChromiumTab, List[Union[str, ChromiumTab]],
                   Tuple[Union[str, ChromiumTab]]],
                   others: bool = False) -> None:
        """Close the passed tabs, multiple tabs can be passed in
        :param tabs_or_ids: the specified tab object or id, multiple tabs can be passed in as a list or tuple
        :param others: whether to close tabs other than the specified tab
        :return: None
        """
        ...

    def activate_tab(self, id_ind_tab: Union[int, str, ChromiumTab]) -> None:
        """ Display a tab page to the front
        :param id_ind_tab: tab page id (str), Tab object or tab page number (int), the number starts from 1
        :return: None
        """
        ...

    def reconnect(self) -> None:
        """Disconnect and reconnect"""
        ...

    def clear_cache(self, cache: bool = True, cookies: bool = True) -> None:
        """Clear cache, optional items to clear
        :param cache: whether to clear cache
        :param cookies: whether to clear cookies
        :return: None
        """
        ...

    def quit(self, timeout: float = 5, force: bool = False, del_data: bool = False) -> None:
        """Close the browser
        :param timeout: timeout (in seconds) for waiting for the browser to close
        :param force: whether to force the process to terminate immediately
        :param del_data: whether to delete the user folder
        :return: None
        """
        ...

    def _new_tab(self,
                 mix: bool = True,
                 url: str = None,
                 new_window: bool = False,
                 background: bool = False,
                 new_context: bool = False) -> Union[ChromiumTab, MixTab]:
        """Create a new tab
        :param mix: whether to create MixTab
        :param url: the URL to which the new tab jumps
        :param new_window: whether to open the tab in a new window
        :param background: whether to disable the new tab, if new_window is True, it will be invalid
        :param new_context: whether to create a new context
        :return: new tab object
        """
        ...

    def _get_tab(self,
                 id_or_num: Union[str, int] = None,
                 title: str = None,
                 url: str = None,
                 tab_type: Union[str, list, tuple] = 'page',
                 mix: bool = True,
                 as_id: bool = False) -> Union[ChromiumTab, str]:
        """Get a tab object. When id_or_num is not None, the following parameters are invalid
        :param id_or_num: The id or serial number of the tab to be obtained. The serial number starts from 1. You can pass in a negative number to get the last one. It is not the visual order, but the activation order
        :param title: The text to match the title, fuzzy matching, if None, it matches all
        :param url: The text to match the url, fuzzy matching, if None, it matches all
        :param tab_type: Tab type, multiple lists can be entered, such as 'page', 'iframe', etc., if None, it matches all
        :param mix: Whether to return a Tab object with switchable modes
        :param as_id: Whether to return the tab id instead of the tab object, invalid when mix=False
        :return: Tab object
        """
        ...

    def _get_tabs(self,
                  title: str = None,
                  url: str = None,
                  tab_type: Union[str, list, tuple] = 'page',
                  mix: bool = True,
                  as_id: bool = False) -> List[ChromiumTab, str]:
        """Find the tabs that meet the conditions and return a list of them. Title and url are in relation
        :param title: The text to match the title
        :param url: The text to match the url
        :param tab_type: The tab type, multiple can be entered as a list
        :param mix: Whether to return a Tab object with switchable modes
        :param as_id: Whether to return the tab id instead of the tab object, invalid when mix=False
        :return: Tab object list
        """
        ...

    def _run_cdp(self, cmd, **cmd_args) -> dict:
        """Execute Chrome DevTools Protocol statement
        :param cmd: protocol item
        :param cmd_args: parameters
        :return: execution result
        """
        ...

    def _get_driver(self, tab_id: str, owner=None) -> Driver:
        """Create and return a Driver for the specified tab id
        :param tab_id: tab id
        :param owner: the object that uses the driver
        :return: Driver object
        """
        ...

    def _onTargetCreated(self, **kwargs): ...

    def _onTargetDestroyed(self, **kwargs): ...

    def _on_disconnect(self): ...
