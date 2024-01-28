v1 = 'a'
v2 = 'a'
v3 = 'b'
v4 = {
    'a': 'a'
}
v5 = {
    'a': 'a'
}
v6 = v5

print(id(v1), 'V1 e V2 vão ser iguais, já que são valores primitivos')
print(id(v2), 'V1 e V2 vão ser iguais, já que são valores primitivos')
print(id(v3), 'V3 != V1 and V3 != V2, pois salva outro valor')
print(id(v4), 'V4 e V5 mesmo sendo iguais são salvos em endereços diferentes na memória, pois não são primitivos')
print(id(v5), 'V4 e V5 mesmo sendo iguais são salvos em endereços diferentes na memória, pois não são primitivos')
print(id(v5['a']), 'Pegando o valor da chave o obj e sendo esse valor "a" com em V1 e V2 ele vai apontar para o mesmo endereço de memória')
print(id(v6), 'Será o mesmo do V5')
print(v5 == v6, 'True')

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True

resultado = 'Não Passou no if' if passou_no_if is None else 'Passou no if'
print(resultado)