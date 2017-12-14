#!/usr/bin/python
# coding=utf-8
import tests.case
from utils.logger import get_logger as logger


'''
组织测试用例
'''


def suite_main():
    report_holder = []
    # 测试用例需要先实例化
    testcase_list = list(filter(lambda x: x.endswith('Test'), dir(tests.case)))
    print(testcase_list)
    # 第一层，遍历所有测试用例
    for testcase in testcase_list:
        logger().info('Loading TestCase ' + testcase+' ...')
        eval('import tests.case.' + testcase)
        obj = eval(testcase+'()')
        testcase_method_list = list(filter(lambda x: x.startswith('test_'), dir(obj)))

        # 第二层, 遍历所有测试方法
        for testcase_method in testcase_method_list:
            report_holder.append(getattr(obj, testcase_method)())

    return report_holder
