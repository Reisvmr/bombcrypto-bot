# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:48:24 2022

@author: reisvmr
"""

import requests
import time





#r = requests.post(URL_TELEGRAM_BASE + "/getUpdate")
#
#resposta_dict = r.json()
# Variaveis do Projetos:
token = '2108042894:AAESUNKSc5INW5ze3s7n-ntTCX3ibYaWgFY'
url_base = 'https://api.telegram.org/bot{token}'

# Capturando mensagen no chat

while True:
    r = requests.get(url_base + "/getMe")
    resposta_dict = r.json()
    print (resposta_dict)
    time.sleep (5)
    