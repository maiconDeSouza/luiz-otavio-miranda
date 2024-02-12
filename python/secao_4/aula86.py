# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
    'authored': True
}



dc = {
    chave: valor.upper() if isinstance(valor, str) else valor for chave, valor in produto.items() if chave != 'authored'
}
print('dc ->', dc)


# Tupla contendo tuplas de chave-valor
chave_valor_tuplas = (
    ("chave1", "valor1"),
    ("chave2", "valor2"),
    ("chave3", "valor3"),
    ("chave4", "valor4")
)

# Usando Dictionary Comprehension para extrair as chaves e valores
dicionario = {chave: valor for chave, valor in chave_valor_tuplas}

print('dicionario ->', dicionario)

# dc -> {'nome': 'CANETA AZUL', 'preco': 2.5, 'categoria': 'ESCRITÓRIO'}
# dicionario -> {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4'}

s1 = {i  for i in range(26)}
print(s1)