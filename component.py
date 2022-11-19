from zope.component import adapts
from adaptador import *

class IAnimal(Interface):
    def expresar(self):
        """Método que permite a un animal expresarse"""

@implementer(IPerro)
class Animal(object):

    adapts(Perro, Gato)

    def __init__(self, perro, gato):
        self.perro = perro
        self.gato = gato
    def expresar(self):
        """Método que permite a un animal expresarse"""
        if isinstance(self.animal, Perro):
            self.animal.ladrar()
        elif isinstance(self.animal, Gato):
            self.animal.maullar()
        else:
            raise Exception("Este animal no sabe expresarse")


perro = Perro('Firulais')
gato = Gato('Garfield')
adaptador = Animal(perro, gato)
adaptador.expresar()
