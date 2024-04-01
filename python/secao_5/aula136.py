# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.endereco = []

    def inserir_endereco(self, rua, numero):
        # Quando Cliente deixar de existir o Endereco deixa de existir
        self.endereco.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for end in self.endereco:
            print(end.numero, end.rua)


class Endereco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero = numero


cliente_1 = Cliente('Maria')
cliente_1.inserir_endereco('Avenida Brasil', 1500)
cliente_1.inserir_endereco('Avenida São Tomaz', 1)

print(cliente_1.endereco)
# [<__main__.Endereco object at 0x7f34f05025d0>, <__main__.Endereco object at 0x7f34f0502630>]

print(cliente_1.listar_enderecos)
