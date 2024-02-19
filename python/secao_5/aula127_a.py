import json


class Dog():
    def __init__(self, name, age, breed) -> None:
        self.name = name
        self.age = age
        self.breed = breed


new_dog = Dog('Dante', 3, 'Pug')

with open('aula127.json', 'w+', encoding='utf-8') as file:
    data = new_dog.__dict__
    json.dump(data, file, ensure_ascii=False, indent=2)
