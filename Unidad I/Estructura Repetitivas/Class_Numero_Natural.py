class NumeroNatural:
    def __init__(self, valor):
        self.valor = valor

    def mostrarNatural(self):
        if self.valor < 0:
            print(f"{self.valor} no es un número natural.")
        else:
            print(f"{self.valor} es un número natural.")
        
def main():
    i = 1
    while i <= 100:
        num = NumeroNatural(i)
        num.mostrarNatural()
        i += 1

if __name__ == "__main__":
    main()