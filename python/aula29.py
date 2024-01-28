number = input('Digite um numero para saber qual é seu dobro: ')

# number_float = float(number)
# print(f'O dobro de {number_float} é: {number_float * 2}')

try:
    number_float = float(number)
    print(f'O dobro de {number_float} é: {number_float * 2}')
except Exception as error:
    print('Muleque, faz um favor! Digite apenas números')
    print(error)

print('bye')