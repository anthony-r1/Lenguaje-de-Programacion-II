class MetodoPago:
    def pago(self):
        pass

class TarjetaCredito(MetodoPago):
    def pago(self):
        print("Se realizo el pago con tarjeta de credito")

class Paypal(MetodoPago):
    def pago(self):
        print("Se realizo el pago con Paypal")

class Efectivo(MetodoPago):
    def pago(self):
        print("Se realizo el pago con efectivo")

pagos = [TarjetaCredito(), Paypal(), Efectivo()]

for p in pagos:
    p.pago()
