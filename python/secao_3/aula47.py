"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import time
palavra_secreta = 'cachorro'
letras_acertadas = ''
tentativas = 0

while True:
    letras_exibir = ''
    total_letras = len(palavra_secreta)
    print('A dica é um Lanche\n')
    letra = input('Digite uma letra ')

    if letra in palavra_secreta:
        letras_acertadas += letra
    
    for letra_in in palavra_secreta:
        if letra_in in letras_acertadas:
            letras_exibir += letra_in
        else:
            letras_exibir += '-'

    tentativas += 1

    if letras_exibir == palavra_secreta:
        print('Fim do jogo')
        print(f'Você acertou a palavra [{letras_exibir}] em {tentativas}')     
    else:
        print(letras_exibir)
