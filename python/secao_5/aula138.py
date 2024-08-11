class Pessoa:
    def __init__(self, nome, sobrenome):
        self.__nome_completo = f"{nome} {sobrenome}"

    def nome_completo(self):
        return self.__nome_completo

    def falar_nome_classe(self):
        return f"{self.nome_completo} {self.__class__.__name__}"


class Endereco:
    def __init__(self, rua, numero):
        self.__endereco_completo = f"{rua}, {numero}"

    def endereco_completo(self):
        return self.__endereco_completo


class Cliente(Pessoa, Endereco):
    def __init__(self, nome, sobrenome, rua, numero):
        Pessoa.__init__(self, nome, sobrenome)
        Endereco.__init__(self, rua, numero)

    def cliente(self):
        return f"{self.nome_completo()} - {self.endereco_completo()}"


dante = Cliente("Dante", "Parrudo Kiko III", "Logo Ali", 23)
print(dante.cliente())
print(dante.falar_nome_classe())

print(20 * "-")


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self, som="fazendo um som."):
        return f"{self.nome} está {som}"


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca


pug = Cachorro("Pugzinho", "Pug")
print(vars(pug))
print(pug.emitir_som("latindo..."))
