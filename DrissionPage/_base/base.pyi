# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from abc import abstractmethod
from typing import Union, Tuple, List, Any, Optional, Dict

from DownloadKit import DownloadKit
from requests import Session
from requests.structures import CaseInsensitiveDict

from .._configs.session_options import SessionOptions
from .._elements.chromium_element import ChromiumElement
from .._elements.none_element import NoneElement
from .._elements.session_element import SessionElement
from .._functions.elements import SessionElementsList
from .._pages.chromium_frame import ChromiumFrame
from .._pages.chromium_page import ChromiumPage
from .._pages.session_page import SessionPage
from .._pages.web_page import WebPage


class BaseParser(object):
    _type: str
    timeout: float

    def __call__(self, locator: Union[Tuple[str, str], str], index: int = 1): ...

    def ele(self,
            locator: Union[Tuple[str, str], str, BaseElement],
            index: int = 1,
            timeout: float = None): ...

    def eles(self, locator: Union[Tuple[str, str], str], timeout=None): ...

    def find(self,
             locators: Union[str, List[str], tuple],
             any_one: bool = True,
             first_ele: bool = True,
             timeout: float = None) -> Union[Dict[str, ChromiumElement], Dict[str, SessionElement],
    Dict[str, List[ChromiumElement]], Dict[str, List[SessionElement]]]:
        """Pass in multiple locators and get multiple ele
        :param locators: list of locators
        :param any_one: return if any locator finds a result
        :param first_ele: whether each locator only gets the first element
        :param timeout: timeout (seconds)
        :return: dict composed of multiple locators, return a list if first_only is False, otherwise an element, return False if there is no result
        """
        ...

    # ----------------The following properties or methods are to be implemented by future generations----------------
    @property
    def html(self) -> str: ...

    def s_ele(self,
              locator: Union[Tuple[str, str], str, BaseElement, None] = None,
              index: int = 1) -> SessionElement: ...

    def s_eles(self, locator: Union[Tuple[str, str], str]) -> SessionElementsList: ...

    def _ele(self,
             locator: Union[Tuple[str, str], str],
             timeout: float = None,
             index: Optional[int] = 1,
             raise_err: bool = None,
             method: str = None): ...

    def _find_elements(self,
                       locator: Union[Tuple[str, str], str],
                       timeout: float,
                       index: Optional[int] = 1,
                       relative: bool = False,
                       raise_err: bool = None): ...


class BaseElement(BaseParser):
    owner: BasePage = ...

    def __init__(self, owner: BasePage = None): ...

    @property
    def timeout(self) -> float:
        """Returns the timeout period for searching elements."""
        ...

    # ----------------The following properties or methods are implemented by descendants----------------
    @property
    def tag(self) -> str: ...

    def parent(self, level_or_loc: Union[tuple, str, int] = 1): ...

    def prev(self, index: int = 1) -> None: ...

    def prevs(self) -> None: ...

    def next(self, index: int = 1): ...

    def nexts(self): ...

    def get_frame(self, loc_or_ind, timeout=None) -> ChromiumFrame:
        """Get a frame object in the element
        :param loc_or_ind: Locator, iframe serial number, serial number starts from 1, negative numbers can be passed to get the last
        :param timeout: Find element timeout (seconds)
        :return: ChromiumFrame Object
        """
        ...

    def _ele(self,
             locator: Union[Tuple[str, str], str],
             timeout: float = None,
             index: Optional[int] = 1,
             relative: bool = False,
             raise_err: bool = None,
             method: str = None):
        """Call the method to get the element
        :param locator: locator
        :param timeout: timeout (seconds)
        :param index: the index to get, starting from 1, you can pass in a negative number to get the last index
        :param relative: whether to position relatively
        :param raise_err: whether to throw an exception when not found
        :param method: the name of the method to call
        :return: element object or a list of them
        """
        ...


