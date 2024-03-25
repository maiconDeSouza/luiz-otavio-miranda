# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self) -> None:
        self._public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado!'

    def mostrar(self):
        return (self.public, self._protected, self.__private)


f = Foo()

f.public = 'casa'
f._protected = 'casa'
f.__private = 'casa'


# print(f_Foo.__private) desconfiguração de nome
print(f.mostrar())
# print(f.__private)
