"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def mostrar(x, y):
    print(f'{x=} e {y=}')

mostrar(9, 23)
mostrar(y='jbl', x='hp')