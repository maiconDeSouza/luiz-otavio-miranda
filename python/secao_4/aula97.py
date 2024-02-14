# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import sys

import aula97_m as m
sys.path.append('/home/mcn/Documentos/meus_testes_em_python')

import teste_aula_97
print('Este modulo se chama', __name__)
print(*sys.path, sep='\n')

m.bom_dia()
teste_aula_97.teste_97()