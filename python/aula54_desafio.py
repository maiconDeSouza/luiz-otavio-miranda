import os
# Lista de compras

shopping_list = []

on = True

while on:
    print('Selecione uma opção')
    print('[i]nserir [a]pagar [l]istar [s]air')
    action = input().lower()

    try:
        if action == 'i':
            os.system('clear')
            print('Digite o novo item')
            new_item = input()
            shopping_list.append(new_item)
        elif action == 'a':
            os.system('clear')
            for item in enumerate(shopping_list):
                print(item)
            print('Digite o indice do item que deve ser excluido')
            indice_item = int(input())
            if indice_item >= 0 and indice_item < len(shopping_list):
                remove_item = shopping_list.pop(indice_item)
                print(f'O item {remove_item} excluido com sucesso!')
            else:
                os.system('clear')
                print('indice invalido!')
        elif action == 'l':
            os.system('clear')
            for item in enumerate(shopping_list):
                print(item)
        elif action == 's':
            os.system('clear')
            print('Bye')
            on = False
        else:
            os.system('clear')
            print('Comando não encontrado')
    except Exception as error:
        os.system('clear')
        print(error)
        print('indice invalido!')
        
       
    
       
       