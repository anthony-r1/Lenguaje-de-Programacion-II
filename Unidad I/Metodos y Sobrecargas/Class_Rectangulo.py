class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base*self.altura
    
Rec = Rectangulo(10,5)
area = Rec.calcular_area()

print(f"El area del rectangulo con los parametros {Rec.base} y {Rec.altura} es :",area)