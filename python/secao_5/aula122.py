class Carro:
    def __init__(self, name, cor):
        self.name = name
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, incremento=10):
        self.velocidade += incremento
        return f'O {self.name} está acelerando a {self.velocidade} km/h!...'

    def parar(self):
        self.velocidade = 0
        return f'O {self.name} parou.'

    def descrever(self):
        return f'O carro {self.name} é da cor {self.cor}.'


fusca = Carro('Fusca', 'azul')
celta = Carro('Celta', 'vermelho')

print(fusca.acelerar())
print(fusca.acelerar(20))
print(celta.descrever())
print(Carro.acelerar(celta, 50))  # Aqui trecho importante
print(fusca.parar())
