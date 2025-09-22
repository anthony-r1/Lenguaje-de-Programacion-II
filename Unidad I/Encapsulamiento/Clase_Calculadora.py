class Calculadora:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def get_num1(self):
        return self.__num1

    def get_num2(self):
        return self.__num2

    def set_num1(self, nuevo_num1):
        if nuevo_num1 > 0:
            self.__num1 = nuevo_num1
        else:
            print("Número invalido")

    def set_num2(self, nuevo_num2):
        if nuevo_num2 > 0:
            self.__num2 = nuevo_num2
        else:
            print("Número invalido")

    def suma(self):
        return self.__num1 + self.__num2

    def resta(self):
        return self.__num1 - self.__num2

    def producto(self):
        return self.__num1 * self.__num2

    def cociente(self):
        return self.__num1 / self.__num2

def main():
    calculadora = Calculadora(2,5)
    print("Suma: ", calculadora.suma())
    print("Resta: ", calculadora.resta())
    print("Producto: ", calculadora.producto())
    print("División: ", calculadora.cociente())
if __name__=="__main__":
    main()