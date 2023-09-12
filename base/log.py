# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/12 22:58
@Author ： kangmingxiao
"""

import logging

class BaseLog:
    def __init__(self):
        self.logger = logging.getLogger("小程序自动化")
        self.logger.setLevel("INFO")

        steam_handler = logging.StreamHandler()
        steam_handler.setLevel("INFO")

        fmt1 = "[%(levelname)s]--[%(name)s--%(asctime)s]: %(message)s"
        ster_fmt1=logging.Formatter(fmt1)
        steam_handler.setFormatter(ster_fmt1)

        self.logger.addHandler(steam_handler)

if __name__ == '__main__':
    test=BaseLog()
    test.logger.info("你好")





