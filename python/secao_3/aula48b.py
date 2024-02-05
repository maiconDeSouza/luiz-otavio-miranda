"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = lista_a.copy()

print(f'endereço de memória lista_a -> {id(lista_a)}')
print(f'endereço de memória lista_b -> {id(lista_b)}')
print(f'endereço de memória lista_c -> {id(lista_c)}')


lista_a[0] = 'Dante'
print('lista_b ->', lista_b)
print('lista_c ->',lista_c)



