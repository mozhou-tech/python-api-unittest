#!/usr/bin/python
# coding=utf-8
import tests.case
import importlib
from utils.logger import get_logger as logger


'''
组织测试用例
'''


def suite_main():
    report_holder = []
    # 测试用例需要先实例化
    testcase_list = list(filter(lambda x: x.endswith('Test'), dir(tests.case)))
    # 第一层，遍历所有测试用例
    for testcase in testcase_list:
        logger().info('Loading TestCase ' + testcase+' ...')
        amodule = importlib.import_module('tests.case.'+testcase)
        obj = getattr(amodule, testcase)()
        testcase_method_list = list(filter(lambda x: x.startswith('test_'), dir(obj)))

        # 第二层, 遍历所有测试方法
        for testcase_method in testcase_method_list:
            result = getattr(obj, testcase_method)()
            report_tuple = (
                result[0]['result']['testcase'],
                result[0]['request_params']['api_path'],
                result[0]['request_params']['method'],
                result[0]['result']['status_code'],
                str(result[0]['request_params']['data']),
                str(result[0]['result']['wait_time'])+'ms',
                str(result[0]['result']['content_length'])+' byte',
                str(result[0]['content']),

            )
            report_holder.append(report_tuple)

    return report_holder
