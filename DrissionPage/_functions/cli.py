# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from click import command, option

from .._functions.tools import configs_to_here as ch
from .._configs.chromium_options import ChromiumOptions
from .._pages.chromium_page import ChromiumPage


@command()
@option("-p", "--set-browser-path", help="Set browser path")
@option("-u", "--set-user-path", help="Set user data path")
@option("-c", "--configs-to-here", is_flag=True, help="Copy the default configuration file to the current path")
@option("-l", "--launch-browser", default=-1, help="Start the browser and pass in the port number.\n0 means using the value in the configuration file.")
def main(set_browser_path, set_user_path, configs_to_here, launch_browser):
    if set_browser_path:
        set_paths(browser_path=set_browser_path)

    if set_user_path:
        set_paths(user_data_path=set_user_path)

    if configs_to_here:
        ch()

    if launch_browser >= 0:
        port = f'127.0.0.1:{launch_browser}' if launch_browser else None
        ChromiumPage(port)


def set_paths(browser_path=None, user_data_path=None):
    """Quick path setting function
    :param browser_path: browser executable file path
    :param user_data_path: user data path
    :return: None
    """
    co = ChromiumOptions()

    if browser_path is not None:
        co.set_browser_path(browser_path)

    if user_data_path is not None:
        co.set_user_data_path(user_data_path)

    co.save()


if __name__ == '__main__':
    main()
