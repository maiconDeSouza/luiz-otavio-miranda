from itertools import zip_longest
# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

lista_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_estados = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista1, lista2):
    intervalo_max = min(len(lista1), len(lista2))
    return [(lista1[i], lista2[i]) for i in range(intervalo_max)]

print(zipper(lista_cidades, lista_estados))

print()

def zipper_2(lista_1, lista_2):
    result = list(zip(lista_1, lista_2))
    return result

print(zipper_2(lista_cidades, lista_estados))

print()

def zipper_3(lista_1, lista_2):
    result = list(zip_longest(lista_1, lista_2))
    return result

print(zipper_3(lista_cidades, lista_estados))

print()

def zipper_4(lista_1, lista_2):
    result = list(zip_longest(lista_1, lista_2, fillvalue='Valor de Preenchimento'))
    return result

print(zipper_4(lista_cidades, lista_estados))