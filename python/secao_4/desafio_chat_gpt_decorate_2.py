NIVEL_ACESSO_ATUAL = "user"

def restricao_acesso(nivel_necessario):
    def decorador(func):
        def wrapper(*args, **kwargs):
            if nivel_necessario == "admin" and NIVEL_ACESSO_ATUAL != "admin":
                print("Acesso negado. Requer nível de acesso: admin.")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorador

@restricao_acesso("admin")
def funcao_restrita():
    print("Acesso concedido à função restrita.")

@restricao_acesso("user")
def outra_funcao():
    print("Acesso concedido à outra função.")

print(funcao_restrita())