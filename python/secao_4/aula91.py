# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(count=0, max=10):
    while True:
        yield count
        if count >= max:
            return 'fim'
        count += 1

gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)

print()

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usando o generator
lista = []
for num in fibonacci(3):
    lista.append(num)

print(lista)