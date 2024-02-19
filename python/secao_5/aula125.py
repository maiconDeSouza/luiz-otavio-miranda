# Atributos de classe vs. Atributos de instância

class Dog:
    # Atributo de classe
    # Este valor é compartilhado por todas as instâncias da classe.
    current_year = 2024

    def __init__(self, name, age):
        """
        Método inicializador que configura os atributos de instância.
        :param name: nome do cachorro.
        :param age: idade do cachorro.
        """
        # Atributos de instância
        # Esses valores são específicos para cada instância.
        self.name = name
        self.age = age

    def get_year_of_birth(self):
        """
        Calcula o ano de nascimento do cachorro com base na idade e no ano atual (atributo de classe).
        :return: Ano de nascimento do cachorro.
        """
        return Dog.current_year - self.age


# Criando instâncias da classe Dog
dog_1 = Dog('Dante', 3)
dog_2 = Dog('Dona Maia', 14)

# Usando o método get_year_of_birth() para calcular o ano de nascimento de cada cachorro
print(f"{dog_1.name} nasceu em {dog_1.get_year_of_birth()}.")
print(f"{dog_2.name} nasceu em {dog_2.get_year_of_birth()}.")

# Demonstração do compartilhamento de atributos de classe
print(f"Ano atual (antes da alteração): {Dog.current_year}")
Dog.current_year = 2025  # Alterando o atributo de classe
print(f"Ano atual (após a alteração): {Dog.current_year}")
print(f"{dog_1.name} nasceu em {
      dog_1.get_year_of_birth()} após a alteração do ano atual.")
print(f"{dog_2.name} nasceu em {
      dog_2.get_year_of_birth()} após a alteração do ano atual.")
