"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

import re
import random

def generate_digit(number_str: str):
    mult = 0
    if len(number_str) == 9:
        mult = 10
    else:
        mult = 11
    soma = 0

    for value in number_str:
        try:
            value_int = int(value)
    
            soma += value_int * mult
            mult -= 1
        except Exception as error:
            print(error)
            return
    soma_ten = soma * 10
    rest = soma_ten % 11
    
    digit = 0 if rest > 9 else rest
    return digit


def create_cpf_completed(nine_first: str):
    treated_string = nine_first.replace('.', '')

    if len(treated_string) != 9:
        return f'O número de caracteres permetido é 9, nem mais nem menos!' 
    
    digit_1 = generate_digit(treated_string)
    ten_first = treated_string + str(digit_1)
    digit_2 = generate_digit(ten_first)
    cpf = ten_first + str(digit_2)
    formatted_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return formatted_cpf

# 732.759.560-00
# 746.824.890-70
# 462.041.420-46
# 262.281.030-08
# 709.975.720-27
# print(create_cpf_completed('732.759.560'))
# print(create_cpf_completed('746.824.890'))
# print(create_cpf_completed('462.041.420'))
# print(create_cpf_completed('262.281.030'))
# print(create_cpf_completed('709.975.720'))

def valid_cpf(cpf):
    treated_cpf= re.sub(r'[^0-9]', '', cpf)
    if len(treated_cpf) != 11:
        print('CPF em fomato errado, favor digitar 000.000.000-00')
        return
    
    nine_first = treated_cpf[0:9]
    test_cpf = create_cpf_completed(nine_first)

    if test_cpf == cpf:
        print(f'O cpf {cpf} é valido!')
    else:
        print(f'O cpf {cpf} é invalido!')

def generate_cpf():
    new_nine_first = ''

    for _ in range(0, 9):
        new_number  = random.randint(0, 9)
        new_nine_first += str(new_number)
    
    new_cpf = create_cpf_completed(new_nine_first)
    return new_cpf
    
valid_cpf('732.759.560-00')
valid_cpf('746.824.890-70')
valid_cpf('462.041.420-46')
valid_cpf('262.281.030-08')
valid_cpf('709.975.720-27')
valid_cpf('233.568.987-23')
valid_cpf(generate_cpf())