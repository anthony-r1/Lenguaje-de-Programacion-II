class Fibonacci:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.secuencia = []

    def generarSerie(self):
        a, b = 0, 1
        for _ in range(self.cantidad):
            self.secuencia.append(a)
            a, b = b, a + b
        return self.secuencia
    
def main():
    cantidad = int(input("Ingrese la cantidad de números de Fibonacci a generar: "))
    mifibonacci = Fibonacci(cantidad)
    resultado = mifibonacci.generarSerie()
    print(f"Los primeros {cantidad} números de Fibonacci son: {resultado}")

if __name__ == "__main__":
    main()