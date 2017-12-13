#!/usr/bin/python
# coding=utf-8

from config import base


class BaseTest(object):

    def __init__(self):
        # 请求URL
        self.base_url = BaseTest.get_base_url('agency')
        self.auth_token = BaseTest.get_auth_token()

    '''
    获取Api Auth Token
    '''
    @classmethod
    def get_auth_token(cls):
        return base.AUTH_TOKEN

    """
    获取基础路由
    """
    @classmethod
    def get_base_url(cls, entry):
        if entry is not None:
            return base.BASE_URL[entry]
        else:
            raise ValueError(u'请填写正确的Entry')

    """
    获取完整的请求URL
    """
    @classmethod
    def get_full_request_url(cls, entry, api_path):
        return cls.get_base_url(entry) + api_path


