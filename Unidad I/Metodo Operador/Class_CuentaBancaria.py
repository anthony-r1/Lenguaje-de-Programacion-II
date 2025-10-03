class CuentaBancaria:
    def __init__(self,titulo, saldo):
        self.titulo = titulo
        self.saldo = saldo

    def mostrar(self):
        print(f"Titular: {self.titulo}, Saldo: S/.{self.saldo:.2f}")
    def __sub__(self, monto):
        if isinstance(monto, (int, float)):
            if monto <= self.saldo:
                return CuentaBancaria(self.titulo, self.saldo - monto)
            else:
                print("Fondos insuficientes")
            return self
        else:
            print("Operación no válida")
            return self
        
titulo = input("Ingrese el titular de la cuenta: ")
saldo = float(input("Ingrese el saldo inicial: "))
monto = float(input("Ingrese el monto a retirar: "))

cuenta1 = CuentaBancaria(titulo, saldo)
cuenta1.mostrar()

cuenta2 = cuenta1 - monto
cuenta2.mostrar()

cuenta3 = cuenta2 - 700
cuenta3.mostrar()