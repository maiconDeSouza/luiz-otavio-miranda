qtd_linhas = 3
qtd_colunas = 3

linha = 1
coluna = 1

while linha <= qtd_linhas:
    print('Batatinha')
    linha += 1
    while coluna <= qtd_colunas:
        print(f'{coluna}')
        coluna += 1
    coluna = 1

print(f'\n{10 * '-'}')

linha = 1
coluna = 1
while linha <= qtd_colunas:
    row = ''
    while coluna <= qtd_colunas:
        row += '-'
        coluna += 1

    print(f'{linha} {row}')
    row = ''
    coluna = 1
    linha += 1