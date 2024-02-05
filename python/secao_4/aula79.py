# exemplo de uso dos sets
palavra_chave = 'cachorro'
tentativas = 0
palavra_secreta = ''
letras_certas = set()

for _ in palavra_chave:
    palavra_secreta += '-'

while True:
    print('Tente des cobrir a palavra chave\n')
    print(palavra_secreta, end='\n')
    print('Diga uma letra')
    palavra_secreta = ''

    letra = input()

    if letra in palavra_chave:
        tentativas += 1
        letras_certas.add(letra)
    else:
        tentativas += 1

    for value in palavra_chave:
        if value in letras_certas:
            palavra_secreta += value
        else:
            palavra_secreta += '-'

    if palavra_chave == palavra_secreta:
        print('Fim do jogo!')
        print('Você acertou a palavra', palavra_chave)
        print(f'Você fez {tentativas} até acertar')
        break