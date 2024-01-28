import time
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
ex1_on = True

while ex1_on:
    print('Digite um Número inteiro')
    number_str = input()
    try:
        number_int = int(number_str)
        even_odd = f'{number_int} é par' if number_int % 2 == 0 else f'{number_int} é impar'
        print(even_odd)
        ex1_on = False
    except Exception as error:
        print('Você não digitou um número inteiro')
        print(error)
        time.sleep(5)
        continue
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
ex2_on = True
while ex2_on:
    print('Digite as horas atual. ex:. 19 ou 01 ou 10')
    hour_str = input()
    try:
        hour_int = int(hour_str)
        valid = hour_int >= 0 and hour_int <= 23
        if not valid:
            print('Digite o horario entre 0 horas até 23 horas')
            time.sleep(5)
            continue

        if hour_int >= 18:
            print('Boa Noite!')
        elif hour_int >= 12:
            print('Boa Tarde!')
        else:
            print('Bom dia!')
        ex2_on = False
    except Exception as error:
        print('Digite apenas números')
        print(error)
        time.sleep(5)
        continue
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
ex3_on = True

while ex3_on:
    print('Digite seu nome')
    name = input()

    length_name = len(name)

    if length_name == 0:
        print('Digite seu nome, não deixe o campo em branco.')
        time.sleep(5)
        continue

    if length_name > 6:
        print('Seu nome é muito grande')
    elif length_name > 4:
        print('Seu nome é normal')
    else:
        print('Seu nome é curto')
    
    ex3_on = False