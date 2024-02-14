# dir, hasattr e getattr em Python
string = 'Dante'
numero = 23

# dir serve para ver todos atributos que estão dentro da minha variável.
# print(dir(string)) 
print(string.isdigit)
print(string.isnumeric)

print()

# hasattr serve para verificar se existe esse atributo ou método dentro daquela variável
def verify(var):
    if hasattr(var, 'upper'):
        print(f'Sim, a variável {var=} do tipo {type(var)} tem o método upper()')
    else:
        print(f'Não, a variável {var=} do tipo {type(var)} não o método upper()')

verify(string)
verify(numero)
print()

metodo = 'upper'

# para atribuir um método ou atributo a variável dinamicamente se usa getattr
print(getattr(string, metodo)())