# -*- coding: utf-8 -*-
"""
@Autor: Vinicius Reis
reisvmr@gmail.com

"""
# Revisão Sobre Python
#####################################
# Dicionarios: []

""" Inicio do Comentario
Lista_vazia = []

Lista_vazia2 = list()

familia = ['Ricardo', 'Ntalia','Bianca']

# Inclusão na lista: 

familia.append('Natalia')
"""
##################################################
# Objetos do tipo tupla ()
"""
" São utilizados para armazenar valores imutaveis"

tupla_vazia = ()

t1 = tuple(['Rio','SG','Estrela'])
"""
#################################################
# Objetos do Tipo Dicionario: = {}
###################################################
"""
    Dicionarios são estruturar de armazenamento de dados do tipo chave:valor
"""
"""

dicionario = {}
    
dicionario2 = dict()
# Forma mas comum de declarar dicionarios
familia = {'Pai':'Herivelto','Mãe':'Tania','TemFilhos':True,'Filhos':'Vinicius'}
# Segunda forma de criar dicionarios
familia2 = dict(Pai="Vinicius",Mãe="Raquel",TemFilhos=False)

# Lista de Tuplas

Lista_Tuplas = [("Pai","João"),("Mãe","Julia"),("TemFilhos",False)]


# Convertendo lista de tuplas em dicionario 

Familia3 = dict(Lista_Tuplas)

# Resgatanto valores de Dicionarios:
    
   # Neste caso prenchemos o nome do dicionario e entre [Achave que estamos buscando] 
Familia3['Pai']
    # Adicionando 1 emento a lista:
        
familia2['Cachorro'] = 'Nina'
    # Add varios elementos a lista

familia2.update({'Casa':False, 'Carro':True})

    # Removendo Chave e Valor

familia2.pop('Carro')
   # Alterar elemento da lista
   
familia2['Cachorro'] = 'Bruce'
    # Busca chave em lista
    
'Mãe' in familia2

    # Adicionando lista em Dicionario
    
familia2['Animais'] = {'Cachorro','Gatos','Peixe'}

"""


#######################################
# Revisão Funçoes
#######################################
"""
def um ():
    x = 1
    print(x)
    dois(x)
    print(x)

def dois (y):
    print(y)
    y = 2
    print(y)
"""

    















