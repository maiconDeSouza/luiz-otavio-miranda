# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

sistema = True
login = False
db_nome_usuario = "comandante"
db_senha = "auau123"
tentativas = 0

while sistema:
    entrada = input("[E]ntrar - [S]air")

    if entrada == "E":
        sistema = False
        login = True
    elif entrada == "S":
        sistema = False
        print("Bye")
    else:
        print("Mano é só 'E' ou 'S' para digitar")

while login:
   nome_de_usuario = input("Nome de usuário ")
   senha = input("senha ")

   if tentativas > 3:
       print("Conta bloqueada")
       login = False
       continue

   if nome_de_usuario == db_nome_usuario and senha == db_senha:
       login = False
       print("Seja bem vinho")
   else:
       print("Tente Novamente")
       tentativas += 1
       
if True and 1:
    print("oi")
else:
    print("tchau")

curto_circuito_1 = '' or 23
curto_circuito_2 = 'jbl' or 25
curto_circuito_3 = '' and 32
curto_circuito_4 = 'jbl' and 64
print('1 ->', curto_circuito_1)
print('2 ->', curto_circuito_2)
print('3 ->', curto_circuito_3)
print('4 ->', curto_circuito_4)

if 1 and 1:
    print(True and 1 and False)