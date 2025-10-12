class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        print("Cuenta creada con éxito. Bienvenido al banco.")

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito de {monto} realizado. Saldo actual: {self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto} realizado. Saldo restante: {self.saldo}")
        else:
            print("Fondos insuficientes para el retiro.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

saldo_inicial = float(input("Ingrese el saldo inicial: "))
cuenta = CuentaBancaria(saldo_inicial)

monto_deposito = float(input("Ingrese el monto a depositar: "))
cuenta.depositar(monto_deposito)

monto_retiro = float(input("Ingrese el monto a retirar: "))
cuenta.retirar(monto_retiro)

cuenta.mostrar_saldo()

del cuenta
try:
    print(cuenta)
except NameError:
    print("Objeto cuenta bancaria destruido")
