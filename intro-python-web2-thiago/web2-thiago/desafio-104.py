# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:57:57 2020

@author: Informatica
"""

'''
	DESAFIO!!!
	1) Implemente um algoritmo para trocar o conteudo de duas variáveis x e y.
	OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''


x = 10
y = 5

z = y
y = x
x = z

print('valor de x:',x)
print('valor de y:',y)

'''
2) Agora faca sem utilizar uma terceira variavel temporaria.
'''

def swap(s1, s2):
    return s2, s1


x, y = swap(x,y)


print('valor de x:',x)
print('valor de y:',y)