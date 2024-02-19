# Problema dos parâmetros mutáveis em funções Python

def add_customer(name, customer_list=[]):
    customer_list.append(name)
    return customer_list


cliente_1 = add_customer('Dante')
add_customer('Dona Maia', cliente_1)


cliente_2 = add_customer('Talu')
add_customer('Delinha', cliente_2)
# acontece isso porque o python reaproveita a lista que foi criado como padrão
print('cliente_1 ->', cliente_1)
print('cliente_2 ->', cliente_2)  # ['Dante', 'Dona Maia', 'Talu', 'Delinha']
# O ideal é criar fora da função que recebe uma lista como padrão, pois ela sempre usará a mesma
# lista independente de quantas vezes você crie, nunca use valores mutaveis como padrão de uma função

# ou fazer assim
print()
print(5 * '#', 'Exemplo 2', 5 * '#')


def add_customer_2(name, customer_list=None):
    if customer_list is None:
        customer_list_new = []
        customer_list_new.append(name)
        return customer_list_new
    if type(customer_list) is list:
        customer_list.append(name)
    else:
        print('deu ruim')

# dessa forma ele sempre gera uma nova lista, pois é criada uma nova lista para toda chamada da função


cliente_3 = add_customer_2('jbl')
add_customer_2('hp', cliente_3)

cliente_4 = add_customer_2('nintendo')
add_customer_2('claro', cliente_4)

print('cliente_3 ->', cliente_3)
print('cliente_4 ->', cliente_4)
