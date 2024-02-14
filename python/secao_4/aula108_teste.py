from itertools import count
keep_counting = True
number_list = []
c = count()

while keep_counting:
    keep = input('digite [s] para continuar ou [n] para sair')
    if keep == 's':
        var = next(c)
        number_list.append(var)
        print(number_list)
    else:
        keep_counting = False

print('Lista final ->', number_list)