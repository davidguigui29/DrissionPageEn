# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from pathlib import Path
from typing import Union, Tuple, List, Any, Literal, Optional

from .._base.base import DrissionElement, BaseElement
from .._elements.session_element import SessionElement
from .._functions.elements import SessionElementsList, ChromiumElementsList
from .._pages.chromium_base import ChromiumBase
from .._pages.chromium_frame import ChromiumFrame
from .._pages.chromium_page import ChromiumPage
from .._pages.chromium_tab import ChromiumTab
from .._pages.web_page import WebPage
from .._units.clicker import Clicker
from .._units.rect import ElementRect
from .._units.scroller import ElementScroller
from .._units.selector import SelectElement
from .._units.setter import ChromiumElementSetter
from .._units.states import ShadowRootStates, ElementStates
from .._units.waiter import ElementWaiter

PIC_TYPE = Literal['jpg', 'jpeg', 'png', 'webp', True]


class ChromiumElement(DrissionElement):
    _tag: Optional[str] = ...
    owner: ChromiumBase = ...
    page: Union[ChromiumPage, WebPage] = ...
    tab: Union[ChromiumPage, ChromiumTab] = ...
    _node_id: int = ...
    _obj_id: str = ...
    _backend_id: int = ...
    _doc_id: Optional[str] = ...
    _scroll: Optional[ElementScroller] = ...
    _clicker: Optional[Clicker] = ...
    _select: Union[SelectElement, None, False] = ...
    _wait: Optional[ElementWaiter] = ...
    _rect: Optional[ElementRect] = ...
    _set: Optional[ChromiumElementSetter] = ...
    _states: Optional[ElementStates] = ...
    _pseudo: Optional[Pseudo] = ...

    def __init__(self,
                 owner: ChromiumBase,
                 node_id: int = None,
                 obj_id: str = None,
                 backend_id: int = None):
        """At least one of node_id, obj_id and backend_id must be passed in
        :param owner: the page object where the element is located
        :param node_id: node id in cdp
        :param obj_id: object id in js
        :param backend_id: backend id
        """
        ...

    def __call__(self,
                 locator: Union[Tuple[str, str], str],
                 index: int = 1,
                 timeout: float = None) -> ChromiumElement:
        """Find an element internally
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param timeout: Timeout (seconds)
        :return: ChromiumElement object or attribute, text
        """
        ...

    def __repr__(self) -> str: ...

    def __eq__(self, other: ChromiumElement) -> bool: ...

    @property
    def tag(self) -> str:
        """Return element tag"""
        ...

    @property
    def html(self) -> str:
        """Return the outerHTML text of an element"""
        ...

    @property
    def inner_html(self) -> str:
        """Returns the innerHTML text of an element"""
        ...

    @property
    def attrs(self) -> dict:
        """Return all attribute properties of an element"""
        ...

    @property
    def text(self) -> str:
        """Returns all text in an element, the text is formatted"""
        ...

    @property
    def raw_text(self) -> str:
        """Return the unformatted text of the element"""
        ...

    @property
    def set(self) -> ChromiumElementSetter:
        """Returns an object for setting element properties"""
        ...

    @property
    def states(self) -> ElementStates:
        """Returns an object for getting the state of an element."""
        ...

    @property
    def pseudo(self) -> Pseudo:
        """Returns an object for getting the content of a pseudo-element."""
        ...

    @property
    def rect(self) -> ElementRect:
        """Returns an object for getting the position of an element"""
        ...

    @property
    def shadow_root(self) -> Union[None, ShadowRoot]:
        """Returns the shadow_root element object of the current element"""
        ...

    @property
    def sr(self) -> Union[None, ShadowRoot]:
        """Returns the shadow_root element object of the current element"""
        ...

    @property
    def scroll(self) -> ElementScroller:
        """Object used to scroll the scroll bar"""
        ...

    @property
    def click(self) -> Clicker:
        """Returns the object used for click"""
        ...

    @property
    def wait(self) -> ElementWaiter:
        """Returns the object to wait for."""
        ...

    @property
    def select(self) -> Union[SelectElement, False]:
        """Returns the Select class that specifically handles drop-down lists. Non-<select> elements return False"""
        ...

    @property
    def value(self) -> str:
        """Returns the value of the element's property attribute"""
        ...

    def parent(self,
               level_or_loc: Union[tuple, str, int] = 1,
               index: int = 1,
               timeout: float = 0) -> ChromiumElement:
        """Returns the parent element of a certain level above. You can specify the number of levels or use query syntax to locate
        :param level_or_loc: the parent element of the level, starting from 1, or the locator
        :param index: when level_or_loc passes in the locator, use this parameter to select the result of the level, starting from 1
        :param timeout: search timeout (seconds)
        :return: parent element object
        """
        ...

    def child(self,
              locator: Union[Tuple[str, str], str, int] = '',
              index: int = 1,
              timeout: float = None,
              ele_only: bool = True) -> Union[ChromiumElement, str]:
        """Returns a direct child element of the current element that meets the conditions. You can use query syntax to filter, and you can specify the number of the filter results to return
        :param locator: Query syntax used for filtering
        :param index: The number of query results, starting from 1
        :param timeout: Timeout for finding nodes (seconds)
        :param ele_only: Whether to only get elements, if False, text and comment nodes are also included
        :return: Direct child elements or node text
        """
        ...

    def prev(self,
             locator: Union[Tuple[str, str], str, int] = '',
             index: int = 1,
             timeout: float = None,
             ele_only: bool = True) -> Union[ChromiumElement, str]:
        """Returns the previous element of the same level that meets the conditions. You can use query syntax to filter, and you can specify the number of the filtered results to return
        :param locator: Query syntax used for filtering
        :param index: The number of the previous query result, starting from 1
        :param timeout: The timeout for finding nodes (seconds)
        :param ele_only: Whether to only get elements, if False, text and comment nodes are also included
        :return: Brother element or node text
        """
        ...

    def next(self,
             locator: Union[Tuple[str, str], str, int] = '',
             index: int = 1,
             timeout: float = None,
             ele_only: bool = True) -> Union[ChromiumElement, str]:
        """Returns a sibling element that meets the conditions after the current element. You can use query syntax to filter, and you can specify the number of the filter results to return
        :param locator: Query syntax used for filtering
        :param index: The number of query results, starting from 1
        :param timeout: Timeout for finding nodes (seconds)
        :param ele_only: Whether to only get elements, if False, text and comment nodes are also included
        :return: Brother element or node text
        """
        ...

    def before(self,
               locator: Union[Tuple[str, str], str, int] = '',
               index: int = 1,
               timeout: float = None,
               ele_only: bool = True) -> Union[ChromiumElement, str]:
        """Returns an element that meets the conditions before the current element in the document.
        You can use query syntax to filter, and you can specify the number of filtered results to return.
        The search range is not limited to elements of the same level, but the entire DOM document.
        :param locator: Query syntax used for filtering.
        :param index: The number of previous query results, starting from 1. 
        :param timeout: Timeout for finding nodes (seconds).
        :param ele_only: Whether to only get elements. When False, text and comment nodes are also included.
        :return: An element or node before this element. """
        ...

    def after(self,
              locator: Union[Tuple[str, str], str, int] = '',
              index: int = 1,
              timeout: float = None,
              ele_only: bool = True) -> Union[ChromiumElement, str]:
        """Returns an element that meets the conditions after the current element in the document.
        You can use query syntax to filter, and you can specify the number of filtered results to return. 
        The search range is not limited to elements of the same level, but the entire DOM document.
        :param locator: Query syntax used for filtering.
        :param index: The number of query results, starting from 1.
        :param timeout: Timeout for finding nodes (seconds).
        :param ele_only: Whether to only get elements. When False, text and comment nodes are also included.
        :return: An element or node after this element. """
        ...

    def children(self,
                 locator: Union[Tuple[str, str], str] = '',
                 timeout: float = None,
                 ele_only: bool = True) -> Union[ChromiumElementsList, List[Union[ChromiumElement, str]]]:
        """Returns a list of direct child elements or nodes that meet the conditions of the current element. You can use query syntax to filter
        :param locator: Query syntax used for filtering
        :param timeout: Timeout for finding nodes (seconds)
        :param ele_only: Whether to get only elements. If False, text and comment nodes are also included
        :return: A list of direct child elements or node text
        """
        ...

    def prevs(self,
              locator: Union[Tuple[str, str], str] = '',
              timeout: float = None,
              ele_only: bool = True) -> Union[ChromiumElementsList, List[Union[ChromiumElement, str]]]:
        """Returns a list of sibling elements or nodes that meet the conditions in front of the current element. You can use query syntax to filter
        :param locator: Query syntax for filtering
        :param timeout: Timeout for finding nodes (seconds)
        :param ele_only: Whether to get only elements. If False, text and comment nodes are also included
        :return: A list of sibling elements or node text
        """
        ...

    def nexts(self,
              locator: Union[Tuple[str, str], str] = '',
              timeout: float = None,
              ele_only: bool = True) -> Union[ChromiumElementsList, List[Union[ChromiumElement, str]]]:
        """Returns a list of sibling elements or nodes that meet the conditions after the current element. You can use query syntax to filter
        :param locator: Query syntax for filtering
        :param timeout: Timeout for finding nodes (seconds)
        :param ele_only: Whether to get only elements. If False, text and comment nodes are also included
        :return: A list of sibling elements or node text
        """
        ...

    def befores(self,
                locator: Union[Tuple[str, str], str] = '',
                timeout: float = None,
                ele_only: bool = True) -> Union[ChromiumElementsList, List[Union[ChromiumElement, str]]]:
        """Returns a list of elements or nodes that meet the conditions before the current element in the document.
        You can use query syntax to filter. The search scope is not limited to elements of the same level, but the entire DOM document.
        :param locator: query syntax used for filtering.
        :param timeout: timeout for finding nodes (seconds).
        :param ele_only: whether to get only elements. If False, text and comment nodes are also included.
        :return: a list of elements or nodes before this element.
        """
        ...

    def afters(self,
               locator: Union[Tuple[str, str], str] = '',
               timeout: float = None,
               ele_only: bool = True) -> Union[ChromiumElementsList, List[Union[ChromiumElement, str]]]:
        """Returns a list of elements or nodes that meet the conditions after the current element in the document.
        You can use query syntax to filter. The search scope is not limited to elements of the same level, but the entire DOM document.
        :param locator: query syntax used for filtering.
        :param timeout: timeout for finding nodes (seconds).
        :param ele_only: whether to get only elements. If False, text and comment nodes are also included.
        :return: a list of elements or nodes after this element.
        """
        ...

    def over(self, timeout: float = None) -> ChromiumElement:
        """Get the topmost element covering this element
        :param timeout: timeout (in seconds) for waiting for the element to appear
        :return: element object
        """
        ...

    def offset(self,
               locator: Optional[str] = None,
               x: int = None,
               y: int = None,
               timeout: float = None) -> ChromiumElement:
        """Get the element at the specified offset relative to the upper left corner of this element. If offset_x and offset_y are both None, locate the middle point of the element
        :param locator: locator, only supports str, and does not support xpath and css
        :param x: horizontal axis offset, rightward is positive
        :param y: vertical axis offset, downward is positive
        :param timeout: timeout (seconds), None uses the page setting
        :return: element object
        """
        ...

    def east(self, loc_or_pixel: Union[str, int, None] = None, index: int = 1) -> ChromiumElement:
        """Get a specified element to the right of an element
        :param loc_or_pixel: locator, only supports str or int, and does not support xpath and css. Pass in int to get it by pixel distance
        :param index: the number, starting from 1
        :return: the element object obtained
        """
        ...

    def south(self, loc_or_pixel: Union[str, int, None] = None, index: int = 1) -> ChromiumElement:
        """Get a specified element below an element
        :param loc_or_pixel: locator, only supports str or int, and does not support xpath and css. Pass in int to get it by pixel distance
        :param index: the number, starting from 1
        :return: the element object obtained
        """
        ...

    def west(self, loc_or_pixel: Union[str, int, None] = None, index: int = 1) -> ChromiumElement:
        """Get a specified element to the left of an element
        :param loc_or_pixel: locator, only supports str or int, and does not support xpath and css. Pass in int to get it by pixel distance
        :param index: the number, starting from 1
        :return: the element object obtained
        """
        ...

    def north(self, loc_or_pixel: Union[str, int, None] = None, index: int = 1) -> ChromiumElement:
        """Get a specified element above the element
        :param loc_or_pixel: locator, only supports str or int, and does not support xpath and css. Pass in int to get it by pixel distance
        :param index: the number, starting from 1
        :return: the element object obtained
        """
        ...

    def _get_relative_eles(self,
                           mode: str = 'north',
                           locator: Union[int, str] = None,
                           index: int = 1) -> ChromiumElement:
        """Get a specified element below the element
        :param locator: locator, only supports str or int, and does not support xpath and css
        :param index: the number, starting from 1
        :return: the element object obtained
        """
        ...

    def check(self, uncheck: bool = False, by_js: bool = False) -> None: ...

    def attr(self, name: str) -> Union[str, None]:
        """Return an attribute value
        :param name: attribute name
        :return: attribute value text, returns None if there is no such attribute
        """
        ...

    def remove_attr(self, name: str) -> None:
        """Delete an attribute attribute of an element
        :param name: attribute name
        :return: None
        """
        ...

    def property(self, name: str) -> Union[str, int, None]:
        """Get a property value
        :param name: property name
        :return: property value text
        """
        ...

    def run_js(self, script: str, *args, as_expr: bool = False, timeout: float = None) -> Any:
        """Execute javascript code on this element
        :param script: js text, this is used in the text to represent this element
        :param args: parameters, corresponding to arguments[0], arguments[1]... in the js text in order
        :param as_expr: whether to run as an expression, args is invalid when True
        :param timeout: js timeout (seconds), if None, use the page timeouts.script setting
        :return: the result of the operation
        """
        ...

    def _run_js(self, script: str, *args, as_expr: bool = False, timeout: float = None) -> Any:
        """Execute javascript code on this element
        :param script: js text, this is used in the text to represent this element
        :param args: parameters, corresponding to arguments[0], arguments[1]... in the js text in order
        :param as_expr: whether to run as an expression, args is invalid when True
        :param timeout: js timeout (seconds), if None, use the page timeouts.script setting
        :return: the result of the operation
        """
        ...

    def run_async_js(self, script: str, *args, as_expr: bool = False) -> None:
        """Execute javascript code on this element asynchronously
        :param script: js text, this is used in the text to represent this element
        :param args: parameters, corresponding to arguments[0], arguments[1]... in the js text in order
        :param as_expr: whether to run as an expression, args is invalid when True
        :return: None
        """
        ...

    def ele(self,
            locator: Union[Tuple[str, str], str],
            index: int = 1,
            timeout: float = None) -> ChromiumElement:
        """Returns an element, attribute or node text that meets the conditions under the current element
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param index: The element to get, starting from 1, and a negative number can be passed in to get the last element
        :param timeout: The timeout for finding an element (seconds), which is the same as the waiting time of the page where the element is located by default
        :return: ChromiumElement object or attribute, text
        """
        ...

    def eles(self,
             locator: Union[Tuple[str, str], str],
             timeout: float = None) -> ChromiumElementsList:
        """Returns all eligible child elements, attributes or node texts under the current element
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param timeout: The timeout for finding an element (in seconds), which defaults to the same waiting time as the page where the element is located
        :return: A list of ChromiumElement objects or attributes and text
        """
        ...

    def s_ele(self,
              locator: Union[Tuple[str, str], str] = None,
              index: int = 1,
              timeout: float = None) -> SessionElement:
        """Find an element that meets the conditions and return it as a SessionElement
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param index: The index to get, starting from 1, and a negative number can be passed in to get the last index
        :param timeout: The timeout for finding an element (seconds), which is the same as the waiting time of the page where the element is located by default
        :return: SessionElement object or attribute, text
        """
        ...

    def s_eles(self,
               locator: Union[Tuple[str, str], str] = None,
               timeout: float = None) -> SessionElementsList:
        """Find all elements that meet the conditions and return them as a list of SessionElement
        :param locator: locator
        :param timeout: timeout for finding elements (seconds), which defaults to the same waiting time as the page where the element is located
        :return: a list of SessionElement or attributes and text
        """
        ...

    def _find_elements(self,
                       locator: Union[Tuple[str, str], str],
                       timeout: float,
                       index: Optional[int] = 1,
                       relative: bool = False,
                       raise_err: bool = False) -> Union[ChromiumElement, ChromiumFrame, ChromiumElementsList]:
        """Returns the child elements, attributes or node texts that meet the conditions of the current element. The first one is returned by default
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param timeout: The timeout for finding an element (in seconds)
        :param index: The result, starting from 1. You can pass in a negative number to get the last result. If it is None, all results will be returned
        :param relative: The parameter used by MixTab to indicate whether it is relatively positioned
        :param raise_err: Whether to throw an exception if the element cannot be found. If it is None, it will be based on the global settings
        :return: ChromiumElement object or text, attribute or a list composed of them
        """
        ...

    def style(self, style: str, pseudo_ele: str = '') -> str:
        """Returns the value of the element style attribute, and can obtain the value of the pseudo-element attribute
        :param style: style attribute name
        :param pseudo_ele: pseudo-element name (if any)
        :return: value of the style attribute
        """
        ...

    def src(self, timeout: float = None, base64_to_bytes: bool = True) -> Union[bytes, str, None]:
        """Returns the element src resource. Base64 can be converted to bytes and returned, and others return str
        :param timeout: Timeout for waiting for resource loading (seconds)
        :param base64_to_bytes: When True, if it is base64 data, convert it to bytes format
        :return: Resource content
        """
        ...

    def save(self,
             path: [str, bool] = None,
             name: str = None,
             timeout: float = None,
             rename: bool = True) -> str:
        """Save images or other resources with src attributes
        :param path: file save path, save to current folder when None
        :param name: file name, get from resource url when None
        :param timeout: timeout (seconds) for waiting for resource loading
        :param rename: whether to automatically rename when encountering duplicate files
        :return: return save path
        """
        ...

    def get_screenshot(self,
                       path: [str, Path] = None,
                       name: str = None,
                       as_bytes: PIC_TYPE = None,
                       as_base64: PIC_TYPE = None,
                       scroll_to_center: bool = True) -> Union[str, bytes]:
        """Screenshot the current element, save it to a file, or return it as bytes
        :param path: file save path
        :param name: full file name, optional suffix 'jpg','jpeg','png','webp'
        :param as_bytes: whether to return the image in byte form, optional 'jpg','jpeg','png','webp', when effective, path parameter and as_base64 parameter are invalid
        :param as_base64: whether to return the image in base64 string form, optional 'jpg','jpeg','png','webp', when effective, path parameter is invalid
        :param scroll_to_center: whether to scroll to the center of the viewport before taking a screenshot
        :return: full path or byte text of the image
        """
        ...

    def input(self, vals: Any, clear: bool = False, by_js: bool = False) -> ChromiumElement:
        """Input text or key combination, can also be used to input file path to input element (paths separated by \n)
        :param vals: text value or key combination
        :param clear: whether to clear the text box before input
        :param by_js: whether to input in js mode, key combination cannot be entered
        :return: None
        """
        ...

    def clear(self, by_js: bool = False) -> ChromiumElement:
        """Clear element text
        :param by_js: Whether to clear using js, if False, use select all + del to simulate input deletion
        :return: None
        """
        ...

    def _input_focus(self) -> None:
        """Make the element focused before typing"""
        ...

    def focus(self) -> ChromiumElement:
        """Gives focus to an element"""
        ...

    def hover(self, offset_x: int = None, offset_y: int = None) -> ChromiumElement:
        """When the mouse is hovering, an offset is accepted, and the offset is relative to the upper left corner of the element. If no offset_x and offset_y values ​​are passed, the mouse hovers at the midpoint of the element
        :param offset_x: x-axis offset relative to the upper left corner of the element
        :param offset_y: y-axis offset relative to the upper left corner of the element
        :return: None
        """
        ...

    def drag(self, offset_x: int = 0, offset_y: int = 0, duration: float = 0.5) -> ChromiumElement:
        """Drag the current element to a relative position
        :param offset_x: x change value
        :param offset_y: y change value
        :param duration: drag time, pass in 0 for instant arrival
        :return: None
        """
        ...

    def drag_to(self,
                ele_or_loc: Union[Tuple[int, int], str, ChromiumElement],
                duration: float = 0.5) -> ChromiumElement:
        """Drag the current element, the target is another element or a coordinate tuple (x, y)
        :param ele_or_loc: another element or a coordinate tuple, the coordinates are the coordinates of the midpoint of the element
        :param duration: drag duration, pass in 0 for instant arrival
        :return: None
        """
        ...

    def _get_obj_id(self, node_id: int = None, backend_id: int = None) -> str: ...

    def _get_node_id(self, obj_id: str = None, backend_id: int = None) -> int: ...

    def _get_backend_id(self, node_id: int) -> int: ...

    def _refresh_id(self) -> None:
        """Refresh other ids according to backend id"""
        ...

    def _get_ele_path(self, mode: str) -> str:
        """Return the absolute css path or xpath path"""
        ...

    def _set_file_input(self, files: Union[str, list, tuple]) -> None:
        """Write the path to the upload control
        :param files: file path list or string, multiple files are separated by carriage returns when it is a string
        :return: None
        """
        ...


