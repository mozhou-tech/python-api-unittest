#!/usr/bin/python
# coding=utf-8

from tests.case.agency.OrderTest import OrderTest


'''
组织测试用例
'''

def suite_main():
    ordertest = OrderTest()
    ordertest.test_order_default_list()