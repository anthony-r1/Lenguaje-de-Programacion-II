from typing import TypeVar, Generic 
import math

T = TypeVar('T',int,float)
class CalculadoraTriangulo(Generic[T]):
    def __init(self,cateto_a:T,cateto_b:T):
        self.cateto_a = cateto_a
        self.cateto_b = cateto_b

    def calcular_hipotenusa(self)-> int:
        a = int(cateto_a)
        b = int(cateto_b)
        hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
        return hipotenusa

    def calcular_area(self)-> int:
        a = int(cateto_a)
        b = int(cateto_b)
        area = cateto_a * cateto_b
        return area

    def calcular_perimetro(self)-> int:
        a = int(cateto_a)
        b = int(cateto_b)
        perimetro = cateto_a + cateto_b + hipotenusa 
        return perimetro

def main():
    try:
        a = int(input("Ingrese el cateto a: "))
        b = int(input("Ingrese el cateto b: "))
        cal = calcular_hipotenusa(a,b)
        cal1 = calcular_area(a,b)
        cal2 = calcular_perimetro(a,b)
        print(f"La el cateto a = {int(a)} y el cateto b = {int(b)}")
        print(f"La hipotenusa de los catetos {int(a)} y {int(b)} es : {cal.calcular_hipotenusa}")
        print(f"El area es : {cal1.calcular_area}")
        print(f"El perimetro es : {cal2.calcular_perimetro}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
