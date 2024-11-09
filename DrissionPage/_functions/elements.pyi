# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from typing import Union, List, Optional, Iterable, Dict

from .._base.base import BaseParser
from .._elements.chromium_element import ChromiumElement
from .._elements.session_element import SessionElement
from .._pages.chromium_base import ChromiumBase
from .._pages.chromium_frame import ChromiumFrame
from .._pages.session_page import SessionPage


class SessionElementsList(list):
    _owner: SessionPage = ...

    def __init__(self,
                 owner: SessionPage = None,
                 *args):
        """
        :param owner: The page that generated the element list
        :param args:
        """
        ...

    def __next__(self) -> SessionElement: ...

    def __getitem__(self, _i) -> Union[SessionElement, List[SessionElement]]: ...

    def __iter__(self) -> List[SessionElement]: ...

    @property
    def get(self) -> Getter:
        """Returns the object used for the property"""
        ...

    @property
    def filter(self) -> SessionFilter:
        """Returns an object for filtering multiple elements"""
        ...

    @property
    def filter_one(self) -> SessionFilterOne:
        """Object for filtering single elements"""
        ...


class ChromiumElementsList(SessionElementsList):
    _owner: ChromiumBase = ...

    def __init__(self,
                 owner: ChromiumBase = None,
                 *args):
        """
        :param owner: The page that generated the element list
        :param args:
        """
        ...

    def __next__(self) -> ChromiumElement: ...

    def __getitem__(self, _i) -> Union[ChromiumElement, List[ChromiumElement]]: ...

    def __iter__(self) -> List[ChromiumElement]: ...

    @property
    def filter(self) -> ChromiumFilter:
        """Returns an object for filtering multiple elements"""
        ...

    @property
    def filter_one(self) -> ChromiumFilterOne:
        """Object for filtering single elements"""
        ...

    def search(self,
               displayed: Optional[bool] = None,
               checked: Optional[bool] = None,
               selected: Optional[bool] = None,
               enabled: Optional[bool] = None,
               clickable: Optional[bool] = None,
               have_rect: Optional[bool] = None,
               have_text: Optional[bool] = None,
               tag: str = None) -> ChromiumFilter:
        """Or relationship filter elements
        :param displayed: whether it is displayed, bool, None means ignoring this item
        :param checked: whether it is selected, bool, None means ignoring this item
        :param selected: whether it is selected, bool, None means ignoring this item
        :param enabled: whether it is available, bool, None means ignoring this item
        :param clickable: whether it is clickable, bool, None means ignoring this item
        :param have_rect: whether it has size and position, bool, None means ignoring this item
        :param have_text: whether it contains text, bool, None means ignoring this item
        :param tag: the specified element type
        :return: filter results
        """
        ...

    def search_one(self,
                   index: int = 1,
                   displayed: Optional[bool] = None,
                   checked: Optional[bool] = None,
                   selected: Optional[bool] = None,
                   enabled: Optional[bool] = None,
                   clickable: Optional[bool] = None,
                   have_rect: Optional[bool] = None,
                   have_text: Optional[bool] = None,
                   tag: str = None) -> ChromiumElement:
        """Or relationship to filter elements and get a result
        :param index: element index, starting from 1
        :param displayed: whether to display, bool, None to ignore this item
        :param checked: whether it is selected, bool, None to ignore this item
        :param selected: whether it is selected, bool, None to ignore this item
        :param enabled: whether it is available, bool, None to ignore this item
        :param clickable: whether it is clickable, bool, None to ignore this item
        :param have_rect: whether it has size and position, bool, None to ignore this item
        :param have_text: whether it contains text, bool, None to ignore this item
        :param tag: the specified element type
        :return: filter results
        """
        ...


