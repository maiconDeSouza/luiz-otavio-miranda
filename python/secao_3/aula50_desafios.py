lista = ['Maria', 'Helena', 'Luiz']

for index, item in enumerate(lista):
    print(index, item)

lista_enumerada = enumerate(lista)
print(lista_enumerada)
print(next(lista_enumerada))

print(10 * '-')
lista_2 = ['HP', 'JBL', 'Switch']
# o ruim de usar o enumerate dentro de uma variável é que você só consegue usar uma vez, este comportamento 
# é estranho em python. Então a melhor forma de fazer é a opção de cima!!!! for index, item in enumerate(lista):
lista_enumerada_2 = enumerate(lista_2)
for value in lista_enumerada_2:
    print(value)

lista_enumerada_2_conv_list = list(enumerate(lista_2))
print(lista_enumerada_2_conv_list)

lista_enumerada_2_conv_tuple = tuple(enumerate(lista_2))
print(lista_enumerada_2_conv_tuple)

lista_enumerada_2_conv_index = list(enumerate(lista_2, start=1))
print(lista_enumerada_2_conv_index )


