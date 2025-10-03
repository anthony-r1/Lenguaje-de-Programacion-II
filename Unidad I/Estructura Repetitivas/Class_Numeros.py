class Numeros:
    def __init__(self, numero):
        self.numero = numero

    def clasificar(self):
        for i in range (0, self.numero + 1):
            if i == 0:
                print("EL numero es CERO")
            elif i % 2 == 0:
                print(f"{i} es un número par")
            else:
                print(f"{i} es un número impar")

def main():

    misNumeros = Numeros(10)
    resultado = misNumeros.clasificar()

if __name__ == "__main__":
    main()