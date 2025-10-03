import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def cal_area(self):
        area = math.pi * (self.radio ** 2)
        return area
    
    def cal_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro
    
    def mostrar_info(self):
        print(f"El radio de nuestro círculo es: {self.radio}")
        print(f"El área, o espacio que ocupa, es: {self.cal_area():.2f}")
        print(f"El perímetro, o su cinturón, es: {self.cal_perimetro():.2f}")

circulo_famoso = Circulo(7)

circulo_famoso.mostrar_info()