class DrissionElement(BaseElement):
    """Base class for ChromiumElement and SessionElement, but not for ShadowRoot"""

    def __init__(self, owner: BasePage = None): ...

    @property
    def link(self) -> str:
        """Returns the href or src absolute url"""
        ...

    @property
    def css_path(self) -> str:
        """Return the css path"""
        ...

    @property
    def xpath(self) -> str:
        """Return the xpath path"""
        ...

    @property
    def comments(self) -> list:
        """Returns a list of element annotation text."""
        ...

    def texts(self, text_node_only: bool = False) -> list:
        """Returns the text of all direct child nodes within an element, including elements and text nodes
        :param text_node_only: whether to return only text nodes
        :return: text list
        """
        ...

    def parent(self,
               level_or_loc: Union[tuple, str, int] = 1,
               index: int = 1,
               timeout: float = None) -> Union[DrissionElement, None]:
        """Returns the parent element of a certain level above. You can specify the number of levels or use query syntax to locate
        :param level_or_loc: the parent element of the level, starting from 1, or locator
        :param index: when level_or_loc passes in the locator, use this parameter to select the result of the level, starting from 1
        :param timeout: time (seconds)
        :return: parent element object
        """
        ...

    def child(self,
              locator: Union[Tuple[str, str], str, int] = '',
              index: int = 1,
              timeout: float = None,
              ele_only: bool = True) -> Union[DrissionElement, str, NoneElement]:
        """Returns a list of direct child elements or nodes, which can be filtered using query syntax
        :param locator: Query syntax used for filtering
        :param index: The number of query results, starting from 1
        :param timeout: Timeout for finding nodes (seconds)
        :param ele_only: Whether to get only elements, if False, text and comment nodes are also included
        :return: A list of direct child elements or node text
        """
        ...

    def prev(self,
             locator: Union[Tuple[str, str], str, int] = '',
             index: int = 1,
             timeout: float = None,
             ele_only: bool = True) -> Union[DrissionElement, str, NoneElement]:
        """Returns the previous sibling element. You can use query syntax to filter. You can specify the number of the filtered results to return
        :param locator: Query syntax used for filtering
        :param index: The number of the previous query result, starting from 1
        :param timeout: The timeout for finding nodes (seconds)
        :param ele_only: Whether to only get elements, if False, text and comment nodes are also included
        :return: sibling elements
        """
        ...

    def next(self,
             locator: Union[Tuple[str, str], str, int] = '',
             index: int = 1,
             timeout: float = None,
             ele_only: bool = True) -> Union[DrissionElement, str, NoneElement]:
        """Returns the next sibling element. You can use query syntax to filter. You can specify the number of the filter results to return
        :param locator: Query syntax used for filtering
        :param index: The next query result, starting from 1
        :param timeout: Timeout for finding nodes (seconds)
        :param ele_only: Whether to only get elements, if False, text and comment nodes are also included
        :return: sibling element
        """
        ...

    def before(self,
               locator: Union[Tuple[str, str], str, int] = '',
               index: int = 1,
               timeout: float = None,
               ele_only: bool = True) -> Union[DrissionElement, str, NoneElement]:
        """Returns the previous sibling element. You can use query syntax to filter. You can specify the number of the filtered results to return
        :param locator: Query syntax used for filtering
        :param index: The number of the previous query result, starting from 1
        :param timeout: The timeout for finding nodes (seconds)
        :param ele_only: Whether to only get elements, if False, text and comment nodes are also included
        :return: An element or node before this element
        """
        ...

    def after(self,
              locator: Union[Tuple[str, str], str, int] = '',
              index: int = 1,
              timeout: float = None,
              ele_only: bool = True) -> Union[DrissionElement, str, NoneElement]:
        """Returns a sibling element behind. You can use query syntax to filter. You can specify the number of the filter results to return
        :param locator: Query syntax used for filtering
        :param index: The number of the query result behind, starting from 1
        :param timeout: The timeout for finding nodes (seconds)
        :param ele_only: Whether to get only elements, if False, text and comment nodes are also included
        :return: An element or node after this element
        """
        ...

    def children(self,
                 locator: Union[Tuple[str, str], str] = '',
                 timeout: float = None,
                 ele_only: bool = True) -> List[Union[DrissionElement, str]]:
        """Returns a list of direct child elements or nodes, which can be filtered using query syntax
        :param locator: Query syntax used for filtering
        :param timeout: Timeout for finding nodes (seconds)
        :param ele_only: Whether to get only elements, if False, text and comment nodes are also included
        :return: A list of direct child elements or node text
        """
        ...

    def prevs(self,
              locator: Union[Tuple[str, str], str] = '',
              timeout: float = None,
              ele_only: bool = True) -> List[Union[DrissionElement, str]]:
        """Returns a list of all previous sibling elements or nodes, which can be filtered using query syntax
        :param locator: Query syntax used for filtering
        :param timeout: Timeout for finding nodes (seconds)
        :param ele_only: Whether to get only elements, if False, text and comment nodes are also included
        :return: List of sibling elements or node text
        """
        ...

    def nexts(self,
              locator: Union[Tuple[str, str], str] = '',
              timeout: float = None,
              ele_only: bool = True) -> List[Union[DrissionElement, str]]:
        """Returns a list of all the following sibling elements or nodes, which can be filtered using query syntax
        :param locator: Query syntax used for filtering
        :param timeout: Timeout for finding nodes (seconds)
        :param ele_only: Whether to get only elements, if False, text and comment nodes are also included
        :return: List of sibling elements or node text
        """
        ...

    def befores(self,
                locator: Union[Tuple[str, str], str] = '',
                timeout: float = None,
                ele_only: bool = True) -> List[Union[DrissionElement, str]]:
        """Returns a list of all the following sibling elements or nodes, which can be filtered using query syntax
        :param locator: Query syntax used for filtering
        :param timeout: Timeout for finding nodes (seconds)
        :param ele_only: Whether to get only elements, if False, text and comment nodes are also included
        :return: A list of the elements or nodes preceding this element
        """
        ...

    def afters(self,
               locator: Union[Tuple[str, str], str] = '',
               timeout: float = None,
               ele_only: bool = True) -> List[Union[DrissionElement, str]]:
        """Returns a list of all previous sibling elements or nodes, which can be filtered using query syntax
        :param locator: Query syntax used for filtering
        :param timeout: Timeout for finding nodes (seconds)
        :param ele_only: Whether to get only elements, if False, text and comment nodes are also included
        :return: A list of elements or nodes following this element
        """
        ...

    def _get_relative(self,
                      func: str,
                      direction: str,
                      brother: bool,
                      locator: Union[Tuple[str, str], str] = '',
                      index: int = 1,
                      timeout: float = None,
                      ele_only: bool = True) -> DrissionElement:
        """Get a relative element or node. You can use query syntax to filter. You can specify the number of filtered results to return
        :param func: method name
        :param direction: direction, 'following' or 'preceding'
        :param locator: query syntax used for filtering
        :param index: the number of previous query results, starting from 1
        :param timeout: timeout for finding nodes (seconds)
        :param ele_only: whether to only get elements, if False, text and comment nodes are also included
        :return: an element or node before this element
        """
        ...

    def _get_relatives(self,
                       index: int = None,
                       locator: Union[Tuple[str, str], str] = '',
                       direction: str = 'following',
                       brother: bool = True,
                       timeout: float = 0.5,
                       ele_only: bool = True) -> List[Union[DrissionElement, str]]:
        """Return a list of sibling elements or nodes as required
        :param index: the index to get. If this parameter is not None, only the element with this index will be obtained
        :param locator: the query syntax used for filtering
        :param direction: 'following' or 'preceding', the direction of search
        :param brother: the search range, whether to search at the same level or before and after the entire DOM
        :param timeout: the search waiting time (seconds)
        :return: element object or string
        """
        ...

    # ----------------The following properties or methods are implemented by descendants----------------
    @property
    def attrs(self) -> dict: ...

    @property
    def text(self) -> str: ...

    @property
    def raw_text(self) -> str: ...

    @abstractmethod
    def attr(self, name: str) -> str: ...

    def _get_ele_path(self, mode) -> str: ...


