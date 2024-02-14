a = 18
b = 0
# neste exemplo eu garanto que vou chegar no print()
try:
    print(a / b)
except Exception as error:
    print(error)
    print(error.__class__.__name__)

print('Aqui estou eu!')