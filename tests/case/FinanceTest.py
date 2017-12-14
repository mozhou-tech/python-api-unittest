#!/usr/bin/python
# coding=utf-8

from tests.case.BaseClass import BaseClass
from utils.logger import logger_for_test_case


class FinanceTest(BaseClass):


    """
    准备变量
    :param self
    """
    def __init__(self):

        self.request_params = {
            'api_path': '',
            'method': 'get',
            'data': {},
            'entry': 'agency'  # 指定入口Base URL
        }





