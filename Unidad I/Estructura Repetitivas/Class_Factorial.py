class Factorial:
    def __init__(self, numero):
        self.numero = numero
        self.resultado = 1
    
    def calcular(self):
        if self.numero < 0:
            print("El factorial no está definido para números negativos.")
            return None
        
        for i in range(1, self.numero + 1):
            self.resultado *= i
        return self.resultado
    
def main():
    mifactorial = Factorial(5)
    resultado = mifactorial.calcular()
    if resultado is not None:
        print(f"El factorial de {mifactorial.numero} es {resultado}")

if __name__ == "__main__":
    main()