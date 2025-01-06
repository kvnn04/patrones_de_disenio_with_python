from abc import ABC, abstractmethod

# Clase abstracta Producto
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# Clases concretas de productos
class Truck(Transport):
    def deliver(self):
        return "Entregando por carretera con un camión."

class Ship(Transport):
    def deliver(self):
        return "Entregando por mar con un barco."

# Clase abstracta Creador (Factory)
class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        # Usa el objeto creado para realizar la entrega
        transport = self.create_transport()
        return transport.deliver()

# Clases concretas de Creador (Factories)
class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()

# Uso del patrón
if __name__ == "__main__":
    # Crear una fábrica de transporte terrestre
    road_logistics = RoadLogistics()
    print(road_logistics.plan_delivery())

    # Crear una fábrica de transporte marítimo
    sea_logistics = SeaLogistics()
    print(sea_logistics.plan_delivery())
