from abc import ABC, abstractmethod
from typing import Optional, Union

class AbsEstrategiaPago(ABC):

    @abstractmethod
    def realizarPago():
        raise NotImplementedError
    
class Paypal(AbsEstrategiaPago):

    def realizarPago(self):
        return'pago realizado con paypal'
         
        
class Debito(AbsEstrategiaPago):

    def realizarPago(self):
        return'pago realizado con Debito'

class EstrategiaPago():

    def __init__(self, tipoPago: AbsEstrategiaPago):
        if not isinstance(tipoPago, (AbsEstrategiaPago)):
            raise 'Agregue un valor, no puede ser nulo'
        
        self._tipoPago = tipoPago

    def realizarPago(self):
        print(self._tipoPago.realizarPago())
    
    def setTipoDePago(self, newTipoPago: Optional[Union[Debito,Paypal,None]]):
        if not isinstance(newTipoPago, (Debito,Paypal,None)):
            print('No admite ese tipos')
        self._tipoPago = newTipoPago

paypal = Paypal()
debito = Debito()


estrategiaPago: EstrategiaPago = EstrategiaPago(tipoPago=paypal)

estrategiaPago.realizarPago()

estrategiaPago.setTipoDePago(newTipoPago=debito)

estrategiaPago.realizarPago()
# Bien implementado