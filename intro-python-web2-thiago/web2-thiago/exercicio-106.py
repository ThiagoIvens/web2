# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

###
## Exercicios
###

import csv

with open('capitais-BR.csv', 'r', encoding='utf8') as capitais:
        st = csv.reader(capitais, delimiter=';')
        for linha in st:
            print(linha)

# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao. Utilize a clausula else no loop implementado.
print('exercicio 1 ----------------')
def define_default_city(state):
    with open('capitais-BR.csv', 'r', encoding='utf8') as capitais:
        st = csv.reader(capitais, delimiter=';')
        l = list(st)
        for linha in l:
            if linha[0] == state:
                return True
        else:
            return False

''' Define a capital do estado de origem como city_origin para um professor existente no arquivo.
Retorna True se a capital do estado de origem existe no arquivo capitais-BR.csv e False, caso contrario.
Keyword arguments:
state -- O estado de origem do professor
'''
pass


# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste e teste se sua funcao estah robusta o suficiente.
print('exercicio 2 ----------------')  
def remover():
    with open("capitais-BR.csv", 'r', encoding='utf8') as capitaisIn:
        estados = csv.reader(capitaisIn, delimiter=';')
        lista = list(estados)
        print(lista)
        lista.remove(['Rio de Janeiro', 'Rio de Janeiro'])
        lista.remove(['Minas Gerais', 'Belo Horizonte'])
        lista.remove(['Espírito Santo', 'Vitória'])
        lista.remove(['São Paulo', 'São Paulo'])
        print(lista)

    with open("capitais-BR.csv", 'w', encoding='utf8') as capitaisOut:
        writer = csv.writer(capitaisOut)
        writer.writerows(lista)


# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de CPF unicos (sem repeticao) e os escreva em um arquivo lista-cpf-unicos.txt. 
#    Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz primeiro.
print('exercicio 3 ----------------')
arquivo = open('lista-cpf-unicos.txt', 'w', encoding='utf8')  
arquivo.close;

def separarcpf():
    with open('lista-cpf.txt', 'r', encoding='utf8' ) as allcpfs:
        for cpf in allcpfs:
                if cpf not in listarUnicos():
                    escrever(cpf)

def listarUnicos():
    with open('lista-cpf-unicos.txt', 'r', encoding='utf8') as cpfUnicos:
        listaUnicos = list(cpfUnicos)
    return listaUnicos
        
def escrever(string):
    with open('lista-cpf-unicos.txt', 'w', encoding='utf8') as cpfU:
        cpfU.write(string)

with open('lista-cpf-unicos.txt', 'r', encoding='utf8') as cpfUnicos:
    cpfs = list(cpfUnicos)
    print(cpfs)
