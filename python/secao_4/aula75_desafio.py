# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def mult(mult_int: int):
    def result(value_int: int):
        result_int = mult_int * value_int 
        return f'O {value_int} multiplicado por {mult_int} vezes é -> {result_int}'
    return result

dobro = mult(2)
triplo = mult(3)
quadroplo = mult(4)

tuple_fn = (dobro, triplo, quadroplo)

for value in tuple_fn:
    print(value(5))