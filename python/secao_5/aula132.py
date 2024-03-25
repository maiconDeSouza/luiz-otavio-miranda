# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, new_cor):
        self.__cor = new_cor


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
caneta.cor = 'Rosa'
print(caneta.cor)
# print(caneta.__cor)
