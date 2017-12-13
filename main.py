#!/usr/bin/python
# coding=utf-8
import sys
from datetime import datetime as dt
# 引入测试套件
from tests.suite.order_suite import suite_main as suite_order_main
from utils.logger import main as logger


start_time = dt.strftime(dt.now(), '%Y-%m-%d %H:%M')


# 自动测试入口


if __name__ == '__main__':
    report_holder = []
    # print(u'==================== Test Begin At : ' + start_time + ' ====================')
    report_holder += suite_order_main()
    # print(report_holder)










# 输出文档 基于openpyxl输出Excel
# 栏目：用例名,Api URL，method,结果,参数，原始返回, 响应时间
