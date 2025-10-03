class NumeroMultiplo:
    def __init__(self, valor):
        self.valor = valor

    def mostrarMultiplo(self):
        if self.valor == 0:
            print(f"El múltiplo de {self.valor} es indefinido.")
        elif self.valor % 3 == 0 and self.valor % 5 == 0:
            print(f"El {self.valor} es múltiplo de 3 y 5.")
        elif self.valor % 3 == 0:
            print(f"El {self.valor} es múltiplo de 3.")
        elif self.valor % 5 == 0:
            print(f"El {self.valor} es múltiplo de 5.")
        else:
            print(f"El {self.valor} no es múltiplo de 3 ni de 5.")  

        print("*"*60)  # Línea de separación

def main():

    i = 0
    while i <= 100:
        num = NumeroMultiplo(i)
        num.mostrarMultiplo()
        i += 1

if __name__ == "__main__":
    main()