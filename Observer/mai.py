# Clase Sujeto (Subject)
class Subject:
    def __init__(self):
        self._observers = []  # Lista de observadores

    def attach(self, observer):
        """Agrega un observador a la lista."""
        self._observers.append(observer)

    def detach(self, observer):
        """Elimina un observador de la lista."""
        self._observers.remove(observer)

    def notify(self, message):
        """Notifica a todos los observadores."""
        for observer in self._observers:
            observer.update(message)

# Interfaz Observador
class Observer:
    def update(self, message):
        """Método a implementar por los observadores concretos."""
        pass

# Clase concreta de Observador
class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        """Recibe actualizaciones del Sujeto."""
        print(f"{self.name} recibió el mensaje: {message}")

# Uso del patrón
if __name__ == "__main__":
    # Crear el sujeto
    subject = Subject()

    # Crear observadores
    observer1 = ConcreteObserver("Observador 1")
    observer2 = ConcreteObserver("Observador 2")

    # Suscribir observadores al sujeto
    subject.attach(observer1)
    subject.attach(observer2)

    # Notificar a los observadores
    subject.notify("Se produjo un cambio importante.")
    subject.notify("Otro evento relevante ocurrió.")

    # Desuscribir un observador
    subject.detach(observer1)

    # Notificar nuevamente
    subject.notify("Un nuevo mensaje, pero no para todos.")
