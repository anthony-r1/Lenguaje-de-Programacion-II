from typing import TypeVar, Generic

T = TypeVar('T', int, float)

class CalculadoraFactorial(Generic[T]):
    def __init__(self, numero: T):
        self.numero = numero

    def calcular_factorial(self) -> int:
        n = int(self.numero)
        if n < 0:
            raise ValueError("El factorial no esta definido para numeros negativos")
        
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
            
        return resultado

def main():
    try:
        n = int(input("ingrese un numero: "))
        cal = CalculadoraFactorial(n)
        print(f"El Factorial de {int(n)} es : {cal.calcular_factorial()}")
    except ValueError as e:
        print(f"Error: {e}")
        
if __name__ == "__main__": 
    main()
