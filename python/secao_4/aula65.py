"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

def saudacao(name: str):
    if len(name) < 3:
        print('Preencha um nome com mais de três caracteres.')
        return
    print(f'Ola {name}, bom dia!')
    
saudacao('Dante')
saudacao('ka')