"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
list_array = [123, True, 'Luiz Otávio', 1.2, []]
list_array.insert(1, '23')
list_array.insert(0, 'Dante')
print(list_array)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
print(lista_c)

lista_a.extend(lista_c)
print(lista_a)