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

    if entrada == "E" or entrada == 'e':
        sistema = False
        login = True
    elif entrada == "S" or entrada == "s":
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