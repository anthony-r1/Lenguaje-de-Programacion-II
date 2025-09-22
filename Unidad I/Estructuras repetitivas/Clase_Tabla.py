class Tabla:
    def __init__(self, numero):
        self.numero = numero

    def multiplicacion(self):
        for i in range (1, 11):
            resultado = self.numero * i
            print(f"{self.numero} X {i} = {resultado}")

def main():
    numero = int(input("Ingrese un número: "))
    resultado = Tabla(numero)
    resultado.multiplicacion()
if __name__=="__main__":
    main()