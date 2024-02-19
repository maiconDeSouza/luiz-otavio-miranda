# Criando arquivos com Python
# Usamos a função open para abrir
# um arquivo em Python (Ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve no final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o múdulo json, mas:
# json.dump = gera um arquivo json
# json.load = leitura

caminho_arquivo = 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.write('Oi')

# arquivo.close()

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('oi\n')  # escrevendo uma linha
    arquivo.write('jbl\n')  # escrevendo uma linha
    arquivo.writelines(('hp\n', 'nintendo\n'))  # escrevendo varias linhas
    # é necessário o \n para pular a linha

    print(f'{5 * '*'}Lietura 1{5 * '*'}')
    arquivo.seek(0, 0)  # volta o curso para a primeira linha
    leitura = arquivo.read()

    print(leitura)
    arquivo.seek(0, 0)  # volta o curso para a primeira linha
    print(f'{5 * '*'}Lietura 2{5 * '*'}')
    # Para ler varias linhas ele vai soltando uma de cada vez
    # o end é usado para não haver a quebra de linha ao fina, pois já vem na escrita
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())  # strip tira o espaço
    print(arquivo.readline(), end='')
    print(arquivo.readline(), end='')

    print(f'{5 * '*'}Lietura 3{5 * '*'}')
    arquivo.seek(0, 0)
    # para ler varias linha e jogar em uma lista
    for linha in arquivo.readlines():
        print(linha.strip())

# o w sempre vai escrever um novo arquivo e o a vai continuar escrevendo naquele arquivo
with open(caminho_arquivo, 'a', encoding='utf-8') as arquivo:
    arquivo.write('pip\n')
    arquivo.write('Atenção')

# import os
# os.remove(caminho_arquivo)
