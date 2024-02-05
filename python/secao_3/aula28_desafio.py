# Exercício
# Peça ao usuário para digitar seu nome
# Peça ao usuário para digitar sua idade
# Se nome e idade forem digitados:
#     Exiba:
#         Seu nome é {nome}
#         Seu nome invertido é {nome invertido}
#         Seu nome contém (ou não) espaços
#         Seu nome tem {n} letras
#         A primeira letra do seu nome é {letra}
#         A última letra do seu nome é {letra}
# Se nada for digitado em nome ou idade: 
#     exiba "Desculpe, você deixou campos vazios."
import time
end = False

while not end:
    print('Por favor, digite seu nome e Sua idade!')
    time.sleep(2)
    name = input('Nome: ')
    time.sleep(2)
    age = input('Idade: ')
    try:
        age_int = int(age)
    except Exception as error:
        print(error)
        continue
    if not name or not age:
        print('Preencha todos os campos')
        continue
    else:
        print(f'Seu nome é {name}')
        print(f'Seu nome invertido é {name[::-1]}')
        espaço = 'sim' if ' ' in name else 'não' 
        print(f'Seu nome contém espaços (sim ou não): {espaço}')
        print(f'Seu nome tem {len(name)} letras')
        print(f'A Primeira letra do seu nome é: {name[0]}')
        print(f'A última letra do meu nome é: {name[len(name) - 1]}')
        end = True
