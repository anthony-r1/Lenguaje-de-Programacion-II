import math
class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError("Subclases deben implementar este método")

    def perimetro(self):
        raise NotImplementedError("Subclases deben implementar este método")

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

# Creación de instancias
circulo = Circulo(5)
rectangulo = Rectangulo(8, 6)

# Impresión formal de los resultados (sin unidades)
print("Nombre de la Figura: Círculo")
print(f"Cálculo del Área: {circulo.area():.2f}")
print(f"Cálculo del Perímetro: {circulo.perimetro():.2f}")
print("---")
print("Nombre de la Figura: Rectángulo")
print(f"Cálculo del Área: {rectangulo.area()}")
print(f"Cálculo del Perímetro: {rectangulo.perimetro()}")
