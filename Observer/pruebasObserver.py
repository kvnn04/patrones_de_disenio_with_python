from abc import ABC, abstractmethod

# Observado
class CanalYutu:
    def __init__(self):
        self._observadores = []

    def aniadirObservador(self, observador):
        print(f'se añadio el subcriptor {observador.nombre}')
        self._observadores.append(observador)
    
    def eliminarObservador(self, observador):
        if not observador in self._observadores:
            print('no ese no esta subscripto')
            return None
        
        print(f'{observador.nombre} eliminado del cana')
        self._observadores.remove(observador)
    
    def notificarATodosLosObservadoresSubscriptos(self, newNoticia):
        if not self._observadores:
            print('no hay nadie subscripto')
            return None

        for i in self._observadores:
            i.notificar(newNoticia)

# Observadores
class Observador(ABC):
    @abstractmethod
    def notificar():
        pass

class Persona(Observador):

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
    
    def notificar(self, noticia: str):
        mensaje: str = f'{self.nombre} tenes una noticia: {noticia}'
        print(mensaje)
        return None

if __name__ == '__main__':
    canal = CanalYutu()

    oneSub: Persona = Persona(nombre='KevinBostero123')
    twoSub: Persona = Persona(nombre='IQ-2')

    canal.aniadirObservador(observador=oneSub)
    canal.aniadirObservador(observador=twoSub)
    canal.notificarATodosLosObservadoresSubscriptos('Boka se clasifica para la libertadores')

    canal.eliminarObservador(twoSub)

    canal.notificarATodosLosObservadoresSubscriptos('Boka se clasifica para la libertadores')





