"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia', 'Maicon')
s2 = criar_saudacao('Boa Noite', 'Maicon')
print(s1)
print(s2)

print(5* '--')
print(s1())
print(s2())
