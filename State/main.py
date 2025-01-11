from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

# Estado: Esperando moneda
class WaitingForCoinState(State):
    def handle(self, context):
        print("Esperando que el cliente inserte una moneda...")
        context.set_state(SelectingProductState())  # Cambiar al estado siguiente

# Estado: Seleccionando producto
class SelectingProductState(State):
    def handle(self, context):
        print("El cliente está seleccionando un producto...")
        context.set_state(DispensingProductState())  # Cambiar al estado siguiente

# Estado: Entregando producto
class DispensingProductState(State):
    def handle(self, context):
        print("Entregando el producto al cliente...")
        context.set_state(WaitingForCoinState())  # Volver al estado inicial

# Contexto que mantiene el estado actual
class VendingMachine:
    def __init__(self):
        self.state = WaitingForCoinState()  # Estado inicial

    def set_state(self, state):
        self.state = state

    # aca esta la clave para que todo funcione
    def request(self):
        self.state.handle(self)

if __name__ == "__main__":
    machine = VendingMachine()

    # Simular el flujo de la máquina expendedora
    machine.request()  # Esperando moneda
    machine.request()  # Seleccionando producto
    machine.request()  # Entregando producto
    machine.request()  # Volver a esperar moneda
