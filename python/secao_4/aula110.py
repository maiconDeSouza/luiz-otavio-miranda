# groupby - agrupando valores (itertools)
import mcn_module as mcn
from itertools import groupby
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

lambada_nota = lambda a: a['nota']
# para trabalhar com o groupby é necessário ordernar primeiro o grupo que você quer trabalhar
alunos_ordenados = [aluno for aluno in sorted(alunos, key=lambada_nota)]

# grupos = groupby(alunos_ordenados, key=lambada_nota)

# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))

grupos = [{'chave': chave, 'grupo': list(grupo)} for chave, grupo in groupby(alunos_ordenados, key=lambada_nota)]
mcn.console_log(grupos, 'Lista de grupos')