# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args) -> int:
    result = 1

    for value in args:
        result *= value
    
    return result




def even_or_odd(number: int) -> str:
    message = f'o número {number} é par' if number % 2 == 0 else f'o número {number} é impar'
    return message

var_mult_1 = mult(1, 2, 3, 4, 5)
print(var_mult_1)

print(even_or_odd(23))
print(even_or_odd(2))
print(even_or_odd(122))
print(even_or_odd(1023))

