#!/usr/bin/python
# coding=utf-8

from config import base


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
    获取基础路由
    """
    @classmethod
    def get_base_url(cls, entry):
        if entry is not None:
            return base.BASE_URL[entry]
        else:
            raise ValueError(u'请填写正确的Entry')