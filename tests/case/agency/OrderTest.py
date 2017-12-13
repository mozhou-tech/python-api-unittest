#!/usr/bin/python
# coding=utf-8

from tests.case.BaseTest import BaseTest


class OrderTest(BaseTest):

    """
    准备变量
    :param self
    """
    def __init__(self):
        # 请求URL
        self.base_url = BaseTest.get_base_url('agency')
        # API Auth Token
        self.auth_token = BaseTest.get_auth_token()
        # 接口请求时间
        self.wait_time = 0
        # API请求地址
        self.request_url = ''
        # 参数
        self.params = {}
        # 请求方法
        self.method = ''

    '''
    获取默认的订单列表
    '''
    def test_order_default_list(self):
        pass