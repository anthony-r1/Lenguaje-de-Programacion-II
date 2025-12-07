from typing import TypeVar
import math

T = TypeVar('T',int,float)

def calcular_hipotenusa(cateto_a:T,cateto_b:T)->T:
    return math.sqrt(cateto_a**2 + cateto_b**2)

print("Hipotenusa =",calcular_hipotenusa(3,3))
print("Hipotenusa =",calcular_hipotenusa(5.5,2.2))
