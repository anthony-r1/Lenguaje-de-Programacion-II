class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado.")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}, Saldo: {self.saldo}")

cuenta1 = CuentaBancaria("Anthony", 1000)
cuenta2 = CuentaBancaria("Nayelin", 500)

cuenta1.depositar(200)
cuenta1.retirar(1500)
cuenta1.mostrar_saldo()

cuenta2.retirar(100)
cuenta2.mostrar_saldo()
