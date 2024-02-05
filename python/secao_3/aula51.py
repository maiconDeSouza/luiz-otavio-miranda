"""
Introdução ao empacotamento e desempacotamento
"""
lista = ['Maria', 'Helena', 'Luiz', 'Dona Maia', 'Dante', 'Taluzinha', 'Delinha']

nome_1, nome_2, nome_3, *resto = lista
print(nome_1) # Maria
print(nome_2) # Helena
print(nome_3) # Luiz
print(resto) # ['Dona Maia', 'Dante', 'Taluzinha', 'Delinha']

# convenção de usar _ para armazenar o restante do itens quando você quer só um
quero_um, *_ = lista
print(quero_um) # Maria
print(_) # ['Helena', 'Luiz', 'Dona Maia', 'Dante', 'Taluzinha', 'Delinha']

# Aqui estou espalhando dentro de outra variável
lista_2 = ['Tupi', 'Mioto']
lista_3 = [*lista_2, *lista]
lista_4 = [*lista_2]
print(lista_3) # ['Tupi', 'Mioto', 'Maria', 'Helena', 'Luiz', 'Dona Maia', 'Dante', 'Taluzinha', 'Delinha']
print(id(lista_2), id(lista_4)) # 139933839826112 139933840040768








