class Ladrillo:
    def __init__(self, longitud, altura, ancho):
        self.longitud = longitud
        self.altura = altura
        self.ancho = ancho

    def calcular(self):
        ladrillo = (1/ ((self.longitud + 0.015) * (self.altura + 0.015)))

longitud = float(input("Ingrese la longitud del ladrillo: "))
altura = float(input("Ingrese la altura del ladrillo: "))
ancho = float(input("Ingrese el ancho del ladrillo: "))

cantidad = Ladrillo(longitud, altura, ancho)

print("La cantidad de ladrillos en 1 m² es: ", cantidad.calcular(), "sin desperdicio")
print("La cantidad de ladrillos corregidos en 1 m² es: ", cantidad.calcular() * 1.05, "con desperdicio del 5%")
print("La cantidad de ladrillos en 8.05 m² es: ", cantidad.calcular() * 1.05 * 8.05)
