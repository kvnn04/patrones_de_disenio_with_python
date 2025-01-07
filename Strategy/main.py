from abc import ABC, abstractmethod

# 1. Interfaz de Estrategia

class EstrategiaDescuento(ABC):
    @abstractmethod
    def calcular_descuento(self, precio):
        pass

# 2. Estrategias concretas

class DescuentoEstudiante(EstrategiaDescuento):
    def calcular_descuento(self, precio):
        return precio * 0.8  # 20% de descuento

class DescuentoJubilado(EstrategiaDescuento):
    def calcular_descuento(self, precio):
        return precio * 0.7  # 30% de descuento

class SinDescuento(EstrategiaDescuento):
    def calcular_descuento(self, precio):
        return precio  # Sin descuento

# 3. Contexto que utiliza una estrategia

class CalculadoraDePrecios:
    def __init__(self):
        self._estrategia = []

    def set_estrategia(self, estrategia: SinDescuento|DescuentoJubilado|DescuentoEstudiante):
        self._estrategia = estrategia

    def calcular_precio(self, precio):
        return self._estrategia.calcular_descuento(precio)


# 4. Uso del patrón Strategy

# Precio base
precio_base = 100

# Estrategia para estudiantes
calculadoraDePrecios = CalculadoraDePrecios()


calculadoraDePrecios.set_estrategia(DescuentoEstudiante())
print("Precio para estudiantes:", calculadoraDePrecios.calcular_precio(precio_base))

# Cambiar estrategia a jubilados
calculadoraDePrecios.set_estrategia(DescuentoJubilado())
print("Precio para jubilados:", calculadoraDePrecios.calcular_precio(precio_base))

# Sin descuento
calculadoraDePrecios.set_estrategia(SinDescuento())
print("Precio sin descuento:", calculadoraDePrecios.calcular_precio(precio_base))
