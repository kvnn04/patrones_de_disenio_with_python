from abc import ABC, abstractmethod

class Tranporte(ABC):
    
    @abstractmethod
    def transportar():
        pass

class Coche(Tranporte):
    def transportar(self):
        print('estoy transportando un producto via terrestre')

class Barco(Tranporte):
    def transportar(self):
        print('estoy transportando un producto via Mar')
# medios de transporte
# -----------------------------------------------------------------------------

# Clase abstracta (fabrica)
class Fabrica(ABC):

    @abstractmethod
    def crearTransporte():
        pass

    def enviar(self):
        transporte = self.crearTransporte()
        print(transporte)

class EntregaTerrestre(Fabrica):
    def crearTransporte(self):
        return Coche()
    

class EntregaMaritima(Fabrica):
    def crearTransporte(self):
        return Barco()
    
tranporteEnCoche = EntregaTerrestre().crearTransporte()

tranporteEnCoche.transportar()

transportarEnBarco = EntregaMaritima().crearTransporte()

transportarEnBarco.transportar()