class ShadowRoot(BaseElement):
    owner: ChromiumBase = ...
    tab: Union[ChromiumPage, ChromiumTab] = ...
    _obj_id: str = ...
    _node_id: int = ...
    _backend_id: int = ...
    parent_ele: ChromiumElement = ...
    _states: Optional[ShadowRootStates] = ...

    def __init__(self, parent_ele: ChromiumElement, obj_id: str = None, backend_id: int = None):
        """
        :param parent_ele: parent element where shadow root is located
        :param obj_id: object id in js
        :param backend_id: backend id in cdp
        """
        ...

    def __call__(self,
                 locator: Union[Tuple[str, str], str],
                 index: int = 1,
                 timeout: float = None) -> ChromiumElement:
        """Find an element internally
        Example: ele2 = ele1('@id=ele_id')
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param index: The index to get, starting from 1, and a negative number can be passed in to get the last index
        :param timeout: Timeout (seconds)
        :return: Element object or attribute, text
        """
        ...

    def __repr__(self) -> str: ...

    def __eq__(self, other: ShadowRoot) -> bool: ...

    @property
    def tag(self) -> str:
        """Return the element tag name"""
        ...

    @property
    def html(self) -> str:
        """Return the outerHTML text"""
        ...

    @property
    def inner_html(self) -> str:
        """Return the inner html text"""
        ...

    @property
    def states(self) -> ShadowRootStates:
        """Returns an object for getting the state of an element."""
        ...

    def run_js(self,
               script: str,
               *args,
               as_expr: bool = False,
               timeout: float = None) -> Any:
        """Run javascript code
        :param script: js text
        :param args: parameters, corresponding to arguments[0], arguments[1]... in the js text in order
        :param as_expr: whether to run as an expression, args is invalid when True
        :param timeout: js timeout (seconds), if None, use the page timeouts.script setting
        :return: the result of the run
        """
        ...

    def _run_js(self,
                script: str,
                *args,
                as_expr: bool = False,
                timeout: float = None) -> Any:
        """Run javascript code
        :param script: js text
        :param args: parameters, corresponding to arguments[0], arguments[1]... in the js text in order
        :param as_expr: whether to run as an expression, args is invalid when True
        :param timeout: js timeout (seconds), if None, use the page timeouts.script setting
        :return: the result of the run
        """
        ...

    def run_async_js(self,
                     script: str,
                     *args,
                     as_expr: bool = False,
                     timeout: float = None) -> None:
        """Execute js code asynchronously
        :param script: js text
        :param args: parameters, corresponding to arguments[0], arguments[1]... in the js text in order
        :param as_expr: whether to run as an expression, args is invalid when True
        :param timeout: js timeout (seconds), if None, use the page timeouts.script setting
        :return: None
        """
        ...

    def parent(self,
               level_or_loc: Union[str, int] = 1,
               index: int = 1,
               timeout: float = 0) -> ChromiumElement:
        """Returns the parent element of a level above. You can specify the number of levels or use query syntax to locate
        :param level_or_loc: the parent element of the level, or the locator
        :param index: when level_or_loc passes in the locator, use this parameter to select the result
        :param timeout: search timeout (seconds)
        :return: ChromiumElement object
        """
        ...

    def child(self,
              locator: Union[Tuple[str, str], str] = '',
              index: int = 1, timeout: float = None) -> ChromiumElement:
        """Returns a list of direct child elements or nodes, which can be filtered using query syntax
        :param locator: Query syntax used for filtering
        :param index: The first query result, starting from 1
        :param timeout: Search timeout (seconds)
        :return: A list of direct child elements or node texts
        """
        ...

    def next(self,
             locator: Union[Tuple[str, str], str] = '',
             index: int = 1, timeout: float = None) -> ChromiumElement:
        """Returns a sibling element that meets the conditions after the current element. You can use query syntax to filter, and you can specify the number of the filter results to return
        :param locator: query syntax used for filtering
        :param index: the number of query results, starting from 1
        :param timeout: search timeout (seconds)
        :return: ChromiumElement object
        """
        ...

    def before(self,
               locator: Union[Tuple[str, str], str] = '',
               index: int = 1, timeout: float = None) -> ChromiumElement:
        """Returns an element that meets the conditions before the current element in the document.
        You can use query syntax to filter, and you can specify the number of filtered results to return.
        The search range is not limited to elements of the same level, but the entire DOM document.
        :param locator: Query syntax used for filtering.
        :param index: The number of the previous query result, starting from 1. 
        :param timeout: Search timeout (seconds) 
        :return: An element or node before this element.
        """
        ...

    def after(self,
              locator: Union[Tuple[str, str], str] = '',
              index: int = 1, timeout: float = None) -> ChromiumElement:
        """Returns an element that meets the conditions after the current element in the document.
        You can use query syntax to filter, and you can specify the number of the filtered results to return. 
        The search range is not limited to elements of the same level, but the entire DOM document. 
        :param locator: query syntax used for filtering. 
        :param index: the number of the query result after, starting from 1. 
        :param timeout: search timeout (seconds) 
        :return: an element or node after this element.
        """
        ...

    def children(self, locator: Union[Tuple[str, str], str] = '', timeout: float = None) -> List[ChromiumElement]:
        """Returns a list of direct child elements or nodes that meet the conditions of the current element, which can be filtered using query syntax
        :param locator: query syntax used for filtering
        :param timeout: search timeout (seconds)
        :return: a list of direct child elements or node text
        """
        ...

    def nexts(self, locator: Union[Tuple[str, str], str] = '', timeout: float = None) -> List[ChromiumElement]:
        """Returns a list of sibling elements or nodes that meet the conditions after the current element. You can use query syntax to filter
        :param locator: query syntax used for filtering
        :param timeout: search timeout (seconds)
        :return: a list of ChromiumElement objects
        """
        ...

    def befores(self, locator: Union[Tuple[str, str], str] = '', timeout: float = None) -> List[ChromiumElement]:
        """Returns a list of elements or nodes that meet the conditions before the current element in the document. 
        You can use query syntax to filter. The search scope is not limited to elements of the same level, but the entire DOM document. 
        :param locator: query syntax used for filtering. 
        :param timeout: search timeout (seconds). 
        :return: a list of elements or nodes before this element. 
        """
        ...

    def afters(self, locator: Union[Tuple[str, str], str] = '', timeout: float = None) -> List[ChromiumElement]:
        """Returns a list of elements or nodes that meet the conditions after the current element in the document. 
        You can use query syntax to filter. The search scope is not limited to elements of the same level, but the entire DOM document. 
        :param locator: query syntax used for filtering. 
        :param timeout: search timeout (seconds). 
        :return: a list of elements or nodes after this element.
        """
        ...

    def ele(self,
            locator: Union[Tuple[str, str], str],
            index: int = 1,
            timeout: float = None) -> ChromiumElement:
        """Returns an element that meets the conditions under the current element
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param index: The index of the element to get, starting from 1, and a negative number can be passed in to get the last index
        :param timeout: The timeout for finding an element (seconds), which is the same as the waiting time of the page where the element is located by default
        :return: ChromiumElement object
        """
        ...

    def eles(self,
             locator: Union[Tuple[str, str], str],
             timeout: float = None) -> ChromiumElementsList:
        """Returns all eligible child elements under the current element
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param timeout: The timeout for finding an element (in seconds), which defaults to the same waiting time as the page where the element is located
        :return: A list of ChromiumElement objects
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
        :param timeout: The timeout for finding an element (seconds). 
        The default is the same as the waiting time of the page where the element is located. 
        :return: SessionElement object or attribute, text. 
        """
        ...

    def s_eles(self, locator: Union[Tuple[str, str], str], timeout: float = None) -> SessionElementsList:
        """Find all elements that meet the conditions and return them in the form of a SessionElement list. 
        It is very efficient when processing complex pages. 
        :param locator: The location information of the element, which can be a loc tuple or a query string. 
        :param timeout: The timeout for finding an element (seconds). 
        By default, it is consistent with the waiting time of the page where the element is located. 
        :return: SessionElement object. 
        """
        ...

    def _find_elements(self,
                       locator: Union[Tuple[str, str], str],
                       timeout: float,
                       index: Optional[int] = 1,
                       relative: bool = False,
                       raise_err: bool = None) -> Union[ChromiumElement, ChromiumFrame, str, ChromiumElementsList]:
        """Returns the child elements, attributes or node texts that meet the conditions of the current element. The first one is returned by default
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param timeout: The timeout for finding an element (in seconds)
        :param index: The result, starting from 1. You can pass in a negative number to get the last result. If it is None, all results will be returned
        :param relative: The parameter used by MixTab to indicate whether it is relatively positioned
        :param raise_err: Whether to throw an exception if the element cannot be found. If it is None, it will be based on the global settings
        :return: ChromiumElement object or a list of its components
        """
        ...

    def _get_node_id(self, obj_id: str) -> int: ...

    def _get_obj_id(self, back_id: int) -> str: ...

    def _get_backend_id(self, node_id: int) -> int: ...


