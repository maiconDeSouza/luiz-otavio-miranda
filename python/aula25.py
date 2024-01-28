# Interpolação básica de strings
# s -> string
# d e i -> int
# f -> float
# x e X -> Hexadecimal (ABCDEF0123456789)

nome = 'Dante'
preco = 100.95897643
variavel = '%s, o preço é R$%.2f' %(nome, preco)
print(variavel)

print('O hexa decima de 223 é %x' %223)