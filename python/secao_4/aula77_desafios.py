# Exercício - sistema de perguntas e respostas
import os
import time
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

respostas_certas = 0
while True:
    for item in perguntas:
        print(item['Pergunta'])
        for i, res in enumerate(item['Opções']):
            print(f'{i}) -> {res}')
        response = input()
        if response == item['Resposta']:
            print('Acertou')
            respostas_certas += 1
        else:
            print('Errou')
        
        time.sleep(5)
        os.system('clear')
    
    break

print('Acertos ->', respostas_certas )