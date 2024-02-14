# decorate com parametros
def decoradora(func):
    print('decora 1')
    def wrapper(*args, **kwargs):
        print('embrulho')
        return func(*args, **kwargs)
    return wrapper

@decoradora
def soma(x, y):
    return x + y

print(soma(5, 3))

print()

def decoradora_2(z):
    def decoradora(func):
        print('decora 1')
        def wrapper(*args, **kwargs):
            print('embrulho')
            result =  func(*args, **kwargs)
            return result + z
        return wrapper
    return decoradora

@decoradora_2(9)
def soma_2(x, y):
    return x + y

print(soma_2(18, 23))
