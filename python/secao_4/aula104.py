# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def check_string(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str):
                return func(*args, **kwargs)
            else:
                return f'mano deu ruim, o {arg=} é do tipo {type(arg)}, mas ela precisa ser str'
        
    return wrapper

@check_string
def inverter_string(string):
    return string[::-1]

print(inverter_string('Dante'))
print(inverter_string([]))