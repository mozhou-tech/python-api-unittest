#!/usr/bin/python
# coding=utf-8

from config import base
import requests
from time import time
import json
from utils.logger import get_logger as logger


class BaseClass(object):

    def __init__(self):
        pass

    '''
    获取Api Auth Token
    '''
    @classmethod
    def get_auth_token(cls):
        return base.AUTH_TOKEN

    """
    获取完整的请求URL
    """
    @classmethod
    def get_full_request_url(cls, entry, api_path):
        if entry is not None:
            return base.BASE_URL[entry] + api_path
        else:
            raise ValueError(u'请填写正确的Entry')

    """
    发起HTTP Request
    """
    @classmethod
    def request(cls, params):
        assert params['method'] in ['get', 'post', 'put', 'delete', 'option']  # 请求方法限制
        # 请求接口
        logger().info('starting request api: ' + cls.get_full_request_url(params['entry'], params['api_path']))
        request_start = time()  # 开始时间
        response = getattr(requests, params['method'])(cls.get_full_request_url(params['entry'], params['api_path']), headers={
            'authorization': 'Bearer ' + cls.get_auth_token()
        }, params=params['data'])
        request_stop = time()   # 结束时间
        assert isinstance(json.loads(response.text.encode('utf8')), dict)

        return {
            'request_params': params,    # 请求参数
            'result': {
                'wait_time': round((request_stop - request_start) * 1000, 2),  # 请求用时
                'status_code': response.status_code,  # 返回状态码
                'content_length': len(response.text)
            },
            'content': json.loads(response.text.encode('utf8')),   # 返回原始内容
        }

    """
    基础断言
    """
    @classmethod
    def report_base(cls, r):
        result = []
        if not r['result']['wait_time'] <= 300:
            result.append('请求时间超过300ms')
        if not r['result']['status_code'] == 200:
            result.append('状态码错误')
        return {'desc': '，'.join(result)}





