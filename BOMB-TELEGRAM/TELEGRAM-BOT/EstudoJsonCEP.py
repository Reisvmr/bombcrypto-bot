# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:48:24 2022

@author: reisvmr
"""

import json

# Atenção abaixo temos uma string:

json_string = '{"First_name":"Vinicius", "Last_name":"Rossum"}'

# Para trabalharmos com o objeto json temos que converte-lo para um Dict :
    
json_dict = json.loads(json_string)

# Exemplo de dicionario 

d = {
     'first_name': 'Vinicius',
     'second_name': 'Reis',
     'titles':['SRE', 'DEVOPS', 'DEVSECOPS'],
}


d_json = json.dumps(d)

print (d_json)