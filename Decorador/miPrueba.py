# Clase base
from abc import ABC, abstractmethod


class CafeAbs(ABC):
    @abstractmethod
    def costo(self):
        pass
    @abstractmethod
    def descripcion(self):
        pass

class Cafe(CafeAbs):
    def costo(self):
        return 10
    
    def descripcion(self):
        return 'El mejor cafe del mundo'

# Clase Decoradora
class CafeDecorator(Cafe):
    def __init__(self, cafe: Cafe):
        self._cafe = cafe

    def costo(self):
        return self._cafe.costo()

    def descripcion(self):
        return self._cafe.descripcion()

# Decoradores concretos
class ConLeche(CafeDecorator):
    def costo(self):
        return self._cafe.costo() + 10

    def descripcion(self):
        return self._cafe.descripcion() + ", con leche"

class ConAzucar(CafeDecorator):
    def costo(self):
        return self._cafe.costo() + 5

    def descripcion(self):
        return self._cafe.descripcion() + ", con azúcar"

# Uso del patrón Decorador
cafe_basico = Cafe()
print(cafe_basico.descripcion(), "- Costo:", cafe_basico.costo())

cafe_con_leche = ConLeche(cafe_basico)
print(cafe_con_leche.descripcion(), "- Costo:", cafe_con_leche.costo())

cafe_completo = ConAzucar(cafe_con_leche)
print(cafe_completo.descripcion(), "- Costo:", cafe_completo.costo())





# lo entendi mal
# from abc import ABC, abstractmethod

# class Cafe(ABC):

#     @abstractmethod
#     def costo():
#         raise NotImplementedError

# class Capuccino(Cafe):

#     def __init__(self):
#         print('que rico capuccino')

#     def costo(self):
#         return '50 pesos'
    
# class Frapuccino(Cafe):

#     def __init__(self):
#         print('que rico frapuccino')

#     def costo(self):
#         return '90 pesos'
    
# class AbstractFactoryCafe(ABC):
    
#     @staticmethod
#     @abstractmethod
#     def crearCapuccino():
#         raise NotImplementedError
    
#     @staticmethod
#     @abstractmethod
#     def crearFrapuccino():
#         raise NotImplementedError

# class MaquinaCafe(AbstractFactoryCafe):

#     @staticmethod
#     def crearCapuccino():
#         return Capuccino()
    
#     @staticmethod
#     def crearFrapuccino():
#         return Frapuccino()
    

# capuccino: Capuccino = MaquinaCafe.crearCapuccino()
# print(capuccino.costo())

# frapuccino: Frapuccino = MaquinaCafe.crearFrapuccino()
# print(frapuccino.costo())
    

