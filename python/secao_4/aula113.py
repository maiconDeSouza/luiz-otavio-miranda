# reduce - faz a redução de um iterável em um valor
import mcn_module as mcn
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

total = reduce(lambda acc, current: acc + current['preco'], produtos, 0)
print(total)