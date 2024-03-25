# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

# import teste_aula_97 neste caso ele não funciona por causo do formatador pep8
# Mas eu add uma nova pasta para o arquivo __main__ procurar

try:  # uma forma de forçar ele add novo caminho onde o __main__ tem que procurar. TBM não é uma boa pratica
    import sys
    sys.path.append('/home/mcn/Documentos/meus_testes_em_python')
except Exception as error:
    print(error)


import aula97_m as m
import teste_aula_97


print('Este modulo se chama', __name__)
# os caminhos onde o __main__ vai procurar o modulos
print(*sys.path, sep='\n')

m.bom_dia()
teste_aula_97.teste_97()
