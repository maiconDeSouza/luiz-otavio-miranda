# Exercício: Decorador de Log de Execução
# Objetivo: Criar um decorador chamado log_execucao que registra o momento em que uma função é 
# chamada e o momento em que ela termina de executar, mostrando também quanto tempo levou para a execução.

# Requisitos:

# O decorador deve imprimir uma mensagem antes de chamar a função original, indicando que a execução começou.
# Após a função ser executada, o decorador deve imprimir uma mensagem indicando que a execução terminou.
# Ambas as mensagens devem incluir o nome da função que está sendo executada.
# O decorador deve mostrar o tempo total de execução da função, em segundos.
# A função decorada deve funcionar normalmente, com seu retorno e argumentos preservados.
# Dicas:

# Use a função time() do módulo time para capturar os momentos antes e depois da execução da função decorada.
# Lembre-se de que um decorador é uma função que recebe uma função como argumento e retorna uma nova função.

import time

def log_execucao(fun):
    def wrapper():
        print(f'Executando a função: {fun.__name__}')
        init = time.time()
        time.sleep(2)
        result = fun()
        end = time.time()
        return f'O resultado da função foi {result} em {end - init:.3f} segundos'
    return wrapper

@log_execucao
def jbl():
    # return [i for i in range(10000001)]
    return [i for i in range(11)]


print(jbl())