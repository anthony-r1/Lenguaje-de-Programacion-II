class Pitagoras:
    def __init__(self, cata, catb):
        self.cata = cata
        self.catb = catb

    def Hipotenusa(self):
        hipotenusa = (self.cata ** 2 + self.catb ** 2) ** 0.5
        return hipotenusa
    
triangulo = Pitagoras(3, 4)
print("La hipotenusa del triangulo es: ", triangulo.Hipotenusa())