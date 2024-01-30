# Calculadora

calc = True

while calc:
    print('Serão pedidos um numero, depois o sinal da operação e depois outro número e depois será devolvido o resultado')
    print('digite apenas números e os sinais validos são:')
    print('+ -> soma')
    print('- -> subtração')
    print('/ -> divisão')
    print('* -> multiplicação')
    print('\nPara sair digite [s] ou [enter] para continuar')
    sair = input().lower().endswith('s')

    if sair:
        print('bye')
        calc = False
        continue

    number_1 = input(f'\n Digite o primeiro número: ')
    sign = input(f'\n Digite a operação desejada: ')
    number_2 = input(f'\n Digite o primeiro número: ')

    try:
        n_1 = int(number_1)
        n_2 = int(number_2)

        if sign == '+':
            print(n_1 + n_2)
        elif sign == '-':
            print(n_1 - n_2)
        elif sign == '/':
            print(n_1 / n_2)
        elif sign == '*':
            print(n_1 * n_2)
        else:
            print('Digite um sinal valído!')
            continue

    except Exception as error:
        print('Digite apenas números')
        continue
else:
    print('End')