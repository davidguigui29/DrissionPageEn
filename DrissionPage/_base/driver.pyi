# -*- coding: utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from queue import Queue
from threading import Thread
from typing import Union, Callable, Dict, Optional

from requests import Response
from websocket import WebSocket

from .._base.chromium import Chromium


class Driver(object):
    id: str
    address: str
    type: str
    owner = ...
    alert_flag: bool
    _websocket_url: str
    _cur_id: int
    _ws: Optional[WebSocket]
    _recv_th: Thread
    _handle_event_th: Thread
    _handle_immediate_event_th: Optional[Thread]
    is_running: bool
    event_handlers: dict
    immediate_event_handlers: dict
    method_results: dict
    event_queue: Queue
    immediate_event_queue: Queue

    def __init__(self, tab_id: str, tab_type: str, address: str, owner=None):
        """
        :param tab_id: tab id
        :param tab_type: tab type
        :param address: browser connection address
        :param owner: the object that created this driver
        """
        ...

    def _send(self, message: dict, timeout: float = None) -> dict:
        """Send information to the browser and return the information returned by the browser
        :param message: data sent to the browser
        :param timeout: timeout, None means infinite
        :return: data returned by the browser
        """
        ...

    def _recv_loop(self) -> None:
        """The daemon thread method for receiving browser information"""
        ...

    def _handle_event_loop(self) -> None:
        """When receiving browser information, execute the bound method"""
        ...

    def _handle_immediate_event_loop(self): ...

    def _handle_immediate_event(self, function: Callable, kwargs: dict):
        """Handles actions that are executed immediately
        :param function: The method to be run
        :param kwargs: Method parameters
        :return: None
        """
        ...

    def run(self, _method: str, **kwargs) -> dict:
        """Execute cdp method
        :param _method: cdp method name
        :param kwargs: cdp parameters
        :return: execution result
        """
        ...

    def start(self) -> bool:
        """Start connection"""
        ...

    def stop(self) -> bool:
        """Disconnect"""
        ...

    def _stop(self) -> None:
        """Disconnect"""
        ...

    def set_callback(self, event: str, callback: Union[Callable, None], immediate: bool = False) -> None:
        """Bind cdp event and callback method
        :param event: cdp event
        :param callback: callback method bound to cdp event
        :param immediate: whether to process the action immediately
        :return: None
        """
        ...


class BrowserDriver(Driver):
    BROWSERS: Dict[str, Driver] = ...
    owner: Chromium = ...

    def __new__(cls, tab_id: str, tab_type: str, address: str, owner: Chromium): ...

    def __init__(self, tab_id: str, tab_type: str, address: str, owner: Chromium): ...

    def get(self, url) -> Response:
        """
        
        :param url: the link to visit
        :return: Response object
        """
        ...
