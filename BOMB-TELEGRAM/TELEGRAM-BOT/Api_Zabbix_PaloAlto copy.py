
"""
Created on Tue Aug 20 15:09:43 2019

@author: viniciusreis
pip install requests
pip install simplejson
pip install urllib3
"""
#######Importando Bibliotecas##################
import requests
import time
import json
import urllib3
import xmltodict
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
urllib3.disable_warnings()
#################################################
###########          Metodo Post       ########## 
############ Declarando as Variaveis ############
#Payload contem todos os parametros que seram utilizados no post em forma de dicionario

while True:
    # Variveis
    url = 'https://10.32.208.101/api/'
    token = 'LUFRPT1idTV0YWlYbHd5ekozRjNOeE1kVnBHbC9lNUE9eTlGWXNncjJSekRpWE1MZ3hHcDVZYkhka3R5ZmoxSjZDV2RHTWxtOWtTUT0='
    type = 'op'
    tunel = '<show><vpn><flow><tunnel-id>6</tunnel-id></flow></vpn></show>'
    vpn = '<show><global-protect-portal><current-user><portal>GP-DECEAGP-GATEWAYGP-DECEA</portal></current-user></global-protect-portal></show>'
    #Payload contem todos os parametros que seram utilizados no post em forma de dicionario
    payload = { 'key' : token, 'type' : type, 'cmd' : tunel}
    # Ler mensagens
    response = requests.get(url, params=payload, verify=False)
    #Converter resultado xml to dict
    xpars = xmltodict.parse(response.text)
    #Converter resultado para json
    json = json.dumps(xpars)
    #Imprimindo resultado
    print (json)
    time.sleep (300)
    

