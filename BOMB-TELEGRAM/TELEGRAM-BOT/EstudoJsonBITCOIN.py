# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:40:00 2022

@author: reisvmr
"""
import requests

def get_ticks(moeda='BTC',metodo='ticker'):
    url_base = f'https://mercadobitcoin.net/{moeda}/{metodo}/'
    r = requests.get(url_base)
    return r.json()
d = get_ticks