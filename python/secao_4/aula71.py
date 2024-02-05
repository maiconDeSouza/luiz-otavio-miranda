"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

def sum_fn(*args):
    # sum = 0
    # for value in args:
    #     sum += value
    # return sum
    total = sum(args)
    return total


var_1 = sum_fn(2, 5, 6, 18, 23)
print(var_1)