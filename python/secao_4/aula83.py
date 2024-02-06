a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

pessoa_complemento = {
    'idade': 16,
    'altura': 1.6
}

(var_1, var_2), (var_3, var_4) = pessoa.items()

print(var_1, var_2)
print(var_3, var_4)
print()
pessoa_completa = {**pessoa, **pessoa_complemento} # dois asteriscos para empacotar
print(pessoa_completa)


# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
print()
def mostrar_argumentos_nomeados(*args, **kwargs):
    print(args)
    print(kwargs)

mostrar_argumentos_nomeados('Dante', 'Dona Maia', produto='som', marca='jbl')

# 2 1
# nome Aline
# sobrenome Souza

# {'nome': 'Aline', 'sobrenome': 'Souza', 'idade': 16, 'altura': 1.6}

# ('Dante', 'Dona Maia')
# {'produto': 'som', 'marca': 'jbl'}