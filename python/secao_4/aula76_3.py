# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda'
}

pessoa_2 = pessoa # copia rasa (shallow copy) -> vai apenas apontar para o mesmo endereço
print('pessoa_2 ->',pessoa_2)
pessoa_2['sobrenome'] = 'Silva'
print('pessoa ->', pessoa)
print('pessoa_2 ->',pessoa_2)

print(5 * '---')

pessoa_3 = pessoa_2.copy() # 
print('pessoa_3 ->',pessoa_3)
pessoa_3['sobrenome'] = 'JBL'
print('pessoa_3 ->',pessoa_3)
print('pessoa_2 ->',pessoa_2)

print(5 * '---')
# Neste exemplo a copia da chave cachorros será uma copia raza, pois o método .copy() não se aprofunda e chave
# cachorros de pessoa_3 e pessoa_4 vai apontar para o mesmo endereço.
# Porém existe o deepcopy que irá copiar tudo, porém depentendo do tamanho do arquivo você pode ter perca de performace
pessoa_3['cachorros'] = ['Dante', 'Talu', 'Dona Maia']
pessoa_4 = pessoa_3.copy()
pessoa_5 = copy.deepcopy(pessoa_3)
pessoa_4['cachorros'].append('Pretinho')
print('pessoa_3 ->',pessoa_3)
print('pessoa_4 ->',pessoa_4)
print('pessoa_5 ->',pessoa_5)




