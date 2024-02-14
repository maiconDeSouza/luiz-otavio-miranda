# Variáveis livres + nonlocal

# def concatenar(primeiro_valor):
#     valor_final = primeiro_valor
#     def interna(segundo_valor):
#         nonlocal valor_final
#         valor_final += segundo_valor
#         return valor_final
#     return interna

# con = concatenar('a')
# print(con('b')) # ab
# print(con('z')) # abz


# UnboundLocalError: cannot access local variable 'valor_final' where it is not associated with a value

# outro teste
# nesta forma eu não usei o nonlocal, mas criei outra variavel, porém se eu precisar do estado anterior ele não gera
def concatenar(primeiro_valor):
    valor_final = primeiro_valor
    def interna(segundo_valor):
        res = valor_final + segundo_valor
        return res
    return interna

con = concatenar('a')
print(con('b')) # ab
print(con('z')) # az