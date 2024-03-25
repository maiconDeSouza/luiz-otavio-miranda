class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []  # Lista de cursos associados ao aluno

    def adicionar_curso(self, curso):
        self.cursos.append(curso)


class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []  # Lista de alunos associados ao curso

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)


# Criando alguns alunos
aluno1 = Aluno('João')
aluno2 = Aluno('Maria')
aluno3 = Aluno('Pedro')
aluno4 = Aluno('Dante')

# Criando alguns cursos
curso1 = Curso('Python para Iniciantes')
curso2 = Curso('Algoritmos e Estruturas de Dados')
curso3 = Curso('Machine Learning')

# Associando alunos aos cursos
curso1.adicionar_aluno(aluno1)
curso1.adicionar_aluno(aluno2)
curso1.adicionar_aluno(aluno4)

curso2.adicionar_aluno(aluno2)
curso2.adicionar_aluno(aluno3)

curso3.adicionar_aluno(aluno1)
curso3.adicionar_aluno(aluno3)

# Exibindo os alunos associados a cada curso
for curso in [curso1, curso2, curso3]:
    print(f'Alunos do curso "{curso.nome}":')
    for aluno in curso.alunos:
        print(f'- {aluno.nome}')
    print()
