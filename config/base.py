#!/usr/bin/python
# coding=utf-8
import logging

BASE_URL = {
    'agency': 'http://pre-deploy-s2b-test.lanzhu.xin',
    'console': 'http://pre-deploy-s2b-test.lanzhu.xin',
    'supplier': 'http://pre-deploy-s2b-test.lanzhu.xin',
}

AUTH_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImZiZjhmY2VjODVhMjY0YWJjNjk2MzQ1ZDA5Y2FjOTkwZjQwMzIxZmM2YzIxYzEyM2QxM2RlNTQ0OWY4M2MwZWNlMjY1MjdhYjQzYWQzOWZlIn0.eyJhdWQiOiIyMSIsImp0aSI6ImZiZjhmY2VjODVhMjY0YWJjNjk2MzQ1ZDA5Y2FjOTkwZjQwMzIxZmM2YzIxYzEyM2QxM2RlNTQ0OWY4M2MwZWNlMjY1MjdhYjQzYWQzOWZlIiwiaWF0IjoxNTEzMTYzMjk1LCJuYmYiOjE1MTMxNjMyOTUsImV4cCI6MTU0NDY5OTI5NSwic3ViIjoiMSIsInNjb3BlcyI6W119.2BsZe6f1hy1-oyDakluwd9atWMeAM2TsX5iijj8ExwDmi0V67MBTt4bvhov-CnrMAQvYSYjdkg9Uj625cMGcs5BcHuosZnZ3K7i-CmF2n6x_rZCTgOO7XKNJfiqiUgcZdZcLuOTVNnO-FnpKuTkn7JaXdhXHoxcJxLRsIjn74Lf_xb8kc1nzsUtfhyxfAM2e-BdYjhFRdC68SQSPiXHrPo7lTNqUs51RCm7qJE2S4rZj6SryY0eYLO4UvstFyH24bBMsD-zI_LSkApQD188xd3VCliJe8KK7-CzBlonwFlhNhQd1VyO5STCHlSKMkx_cC-qX1Y0jj53GiJxLYmCvP8zj15LBIS5_IbykgonEpBvg5nwS_hDG2g2WorGXPklZbDNb-DDQrcyG5e27mUC7hPGQy-1RBehJIlCTo72M5ez8Ma4Z07tbvQsrIUnXPOypllvjotjKVb84ITRxQsBMph5G6Q6o_FcnZchBbUeVFttqMsVI4PlTLzTSNWRyjzvz0jrPRDoPiMqpXlEIM3vPqz211ZwFrRg5yt_3GpSFRzg31pbvJEsLibmjijzj-FrGBIjOHHfBBeUCRtiqzetXifOz9yJ-NliyfLPhKszbMVLtyZsZcmQSZbdPb8OftECZsVuAQEQ9KxjfdrrvYOdfxTtjvaB4T-5o3yv5HqeqdEA'



LOGGING = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.INFO}
        },
    root = {
        'handlers': ['h'],
        'level': logging.INFO,
    },
)