#!/usr/bin/python
# coding=utf-8

from tests.case.BaseTest import BaseTest
import requests
from utils.logger import main as logger
from time import time


class OrderTest(BaseTest):

    """
    准备变量
    :param self
    """
    def __init__(self):
        # 请求URL
        self.api_path = ''
        # 接口请求时间
        self.wait_time = 0
        # 参数
        self.params = {}
        # 请求方法
        self.method = ''
        self.entry = 'agency'

        self.params = {
           'user_id': 1
        }

    '''
    获取默认的订单列表
    '''
    def test_order_default_list(self):
        # 指定要测试的API
        self.api_path = '/api/v2/agency/order/query/order-operate'
        self.method = 'get'
        # 请求接口
        request_start = time()
        r = getattr(requests, self.method)(BaseTest.get_full_request_url(self.entry, self.api_path), headers = {
            'authorization': 'Bearer ' + OrderTest.get_auth_token()
        }, params=self.params)
        request_stop = time()
        logger().debug((request_stop-request_start)*1000)
        print(r.text)
        # assert r['errcode'] == 0

