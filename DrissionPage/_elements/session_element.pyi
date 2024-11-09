# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from typing import Union, List, Tuple, Optional

from lxml.html import HtmlElement

from .._base.base import DrissionElement, BaseElement
from .._elements.chromium_element import ChromiumElement
from .._functions.elements import SessionElementsList
from .._pages.chromium_base import ChromiumBase
from .._pages.chromium_frame import ChromiumFrame
from .._pages.session_page import SessionPage


class SessionElement(DrissionElement):
    """Static element object"""

    def __init__(self, ele: HtmlElement, owner: Union[SessionPage, None] = None):
        self._inner_ele: HtmlElement = ...
        self.owner: SessionPage = ...
        self.page: SessionPage = ...

    def __call__(self,
                 locator: Union[Tuple[str, str], str],
                 index: int = 1,
                 timeout: float = None) -> SessionElement:
        """Find an element internally
        Example: ele2 = ele1('@id=ele_id')
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param index: The element number, starting from 1, and a negative number can be passed in to get the last element
        :param timeout: has no practical effect
        :return: SessionElement object or attribute, text
        """
        ...

    def __repr__(self) -> str: ...

    def __eq__(self, other: SessionElement) -> bool: ...

    @property
    def inner_ele(self) -> HtmlElement: ...

    @property
    def tag(self) -> str:
        """Return element type"""
        ...

    @property
    def html(self) -> str:
        """Return the outerHTML text"""
        ...

    @property
    def inner_html(self) -> str:
        """Returns the innerHTML text of an element"""
        ...

    @property
    def attrs(self) -> dict:
        """Return all attributes and values ​​of an element"""
        ...

    @property
    def text(self) -> str:
        """Return the text inside an element"""
        ...

    @property
    def raw_text(self) -> str:
        """Return the unformatted text of the element"""
        ...

    def parent(self,
               level_or_loc: Union[tuple, str, int] = 1,
               index: int = 1,
               timeout: float = None) -> SessionElement:
        """Returns the parent element of a certain level above. You can specify the number of levels or use query syntax to locate
        :param level_or_loc: the parent element of the level, or the locator
        :param index: when level_or_loc passes in the locator, use this parameter to select the result of the level
        :param timeout: This parameter has no actual effect
        :return: the parent element object
        """
        ...

    def child(self,
              locator: Union[Tuple[str, str], str, int] = '',
              index: int = 1,
              timeout: float = None,
              ele_only: bool = True) -> Union[SessionElement, str]:
        """Returns a direct child element of the current element that meets the conditions. You can use query syntax to filter, and you can specify the number of the filter results to return
        :param locator: Query syntax used for filtering
        :param index: The number of query results, starting from 1
        :param timeout: This parameter has no actual effect
        :param ele_only: Whether to only get elements, when False, text and comment nodes are also included
        :return: Direct child elements or node text
        """
        ...

    def prev(self,
             locator: Union[Tuple[str, str], str, int] = '',
             index: int = 1,
             timeout: float = None,
             ele_only: bool = True) -> Union[SessionElement, str]:
        """Returns the previous element of the same level that meets the conditions. You can use query syntax to filter, and you can specify the number of the filtered results to return
        :param locator: Query syntax used for filtering
        :param index: The previous query result, starting from 1
        :param timeout: This parameter has no actual effect
        :param ele_only: Whether to only get elements, when False, text and comment nodes are also included
        :return: The element of the same level
        """
        ...

    def next(self,
             locator: Union[Tuple[str, str], str, int] = '',
             index: int = 1,
             timeout: float = None,
             ele_only: bool = True) -> Union[SessionElement, str]:
        """Returns a sibling element that meets the conditions after the current element. You can use query syntax to filter, and you can specify the number of the filter results to return
        :param locator: Query syntax used for filtering
        :param index: The number of query results, starting from 1
        :param timeout: This parameter has no actual effect
        :param ele_only: Whether to only get elements, when False, text and comment nodes are also included
        :return: sibling elements
        """
        ...

    def before(self,
               locator: Union[Tuple[str, str], str, int] = '',
               index: int = 1,
               timeout: float = None,
               ele_only: bool = True) -> Union[SessionElement, str]:
        """Returns an element that meets the conditions before the current element in the document.
        You can use query syntax to filter, and you can specify the number of filtered results to return. 
        The search range is not limited to elements of the same level, but the entire DOM document. 
        :param locator: Query syntax used for filtering. 
        :param index: The number of the previous query result, starting from 1. 
        :param timeout: This parameter has no actual effect. 
        :param ele_only: Whether to only get elements. When False, text and comment nodes are also included. 
        :return: An element or node before this element. 
        """
        ...

    def after(self,
              locator: Union[Tuple[str, str], str, int] = '',
              index: int = 1,
              timeout: float = None,
              ele_only: bool = True) -> Union[SessionElement, str]:
        """Returns an element that meets the conditions after the current element in the document. 
        You can use query syntax to filter, and you can specify the number of filtered results to return. 
        The search range is not limited to elements of the same level, but the entire DOM document. 
        :param locator: Query syntax used for filtering. 
        :param index: The number of query results, starting from 1. 
        :param timeout: This parameter has no actual effect. 
        :param ele_only: Whether to only get elements. When False, text and comment nodes are also included. 
        :return: An element or node after this element. 
        """
        ...

    def children(self,
                 locator: Union[Tuple[str, str], str] = '',
                 timeout: float = None,
                 ele_only: bool = True) -> Union[SessionElementsList, List[Union[SessionElement, str]]]:
        """Returns a list of direct child elements or nodes that meet the conditions of the current element. You can use query syntax to filter
        :param locator: Query syntax used for filtering
        :param timeout: This parameter has no actual effect
        :param ele_only: Whether to get only elements. When False, text and comment nodes are also included
        :return: A list of direct child elements or node text
        """
        ...

    def prevs(self,
              locator: Union[Tuple[str, str], str] = '',
              timeout: float = None,
              ele_only: bool = True) -> Union[SessionElementsList, List[Union[SessionElement, str]]]:
        """Returns a list of the same-level elements or nodes that meet the conditions in front of the current element. You can use the query syntax to filter
        :param locator: The query syntax used for filtering
        :param timeout: This parameter has no actual effect
        :param ele_only: Whether to get only elements, when False, text and comment nodes are also included
        :return: A list of the same-level elements or node texts
        """
        ...

    def nexts(self,
              locator: Union[Tuple[str, str], str] = '',
              timeout: float = None,
              ele_only: bool = True) -> Union[SessionElementsList, List[Union[SessionElement, str]]]:
        """Returns a list of the same-level elements or nodes that meet the conditions after the current element. You can use the query syntax to filter
        :param locator: The query syntax used for filtering
        :param timeout: This parameter has no actual effect
        :param ele_only: Whether to get only elements. When False, text and comment nodes are also included
        :return: A list of the same-level elements or node texts
        """
        ...

    def befores(self,
                locator: Union[Tuple[str, str], str] = '',
                timeout: float = None,
                ele_only: bool = True) -> Union[SessionElementsList, List[Union[SessionElement, str]]]:
        """Returns a list of elements or nodes that meet the conditions before the current element in the document. 
        You can use query syntax to filter. The search scope is not limited to elements of the same level, but the entire DOM document. 
        :param locator: Query syntax used for filtering. 
        :param timeout: This parameter has no actual effect. 
        :param ele_only: Whether to get only elements. When False, text and comment nodes are also included. 
        :return: A list of elements or nodes before this element. 
        """
        ...

    def afters(self,
               locator: Union[Tuple[str, str], str] = '',
               timeout: float = None,
               ele_only: bool = True) -> Union[SessionElementsList, List[Union[SessionElement, str]]]:
        """Returns a list of elements or nodes that meet the conditions after the current element in the document. 
        You can use query syntax to filter. The search scope is not limited to elements of the same level, but the entire DOM document. 
        :param locator: Query syntax used for filtering. 
        :param timeout: This parameter has no actual effect. 
        :param ele_only: Whether to get only elements. When False, text and comment nodes are also included. 
        :return: A list of elements or nodes after this element. 
        """
        ...

    def attr(self, name: str) -> Optional[str]:
        """Returns the attribute value
        :param name: attribute name
        :return: attribute value text, returns None if there is no such attribute
        """
        ...

    def ele(self,
            locator: Union[Tuple[str, str], str],
            index: int = 1,
            timeout: float = None) -> SessionElement:
        """Returns an element, attribute or node text that meets the conditions under the current element
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param index: The number of elements, starting from 1, and a negative number can be passed in to get the last number
        :param timeout: has no practical effect
        :return: SessionElement object or attribute, text
        """
        ...

    def eles(self,
             locator: Union[Tuple[str, str], str],
             timeout: float = None) -> SessionElementsList:
        """Returns all eligible child elements, attributes or node texts of the current element
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param timeout: has no practical effect
        :return: SessionElement object or a list of attributes and text
        """
        ...

    def s_ele(self,
              locator: Union[Tuple[str, str], str] = None,
              index: int = 1) -> SessionElement:
        """Returns an element, attribute or node text that meets the conditions under the current element
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param index: The index to get, starting from 1, and a negative number can be passed in to get the last index
        :return: SessionElement object or attribute, text
        """
        ...

    def s_eles(self, locator: Union[Tuple[str, str], str]) -> SessionElementsList:
        """Returns all eligible child elements, attributes or node texts under the current element
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :return: SessionElement object or a list of attributes and text
        """
        ...

    def _find_elements(self,
                       locator: Union[Tuple[str, str], str],
                       timeout: float,
                       index: Optional[int] = 1,
                       relative: bool = False,
                       raise_err: bool = None) -> Union[SessionElement, SessionElementsList]:
        """Returns the child elements, attributes or node texts that meet the conditions of the current element
        :param locator: The location information of the element, which can be a loc tuple or a query string
        :param timeout: It has no practical effect and is used to correspond to the parent class
        :param index: The result, starting from 1, you can pass in a negative number to get the last result, and return all results if it is None
        :param relative: The parameter used by MixTab to indicate whether it is relatively positioned
        :param raise_err: Whether to throw an exception if the element cannot be found, if it is None, it will be based on the global settings
        :return: SessionElement object
        """
        ...

    def _get_ele_path(self, mode: str) -> str:
        """Get css path or xpath path
        :param mode: 'css' or 'xpath'
        :return: css path or xpath path
        """
        ...


def make_session_ele(html_or_ele: Union[str, SessionElement, SessionPage, ChromiumElement, BaseElement, ChromiumFrame,
ChromiumBase],
                     loc: Union[str, Tuple[str, str]] = None,
                     index: Optional[int] = 1,
                     method: Optional[str] = None) -> Union[SessionElement, SessionElementsList]:
    """Search for an element from the received object or html text and return a SessionElement object
    If you want to generate a SessionElement directly from html without searching in the lower level, enter None in loc
    :param html_or_ele: html text, BaseParser object
    :param loc: locate tuple or string, if None, do not search in the lower level, return the root element
    :param index: get the element, starting from 1, you can pass in a negative number to get the last one, None to get all
    :param method: the method to call this method
    :return: return a SessionElement element or list, or attribute text
    """
    ...
