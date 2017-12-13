#!/usr/bin/python
# coding=utf-8

import logging
from logging.config import dictConfig
from config.base import LOGGING as logging_config


"""
返回logging对象
"""


def main():
    dictConfig(logging_config)
    logger = logging.getLogger()
    return logger

