# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2024  # atributo de classe

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @classmethod  # Você passa o decorate
    # você tem que passar a instancia da classe que costumamos chmar de cls
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, age):
        return cls('Anônima', age)


p1 = Pessoa('Ariteus', 48)
p2 = Pessoa.criar_com_50_anos('Helena')
print(p2.name, p2.age)
p3 = Pessoa.criar_sem_nome(23)
print(p3.name, p3.age)


Pessoa.metodo_de_classe()
