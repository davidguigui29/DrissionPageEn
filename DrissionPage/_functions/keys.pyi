# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from typing import Tuple, Union, Any

from .._pages.chromium_base import ChromiumBase


class Keys:
    """Special keys"""
    CTRL_A: tuple
    CTRL_C: tuple
    CTRL_X: tuple
    CTRL_V: tuple
    CTRL_Z: tuple
    CTRL_Y: tuple

    NULL: str
    CANCEL: str
    HELP: str
    BACKSPACE: str
    TAB: str
    CLEAR: str
    RETURN: str
    ENTER: str
    SHIFT: str
    CONTROL: str
    CTRL: str
    ALT: str
    PAUSE: str
    ESCAPE: str
    SPACE: str
    PAGE_UP: str
    PAGE_DOWN: str
    END: str
    HOME: str
    LEFT: str
    UP: str
    RIGHT: str
    DOWN: str
    INSERT: str
    DELETE: str
    DEL: str
    SEMICOLON: str
    EQUALS: str

    NUMPAD0: str
    NUMPAD1: str
    NUMPAD2: str
    NUMPAD3: str
    NUMPAD4: str
    NUMPAD5: str
    NUMPAD6: str
    NUMPAD7: str
    NUMPAD8: str
    NUMPAD9: str
    MULTIPLY: str
    ADD: str
    SUBTRACT: str
    DECIMAL: str
    DIVIDE: str

    F1: str
    F2: str
    F3: str
    F4: str
    F5: str
    F6: str
    F7: str
    F8: str
    F9: str
    F10: str
    F11: str
    F12: str

    META: str
    COMMAND: str


keyDefinitions: dict = ...
modifierBit: dict = ...


def keys_to_typing(value: Union[str, int, list, tuple]) -> Tuple[int, str]:
    """Connect the content to be input into a string, and remove the ctrl and other keys.
    The returned modifier indicates whether a key combination is pressed"""
    ...


def make_input_data(modifiers: int,
                    key: str,
                    key_up: bool = False) -> dict:
    """
    :param modifiers: function key settings
    :param key: key character
    :param key_up: whether to raise
    :return: None
    """
    ...


def send_key(page: ChromiumBase, modifier: int, key: str) -> None:
    """Send a word. The characters on the keyboard trigger the key, and the others send text directly
    :param page: the page where the action is located
    :param modifier: function key information
    :param key: the key to be input
    :return: None
    """
    ...


def input_text_or_keys(page: ChromiumBase, text_or_keys: Any) -> None:
    """Enter text or key combinations. Key combinations are entered in tuple form
    :param page: ChromiumBase object
    :param text_or_keys: text value or key combination
    :return: self
    """
    ...
