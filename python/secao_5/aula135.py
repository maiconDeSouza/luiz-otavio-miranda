# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        valor = sum([p.preco for p in self._produtos])
        return f'Valor total é R${valor}'

    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
# Caneta 1.2
# Camiseta 20
# Valor total é R$21.2
print(carrinho.total())

print(10 * "-")


class Departamento:
    def __init__(self, nome_departamento):
        self.nome_departamento = nome_departamento
        self.__funcionarios_do_departamento = []

    def inserir_funcionario(self, *funcionario):
        for f in funcionario:
            self.__funcionarios_do_departamento.append(f.nome)

    def listar_funcionario(self):
        for f in self.__funcionarios_do_departamento:
            print(f)


class Funcionario:
    def __init__(self, nome):
        self.nome = nome


vendas = Departamento("Vendas")
f_1 = Funcionario("Joarez")
f_2 = Funcionario("Alexandre")

vendas.inserir_funcionario(f_1, f_2)
vendas.listar_funcionario()
