import random
import string
# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def __str__(self):
        connection_str = self.__dict__
        return f"{connection_str}"

    def set_user(self, new_user):  # método setter
        self.user = new_user

    def set_password(self, new_password):
        self.password = new_password

    @classmethod
    def set_host_user_password(cls, user, password, host='localhost'):
        c = cls(host)
        c.set_user(user)
        c.set_password(password)
        return c

    @staticmethod  # não tem acesso ao cls e nem ao self
    def generate_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password


c1 = Connection()
print(c1)

c1.set_user('Danto')
c1.set_password('Auau123')
print(c1)


new_password = Connection.generate_password(5)
print(new_password)
c2 = Connection.set_host_user_password('John', new_password)
print(c2)
