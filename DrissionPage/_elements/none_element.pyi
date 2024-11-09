# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from typing import Any

from .._base.base import BasePage


class NoneElement(object):
    def __init__(self,
                 page: BasePage = None,
                 method: str = None,
                 args: dict = None):
        """
        :param page: the page where the element is located
        :param method: the method to find the element
        :param args: the parameters to find the element
        """
        ...

    def __call__(self, *args, **kwargs) -> NoneElement: ...

    def __repr__(self) -> str: ...

    def __getattr__(self, item: str) -> str: ...

    def __eq__(self, other: Any) -> bool: ...

    def __bool__(self) -> bool: ...
