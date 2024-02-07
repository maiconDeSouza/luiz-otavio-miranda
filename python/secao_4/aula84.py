from pprint import pprint
# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))

def pmcn(v):
    pprint(v, sort_dicts=False, width=40)

lista = []
for numero in range(1, 11):
    if numero % 2 == 0:
        lista.append(numero)

print('lista ->', lista)

lista_2 = [numero for numero in range(1, 11) if numero % 2 == 0]

print('lista_2 ->', lista_2)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [{**produto, 'desc': 0.5} for produto in produtos]
print()
print('novos_produtos ->', *novos_produtos, sep='\n')

novos_produtos_2 = [{**produto} if produto['preco'] <= 20 else {**produto, 'preco': produto['preco'] * 1.10} for produto in produtos]

print()
print('novos_produtos_2 ->', *novos_produtos_2, sep='\n')

print()
pmcn(novos_produtos_2)
