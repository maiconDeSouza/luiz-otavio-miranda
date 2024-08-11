from log import LogFileMixin


class Eletronicos(LogFileMixin):
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
        msg = f"{self._nome} Ligado..."
        super().log_sucess(msg)

    def desligado(self):
        if self._ligado:
            self._ligado = False
        msg = f"{self._nome} Desligado..."
        super().log_sucess(msg)


class Celular(Eletronicos):
    pass


i_phone = Celular("iPHONE")
i_phone.ligar()
