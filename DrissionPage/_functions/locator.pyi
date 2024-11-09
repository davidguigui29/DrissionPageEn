# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from typing import Union


def locator_to_tuple(loc: str) -> dict:
    """Parse the positioning string to generate dict format data
    :param loc: string to be processed
    :return: format: {'and': bool, 'args': ['attribute name', 'matching method', 'attribute value', whether to deny]}
    """
    ...


def is_loc(text: str) -> bool:
    """Returns whether text is a locator"""
    ...


def get_loc(loc: Union[tuple, str],
            translate_css: bool = False,
            css_mode: bool = False) -> tuple:
    """Receive the location syntax of this library or the selenium location tuple, convert it to a standard location tuple, and translate the css selector to xpath
    :param loc: location syntax of this library or the selenium location tuple
    :param translate_css: whether to translate the css selector to xpath for relative positioning
    :param css_mode: whether to use the css selector mode as much as possible
    :return: DrissionPage location tuple
    """
    ...


def str_to_xpath_loc(loc: str) -> tuple:
    """Process element search statement
    :param loc: search syntax string
    :return: matcher tuple
    """
    ...


def str_to_css_loc(loc: str) -> tuple:
    """Process element search statement
    :param loc: search syntax string
    :return: matcher tuple
    """
    ...


def translate_loc(loc: tuple) -> tuple:
    """Convert the loc tuple of By type to css selector or xpath type
    :param loc: loc tuple of By type
    :return: loc tuple of css selector or xpath type
    """
    ...


def translate_css_loc(loc: tuple) -> tuple:
    """Convert the loc tuple of By type to css selector or xpath type
    :param loc: loc tuple of By type
    :return: loc tuple of css selector or xpath type
    """
    ...


def css_trans(txt: str) -> str:
    """Special character escape in css string
    :param txt: text to be processed
    :return: processed text
    """
    ...
