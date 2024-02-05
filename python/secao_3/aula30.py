"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 62  # velocidade atual do carro
local_carro = 98  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

test_local = local_carro >= LOCAL_1 - RADAR_RANGE and local_carro <= LOCAL_1 + RADAR_RANGE

if velocidade <= RADAR_1:
    print('Só na Maciota')
elif test_local:
    print('Manda dinheiro para Estado. Multado!')
else:
    print('Escapou!!!! da Multa!')