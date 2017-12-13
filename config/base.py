#!/usr/bin/python
# coding=utf-8
import logging

BASE_URL = {
    'agency': 'http://pre-deploy-s2b-test.lanzhu.xin',
    'console': 'http://pre-deploy-s2b-test.lanzhu.xin',
    'supplier': 'http://pre-deploy-s2b-test.lanzhu.xin',
}

AUTH_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImZiMjI2MjQ0MDQ5ZDZmZTI5ODFiMGEwYzgxYTNmOWM3ZTJjNDcxOTdmMjQyNGU5MTVkNWNjMGIxNGI1ZWIxZGZhN2ZiN2JmMTcyNjhlMTExIn0.eyJhdWQiOiIyMSIsImp0aSI6ImZiMjI2MjQ0MDQ5ZDZmZTI5ODFiMGEwYzgxYTNmOWM3ZTJjNDcxOTdmMjQyNGU5MTVkNWNjMGIxNGI1ZWIxZGZhN2ZiN2JmMTcyNjhlMTExIiwiaWF0IjoxNTEzMTQ3NzM3LCJuYmYiOjE1MTMxNDc3MzcsImV4cCI6MTU0NDY4MzczNywic3ViIjoiMSIsInNjb3BlcyI6W119.JfLAec2HTUIYBc83jx3Wq4nZdtinNdqHcLmhXObkIiN6zdMJYCGtb817FLOYUHr11BCh6p3lp4YrEM7_5R_jzSRbXBgL-lKDlnY4yUIi97kab9Q0Ge8Wb-crY-yVOAMAuN6JmeiuF8vVe8s94fxW2dvfMeLjOwLRRARgWQfXG0FoMmx9hV53_Q6lPHoz8BoI3qMNq3MDJyvOnAPFK5T3xlZVvKbbTDIaBlQ8Ouf1p3xy6jlQVd4XgDX7sY1j--HlTcTkqzX2PaTdGQd3WRwwtaJYgXSoaXSyHTSNCUxRPis5X2fit5dR89Ojh1tT5N2GdsMrcn9g0LNANZRs5whEoY3foe35LzM4br1BEZMYfgrjFxRtE5YBIEChhTYdDe7XWzpiamjERNgkD0SWHX04sRptLRHSEDjmUjgCL-IA_s_Ezerj4j7azuAy_jhn2-y3X_2se3eQ7ZrL-d2MKgTPRbcCg0G_dv0Eh4hBrBP3pJkIt2Bb36LoLzeO9DaP25Pm56Aus9WsFYz7nYi7FG0onVgM8GtUl7d3ux7Pgq2KYR0WyeUZPbJrKW8-17f37kIP8CrNltON_CK28g_21U5Az5NWuo_Q0h7289ANeD4aAj_F60vuh2mzMcMSYkCg7ZSrEGETONDYBoRZHpNMvpEkvBl88kdclK-7_iisOisBsUk'


LOGGING = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
        },
    root = {
        'handlers': ['h'],
        'level': logging.DEBUG,
    },
)