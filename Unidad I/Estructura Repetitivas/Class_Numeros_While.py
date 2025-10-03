class Numeros:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.contador = 1

    def imprimir(self):
        while self.contador <= 10:
            print(self.contador)
            self.contador += 1

def main():
    cantidad = int(input("Ingrese un número: "))
    misNumeros = Numeros(cantidad)
    misNumeros.imprimir()

if __name__ == "__main__":
    main()