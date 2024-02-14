import copy

def view(lista, name):
    print(name)
    print(*lista, sep='\n')
    print()
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos_10_por_cento = [{**produto, 'preco': round(produto['preco'] * 1.10, 2)} for produto in copy.deepcopy(produtos)]
produtos_10_por_cento[0]['nome'] = 'Produto 9'

view(produtos, 'Lista de Produtos Original')
view(produtos_10_por_cento, 'Copia')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
nome_do_maior_para_menor = sorted(produtos_10_por_cento, key=lambda p: p['nome'], reverse=True)
view(nome_do_maior_para_menor, 'Do maior nome para o menor')
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
menor = lambda produto: produto['preco']
preco_do_menor_para_maior = sorted(produtos_10_por_cento, key=menor)
view(preco_do_menor_para_maior, 'Do menor Preço para o Maior')