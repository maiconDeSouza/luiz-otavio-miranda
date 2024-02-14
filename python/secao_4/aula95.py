# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def validate_number_types(value):
    value_type = type(value)
    if  isinstance(value, (int, float)):
        return True
    else:
        raise TypeError(f'O {value=} é do tipo {value_type} para que essa função funcione precisa informar um float ou int')

def check_divisor_nonzero(d):
    if d == 0:
        raise ZeroDivisionError(f'O divisor não pode ser 0')
    else:
        return True

def calculate_quotient(n: int | float, d: float | int):
    try:
        validate_number_types(n)
        validate_number_types(d)
        check_divisor_nonzero(d)
    except Exception as error:
        return f'{error.__class__.__name__} -> {error}'
    
    result = n / d
    if result.is_integer():
        return int(result)
    else:
        return result


print(calculate_quotient(82, 0)) # ZeroDivisionError -> O divisor não pode ser 0
print(calculate_quotient(82, '5')) # TypeError -> O value='5' é do tipo <class 'str'> para que essa função funcione precisa informar um float ou int
print(calculate_quotient((), '5')) # TypeError -> O value=() é do tipo <class 'tuple'> para que essa função funcione precisa informar um float ou int
print(calculate_quotient(25, 25)) # 1
print(calculate_quotient(1, 2)) # 0.5
print(calculate_quotient(6, 2)) # 3
print(calculate_quotient(17, 5)) # 3.4





