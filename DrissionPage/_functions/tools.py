# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from pathlib import Path
from platform import system
from shutil import rmtree
from tempfile import gettempdir
from threading import Lock
from time import perf_counter, sleep

from .._configs.options_manage import OptionsManager
from ..errors import (ContextLostError, ElementLostError, CDPError, PageDisconnectedError, NoRectError,
                      AlertExistsError, WrongURLError, StorageError, CookieFormatError, JavaScriptError)


class PortFinder(object):
    used_port = set()
    prev_time = 0
    lock = Lock()
    checked_paths = set()

    def __init__(self, path=None):
        tmp = Path(path) if path else Path(gettempdir()) / 'DrissionPage'
        self.tmp_dir = tmp / 'autoPortData'
        self.tmp_dir.mkdir(parents=True, exist_ok=True)
        if str(self.tmp_dir.absolute()) not in PortFinder.checked_paths:
            for i in self.tmp_dir.iterdir():
                if i.is_dir() and not port_is_using('127.0.0.1', i.name):
                    rmtree(i, ignore_errors=True)
            PortFinder.checked_paths.add(str(self.tmp_dir.absolute()))

    def get_port(self, scope=None):
        from random import randint
        with PortFinder.lock:
            if PortFinder.prev_time and perf_counter() - PortFinder.prev_time > 60:
                PortFinder.used_port.clear()
            if scope in (True, None):
                scope = (9600, 59600)
            max_times = scope[1] - scope[0]
            times = 0
            while times < max_times:
                times += 1
                port = randint(*scope)
                if port in PortFinder.used_port or port_is_using('127.0.0.1', port):
                    continue
                path = self.tmp_dir / str(port)
                if path.exists():
                    try:
                        rmtree(path)
                    except:
                        continue
                PortFinder.used_port.add(port)
                PortFinder.prev_time = perf_counter()
                return port, str(path)
            raise OSError('No available port found.')


def port_is_using(ip, port):
    from socket import socket, AF_INET, SOCK_STREAM
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(.1)
    result = s.connect_ex((ip, int(port)))
    s.close()
    return result == 0


def clean_folder(folder_path, ignore=None):
    ignore = [] if not ignore else ignore
    p = Path(folder_path)

    for f in p.iterdir():
        if f.name not in ignore:
            if f.is_file():
                f.unlink()
            elif f.is_dir():
                rmtree(f, True)


def show_or_hide_browser(page, hide=True):
    if not page.browser.address.startswith(('127.0.0.1', 'localhost')):
        return

    if system().lower() != 'windows':
        raise OSError('This method can only be used on Windows systems.')

    try:
        from win32gui import ShowWindow
        from win32con import SW_HIDE, SW_SHOW
    except ImportError:
        raise ImportError('Please install first: pip install pypiwin32')

    pid = page._page.process_id
    if not pid:
        return None
    hds = get_hwnds_from_pid(pid, page.title)
    sw = SW_HIDE if hide else SW_SHOW
    for hd in hds:
        ShowWindow(hd, sw)


def get_browser_progress_id(progress, address):
    if progress:
        return progress.pid

    from os import popen
    port = address.split(':')[-1]
    txt = ''
    progresses = popen(f'netstat -nao | findstr :{port}').read().split('\n')
    for progress in progresses:
        if 'LISTENING' in progress:
            txt = progress
            break
    if not txt:
        return None

    return txt.split(' ')[-1]


def get_hwnds_from_pid(pid, title):
    try:
        from win32gui import IsWindow, GetWindowText, EnumWindows
        from win32process import GetWindowThreadProcessId
    except ImportError:
        raise ImportError('Please install win32gui first, pip install pypiwin32')

    def callback(hwnd, hds):
        if IsWindow(hwnd) and title in GetWindowText(hwnd):
            _, found_pid = GetWindowThreadProcessId(hwnd)
            if str(found_pid) == str(pid):
                hds.append(hwnd)
            return True

    hwnds = []
    EnumWindows(callback, hwnds)
    return hwnds


def wait_until(function, kwargs=None, timeout=10):
    if kwargs is None:
        kwargs = {}
    end_time = perf_counter() + timeout
    while perf_counter() < end_time:
        value = function(**kwargs)
        if value:
            return value
        sleep(.01)
    raise TimeoutError


def configs_to_here(save_name=None):
    om = OptionsManager('default')
    save_name = f'{save_name}.ini' if save_name is not None else 'dp_configs.ini'
    om.save(save_name)


def raise_error(result, ignore=None, user=False):
    error = result['error']
    if error in ('Cannot find context with specified id', 'Inspected target navigated or closed',
                 'No frame with given id found'):
        r = ContextLostError()
    elif error in ('Could not find node with given id', 'Could not find object with given id',
                   'No node with given id found', 'Node with given id does not belong to the document',
                   'No node found for given backend id'):
        r = ElementLostError()
    elif error in ('connection disconnected', 'No target with given id found'):
        r = PageDisconnectedError()
    elif error == 'alert exists.':
        r = AlertExistsError()
    elif error in ('Node does not have a layout object', 'Could not compute box model.'):
        r = NoRectError()
    elif error == 'Cannot navigate to invalid URL':
        r = WrongURLError(f'Invalid url: {result["args"]["url"]}. Maybe add "http://"？')
    elif error == 'Frame corresponds to an opaque origin and its storage key cannot be serialized':
        r = StorageError()
    elif error == 'Sanitizing cookie failed':
        r = CookieFormatError(f'Incorrect cookie format: {result["args"]}')
    elif error == 'Invalid header name':
        r = ValueError(f'The header name is incorrect. \nParameters: {result["args"]["headers"]}')
    elif error == 'Given expression does not evaluate to a function':
        r = JavaScriptError(f'The incoming js cannot be parsed into a function:\n{result["args"]["functionDeclaration"]}')
    elif error.endswith("' wasn't found"):
        r = RuntimeError(f'The corresponding function was not found, the method is wrong or your browser is too old. \nMethod: {result["method"]}\nParameters: {result["args"]}')
    elif result['type'] == 'timeout':
        from DrissionPage import __version__
        txt = f'\nError: {result["error"]}\nMethod: {result["method"]}\nParameters: {result["args"]}\n' \
              f'Version: {__version__}\nTimeout, probably the browser is stuck.'
        r = TimeoutError(txt)
    elif result['type'] == 'call_method_error' and not user:
        from DrissionPage import __version__
        txt = f'\nError: {result["error"]}\nMethod: {result["method"]}\nParameters: {result["args"]}\n' \
              f'Version: {__version__}\nThis error may mean that there is a bug in the program. Please provide the error message and the method to reproduce it.' \
              'Inform the author, thank you. \nReport website: https://gitee.com/g1879/DrissionPage/issues'
        r = CDPError(txt)
    else:
        r = RuntimeError(result)

    if not ignore or not isinstance(r, ignore):
        raise r
