class Singleton:
    _instancia = None  # Variable de clase para almacenar la única instancia

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls, *args, **kwargs)
        return cls._instancia

    def mostrar_mensaje(self):
        print("¡Hola desde el Singleton!")


if __name__ == "__main__":
    # Crear dos objetos aparentemente diferentes
    singleton1 = Singleton()
    singleton2 = Singleton()

    # Ambos son la misma instancia
    print(singleton1 is singleton2)  # True
    if singleton1 == singleton2:
        print('True, Boka')
    # Usar un método de la instancia
    singleton1.mostrar_mensaje()

# --------------------------------------------------------------------------------------------------

class Singleton:
    _instancia = None  # Variable de clase para almacenar la única instancia

    def __init__(self, nombre):
        if not hasattr(self, 'nombre'):  # Evitar sobrescribir si ya se inicializó
            self.nombre = nombre

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            # cls._instancia = super().__new__(cls, *args, **kwargs)
            # Crea la única instancia usando super().__new__
            cls._instancia = super(Singleton, cls).__new__(cls)                         # Usando Singleton con un __init__
        return cls._instancia

    def mostrar_mensaje(self):
        print("¡Hola desde el Singleton!")


if __name__ == "__main__":
    # Crear dos objetos aparentemente diferentes
    singleton1 = Singleton('kevin')
    singleton2 = Singleton('Boka')

    # Ambos son la misma instancia
    print(singleton1 is singleton2)  # True
    if singleton1 == singleton2:
        print(singleton2.nombre)
    # Usar un método de la instancia
    singleton1.mostrar_mensaje()