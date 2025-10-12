class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo if saldo >= 0 else 0
    
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print("Error: No se puede asignar un saldo negativo.")
    
    def mostrar_datos(self):
        print(f"Titular: {self.__titular}")
        print(f"Saldo: S/. {self.__saldo:.2f}")

if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Ana Perez", 5000)
    cuenta1.mostrar_datos()
    cuenta1.set_saldo(7000)
    cuenta1.mostrar_datos()
    cuenta1.set_saldo(-100) 