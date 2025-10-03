class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
    
operacion = Rectangulo(5, 10)

print("El area del rectangulo es: ", operacion.area())
print("El perimetro del rectangulo es: ", operacion.perimetro())