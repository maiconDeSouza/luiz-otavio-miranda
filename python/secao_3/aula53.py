# Tipo tupla - Uma lista imutável
# A Tupla é mais rapida 
# da para criar tbm usando ()
nomes = 'Maria', 'Helena', 'Luiz'
print(nomes)
print(type(nomes))

#conversão
nomes_2 = list(nomes)
print(type(nomes_2))
nomes_3 = tuple(nomes_2)
print(type(nomes_3))
