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
            print("El número debe ser mayor que 0")
    
    def set_num2(self, nuevo_num2):
        if nuevo_num2 > 0:
            self.__num2 = nuevo_num2
        else:
            print("El número debe ser mayor que 0")

    def sumar(self):
        return self.__num1 + self.__num2
    
    def restar(self):
        return self.__num1 - self.__num2
    
    def multiplicar(self):
        return self.__num1 * self.__num2    
    
    def dividir(self):
        if self.__num2 != 0:
            return self.__num1 / self.__num2
        else:
            return "Error: División por cero"
        
def main():
    calc = Calculadora(10, 5)
    print("Suma:", calc.sumar())
    print("Resta:", calc.restar())
    print("Multiplicación:", calc.multiplicar())
    print("División:", calc.dividir())

if __name__ == "__main__":
    main()