import math
import time
# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.


class Classe:
    @staticmethod
    def funcao_que_esta_na_classe():
        print('Oi')

    @staticmethod
    def get_current_time_and_pi():
        pi = math.pi
        current_time = time.strftime("%H:%M:%S")
        return f"nesta exata hora {current_time} o valor de PI continua sendo {pi}"


c1 = Classe()
c1.funcao_que_esta_na_classe()
Classe.funcao_que_esta_na_classe()
print(Classe.get_current_time_and_pi())
