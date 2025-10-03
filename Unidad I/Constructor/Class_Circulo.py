import math
class Circulo:
    def __init__(self,radio):
        self.radio = radio
        print("Objeto circular creado")

    def calular_area(self):
        area = math.pi*self.radio**2
        return area
    
radio_usuario = float(input("Ingrese el radio del circulo: "))

circulo1 = Circulo(radio_usuario)
resultado = circulo1.calular_area()
print(f"El area del circulo es: {resultado}")

del circulo1

try:
    print(circulo1)
except NameError:
    print("El objeto circulo1 ya no existe")