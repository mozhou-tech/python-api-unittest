#!/usr/bin/python
# coding=utf-8

from tests.case.BaseTest import BaseTest
from utils.logger import main as logger


class OrderTest(BaseTest):

    """
    准备变量
    :param self
    """
    def __init__(self):
        # 接口请求时间
        self.wait_time = 0
        self.request_params = {
            'api_path': '',
            'method': 'get',
            'data': {
                'user_id': 1
            },
            'entry': 'agency'  # 指定入口Base URL
        }


    '''
    获取默认的订单列表
    '''
    def test_order_default_list(self):
        # 指定要测试的API
        self.request_params['api_path'] = '/api/v2/agency/order/query/order-operate'
        self.request_params['method'] = 'get'

        r = BaseTest.request(self.request_params)

        print(r[1])
        # assert r['errcode'] == 0