def find_in_chromium_ele(ele: ChromiumElement,
                         locator: Union[str, Tuple[str, str]],
                         index: Optional[int] = 1,
                         timeout: float = None,
                         relative: bool = True) -> Union[ChromiumElement, List[ChromiumElement]]:
    """Search in chromium elements
    :param ele: ChromiumElement object
    :param locator: element location tuple
    :param index: the result, starting from 1, you can pass in a negative number to get the last result, and return all if None
    :param timeout: timeout for finding elements (seconds)
    :param relative: MixTab is used to mark whether relative positioning is used
    :return: Returns the ChromiumElement element or a list of them
    """
    ...


def find_by_xpath(ele: ChromiumElement,
                  xpath: str,
                  index: Optional[int],
                  timeout: float,
                  relative: bool = True) -> Union[ChromiumElement, List[ChromiumElement]]:
    """Execute xpath to find an element in an element
    :param ele: Find in this element
    :param xpath: Search statement
    :param index: The result, starting from 1, you can pass in a negative number to get the last result, None returns all
    :param timeout: Timeout (seconds)
    :param relative: Whether to position relatively
    :return: ChromiumElement or a list of it
    """
    ...


def find_by_css(ele: ChromiumElement,
                selector: str,
                index: Optional[int],
                timeout: float) -> Union[ChromiumElement, List[ChromiumElement],]:
    """Execute the search for elements in the element using css selector
    :param ele: Search in this element
    :param selector: Search statement
    :param index: The result, starting from 1, you can pass in a negative number to get the last result, and return all if it is None
    :param timeout: Timeout (seconds)
    :return: ChromiumElement or a list of it
    """
    ...


