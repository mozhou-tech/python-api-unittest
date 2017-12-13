#!/usr/bin/python
# coding=utf-8

from config import base
import requests
from time import time


class BaseTest(object):

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
        # 请求接口
        request_start = time()
        response = getattr(requests, params['method'])(cls.get_full_request_url(params['entry'], params['api_path']), headers={
            'authorization': 'Bearer ' + cls.get_auth_token()
        }, params=params['data'])
        request_stop = time()
        wait_time = (request_stop - request_start) * 1000
        return response, wait_time



