# coding=utf-8

import json

from util.comm import call_api

def do_support (params, exchange, market):
    res = call_api(params, '/exchange-support', exchange=exchange, market=market)
    if exchange is None:
        for xchg in res['exchanges']:
            print(xchg)
    else:
        markets = res.get('markets', None)
        if markets:
            if market is None:
                for name, market in markets.items():
                    ids = market['ids']
                    cryptowatch = market['cryptowatch']
                    resolutions = market['resolutions']
                    print(f'{name}: {ids}: {cryptowatch}: {resolutions}')
            else:
                for market in markets:
                    ids = market['ids']
                    cryptowatch = market['cryptowatch']
                    resolutions = market['resolutions']
                    print(f'{ids}: {cryptowatch}: {resolutions}')

