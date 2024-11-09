# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from http.cookiejar import CookieJar, Cookie
from pathlib import Path
from typing import Any, Union, Tuple, Optional

from requests import Session
from requests.adapters import HTTPAdapter
from requests.auth import HTTPBasicAuth
from requests.cookies import RequestsCookieJar
from requests.structures import CaseInsensitiveDict


class SessionOptions(object):
    """Configuration class for the requests.Session object"""

    ini_path: Optional[str] = ...
    _download_path: str = ...
    _headers: Union[dict, CaseInsensitiveDict, None] = ...
    _cookies: Union[list, RequestsCookieJar, None] = ...
    _auth: Optional[tuple] = ...
    _proxies: Optional[dict] = ...
    _hooks: Optional[dict] = ...
    _params: Union[dict, None] = ...
    _verify: Optional[bool] = ...
    _cert: Union[str, tuple, None] = ...
    _adapters: Optional[list] = ...
    _stream: Optional[bool] = ...
    _trust_env: Optional[bool] = ...
    _max_redirects: Optional[int] = ...
    _timeout: float = ...
    _del_set: set = ...
    _retry_times: int = ...
    _retry_interval: float = ...

    def __init__(self,
                 read_file: [bool, None] = True,
                 ini_path: Union[str, Path] = None):
        """
        :param read_file: Whether to read the configuration from a file
        :param ini_path: Path to the ini file
        """
        ...

    @property
    def download_path(self) -> str:
        """Returns the default download path property"""
        ...

    def set_download_path(self, path: Union[str, Path]) -> SessionOptions:
        """Sets the default download path
        :param path: Download path
        :return: Returns the current object
        """
        ...

    @property
    def timeout(self) -> float:
        """Returns the timeout property"""
        ...

    def set_timeout(self, second: float) -> SessionOptions:
        """Sets the timeout value
        :param second: Number of seconds
        :return: Returns the current object
        """
        ...

    @property
    def proxies(self) -> dict:
        """Returns the proxies settings"""
        ...

    def set_proxies(self, http: Union[str, None], https: Union[str, None] = None) -> SessionOptions:
        """Sets the proxies parameters
        :param http: HTTP proxy address
        :param https: HTTPS proxy address
        :return: Returns the current object
        """
        ...

    @property
    def retry_times(self) -> int:
        """Returns the number of retries for connection failures"""
        ...

    @property
    def retry_interval(self) -> float:
        """Returns the retry interval (in seconds) for connection failures"""
        ...

    def set_retry(self, times: int = None, interval: float = None) -> SessionOptions:
        """Sets the retry behavior for connection failures
        :param times: Number of retries
        :param interval: Retry interval
        :return: Current object
        """
        ...

    @property
    def headers(self) -> dict:
        """Returns the headers settings"""
        ...

    def set_headers(self, headers: Union[dict, str, None]) -> SessionOptions:
        """Sets the headers parameters
        :param headers: The value for headers. Passing None marks for deletion in the ini file
        :return: Returns the current object
        """
        ...

    def set_a_header(self, name: str, value: str) -> SessionOptions:
        """Sets one item in the headers
        :param name: Header name
        :param value: Header value
        :return: Returns the current object
        """
        ...

    def remove_a_header(self, name: str) -> SessionOptions:
        """Removes one item from the headers
        :param name: Name of the header to remove
        :return: Returns the current object
        """
        ...

    def clear_headers(self) -> SessionOptions:
        """Clears all header parameters"""
        ...

    @property
    def cookies(self) -> list:
        """Returns cookies as a list"""
        ...

    def set_cookies(self, cookies: Union[Cookie, CookieJar, list, tuple, str, dict, None]) -> SessionOptions:
        """Sets one or more cookies
        :param cookies: Cookies. Can be Cookie, CookieJar, list, tuple, str, or dict. Passing None marks for deletion in the ini file
        :return: Returns the current object
        """
        ...

    @property
    def auth(self) -> Union[Tuple[str, str], HTTPBasicAuth]:
        """Returns authentication settings"""
        ...

    def set_auth(self, auth: Union[Tuple[str, str], HTTPBasicAuth, None]) -> SessionOptions:
        """Sets the authentication tuple or object
        :param auth: Authentication tuple or object
        :return: Returns the current object
        """
        ...

    @property
    def hooks(self) -> dict:
        """Returns callback hooks"""
        ...

    def set_hooks(self, hooks: Union[dict, None]) -> SessionOptions:
        """Sets callback hooks
        :param hooks: Callback hooks
        :return: Returns the current object
        """
        ...

    @property
    def params(self) -> dict:
        """Returns the connection parameters settings"""
        ...

    def set_params(self, params: Union[dict, None]) -> SessionOptions:
        """Sets the query parameters dictionary
        :param params: Query parameters dictionary
        :return: Returns the current object
        """
        ...

    @property
    def verify(self) -> bool:
        """Returns whether SSL certificate verification is enabled"""
        ...

    def set_verify(self, on_off: Union[bool, None]) -> SessionOptions:
        """Sets whether to verify SSL certificates
        :param on_off: Whether to verify SSL certificates
        :return: Returns the current object
        """
        ...

    @property
    def cert(self) -> Union[str, tuple]:
        """Returns the SSL certificate settings"""
        ...

    def set_cert(self, cert: Union[str, Tuple[str, str], None]) -> SessionOptions:
        """Path to the SSL client certificate file (in .pem format), or a tuple ('cert', 'key')
        :param cert: Certificate path or tuple
        :return: Returns the current object
        """
        ...

    @property
    def adapters(self) -> list:
        """Returns the adapters settings"""
        ...

    def add_adapter(self, url: str, adapter: HTTPAdapter) -> SessionOptions:
        """Adds an adapter
        :param url: The URL for the adapter
        :param adapter: Adapter object
        :return: Returns the current object
        """
        ...

    @property
    def stream(self) -> bool:
        """Returns whether stream mode is enabled"""
        ...

    def set_stream(self, on_off: Union[bool, None]) -> SessionOptions:
        """Sets whether to use stream mode
        :param on_off: Whether to use stream mode
        :return: Returns the current object
        """
        ...

    @property
    def trust_env(self) -> bool:
        """Returns whether to trust the environment settings"""
        ...

    def set_trust_env(self, on_off: Union[bool, None]) -> SessionOptions:
        """Sets whether to trust the environment
        :param on_off: Whether to trust the environment
        :return: Returns the current object
        """
        ...

    @property
    def max_redirects(self) -> int:
        """Returns the maximum number of redirects"""
        ...

    def set_max_redirects(self, times: Union[int, None]) -> SessionOptions:
        """Sets the maximum number of redirects
        :param times: Maximum number of redirects
        :return: Returns the current object
        """
        ...

    def _sets(self, arg: str, val: Any) -> None:
        """Assigns a value to an attribute or marks it for deletion
        :param arg: Attribute name
        :param val: Parameter value
        :return: None
        """
        ...

    def save(self, path: str = None) -> str:
        """Saves the settings to a file
        :param path: Path to the ini file. Pass 'default' to save to the default ini file
        :return: Absolute path to the saved file
        """
        ...

    def save_to_default(self) -> str:
        """Saves the current configuration to the default ini file"""
        ...

    def as_dict(self) -> dict:
        """Returns this object as a dictionary"""
        ...

    def make_session(self) -> Tuple[Session, Optional[CaseInsensitiveDict]]:
        """Generates a Session object based on internal configurations, with headers separated from the object"""
        ...

    def from_session(self, session: Session, headers: CaseInsensitiveDict = None) -> SessionOptions:
        """Reads configurations from a Session object
        :param session: Session object
        :param headers: headers
        :return: Current object
        """
        ...


def session_options_to_dict(options: Union[dict, SessionOptions, None]) -> Union[dict, None]:
    """Converts session configuration object to dictionary
    :param options: SessionOptions object or dictionary
    :return: Configuration dictionary, or None if options is None
    """
    ...