class SessionFilterOne(object):
    _list: SessionElementsList = ...
    _index: int = ...

    def __init__(self, _list: SessionElementsList):
        """
        :param _list: element list object
        """
        ...

    def __call__(self, index: int = 1) -> SessionFilterOne:
        """Return the element in the result
        :param index: element index, starting from 1
        :return: the object itself
        """
        ...

    def tag(self, name: str, equal: bool = True) -> SessionElement:
        """Filter a certain element
        :param name: tab name
        :param equal: True means matching this element, False means matching non-this element
        :return: filter result
        """
        ...

    def attr(self, name: str, value: str, equal: bool = True) -> SessionElement:
        """Filter elements based on whether they have a certain attribute value
        :param name: attribute name
        :param value: attribute value
        :param equal: True means matching elements whose name value is value, False means matching elements whose name value is not value
        :return: Filter result
        """
        ...

    def text(self, text: str, fuzzy: bool = True, contain: bool = True) -> SessionElement:
        """Filter elements based on whether they contain the specified text
        :param text: the text to match
        :param fuzzy: whether to fuzzy match
        :param contain: whether to contain the string, False means not to contain
        :return: filter result
        """
        ...

    def _get_attr(self,
                  name: str,
                  value: str,
                  method: str,
                  equal: bool = True) -> SessionElement:
        """Returns an element that can obtain a certain value through a certain method
        :param name: attribute name
        :param value: attribute value
        :param method: method name
        :return: filter result
        """
        ...


class SessionFilter(SessionFilterOne):

    def __iter__(self) -> Iterable[SessionElement]: ...

    def __next__(self) -> SessionElement: ...

    def __len__(self) -> int: ...

    def __getitem__(self, item: int) -> SessionElement: ...

    @property
    def get(self) -> Getter:
        """Returns an object for getting element attributes"""
        ...

    def tag(self, name: str, equal: bool = True) -> SessionFilter:
        """Filter a certain element
        :param name: tab name
        :param equal: True means matching this element, False means matching non-this element
        :return: filter result
        """
        ...

    def attr(self, name: str, value: str, equal: bool = True) -> SessionFilter:
        """Filter elements based on whether they have a certain attribute value
        :param name: attribute name
        :param value: attribute value
        :param equal: True means matching elements whose name value is value, False means matching elements whose name value is not value
        :return: Filter result
        """
        ...

    def text(self, text: str, fuzzy: bool = True, contain: bool = True) -> SessionFilter:
        """Filter elements based on whether they contain the specified text
        :param text: the text to match
        :param fuzzy: whether to fuzzy match
        :param contain: whether to contain the string, False means not to contain
        :return: filter result
        """
        ...

    def _get_attr(self,
                  name: str,
                  value: str,
                  method: str,
                  equal: bool = True) -> SessionFilter:
        """Returns an element that can obtain a certain value through a certain method
        :param name: attribute name
        :param value: attribute value
        :param method: method name
        :return: filter result
        """
        ...


class ChromiumFilterOne(SessionFilterOne):
    _list: ChromiumElementsList = ...

    def __init__(self, _list: ChromiumElementsList):
        """
        :param _list: element list object
        """
        ...

    def __call__(self, index: int = 1) -> ChromiumFilterOne:
        """Return the element in the result
        :param index: element index, starting from 1
        :return: the object itself
        """
        ...

    def tag(self, name: str, equal: bool = True) -> SessionElement:
        """Filter a certain element
        :param name: tab name
        :param equal: True means matching this element, False means matching non-this element
        :return: filter result
        """
        ...

    def attr(self, name: str, value: str, equal: bool = True) -> ChromiumElement:
        """Filter elements based on whether they have a certain attribute value
        :param name: attribute name
        :param value: attribute value
        :param equal: True means matching elements whose name value is value, False means matching elements whose name value is not value
        :return: Filter result
        """
        ...

    def text(self,
             text: str,
             fuzzy: bool = True,
             contain: bool = True) -> ChromiumElement:
        """Filter elements based on whether they contain the specified text
        :param text: the text to match
        :param fuzzy: whether to fuzzy match
        :param contain: whether to contain the string, False means not to contain
        :return: filter result
        """
        ...

    def displayed(self, equal: bool = True) -> ChromiumElement:
        """Filter elements based on whether they are displayed
        :param equal: whether to match displayed elements, False matches non-displayed
        :return: filter results
        """
        ...

    def checked(self, equal: bool = True) -> ChromiumElement:
        """Filter elements based on whether they are selected
        :param equal: whether to match selected elements, False matches unselected ones
        :return: filter results
        """
        ...

    def selected(self, equal: bool = True) -> ChromiumElement:
        """Filter elements based on whether they are selected, used for <select> element items
        :param equal: whether to match selected elements, False matches unselected elements
        :return: Filter results
        """
        ...

    def enabled(self, equal: bool = True) -> ChromiumElement:
        """Filter elements based on availability
        :param equal: whether to match available elements, False means matching disabled elements
        :return: filter results
        """
        ...

    def clickable(self, equal: bool = True) -> ChromiumElement:
        """Filter elements based on whether they are clickable
        :param equal: whether to match clickable elements, False means the match is not clickable
        :return: filter result
        """
        ...

    def have_rect(self, equal: bool = True) -> ChromiumElement:
        """Filter elements based on whether they have a size
        :param equal: whether to match elements with a size, False means matching elements without a size
        :return: Filter results
        """
        ...

    def style(self, name: str, value: str, equal: bool = True) -> ChromiumElement:
        """Filter elements based on whether they have a certain style value
        :param name: attribute name
        :param value: attribute value
        :param equal: True means matching elements whose name value is value, False means matching elements whose name value is not value
        :return: Filter result
        """
        ...

    def property(self,
                 name: str,
                 value: str, equal: bool = True) -> ChromiumElement:
        """Filter elements based on whether they have a certain property value
        :param name: property name
        :param value: property value
        :param equal: True means matching elements whose name value is value, False means matching elements whose name value is not value
        :return: Filter result
        """
        ...

    def _get_attr(self,
                  name: str,
                  value: str,
                  method: str, equal: bool = True) -> ChromiumElement:
        """Returns an element that can obtain a certain value through a certain method
        :param name: attribute name
        :param value: attribute value
        :param method: method name
        :return: filter result
        """
        ...

    def _any_state(self, name: str, equal: bool = True) -> ChromiumElement:
        """
        :param name: state name
        :param equal: whether it is the specified state, False means negative state
        :return: selected list
        """
        ...


