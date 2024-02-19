# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname

    def __str__(self) -> str:
        return f'{self.name} {self.lastname}'


p1 = Pessoa('Dante', 'Parrudo Kiko III')

print(p1)
