import importlib
# mesmo chando varias vezes o python vai importar uma única vez
for i in range(3):
    import aula98_m
    print(i)

# Aqui é uma forma de recarregar mais varias vezes quando for necessário para um caso especifico
    # um exemplo é quando um valor do modulo precisa ser atualizado
for i in range(3):
    importlib.reload(aula98_m)
    print(i)