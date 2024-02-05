# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iteráveis) ou {1, 2, 3}

set_1 = set()
set_1 = {'Luiz', 1, 2, 3}
print('set_1 ->', set_1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
set_2 = {1, 2, 3, 3, 4, 5, 1 }
print('set_2 ->', set_2)
print('set_2 ->', type(set_2))

list_1 = ["Ana", "Bruno", "Carla", "David", "Eva", "Bruno", "Fernanda", "Gabriel", "Ana", "Henrique"]
set_3 = set(list_1)
list_2 = list(set_3)
print('list_1 ->', list_1)
print('set_3 ->', set_3) # ele limpa naturalmente # não garante ordem
print('list_2 ->', list_2)



# Métodos úteis:
# add, update, clear, discard
set_3.add('Dante')
# set_3.update('Dona Maia') # dessa forma ele vai inteirar sobre arquivo para espalhar ele
set_3.update(('Dona Maia',)) # forma de usar o update para colocar um valor interável, não esquecer de colocar 
# a virgula no final
print('set_3 ->', set_3)
set_1.clear()
print('set_1 ->', set_1)

set_3.discard('Dona Maia')
set_3.discard('Luiz Otávio') # se ele não encontar não acontece nada
print('set_3 ->', set_3)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
set_operadores_1 = {1, 2, 3}
set_operadores_2 = {2, 3, 4}
set_operadores_3 = set_operadores_1 | set_operadores_2 # vai unir os dois tirando os duplicados
print('set_operadores_3 ->', set_operadores_3)
set_operadores_4 = set_operadores_1 & set_operadores_2 # vai unir apenas os que aparecem am ambos
print('set_operadores_4 ->', set_operadores_4)
set_operadores_5 = set_operadores_1 - set_operadores_2  #v ai retornar apenas os valores unicos dentro do set da 
# esrqueda
print('set_operadores_5 ->', set_operadores_5)
set_operadores_6 = set_operadores_1 ^ set_operadores_2 
print('set_operadores_6 ->', set_operadores_6) # vai retornar os valores unicos dentro de ambos


