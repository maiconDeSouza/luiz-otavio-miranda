# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class MinhaString(str):  # estou herdando de string
    def upper(self):  # estou sobrescrevendo o méto upper() de str
        print("ABC")  # aqui coloquei algo a mais
        return super().upper()  # aqui usei o método nativo da super classe str


minha_string = MinhaString("Dante")

print(minha_string.upper())

print(20 * "-")

# Definição da classe A, que será a classe base.


class A:
    # Um atributo de classe, compartilhado por todas as instâncias de A (e suas subclasses).
    atributo_a = "Atribudo A"

    # Um método que retorna a string "A".
    def metodo(self):
        return "A"


# Definição da classe B, que herda da classe A.
class B(A):
    # Um novo atributo de classe específico de B.
    atributo_b = "Atribudo B"

    # Sobrescrita do método 'metodo' da classe A. Agora ele retorna "B" em vez de "A".
    def metodo(self):
        return "B"


# Definição da classe C, que herda da classe B.
class C(B):
    # Um novo atributo de classe específico de C.
    atributo_c = "Atribudo C"

    # Sobrescrita do método 'metodo' da classe B.
    def metodo(self):
        # Usando `super()` para chamar o método `metodo` da classe que é ancestral de B, que é a classe A.
        # Isso imprime o retorno do método `metodo` da classe A, que é "A".
        print(super(B, self).metodo())

        # Usando `super()` para chamar o método `metodo` da classe imediatamente superior, que é a classe B.
        # Isso imprime o retorno do método `metodo` da classe B, que é "B".
        print(super().metodo())

        # Retorna a string "C", indicando que o método `metodo` da classe C foi chamado.
        return "C"


# Criação de uma instância da classe C.
c = C()

# Atributo 'atributo_a' vem da classe A.
print(c.atributo_a)  # Saída: "Atribudo A"

# Atributo 'atributo_b' vem da classe B.
print(c.atributo_b)  # Saída: "Atribudo B"

# Atributo 'atributo_c' vem da classe C.
print(c.atributo_c)  # Saída: "Atribudo C"

# Chama o método `metodo` da instância `c`, que pertence à classe C.
# Isso primeiro imprime "A" (do método `metodo` da classe A) e "B" (do método `metodo` da classe B),
# e depois retorna "C", que é o valor retornado pelo método `metodo` da classe C.
print(c.metodo())  # Saída: "A", "B", "C"
