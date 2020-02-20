# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:01:17 2020

@author: PICHAU
"""
# LISTS
# https://docs.python.org/3/tutorial/introduction.html#lists

# list slicing [inicio:fim:passo]

weekdays = ['mon','tues','wed','thurs','fri']

print(weekdays)
print(type(weekdays))

days = weekdays[0]         # elemento 0
days = weekdays[0:3]       # elementos 0, 1, 2
days = weekdays[:3]        # elementos 0, 1, 2
days = weekdays[-1]        # ultimo elemento

test = weekdays[3:]        # elementos 3, 4

weekdays

days = weekdays[-2]        # ultimo elemento (elemento 4
days = weekdays[::]        # all elementos
days = weekdays[::2]       # cada segundo elemento (0, 2, 4)
days = weekdays[::-1]      # reverso (4, 3, 2, 1, 0)

all_days = weekdays + ['sat','sun']     # concatenar

print(all_days)

# Usando append
days_list = ['mon','tues','wed','thurs','fri']
days_list.append('sat')
days_list.append('sun')

print(days_list)
print(days_list == all_days)

list = ['a', 1, 3.14159265359]
print(list)
print(type(list))
# list.reverse()
# print(list)

#########
# Exercicios - Listas
# Faca sem usar loops
#########

print('---------------exercicios-------------')
# Como selecionar 'wed' pelo indice?
print(days_list.index('wed'))

# Como verificar o tipo de 'mon'?
print(type(days_list[days_list.index('mon')]))

# Como separar 'wed' até 'fri'?
a = days_list.index('wed')
b = days_list.index('fri')+1
print(days_list[a:b])

# Quais as maneiras de selecionar 'fri' por indice?
print(days_list.index('fri'))

# Qual eh o tamanho dos dias e days_list?
print(len(days_list))

# Como inverter a ordem dos dias?
days_list = days_list[::-1]
print(days_list)

# Como inserir a palavra 'zero' entre 'a' e 1 de list?
list.insert(1, 'zero')
print(list)

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
ultimo_elemento = list[-1]
list.remove(ultimo_elemento)
print(list)
print('Ultimo elemento que fora removido: ', ultimo_elemento)

# Como limpar list?
list.clear()
print(list)

# Como deletar list?
del(list)
