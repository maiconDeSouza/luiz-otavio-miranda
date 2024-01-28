# Fatiamento de strings
#  0 1 2 3 4 5 6 7 8 9 10 11 12
#  Hello, World!
# -13-12-11-10-9-8-7-6-5-4-3-2-1
# Fatiamento [i:f:p] [::]
# Obs.: a função len retorna a qtd 
# de caracteres da str

variavel = 'Hello, World!'
print(variavel[3:])
print(variavel[3:11])
print(variavel[:3])
print(len(variavel))
print(len(variavel[:3]))
print(variavel[:len(variavel):4])
print(variavel[::-1])
