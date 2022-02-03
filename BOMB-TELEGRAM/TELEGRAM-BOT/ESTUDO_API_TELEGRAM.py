# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:48:24 2022

@author: reisvmr
"""

import requests
import time
import json
#r = requests.post(URL_TELEGRAM_BASE + "/getUpdate")
#
#resposta_dict = r.json()
# Variaveis do Projetos:
#token = '2108042894:AAESUNKSc5INW5ze3s7n-ntTCX3ibYaWgFY'
#url_base = 'https://api.telegram.org/bot{token}/getUpdate'    
#token = '2108042894:AAESUNKSc5INW5ze3s7n-ntTCX3ibYaWgFY'

#payload = { 'token' : chave}
# Capturando mensagen no chat

class TelegramBot:
    
    def __init__(self):
        token = '2108042894:AAESUNKSc5INW5ze3s7n-ntTCX3ibYaWgFY'
        self.url_base = f'https://api.telegram.org/bot{token}/getUpdates'
        
    def Iniciar(self):
        update_id = Nome
        
    
   
while True:
    # Variveis
    token = '2108042894:AAESUNKSc5INW5ze3s7n-ntTCX3ibYaWgFY'
    # Ler mensagens
    url_base = f'https://api.telegram.org/bot{token}/getUpdates'   
    resultado = requests.get(url_base)
    # Imprime Resultados
    print (resultado.json())
    time.sleep (5)
    
