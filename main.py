#!/usr/bin/python
# coding=utf-8
import sys
from datetime import datetime as dt
# 引入测试套件
from tests.suite.suite_main import suite_main
from utils.logger import get_logger as logger
from openpyxl import Workbook
from datetime import datetime as dt
import sys,os


# 自动测试入口

if __name__ == '__main__':

    report_holder = suite_main()
    logger().info('Outputting to a excel file ...')
    # 输出文档 基于openpyxl输出Excel
    # 栏目：用例名,Api URL，method,结果,参数，原始返回, 响应时间
    report_path_name = sys.path[0] + "/reports/" + dt.strftime(dt.now(), '%b%d%y%H%M') +".xlsx"
    wb = Workbook()
    for sheet in wb:
        for item in report_holder:
            sheet.append(item)

    wb.save(filename=report_path_name)
    logger().info('Report saved to '+report_path_name)
