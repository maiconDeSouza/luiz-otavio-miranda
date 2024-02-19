# Mantendo o estado dentro da classe
class Camera:
    def __init__(self, name, recording=False) -> None:
        self.name = name
        self.recording = recording

    def record(self):
        if self.recording:
            return f'A camera {self.name} já está filmando..!'

        self.recording = True
        return f'A camera {self.name} começou a filmar!'

    def stop_record(self):
        if self.recording:
            self.recording = False
            return f'A camera {self.name} parou de filmar!'

        return f'A camera {self.name} não estava filmando..!'

    def photograph(self):
        if self.recording:
            return f'A Camera {self.name} não consegue fotografar durante uma filmagem..!'

        return f'A Camera {self.name} fotografou com sucesso!'


c1 = Camera('Canon')
c2 = Camera('Sony')

print(c1.record())
print(c1.record())
print(c1.photograph())
print(c2.stop_record())
print(c2.photograph())
