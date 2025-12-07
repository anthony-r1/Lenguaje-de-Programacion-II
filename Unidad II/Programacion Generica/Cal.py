from typing import TypeVar, Generic 
import math

T = TypeVar('T', int, float)
class CalculadoraTriangulo(Generic[T]):
    def __init__(self, cateto_a: T, cateto_b: T):
        self.cateto_a = cateto_a
        self.cateto_b = cateto_b
        self.hipotenusa = self._calcular_hipotenusa_interna()

    def _calcular_hipotenusa_interna(self) -> float:
        return math.sqrt(self.cateto_a**2 + self.cateto_b**2)

    def calcular_hipotenusa(self) -> float:
        return self.hipotenusa

    def calcular_area(self) -> float:
        area = (self.cateto_a * self.cateto_b) / 2.0
        return area

    def calcular_perimetro(self) -> float:
        perimetro = self.cateto_a + self.cateto_b + self.hipotenusa
        return perimetro

def main():
    try:
        a = float(input("Ingrese el cateto a: "))
        b = float(input("Ingrese el cateto b: "))
        
        if a <= 0 or b <= 0:
            raise ValueError("Los catetos deben ser positivos")
            
        cal = CalculadoraTriangulo(a, b) 
        
        print(f"La el cateto a = {a} y el cateto b = {b}")
        
        print(f"La hipotenusa es: {cal.calcular_hipotenusa()}")
        print(f"El área es: {cal.calcular_area()}")
        print(f"El perímetro es: {cal.calcular_perimetro()}")
        
    except ValueError as ve:
        print("Error.",ve)

if __name__ == "__main__":
    main()
