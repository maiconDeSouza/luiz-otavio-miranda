# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

def recursiva(init=0, end=10):
    if init == end:
        return init
    else:
        print(init)
        init += 1
        return recursiva(init, end)
print('recursiva 1')
r = recursiva(0, 10)
print(r)

print()
# Limite de chamadas recursivas [Previous line repeated 996 more times] RecursionError: maximum recursion depth exceeded
# Porém é possível setar um valor maior
# import sys
# sys.setrecursionlimit(1020)
# def recursiva_2(init=0, end=10):
#     print(init, end)

#     if init == end:
#         print(init, end)
#         return
#     else:
#         print(init, end)
#         init += 1
#         return recursiva_2(init, end)


# recursiva_2(0, 1000) 

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print('factorial')
print('5! = ', factorial(5))
print('5! = ', factorial(10))
