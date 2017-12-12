#!/usr/bin/python
# coding=utf-8

'''
在整个项目的测试过程，登录可能不止用到一次，如果每次都这么写，会不会太冗余了？ 对，确实太冗余了，
下面做一下简单的封装，把登录接口的调用封装到一个方法里，把调用参数暴漏出来
'''

import requests
import unittest
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

class DemoApi(object):
    def __init__(self, base_url):
        self.base_url = base_url
    def login(self, username, password):
        """
        登录接口
        :param username: 用户名
        :param password: 密码
        """
        url = urljoin(self.base_url, 'login')
        data = {
            'username': username,
            'password': password
        }
        return requests.post(url, data=data).json()
    def get_cookies(self, username, password):
        """
        获取登录cookies
        """
        url = urljoin(self.base_url, 'login')
        data = {
            'username': username,
            'password': password
        }
        return requests.post(url, data=data).cookies
    def info(self, cookies):
        """
        详情接口
        """
        url = urljoin(self.base_url, 'info')
        return requests.get(url, cookies=cookies).json()
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_url = 'http://127.0.0.1:5000'
        cls.username = 'admin'
        cls.password = '123456'
        cls.app = DemoApi(cls.base_url)
    def test_login(self):
        """
        测试登录
        """
        response = self.app.login(self.username, self.password)
        assert response['code'] == 200
        assert response['msg'] == 'success'
    def test_info(self):
        """
        测试获取详情信息
        """
        cookies = self.app.get_cookies(self.username, self.password)
        response = self.app.info(cookies)
        assert response['code'] == 200
        assert response['msg'] == 'success'
        assert response['data'] == 'info'