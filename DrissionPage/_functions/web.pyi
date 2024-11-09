# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from pathlib import Path
from typing import Union, Optional, Tuple

from .._base.base import DrissionElement, BaseParser
from .._elements.chromium_element import ChromiumElement
from .._pages.chromium_base import ChromiumBase
from .._pages.chromium_page import ChromiumPage
from .._pages.chromium_tab import ChromiumTab


def get_ele_txt(e: DrissionElement) -> str:
    """Get all text in an element
    :param e: element object
    :return: all text in an element
    """
    ...


def format_html(text: str) -> str:
    """Handle HTML encoded characters
    :param text: HTML text
    :return: Formatted HTML text
    """
    ...


def location_in_viewport(page: ChromiumBase, loc_x: float, loc_y: float) -> bool:
    """Determine whether the given coordinates are in the viewport |n
    :param page: ChromePage object
    :param loc_x: page absolute coordinate x
    :param loc_y: page absolute coordinate y
    :return: bool
    """
    ...


def offset_scroll(ele: ChromiumElement, offset_x: float, offset_y: float) -> Tuple[int, int]:
    """Receive element and offset coordinates, scroll the coordinates to the middle of the page, and return the coordinates of the point.
    When there is an offset, the coordinates of the upper left corner of the element are used as the reference, and when there is no offset, the coordinates of click_point are used as the reference.
    :param ele: element object
    :param offset_x: offset x
    :param offset_y: offset y
    :return: relative coordinates
    """
    ...


def make_absolute_link(link: str, baseURI: str = None) -> str:
    """Get the absolute URL
    :param link: hyperlink
    :param baseURI: page or iframe URL
    :return: absolute link
    """
    ...


def is_js_func(func: str) -> bool:
    """Check if the text is a js function"""
    ...


def get_blob(page: ChromiumBase, url: str, as_bytes: bool = True) -> bytes:
    """Get the blob resource
    :param page: the page object where the resource is located
    :param url: the resource url
    :param as_bytes: whether to return in bytes
    :return: the resource content
    """
    ...


def save_page(tab: Union[ChromiumPage, ChromiumTab],
              path: Union[Path, str, None] = None,
              name: Optional[str] = None,
              as_pdf: bool = False,
              kwargs: dict = None) -> Union[bytes, str]:
    """Save the current page as a file. If both path and name are None, only text is returned. 
    :param tab: Tab or Page object. 
    :param path: Save path. If None and name is not None, save in the current path. 
    :param name: File name. If None and path is not None, use the title attribute value. 
    :param as_pdf: Save as pdf if True, otherwise save as mhtml and ignore kwargs. 
    :param kwargs: PDF generation parameters. 
    :return: Return bytes if as_pdf is True, otherwise return file text. 
    :param kwargs: PDF generation parameters.
    """
    ...


def get_mhtml(page: Union[ChromiumPage, ChromiumTab],
              path: Optional[Path] = None,
              name: Optional[str] = None) -> Union[bytes, str]:
    """Save the current page as an mhtml file. If both path and name parameters are None, only the mhtml text is returned
    :param page: the page object to be saved
    :param path: the saving path. If it is None and name is not None, it is saved in the current path
    :param name: the file name. If it is None and path is not None, the title attribute value is used
    :return: mhtml text
    """
    ...


def get_pdf(page: Union[ChromiumPage, ChromiumTab],
            path: Optional[Path] = None,
            name: Optional[str] = None,
            kwargs: dict = None) -> Union[bytes, str]:
    """Save the current page as a pdf file. If both path and name are None, only bytes are returned. 
    :param page: the page object to be saved. 
    :param path: the save path. If None and name is not None, save in the current path. 
    :param name: the file name. If None and path is not None, use the title attribute value. 
    :param kwargs: pdf generation parameters. 
    :return: pdf text. """
    ...


def tree(ele_or_page: BaseParser,
         text: Union[int, bool] = False,
         show_js: bool = False,
         show_css: bool = False) -> None:
    """Print out the DOM structure of the page or element object
    :param ele_or_page: page or element object
    :param text: whether to print text, enter a number to specify the upper limit of the printed text length
    :param show_js: whether to include the text in <script> when printing text, invalid when the text parameter is False
    :param show_css: whether to include the text in <style> when printing text, invalid when the text parameter is False
    :return: None
    """
    ...


def format_headers(txt: str) -> dict:
    """Generate dict format headers from text copied from the browser, text is separated by newlines
    :param txt: original text format headers copied from the browser
    :return: dict format headers
    """
    ...
