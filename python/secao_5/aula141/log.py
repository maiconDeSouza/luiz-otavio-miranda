from pathlib import Path
from datetime import datetime


LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError("Este método deve ser sobrescrito")

    def log_error(self, msg):
        self._log(f"{self.__gerar_data_horario()} -> Error: {msg}")

    def log_sucess(self, msg):
        self._log(f"{self.__gerar_data_horario()} -> Sucess: {msg}")

    def __gerar_data_horario(self):
        data_hora_atual = datetime.now()
        data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
        return data_hora_formatada


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f"{msg} ({self.__class__.__name__})"
        with open(LOG_FILE, 'a') as f:
            f.write(msg_formatada)
            f.write("\n")


if __name__ == "__main__":
    l = Log()
    l.log("Erro qualquer!")
