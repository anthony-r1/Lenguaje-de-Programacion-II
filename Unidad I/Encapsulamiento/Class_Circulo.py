import math
class Circulo:
    def __init__(self, radio):
        self.__radio = radio
    
    def get_radio(self):
        return self.__radio
    
    def set_radio(self, nuevo_radio):
        if nuevo_radio > 0:
            self.__radio = nuevo_radio
        else:
            print("El radio debe ser mayor que 0")

    def calcular_area(self):
        return math.pi * (self.__radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.__radio
    
circulo = Circulo(5)
print("Area del circulo: ", round(circulo.calcular_area(), 2))
print("Perimetro del circulo: ", round(circulo.calcular_perimetro(), 2))