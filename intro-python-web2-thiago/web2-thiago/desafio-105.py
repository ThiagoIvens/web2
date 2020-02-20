# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:18:48 2020

@author: Informatica
"""

'''
DESAFIO!!!
	1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
	OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
    
'''

lista = []

x = 0


def recursive(x):
    if x % 2 == 0:
            lista.append(x)
            x = x + 1      
    else:
            x = x + 1
            
    if x == 0 or len(lista) == 1000:
        return 1
    else:
        recursive(x)
            
            
    
recursive(x)

for y in lista:
    print(y)
    
'''
2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. 
        Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.
'''

lista2 = []

for c in range(99999999999999999999999999):
    lista2.append(c)


for z in lista2:
    print(z)
