import random
def lotofacil():
    numeros_sorteados = set()

    while len(numeros_sorteados) < 15:
        sorteado = random.randint(1, 25)
        numeros_sorteados.add(sorteado)

    return numeros_sorteados