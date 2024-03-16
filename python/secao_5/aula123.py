# Escopo da Classe e de Métodos da classe
class Animal:
    varivavel2 = 'Alguma coisa'

    def __init__(self, name) -> None:
        self.name = name
        varivavel = 'Alguma coisa'

    # def alguma_coisa(self):
    #     return f'O {self.name} está comento o {variavel}' -> não tem acesso
    def se_alimentar(self, alimento):
        return f'O {self.name} está se alimentando com {alimento}'


leao = Animal('Leão')
# print(leao.alguma_coisa()) -> vai gerar um erro, pois tem um valor que não está
# no escopo desse método
print(leao.se_alimentar('Macarrão instantâneo'))

print(Animal.varivavel2)
