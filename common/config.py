import os


class config(object):

    env = os.getenv('env','stg')
    if env == 'stg':
        gateway_url = "https://baymax-apisix-stg.c6b.internal.fpdev.tech"
        aaaa = '1'

    elif env == 'dev':
        gateway_url = "http://trading-system-gateway-stg-c.c6b.internal.fpdev.tech"
        aaaa = '1'


config = config()

