import math
class Comida:
    def __init__(self,proteinas,carbohidratos,grasas):
        self.proteinas = proteinas
        self.carbohidratos = carbohidratos
        self.grasas = grasas
        print("Objeto Comida creado")
        print(f"Proteínas: {self.proteinas}g, Carbohidratos: {self.carbohidratos}g, Grasas: {self.grasas}g")

    def calcular_calorias(self):
        calorias = (self.proteinas * 4) + (self.carbohidratos * 4) + (self.grasas * 9)
        return calorias
    
    def mostrar_info(self):
        print("Información nutricional")
        print(f"Proteínas: {self.proteinas}g")
        print(f"Carbohidratos: {self.carbohidratos}g")
        print(f"Grasas: {self.grasas}g")
        print(f"Calorías: {self.calcular_calorias()} kcal")

almuerzo = Comida(proteinas=30, carbohidratos=50, grasas=20)
almuerzo.mostrar_info()

del almuerzo

try:
    print(almuerzo)
except NameError:
    print("El almuerzo ya no existe")