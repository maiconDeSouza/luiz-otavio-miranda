"""
Higher Order Functions
Funções de primeira classe
"""

def sum_tupla(*args):
    total = sum(args)
    return total

def view_sum_styles(funcao, *args):
    total = funcao(*args)  
    return f'A soma da tupla {args} é -> {total}' 

result = view_sum_styles(sum_tupla, 1, 2, 3, 4, 5)
print(result)