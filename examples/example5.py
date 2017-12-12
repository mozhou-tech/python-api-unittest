#!/usr/bin/python
# coding=utf-8

'''
封装重复操作
'''

class DemoApi(object):
    def __init__(self, base_url):
        self.base_url = base_url

    @request(url='login', method='post')   # 修饰器
    def login(self, username, password):
        """
        登录接口
        """
        data = {
            'username': username,
            'password': password
        }
        return {'data': data}

    @request(url='info', method='get')
    def info(self):
        """
        详情接口
        """
        pass