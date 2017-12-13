#!/usr/bin/python
# coding=utf-8

from tests.case.BaseTest import BaseTest
from utils.logger import main as logger
import sys



class OrderTest(BaseTest):


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
    def test_order_default_list(self):
        logger().info('running testcase: ' + __name__+'.'+sys._getframe().f_code.co_name+'.')
        # 准备参数
        self.request_params['api_path'] = '/api/v2/agency/order/query/order-operate'
        self.request_params['method'] = 'get'
        self.request_params['data'] = {'user_id': 1}

        r = BaseTest.request(self.request_params)   # 请求接口
        info = BaseTest.report_base(r)         # 基础判断

        # 写log
        logger().info(dict(r['result'], **info))
        logger().info('testcase run finished.')

        return r

    """
    订单详情
    """
    def test_order_detail(self):
        logger().info('running testcase: ' + __name__ + '.' + sys._getframe().f_code.co_name + '.')
        # 准备参数
        self.request_params['api_path'] = '/api/v2/manage/order-manage/order-detail/order-main'
        self.request_params['method'] = 'get'
        self.request_params['data'] = {'order_item_id': 507224}

        r = BaseTest.request(self.request_params)  # 请求接口
        info = BaseTest.report_base(r)  # 基础判断

        # 写log
        logger().info(dict(r['result'], **info))
        logger().info('testcase run finished.')

        return r


