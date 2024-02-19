# __dict__ e vars para atributos de instância
class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


dados = {'name': 'Dante', 'age': 3}
dog_1 = Dog(**dados)  # desempacotando na instanciação da classe
print(dog_1.__dict__)  # vai entregar os atributos de instância como um dicionário
print(vars(dog_1))  # Vars tbm
