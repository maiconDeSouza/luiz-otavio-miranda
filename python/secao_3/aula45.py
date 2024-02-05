"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

name = iter('Dante')
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))

print(f'{'Como funciona o for por de baixo dos panoa':-^100}')
name_2 = 'João'
inter = iter(name_2)
while True:
    try:
        print(next(inter))
    except StopIteration:
        break



