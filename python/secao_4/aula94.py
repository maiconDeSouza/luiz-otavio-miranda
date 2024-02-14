try:
    print(x)
except NameError:
    print("A variável x não está definida.")
except:
    print("Algo deu errado.")
else:
    print("Nada deu errado.")
finally:
    print("O bloco 'try except' está concluído.")