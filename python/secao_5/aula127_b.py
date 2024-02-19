import aula127_a
import json

data = None

try:
    with open('aula127.json', 'r+', encoding='utf-8') as file:
        data = json.load(file)
        new_dog = aula127_a.Dog(**data)
        print(vars(new_dog))
except Exception as error:
    print('Não tem JSON')
    print(error)
    print(error.__class__)
