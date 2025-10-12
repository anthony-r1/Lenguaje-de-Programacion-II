class Factorial:
    def __init__(self, numero):
        self.__numero = numero
    
    def calcular(self):
        if self.__numero < 0:
            return "El factorial no está definido para números negativos"
        elif self.__numero == 0 or self.__numero == 1:
            return 1
        else:
            factorial = 1
            for i in range(2, self.__numero + 1):
                factorial *= i
            return factorial
    
    def mostrar_resultado(self):
        resultado = self.calcular()
        print(f"El factorial de {self.__numero} es: {resultado}")

if __name__ == "__main__":
    factorial_obj = Factorial(5)
    factorial_obj.mostrar_resultado()
