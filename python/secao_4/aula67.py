# Valores padrão para parâmetros
# Ao definir uma função, os parâmetros podem
# ter valores padrão. Caso o valor não seja
# enviado para o parâmetro, o valor padrão será
# usado.
# Refatorar: editar o seu código.

def soma(x, y, z=None):
    if z is not None:
        print(x + y + z)
    else:
        print(x + y)

soma(1, 2)
soma(23, 77)
soma(100, 200)
soma(1, 2, 3)