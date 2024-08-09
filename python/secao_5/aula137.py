# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome_carro = nome

    def qual_o_motor_e_fabricante(self, fabricante, motor):
        print(f"O {self.nome_carro} é fabricado pela montadora {
              fabricante.nome_fabricante} e tem motor {motor.nome_motor}")
        print(50 * "-")


class Motor:
    def __init__(self, nome):
        self.nome_motor = nome
        self.carros = []

    def add_carros(self, *carros):
        for carro in carros:
            self.carros.append(carro)

    def mostra_os_carros_com_este_motor(self):
        print(f"Motor: {self.nome_motor}")
        for carro in self.carros:
            print(f" - {carro.nome_carro}")
        print(50 * "-")


class Fabricante:
    def __init__(self, nome):
        self.nome_fabricante = nome
        self.carros = []
        self.motores = []

    def add_motores(self, *motores):
        for motor in motores:
            self.motores.append(motor)

    def motores_do_fabricante(self):
        print(f"Fabricante: {self.nome_fabricante}")
        for motor in self.motores:
            print(f" - {motor.nome_motor}")
        print(50 * "-")

    def add_carros(self, *carros):
        for carro in carros:
            self.carros.append(carro)

    def carros_do_fabricante(self):
        print(f"Fabricante: {self.nome_fabricante}")
        for carro in self.carros:
            print(f" - {carro.nome_carro}")


celta = Carro("Celta")
ka = Carro("Ka")
gol = Carro("Gol")
opala = Carro("Opala")

vhc = Motor("vhc")
iron_duke = Motor("Iron Duke")
cht = Motor("cht")

gm = Fabricante("GM")
ford = Fabricante("Ford")
vw = Fabricante("VW")


vhc.add_carros(celta)
iron_duke.add_carros(opala)
cht.add_carros(ka, gol)
celta.qual_o_motor_e_fabricante(gm, vhc)

gm.add_carros(celta, opala)
ford.add_carros(ka)
vw.add_carros(gol)

gm.add_motores(vhc, iron_duke)
ford.add_motores(cht)
vw.add_motores(cht)

cht.mostra_os_carros_com_este_motor()
vhc.mostra_os_carros_com_este_motor()
iron_duke.mostra_os_carros_com_este_motor()

gm.carros_do_fabricante()
gm.motores_do_fabricante()

ford.carros_do_fabricante()
ford.motores_do_fabricante()

vw.carros_do_fabricante()
vw.motores_do_fabricante()
