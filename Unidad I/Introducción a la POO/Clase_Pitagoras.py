class Pitagoras:
    def __init__(self, catetoa, catetob):
        self.catetoa = catetoa
        self.catetob = catetob

    def Hipotenusa(self):
        return (self.catetoa ** 2 + self.catetob ** 2)**(1/2)

triangulo = Pitagoras(4,3)

print("La hipotenusa es", triangulo.Hipotenusa())