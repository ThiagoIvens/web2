# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:51:27 2020

@author: Informatica
"""

# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável
# 3) Quantos caracteres cada título tem?
# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}


book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'


'''============================================================================'''
# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável
# 3) Quantos caracteres cada título tem?
titulo1 = book1.split(' by ')
t1 = titulo1[0]
print(t1)
print(len(t1))

titulo2 = book2.split(' by ')
t2 = titulo2[0]
print(t2)
print(len(t2))

titulo3 = book3.split(' by ')
t3 = titulo3[0]
print(t3)
print(len(t3))

# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}
resto1 = titulo1[1].split(', ')
resto2 = titulo2[1].split(', ')
resto3 = titulo3[2].split(', ')

print('Titulo: ', t1,', Autor: ', resto1[0],', Ano: ', resto1[1])
print('Titulo: ', t2,', Autor: ', resto2[0],', Ano: ', resto2[1])
print('Titulo: ', t3,', Autores: ', titulo3[1] ,' e ', resto3[0],', Ano: ', resto3[1])

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = palindrome_one.lower().replace(' ','')
palindrome_two = palindrome_two.lower().replace(' ','')
palindrome_three = palindrome_three.lower().replace(' ','')
palindrome_four = palindrome_four.lower().replace(' ','')

if(palindrome_one == palindrome_one[::-1]):
    print(palindrome_one, ' é um palindrome perfeito')
    

if(palindrome_two == palindrome_two[::-1]):
    print(palindrome_two, ' é um palindrome perfeito')

if(palindrome_three == palindrome_three[::-1]):
    print(palindrome_three, ' é um palindrome perfeito')

if(palindrome_four == palindrome_four[::-1]):
    print(palindrome_four, ' é um palindrome perfeito')