# def executa(funcao, *args):
#     return funcao(*args)



funcao = lambda *args: args

executa = lambda fun, *args: fun(*args)

print(executa(funcao, 2, 8, 23, 'Dante'))

# def soma(x, y):
#     return x + y

soma = lambda x, y: x + y
print(soma(2, 3))


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

multiplica = lambda multiplicador: lambda numero: multiplicador * numero

retorno_1 = multiplica(2)

print(retorno_1(3))