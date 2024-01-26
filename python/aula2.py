import json
print("Hello, World!")
print(23, 25, sep="/")
print("Olá", "mundo", sep="-", end="!\n")

with open('saida.json', 'w') as f:
    json.dump({"name": "Dante"}, f)  # Escreve no arquivo saida.json
