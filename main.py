#!/usr/bin/python
# coding=utf-8
import sys
from datetime import datetime as dt
# 引入测试套件
from tests.suite.order_suite import suite_main as order_suite_main

start_time = dt.strftime(dt.now(),'%Y-%m-%d %H:%M')

print(u'==================== Test Begin At : '+start_time+' ====================')

# 自动测试入口


if __name__ == '__main__':
    order_suite_main()










# 输出文档 基于openpyxl输出Excel
# 栏目：用例名,Api URL，method,结果,参数，原始返回, 响应时间
