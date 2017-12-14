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


    '''
    获取默认的订单列表
    '''
    @logger_for_test_case
    def test_order_default_list(self):
        # 准备参数
        self.request_params['api_path'] = '/api/v2/agency/order/query/order-operate'
        self.request_params['method'] = 'get'
        self.request_params['data'] = {'user_id': 1}
        # 请求接口
        r = self.request(self.request_params)
        # 运行基础断言
        info = self.report_base(r)         # 基础判断
        # 自定义断言
        # code...
        return r, info

    """
    订单详情
    """
    @logger_for_test_case
    def test_order_detail(self):
        # 准备参数
        self.request_params['api_path'] = '/api/v2/manage/order-manage/order-detail/order-main'
        self.request_params['method'] = 'get'
        self.request_params['data'] = {'order_item_id': 507224}
        # 请求接口
        r = self.request(self.request_params)  # 请求接口
        # 运行基础断言
        info = self.report_base(r)  # 基础判断
        # 运行自定义断言
        # code...
        return r, info



