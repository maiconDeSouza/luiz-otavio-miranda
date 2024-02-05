# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordenar(item):
#     return item['nome']

# lista.sort(key=ordenar)

lista.sort(key=lambda item: item['nome'])

print(lista)

soma = lambda x, y: x + y
print(soma(15, 23))

# lista = [2, 48, 1, 23, 3, 18, 99]
# new_list = sorted(lista)
# print(new_list)