class SumaNaturales:
    def __init__(self, limite):
        self.limite = limite
        self.suma = 0

    def calcular_suma(self):
        for i in range(1, self.limite + 1):
            self.suma += i
        return self.suma
    
def main():
    miSuma = SumaNaturales(10)
    resultado = miSuma.calcular_suma()
    print(f"La suma de los primeros 10 números naturales es: {resultado}")

if __name__ == "__main__":
    main()  