class ChromiumFilter(ChromiumFilterOne):

    def __iter__(self) -> Iterable[ChromiumElement]: ...

    def __next__(self) -> ChromiumElement: ...

    def __len__(self) -> int: ...

    def __getitem__(self, item: int) -> ChromiumElement: ...

    @property
    def get(self) -> Getter:
        """Returns an object for getting element attributes"""
        ...

    def tag(self, name: str, equal: bool = True) -> ChromiumFilter:
        """Filter a certain element
        :param name: tab name
        :param equal: True means matching this element, False means matching non-this element
        :return: filter result
        """
        ...

    def attr(self, name: str, value: str, equal: bool = True) -> ChromiumFilter:
        """Filter elements based on whether they have a certain attribute value
        :param name: attribute name
        :param value: attribute value
        :param equal: True means matching elements whose name value is value, False means matching elements whose name value is not value
        :return: Filter result
        """
        ...

    def text(self, text: str, fuzzy: bool = True, contain: bool = True) -> ChromiumFilter:
        """Filter elements based on whether they contain the specified text
        :param text: the text to match
        :param fuzzy: whether to fuzzy match
        :param contain: whether to contain the string, False means not to contain
        :return: filter result
        """
        ...

    def displayed(self, equal: bool = True) -> ChromiumFilter:
        """Filter elements based on whether they are displayed
        :param equal: whether to match displayed elements, False matches non-displayed
        :return: filter results
        """
        ...

    def checked(self, equal: bool = True) -> ChromiumFilter:
        """Filter elements based on whether they are selected
        :param equal: whether to match selected elements, False matches unselected ones
        :return: filter results
        """
        ...

    def selected(self, equal: bool = True) -> ChromiumFilter:
        """Filter elements based on whether they are selected, used for <select> element items
        :param equal: whether to match selected elements, False matches unselected elements
        :return: Filter results
        """
        ...

    def enabled(self, equal: bool = True) -> ChromiumFilter:
        """Filter elements based on availability
        :param equal: whether to match available elements, False means matching disabled elements
        :return: filter results
        """
        ...

    def clickable(self, equal: bool = True) -> ChromiumFilter:
        """Filter elements based on whether they are clickable
        :param equal: whether to match clickable elements, False means the match is not clickable
        :return: filter result
        """
        ...

    def have_rect(self, equal: bool = True) -> ChromiumFilter:
        """Filter elements based on whether they have a size
        :param equal: whether to match elements with a size, False means matching elements without a size
        :return: Filter results
        """
        ...

    def style(self, name: str, value: str, equal: bool = True) -> ChromiumFilter:
        """Filter elements based on whether they have a certain style value
        :param name: attribute name
        :param value: attribute value
        :param equal: True means matching elements whose name value is value, False means matching elements whose name value is not value
        :return: Filter result
        """
        ...

    def property(self,
                 name: str,
                 value: str, equal: bool = True) -> ChromiumFilter:
        """Filter elements based on whether they have a certain property value
        :param name: property name
        :param value: property value
        :param equal: True means matching elements whose name value is value, False means matching elements whose name value is not value
        :return: Filter result
        """
        ...

    def search_one(self,
                   index: int = 1,
                   displayed: Optional[bool] = None,
                   checked: Optional[bool] = None,
                   selected: Optional[bool] = None,
                   enabled: Optional[bool] = None,
                   clickable: Optional[bool] = None,
                   have_rect: Optional[bool] = None,
                   have_text: Optional[bool] = None,
                   tag: str = None) -> ChromiumElement:
        """Or relationship to filter elements and get a result
        :param index: element index, starting from 1
        :param displayed: whether to display, bool, None to ignore this item
        :param checked: whether it is selected, bool, None to ignore this item
        :param selected: whether it is selected, bool, None to ignore this item
        :param enabled: whether it is available, bool, None to ignore this item
        :param clickable: whether it is clickable, bool, None to ignore this item
        :param have_rect: whether it has size and position, bool, None to ignore this item
        :param have_text: whether it contains text, bool, None to ignore this item
        :param tag: the specified element type
        :return: filter results
        """
        ...

    def search(self,
               displayed: Optional[bool] = None,
               checked: Optional[bool] = None,
               selected: Optional[bool] = None,
               enabled: Optional[bool] = None,
               clickable: Optional[bool] = None,
               have_rect: Optional[bool] = None,
               have_text: Optional[bool] = None,
               tag: str = None) -> ChromiumFilter:
        """Or relationship filter elements
        :param displayed: whether it is displayed, bool, None means ignoring this item
        :param checked: whether it is selected, bool, None means ignoring this item
        :param selected: whether it is selected, bool, None means ignoring this item
        :param enabled: whether it is available, bool, None means ignoring this item
        :param clickable: whether it is clickable, bool, None means ignoring this item
        :param have_rect: whether it has size and position, bool, None means ignoring this item
        :param have_text: whether it contains text, bool, None means ignoring this item
        :param tag: the specified element type
        :return: filter results
        """
        ...

    def _get_attr(self,
                  name: str,
                  value: str,
                  method: str, equal: bool = True) -> ChromiumFilter:
        """Returns an element that can obtain a certain value through a certain method
        :param name: attribute name
        :param value: attribute value
        :param method: method name
        :return: filter result
        """
        ...

    def _any_state(self, name: str, equal: bool = True) -> ChromiumFilter:
        """
        :param name: state name
        :param equal: whether it is the specified state, False means negative state
        :return: selected list
        """
        ...


