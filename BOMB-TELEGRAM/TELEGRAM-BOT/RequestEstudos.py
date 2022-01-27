# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:20:21 2022

@author: reisvmr
"""

import requests



# resp = requests.get("http://viacep.com.br/ws/24455050/json")

# #print(resp.texte)

# dd = resp.json()

# dt =resp.text

# print( dd )
# Criando func que coleta do endereço

def get_info_cep(cep):
    url_base = f'http://viacep.com.br/ws/{cep}/json'
    r = requests.get(url_base)
    return r.json()


d = get_info_cep("24455050")

def retorna_rua(d):
    return d['logradouro']


def retorna_bairro(d):
    return d['bairro']


