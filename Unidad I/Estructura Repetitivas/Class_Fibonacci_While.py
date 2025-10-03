class Fibonacci:
    def __init__(self,cantidad):
        self.cantidad = cantidad
        self.a = 0
        self.b = 1
        self.contador = 0

    def generarSerie(self):
        print(f"Los primeros {self.cantidad} números de Fibonacci son:")
        while self.contador < self.cantidad:
            print(self.a, end=' ')
            c = self.a + self.b
            self.a = self.b
            self.b = c
            self.contador += 1
        print()  # Para una nueva línea al final
        return
    
def main():
    cantidad = int(input("Ingrese la cantidad de números de Fibonacci a generar: "))
    mifibonacci = Fibonacci(cantidad)
    mifibonacci.generarSerie()

if __name__ == "__main__":
    main()