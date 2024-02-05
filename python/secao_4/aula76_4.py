p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda'
}

print(p1['nome'])
print(p1.get('nome'))

print(5 * '---')

# print(p1['idade']) -> vai gerar erro
print(p1.get('idade'))

print(5 * '---')

# sobrenome = p1.pop('sobrenome')
# print(sobrenome)

ultima_chamada = p1.popitem()
print(ultima_chamada)
print(p1)

p1.update({
    'sobrenome': 'Silva',
    'idade': 30
})

p1.update(is_valid=True)

print(p1)
