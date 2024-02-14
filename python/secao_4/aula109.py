# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def view(value, title):
    print(title)
    print(*value, sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]


camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]
pessoas_list_1 = list(combinations(pessoas, 2))
view(pessoas_list_1, 'Combinação de pessoas no grupo de dois, sem repetição')

pessoas_list_2 = list(permutations(pessoas, 2))
view(pessoas_list_2, 'Combinação de pessoas no grupo de dois, com todas as possibilidades')

camisetas_list_1 = list(product(*camisetas))
view(camisetas_list_1, 'Todas combinações possiveis de lista dentro de lista')
