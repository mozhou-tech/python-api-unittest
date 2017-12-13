#!/usr/bin/python
# coding=utf-8

from tests.case.agency.OrderTest import OrderTest


'''
组织测试用例
'''

def suite_main():
    report_holder = []
    # 测试用例需要先实例化
    ordertest = OrderTest()
    report_holder.append(ordertest.test_order_default_list())
    report_holder.append(ordertest.test_order_detail())


    return report_holder