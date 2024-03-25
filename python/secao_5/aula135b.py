class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []  # Lista de livros na biblioteca

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print(f"Livros na biblioteca {self.nome}:")
        for livro in self.livros:
            print(f"{livro.titulo} - {livro.autor}")


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


# Criando objetos Livro
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
livro2 = Livro("Dom Quixote", "Miguel de Cervantes")
livro3 = Livro("1984", "George Orwell")

# Criando objeto Biblioteca
biblioteca = Biblioteca("Biblioteca Municipal")

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listando os livros na biblioteca
biblioteca.listar_livros()
