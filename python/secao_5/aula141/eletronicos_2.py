from log import LogFileMixin


class Eletronicos():
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self, log_m):
        if not self._ligado:
            self._ligado = True
        msg = f"{self._nome} Ligado..."
        log_m.log_sucess(msg)

    def desligado(self, log_m):
        if self._ligado:
            self._ligado = False
        msg = f"{self._nome} Desligado..."
        log_m.log_sucess(msg)


class Celular(Eletronicos):
    pass


i_phone = Celular("iPHONE")
logger = LogFileMixin()
i_phone.desligado(logger)