class BasePage(BaseParser):
    """Base class for page classes"""

    _url_available: Optional[bool] = ...
    retry_times: int = ...
    retry_interval: float = ...
    _download_path: Optional[str] = ...
    _DownloadKit: Optional[DownloadKit] = ...
    _none_ele_return_value: bool = ...
    _none_ele_value: Any = ...
    _page: Union[ChromiumPage, SessionPage, WebPage] = ...
    _session: Optional[Session] = ...
    _headers: Optional[CaseInsensitiveDict] = ...
    _session_options: Optional[SessionOptions] = ...

    def __init__(self): ...

    @property
    def title(self) -> Union[str, None]:
        """Return to page title"""
        ...

    @property
    def url_available(self) -> bool:
        """Returns the validity of the currently visited URL"""
        ...

    @property
    def download_path(self) -> str:
        """Return to the default download path"""
        ...

    @property
    def download(self) -> DownloadKit:
        """Returns the downloader object"""
        ...

    def _before_connect(self, url: str, retry: int, interval: float) -> tuple:
        """Preparation before connection
        :param url: URL to be accessed
        :param retry: Number of retries
        :param interval: Retry interval
        :return: Tuple consisting of number of retries, interval, and whether it is a file
        """
        ...

    def _set_session_options(self, session_or_options: Union[Session, SessionOptions] = None) -> None:
        """Startup configuration
        :param session_or_options: Session, SessionOptions object
        :return: None
        """
        ...

    def _create_session(self) -> None:
        """Create a built-in Session object"""
        ...

    # ----------------The following properties or methods are implemented by descendants----------------
    @property
    def url(self) -> str: ...

    @property
    def json(self) -> dict: ...

    @property
    def user_agent(self) -> str: ...

    @abstractmethod
    def get(self, url: str, show_errmsg: bool = False, retry: int = None, interval: float = None): ...

    def _ele(self,
             locator,
             timeout: float = None,
             index: Optional[int] = 1,
             raise_err: bool = None,
             method: str = None):
        """Call the method to get the element
        :param locator: locator
        :param timeout: timeout (seconds)
        :param index: the index to get, starting from 1, you can pass in a negative number to get the last index
        :param raise_err: whether to throw an exception when not found
        :param method: the method name to call
        :return: element object or a list of them
        """
        ...
