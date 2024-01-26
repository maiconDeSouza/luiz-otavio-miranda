on = True

while on:
    comando = input('Você quer "entrar" ou "sair" ')
    if comando == 'entrar':
        print('Você entrou no sistema')
        on = False
    elif comando == 'sair':
        print('Você não entrou no sistema')
        on = False
    else:
        print('digite apenas "entrar" ou "sair"')