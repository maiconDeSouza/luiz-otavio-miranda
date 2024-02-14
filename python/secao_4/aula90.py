import sys
# Generator expression, Iterables e Iterators em Python
string = 'Eu tenho __iter__'

# iterador = string.__iter__()
# print(iterador.__next__())
# print(iterador.__next__())

iterador = iter(string)
print(next(iterador)) # E
print(next(iterador)) # U

lista = [n for n in range(1, 1000001)]
generator = (n for n in range(1, 1000001))

# generator[0] não tem indice
# len(generator) não tem tamanho

print(sys.getsizeof(lista)) # 8448728 -> tamanho
print(sys.getsizeof(generator)) # 192 -> tamanho

print(next(generator)) # 1
print(next(generator)) # 2


