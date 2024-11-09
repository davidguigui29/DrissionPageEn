# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from http.cookiejar import Cookie
from typing import Union

from requests import Session
from requests.cookies import RequestsCookieJar

from .._base.chromium import Chromium
from .._pages.chromium_base import ChromiumBase


def cookie_to_dict(cookie: Union[Cookie, str, dict]) -> dict:
    """Convert Cookie object to dict format
    :param cookie: Cookie object, string or dictionary
    :return: cookie dictionary
    """
    ...


def cookies_to_tuple(cookies: Union[RequestsCookieJar, list, tuple, str, dict, Cookie]) -> tuple:
    """Convert cookies to tuple format
    :param cookies: cookies information, can be CookieJar, list, tuple, str, dict
    :return: Return cookies in tuple format
    """
    ...


def set_session_cookies(session: Session,
                        cookies: Union[RequestsCookieJar, list, tuple, str, dict]) -> None:
    """Set cookies for the Session object
    :param session: Session object
    :param cookies: Cookies information
    :return: None
    """
    ...


def set_browser_cookies(browser: Chromium,
                        cookies: Union[RequestsCookieJar, list, tuple, str, dict]) -> None:
    """Set cookies value
    :param browser: page object
    :param cookies: cookies information
    :return: None
    """
    ...


def set_tab_cookies(page: ChromiumBase,
                    cookies: Union[RequestsCookieJar, list, tuple, str, dict]) -> None:
    """Set cookies value
    :param page: page object
    :param cookies: cookies information
    :return: None
    """
    ...


def is_cookie_in_driver(page: ChromiumBase, cookie: dict) -> bool:
    """Query whether the cookie is in the browser
    :param page: BasePage object
    :param cookie: dict format cookie
    :return: bool
    """
    ...


def format_cookie(cookie: dict) -> dict:
    """Set the cookie to a usable format
    :param cookie: dict format cookie
    :return: formatted cookie dictionary
    """
    ...


class CookiesList(list):
    def as_dict(self) -> dict:
        """Return in dict format, containing only name and value fields"""
        ...

    def as_str(self) -> str:
        """Return in str format, containing only name and value fields"""
        ...

    def as_json(self) -> str:
        """Return in json format"""
        ...

    def __next__(self) -> dict: ...
