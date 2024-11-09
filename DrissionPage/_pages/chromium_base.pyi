# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from pathlib import Path
from typing import Union, Tuple, Any, Optional, Literal

from requests import Session

from .chromium_page import ChromiumPage
from .chromium_tab import ChromiumTab
from .mix_tab import MixTab
from .web_page import WebPage
from .._base.base import BasePage
from .._base.chromium import Chromium
from .._base.driver import Driver
from .._elements.chromium_element import ChromiumElement
from .._elements.session_element import SessionElement
from .._functions.cookies import CookiesList
from .._functions.elements import SessionElementsList, ChromiumElementsList
from .._pages.chromium_frame import ChromiumFrame
from .._units.actions import Actions
from .._units.console import Console
from .._units.listener import Listener
from .._units.rect import TabRect
from .._units.screencast import Screencast
from .._units.scroller import Scroller, PageScroller
from .._units.setter import ChromiumBaseSetter
from .._units.states import PageStates
from .._units.waiter import BaseWaiter

PIC_TYPE = Literal['jpg', 'jpeg', 'png', 'webp', True]


class ChromiumBase(BasePage):
    """Tab, Frame, Page base class"""
    _tab: Union[ChromiumTab, MixTab, ChromiumFrame, ChromiumPage, WebPage] = ...
    _browser: Chromium = ...
    _driver: Optional[Driver] = ...
    _frame_id: str = ...
    _is_reading: bool = ...
    _is_timeout: bool = ...
    _timeouts: Timeout = ...
    _first_run: bool = ...
    _is_loading: Optional[bool] = ...
    _load_mode: str = ...
    _scroll: Optional[Scroller] = ...
    _url: str = ...
    _root_id: Optional[str] = ...
    _upload_list: Optional[list] = ...
    _wait: Optional[BaseWaiter] = ...
    _set: Optional[ChromiumBaseSetter] = ...
    _screencast: Optional[Screencast] = ...
    _actions: Optional[Actions] = ...
    _listener: Optional[Listener] = ...
    _states: Optional[PageStates] = ...
    _alert: Alert = ...
    _has_alert: bool = ...
    _auto_handle_alert: Optional[bool] = ...
    _doc_got: bool = ...
    _load_end_time: float = ...
    _init_jss: list = ...
    _ready_state: Optional[str] = ...
    _rect: Optional[TabRect] = ...
    _console: Optional[Console] = ...
    _disconnect_flag: bool = ...
    _type: str = ...

    def __init__(self,
                 browser: Chromium,
                 tab_id: str = None):
        """
        :param browser: Chromium
        :param tab_id: The tab id to be controlled. If not specified, the default is the active tab
        """
        ...

    def __call__(self,
                 locator: Union[Tuple[str, str], str, ChromiumElement],
                 index: int = 1,
                 timeout: float = None) -> ChromiumElement:
        """Find an element internally
        Example: ele = page('@id=ele_id')
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param index: The element to get, starting from 1, and a negative number can be passed in to get the last element
        :param timeout: Timeout (seconds)
        :return: ChromiumElement object
        """
        ...

    def _d_set_runtime_settings(self) -> None: ...

    def _connect_browser(self, target_id: str = None) -> None:
        """Connect to the browser and run for the first time
        :param target_id: target id to be controlled, if not specified, the default is the active tab
        :return: None
        """
        ...

    def _driver_init(self, target_id: str) -> None:
        """CDP parameter initialization to be performed after creating a new page or refreshing the page
        :param target_id: target id to jump to
        :return: None
        """
        ...

    def _get_document(self, timeout: float = 10) -> bool:
        """Get the page document
        :param timeout: timeout (seconds)
        :return: whether the acquisition is successful
        """
        ...

    def _onFrameDetached(self, **kwargs) -> None: ...

    def _onFrameAttached(self, **kwargs) -> None: ...

    def _onFrameStartedLoading(self, **kwargs):
        """Execute when the page starts loading"""
        ...

    def _onFrameNavigated(self, **kwargs):
        """Execute when the page jumps"""
        ...

    def _onDomContentEventFired(self, **kwargs):
        """Re-read the page content after the page is refreshed or changed"""
        ...

    def _onLoadEventFired(self, **kwargs):
        """Re-read the page content after the page is refreshed or changed"""
        ...

    def _onFrameStoppedLoading(self, **kwargs):
        """Execute after the page is loaded"""
        ...

    def _onFileChooserOpened(self, **kwargs):
        """Execute when the file selection box is opened"""
        ...

    def _wait_to_stop(self):
        """Stop loading the page when the eager strategy times out"""
        ...

    @property
    def wait(self) -> BaseWaiter:
        """Returns the object to wait for."""
        ...

    @property
    def set(self) -> ChromiumBaseSetter:
        """Returns the object used for settings"""
        ...

    @property
    def screencast(self) -> Screencast:
        """Returns the object used for screen recording"""
        ...

    @property
    def actions(self) -> Actions:
        """Returns the object used to execute the action chain."""
        ...

    @property
    def listen(self) -> Listener:
        """Returns the object used to listen for packets"""
        ...

    @property
    def states(self) -> PageStates:
        """Returns an object for getting status information"""
        ...

    @property
    def scroll(self) -> PageScroller:
        """Returns the object used to scroll the scroll bar."""
        ...

    @property
    def rect(self) -> TabRect:
        """Returns the object that gets the window coordinates and size"""
        ...

    @property
    def console(self) -> Console:
        """Returns the object that gets the console information"""
        ...

    @property
    def timeout(self) -> float:
        """Return timeout settings"""
        ...

    @property
    def timeouts(self) -> Timeout:
        """Return the timeouts setting"""
        ...

    @property
    def browser(self) -> Chromium:
        """Returns the browser object"""
        ...

    @property
    def driver(self) -> Driver:
        """Returns the Driver object used to control the browser"""
        ...

    @property
    def title(self) -> str:
        """Return the current page title"""
        ...

    @property
    def url(self) -> str:
        """Return the current page URL"""
        ...

    @property
    def _browser_url(self) -> str:
        """Used to be covered by MixTab"""
        ...

    @property
    def html(self) -> str:
        """Return the HTML text of the current page"""
        ...

    @property
    def json(self) -> Union[dict, None]:
        """When the return content is in json format, it returns the corresponding dictionary, and returns None when it is not in json format"""
        ...

    @property
    def tab_id(self) -> str:
        """Return the current tab id"""
        ...

    @property
    def _target_id(self) -> str:
        """Return the current tab id"""
        ...

    @property
    def active_ele(self) -> ChromiumElement:
        """Returns the currently focused element"""
        ...

    @property
    def load_mode(self) -> Literal['none', 'normal', 'eager']:
        """Returns the page loading strategy, there are 3 types: 'none', 'normal', 'eager'"""
        ...

    @property
    def user_agent(self) -> str:
        """Returns the user agent"""
        ...

    @property
    def upload_list(self) -> list:
        """Return to the list of files waiting to be uploaded"""
        ...

    @property
    def session(self)->Session:
        """Returns the Session object used for switching modes or downloading."""
        ...

    @property
    def _js_ready_state(self) -> str:
        """Returns the ready state information obtained by js"""
        ...

    def run_cdp(self, cmd: str, **cmd_args) -> dict:
        """Execute Chrome DevTools Protocol statement
        :param cmd: protocol item
        :param cmd_args: parameters
        :return: execution result
        """
        ...

    def run_cdp_loaded(self, cmd: str, **cmd_args) -> dict:
        """Execute Chrome DevTools Protocol statements, waiting for the page to load before executing
        :param cmd: protocol project
        :param cmd_args: parameters
        :return: execution result
        """
        ...

    def _run_cdp(self, cmd: str, **cmd_args) -> dict:
        """Execute Chrome DevTools Protocol statement
        :param cmd: protocol item
        :param cmd_args: parameters
        :return: execution result
        """
        ...

    def _run_cdp_loaded(self, cmd: str, **cmd_args) -> dict:
        """Execute Chrome DevTools Protocol statements, waiting for the page to load before executing
        :param cmd: protocol project
        :param cmd_args: parameters
        :return: execution result
        """
        ...

    def run_js(self, script: Union[str, Path], *args, as_expr: bool = False, timeout: float = None) -> Any:
        """Run javascript code
        :param script: js text or js file path
        :param args: parameters, corresponding to arguments[0], arguments[1]... in js text in order
        :param as_expr: whether to run as an expression, args is invalid when True
        :param timeout: js timeout (seconds), if None, use the page timeouts.script setting
        :return: the result of the run
        """
        ...

    def run_js_loaded(self, script: Union[str, Path], *args, as_expr: bool = False, timeout: float = None) -> Any:
        """Run javascript code, wait for the page to load before executing
        :param script: js text or js file path
        :param args: parameters, corresponding to arguments[0], arguments[1]... in the js text in order
        :param as_expr: whether to run as an expression, args is invalid when True
        :param timeout: js timeout (seconds), use the page timeouts.script property value when None
        :return: the result of running
        """
        ...

    def _run_js(self, script: Union[str, Path], *args, as_expr: bool = False, timeout: float = None) -> Any:
        """Run javascript code
        :param script: js text or js file path
        :param args: parameters, corresponding to arguments[0], arguments[1]... in js text in order
        :param as_expr: whether to run as an expression, args is invalid when True
        :param timeout: js timeout (seconds), if None, use the page timeouts.script setting
        :return: the result of the run
        """
        ...

    def _run_js_loaded(self, script: Union[str, Path], *args, as_expr: bool = False, timeout: float = None) -> Any:
        """Run javascript code, wait for the page to load before executing
        :param script: js text or js file path
        :param args: parameters, corresponding to arguments[0], arguments[1]... in the js text in order
        :param as_expr: whether to run as an expression, args is invalid when True
        :param timeout: js timeout (seconds), use the page timeouts.script property value when None
        :return: the result of running
        """
        ...

    def run_async_js(self, script: Union[str, Path], *args, as_expr: bool = False) -> None:
        """Execute js code or js file path asynchronously
        :param script: js text
        :param args: parameters, corresponding to arguments[0], arguments[1]... in the js text in order
        :param as_expr: whether to run as an expression, args is invalid when True
        :return: None
        """
        ...

    def get(self, url: str, show_errmsg: bool = False, retry: int = None,
            interval: float = None, timeout: float = None) -> Union[None, bool]:
        """Access url
        :param url: target url
        :param show_errmsg: whether to display and throw exceptions
        :param retry: number of retries, use the retry_times attribute value of the page object when None
        :param interval: retry interval (seconds), use the retry_interval attribute value of the page object when None
        :param timeout: connection timeout (seconds), use the timeouts.page_load attribute value of the page object when None
        :return: whether the target url is available
        """
        ...

    def cookies(self, all_domains: bool = False, all_info: bool = False) -> CookiesList:
        """Return cookies information
        :param all_domains: whether to return cookies for all domains
        :param all_info: whether to return all information, only name, value, domain are returned when False
        :return: cookies information
        """
        ...

    def ele(self,
            locator: Union[Tuple[str, str], str, ChromiumElement, ChromiumFrame],
            index: int = 1,
            timeout: float = None) -> ChromiumElement:
        """Get an element object that meets the conditions
        :param locator: locator or element object
        :param index: the element to get, starting from 1, you can pass in a negative number to get the last element
        :param timeout: search timeout (seconds), the default is the same as the page waiting time
        :return: ChromiumElement object
        """
        ...

    def eles(self,
             locator: Union[Tuple[str, str], str],
             timeout: float = None) -> ChromiumElementsList:
        """Get all element objects that meet the conditions
        :param locator: locator or element object
        :param timeout: search timeout (seconds), the default is the same as the page waiting time
        :return: a list of ChromiumElement objects
        """
        ...

    def s_ele(self,
              locator: Union[Tuple[str, str], str] = None,
              index: int = 1,
              timeout: float = None) -> SessionElement:
        """Find an element that meets the conditions and return it in the form of SessionElement. 
        It is very efficient when processing complex pages. 
        :param locator: The location information of the element, which can be a loc tuple or a query string. 
        :param index: The index to get, starting from 1, and a negative number can be passed in to get the last index. 
        :param timeout: The timeout for finding an element (seconds), which is the same as the page waiting time by default. 
        :return: SessionElement object or attribute, text. 
        """
        ...

    def s_eles(self,
               locator: Union[Tuple[str, str], str],
               timeout: float = None) -> SessionElementsList:
        """Find all elements that meet the conditions and return them as a list of SessionElement
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param timeout: The timeout for finding an element (seconds), which is the same as the page waiting time by default
        :return: A list of SessionElement objects
        """
        ...

    def _find_elements(self,
                       locator: Union[Tuple[str, str], str, ChromiumElement, ChromiumFrame],
                       timeout: float,
                       index: Optional[int] = 1,
                       relative: bool = False,
                       raise_err: bool = None) -> Union[ChromiumElement, ChromiumFrame, ChromiumElementsList]:
        """Perform element search
        :param locator: locator or element object
        :param timeout: search timeout (seconds)
        :param index: the result, starting from 1, you can pass in a negative number to get the last result, if None, return all
        :param relative: MixTab parameter indicating whether relative positioning
        :param raise_err: whether to throw an exception if the element cannot be found, if None, according to the global settings
        :return: ChromiumElement object or list of element objects
        """
        ...

    def refresh(self, ignore_cache: bool = False) -> None:
        """Refresh the current page
        :param ignore_cache: whether to ignore the cache
        :return: None
        """
        ...

    def forward(self, steps: int = 1) -> None:
        """Go forward a number of steps in the browsing history
        :param steps: number of steps forward
        :return: None
        """
        ...

    def back(self, steps: int = 1) -> None:
        """Go back a number of steps in the browsing history
        :param steps: number of steps to go back
        :return: None
        """
        ...

    def _forward_or_back(self, steps: int) -> None:
        """Execute the browser forward or backward, skipping the history with the same URL
        :param steps: number of steps
        :return: None
        """
        ...

    def stop_loading(self) -> None:
        """The page stopped loading"""
        ...

    def remove_ele(self, loc_or_ele: Union[ChromiumElement, ChromiumFrame, str, Tuple[str, str]]) -> None:
        """Remove an element from the page
        :param loc_or_ele: element object or locator
        :return: None
        """
        ...

    def add_ele(self,
                html_or_info: Union[str, Tuple[str, dict]],
                insert_to: Union[ChromiumElement, str, Tuple[str, str], None] = None,
                before: Union[ChromiumElement, str, Tuple[str, str], None] = None) -> ChromiumElement:
        """Create a new element
        :param html_or_info: HTML text or information of the new element. The information format is: (tag, {attr1: value, ...})
        :param insert_to: Which element to insert into, can receive element object and locator, if it is None and it is html, add it to body, if it is not html, do not insert
        :param before: Before which child node to insert, can receive object and locator, if it is None, insert it to the end of the parent element
        :return: Element object
        """
        ...

    def get_frame(self,
                  loc_ind_ele: Union[str, int, tuple, ChromiumFrame, ChromiumElement],
                  timeout: float = None) -> ChromiumFrame:
        """Get a frame object in the page
        :param loc_ind_ele: locator, iframe number, ChromiumFrame object, the number starts from 1, and a negative number can be passed in to get the last one
        :param timeout: find element timeout (seconds)
        :return: ChromiumFrame object
        """
        ...

    def get_frames(self,
                   locator: Union[str, tuple] = None,
                   timeout: float = None) -> ChromiumElementsList:
        """Get all frame objects that meet the conditions
        :param locator: locator, return all if None
        :param timeout: search timeout (seconds)
        :return: list of ChromiumFrame objects
        """
        ...

    def session_storage(self, item: str = None) -> Union[str, dict, None]:
        """Return sessionStorage information. If item is not set, all items will be retrieved
        :param item: item to be retrieved. If not set, all items will be returned
        :return: one or all items of sessionStorage
        """
        ...

    def local_storage(self, item: str = None) -> Union[str, dict, None]:
        """Return localStorage information. If item is not set, all items will be retrieved
        :param item: the item to be retrieved. If not set, all items will be returned
        :return: one or all items of localStorage
        """
        ...

    def get_screenshot(self, path: [str, Path] = None, name: str = None, as_bytes: PIC_TYPE = None,
                       as_base64: PIC_TYPE = None, full_page: bool = False, left_top: Tuple[int, int] = None,
                       right_bottom: Tuple[int, int] = None) -> Union[str, bytes]:
        """Screenshot the page. You can take screenshots of the entire webpage, visible webpage, or a specified range. Screenshots outside the visible range require browser support of version 90 or above
        :param path: Save path
        :param name: Full file name, optional suffix 'jpg','jpeg','png','webp'
        :param as_bytes: Whether to return the image in byte form, optional 'jpg','jpeg','png','webp', when effective, path parameters and as_base64 parameters are invalid
        :param as_base64: Whether to return the image in base64 string form, optional 'jpg','jpeg','png','webp', when effective, path parameters are invalid
        :param full_page: Whether to take a full page screenshot, True to capture the entire webpage, False to capture the visible window
        :param left_top: The coordinates of the upper left corner of the capture range
        :param right_bottom: The coordinates of the lower right corner of the capture range
        :return: Full path or byte text of the image
        """
        ...

    def add_init_js(self, script: str) -> str:
        """Add an initialization script to be executed before any script is loaded on the page
        :param script: js text
        :return: id of the added script
        """
        ...

    def remove_init_js(self, script_id: str = None) -> None:
        """Delete the initialization script. Delete all scripts when None is passed to js_id
        :param script_id: script id
        :return: None
        """
        ...

    def clear_cache(self, session_storage: bool = True, local_storage: bool = True, cache: bool = True,
                    cookies: bool = True) -> None:
        """Clear cache, optional items to clear
        :param session_storage: whether to clear sessionStorage
        :param local_storage: whether to clear localStorage
        :param cache: whether to clear cache
        :param cookies: whether to clear cookies
        :return: None
        """
        ...

    def disconnect(self) -> None:
        """Disconnect from the page without closing it"""
        ...

    def reconnect(self, wait: float = 0) -> None:
        """Disconnect from the original page and reconnect
        :param wait: Wait for a few seconds after disconnecting before reconnecting
        :return: None
        """
        ...

    def handle_alert(self, accept: Optional[bool] = True, send: str = None, timeout: float = None,
                     next_one: bool = False) -> Union[str, False]:
        """Process the prompt box, and automatically wait for the prompt box to appear
        :param accept: True means confirmation, False means cancellation, None will not press the button but still return the text value
        :param send: You can enter text when processing the prompt prompt box
        :param timeout: The timeout (seconds) for waiting for the prompt box to appear. If None, use the value of the self.timeout attribute
        :param next_one: Whether to process the next prompt box. When True, the timeout parameter is invalid
        :return: The text of the prompt box content. If the prompt box is not waiting, False is returned
        """
        ...

    def _handle_alert(self, accept: bool = True, send: str = None, timeout: float = None,
                      next_one: bool = False) -> Union[str, False]:
        """Process the prompt box, and automatically wait for the prompt box to appear
        :param accept: True means confirmation, False means cancellation, other values ​​will not press the button but still return the text value
        :param send: You can enter text when processing the prompt prompt box
        :param timeout: The timeout (seconds) for waiting for the prompt box to appear. If it is None, use the value of the self.timeout attribute
        :param next_one: Whether to process the next prompt box. When it is True, the timeout parameter is invalid
        :return: The text of the prompt box content. If the prompt box is not waiting, False is returned
        """
        ...

    def _on_alert_open(self, **kwargs):
        """The method triggered when alert appears"""
        ...

    def _on_alert_close(self, **kwargs):
        """The method triggered when alert is closed"""
        ...

    def _wait_loaded(self, timeout: float = None) -> bool:
        """Wait for the page to load, and stop loading if the page is loaded after a timeout
        :param timeout: timeout (seconds)
        :return: Success or failure, return False if the page is loaded after a timeout
        """
        ...

    def _d_connect(self, to_url: str, times: int = 0, interval: float = 1, show_errmsg: bool = False,
                   timeout: float = None) -> Union[bool, None]:
        """Try to connect, retry several times
        :param to_url: URL to be accessed
        :param times: Number of retries
        :param interval: Retry interval (seconds)
        :param show_errmsg: Whether to throw an exception
        :param timeout: Connection timeout (seconds)
        :return: Whether it is successful, return None to indicate uncertainty
        """
        ...

    def _get_screenshot(self, path: [str, Path] = None, name: str = None, as_bytes: PIC_TYPE = None,
                        as_base64: PIC_TYPE = None, full_page: bool = False, left_top: Tuple[float, float] = None,
                        right_bottom: Tuple[float, float] = None, ele: ChromiumElement = None) -> Union[str, bytes]:
        """Screenshot the page. You can take screenshots of the entire webpage, visible webpage, or a specified range. Screenshots outside the visible range require browser support of version 90 or above
        :param path: Save path
        :param name: Full file name, optional suffix 'jpg','jpeg','png','webp'
        :param as_bytes: Whether to return the image in byte form, optional 'jpg','jpeg','png','webp', when effective, path parameters and as_base64 parameters are invalid
        :param as_base64: Whether to return the image in base64 string form, optional 'jpg','jpeg','png','webp', when effective, path parameters are invalid
        :param full_page: Whether to take a full page screenshot, True to capture the entire webpage, False to capture the visible window
        :param left_top: The coordinates of the upper left corner of the capture range
        :param right_bottom: The coordinates of the lower right corner of the capture range
        :param ele: Set the screenshot of the element in the foreign iframe
        :return: The full path of the image or byte text
        """
        ...


class Timeout(object):
    """Class used to save d mode timeout information"""
    base: float = ...
    page_load: float = ...
    script: float = ...

    def __init__(self, base=None, page_load=None, script=None):
        """
        :param base: default timeout
        :param page_load: page load timeout
        :param script: js timeout
        """
        ...

    @property
    def as_dict(self) -> dict:
        """Return the timeout settings in dict format"""
        ...


class Alert(object):
    """Class used to save alert information"""
    activated: Optional[bool] = ...
    text: Optional[str] = ...
    type: Optional[str] = ...
    defaultPrompt: Optional[str] = ...
    response_accept: Optional[str] = ...
    response_text: Optional[str] = ...
    handle_next: Optional[bool] = ...
    next_text: Optional[str] = ...
    auto: Optional[bool] = ...

    def __init__(self, auto: bool = None): ...
