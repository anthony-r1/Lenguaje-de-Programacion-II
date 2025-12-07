class Rectangulo:
    def calcular(self):
        print("El area del Rectangulo es: b * h.")
        areaR = base * altura
        return areaR
class Cuadrado:
    def calcular(self):
        print("El area del Cuadrado es: l * l.")
        areaC = lado * lado
        return areaC
class Circulo:
    def calcular(self):
        print("El area del Circulo es: π * r^2")
        areaCi= pi * (radio * radio)
        return areaCi
class Triangulo:
    def calcular(self):
        print("El area del Triangulo es: (b * h)/2.")
        areaT = (base * altura)/2
        return areaT

def area(obj):
    result = obj.calcular()
    print("El cálculo es:", result)

try:
    base = int(input("Ingrese la base: "))    
    altura = int(input("Ingrese la altura: ")) 
    lado = int(input("Ingrese el lado: ")) 
    radio = int(input("Ingrese el radio: "))    
    pi = 3.14159

    figuras = [Rectangulo(),Cuadrado(),Circulo(),Triangulo()]

    for obj2 in figuras:
        area(obj2)

except ValueError:
    print("\nError: Por favor, ingrese solo números enteros para las dimensiones.")