def make_chromium_eles(page: Union[ChromiumBase, ChromiumPage, WebPage, ChromiumTab, ChromiumFrame],
                       _ids: Union[tuple, list, str, int],
                       index: Optional[int] = 1,
                       is_obj_id: bool = True,
                       ele_only: bool = False
                       ) -> Union[ChromiumElement, ChromiumFrame, ChromiumElementsList]:
    """Generate the corresponding element object according to the node id or object id
    :param page: ChromiumPage object
    :param _ids: element id list
    :param index: get the number, return all if None
    :param is_obj_id: whether the passed id is obj id or node id
    :param ele_only: whether to return only ele, effective when searching for elements on the page
    :return: browser element object or a list of them, return False if generation fails
    """
    ...


def make_js_for_find_ele_by_xpath(xpath: str, type_txt: str, node_txt: str) -> str:
    """Generate js text that uses xpath to find elements in elements
    :param xpath: xpath text
    :param type_txt: search type
    :param node_txt: node type
    :return: js text
    """
    ...


def run_js(page_or_ele: Union[ChromiumBase, ChromiumElement, ShadowRoot],
           script: str,
           as_expr: bool,
           timeout: float,
           args: tuple = ...) -> Any:
    """Run javascript code
    :param page_or_ele: page object or element object
    :param script: js text
    :param as_expr: whether to run as an expression, args is invalid when True
    :param timeout: timeout (seconds)
    :param args: parameters, corresponding to arguments[0], arguments[1]... in js text in order
    :return: js execution result
    """
    ...


def parse_js_result(page: ChromiumBase,
                    ele: ChromiumElement,
                    result: dict,
                    end_time: float):
    """Parse the result returned by js"""
    ...


def convert_argument(arg: Any) -> dict:
    """Convert the parameters into a form that js can receive"""
    ...


class Pseudo(object):
    _ele: ChromiumElement = ...

    def __init__(self, ele: ChromiumElement):
        """
        :param ele: ChromiumElement
        """
        ...

    @property
    def before(self) -> str:
        """Returns the text content of the ::before pseudo-element of the current element"""
        ...

    @property
    def after(self) -> str:
        """Returns the text content of the ::after pseudo-element of the current element"""
        ...
