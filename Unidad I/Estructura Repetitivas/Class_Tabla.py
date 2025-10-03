class Tabla:
    def __init__(self, numero):
        self.numero = numero

    def multiplicar(self):
        for i in range(1, 11):
            resultado = self.numero * i
            print(f"{self.numero} x {i} = {resultado}")

def main():
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    miTabla = Tabla(numero)
    miTabla.multiplicar()

if __name__ == "__main__":
    main()