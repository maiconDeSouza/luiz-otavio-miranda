# map, partial, GeneratorType e esgotamento de Iterators
import mcn_module as mcn

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumenta_10(produto):
    produto['preco'] = round(produto['preco'] * 1.1, 2)
    return produto

# novos_produtos = map(lambda produto: {**produto, 'preco': round(produto['preco'] * 1.1, 2)}, produtos)
novos_produtos = map(aumenta_10, produtos)


mcn.console_log(novos_produtos, 'Nova lista de produtos com aumento de 10%')