lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))

print('lista ->', lista)

lista_2 = [(x, y) for x in range(3) for y in range(3)]

print('lista_2 ->', lista_2)
