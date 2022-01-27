# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:35:55 2022

@author: reisvmr
"""
##############################
# POO
##############################

class Veiculo:
       def __init__(self, nome, tipo):
        self._nome = nome
        self._tipo = tipo


v2 = Veiculo("Caminhão", "Terrestre")

v2.tipoVeiculo()

moto = Veiculo("Honda","CB300")

barco = Veiculo("Barco pequeno","Marítimo")
