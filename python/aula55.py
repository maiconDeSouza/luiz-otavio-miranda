from decimal import Decimal
"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

numero_1 = Decimal('0.1') 
numero_2 = Decimal('0.7')
resultado = numero_1 + numero_2 # se você não tranformar os números em string o decima
# vai retornar 0.7999999999999999611421941381 ainda com mais casas decimais
print(resultado)
print(f'{resultado:.2f}')
print(round(resultado, 2))