class Getter(object):
    _list: SessionElementsList = ...

    def __init__(self, _list: SessionElementsList):
        """
        :param _list: element list object
        """
        ...

    def links(self) -> List[str]:
        """Returns a list of link attributes for all elements"""
        ...

    def texts(self) -> List[str]:
        """Returns a list of all elements' text attributes"""
        ...

    def attrs(self, name: str) -> List[str]:
        """Returns a list of attr attributes specified by all elements
        :param name: attribute name
        :return: a list of attribute texts
        """
        ...


def get_eles(locators: Union[str, List[str], tuple],
             owner: BaseParser,
             any_one: bool = False,
             first_ele: bool = True,
             timeout: float = 10) -> Union[Dict[str, ChromiumElement], Dict[str, SessionElement],
Dict[str, List[ChromiumElement]], Dict[str, List[SessionElement]]]:
    """Pass in multiple locators to get multiple ele
    :param locators: list of locators
    :param owner: page or element object
    :param any_one: return if any one is found
    :param first_ele: whether to get only the first element for each locator
    :param timeout: timeout (seconds)
    :return: dict composed of multiple locators, return a list if first_only is False, otherwise an element, return False if no result
    """
    ...


def get_frame(owner: BaseParser,
              loc_ind_ele: Union[str, int, tuple, ChromiumFrame, ChromiumElement],
              timeout: float = None) -> ChromiumFrame:
    """Get a frame object in the page
    :param owner: the object in which the element is to be found
    :param loc_ind_ele: locator, iframe number, ChromiumFrame object, the number starts from 1, and a negative number can be passed in to get the last one
    :param timeout: timeout for finding an element (seconds)
    :return: ChromiumFrame object
    """
    ...
