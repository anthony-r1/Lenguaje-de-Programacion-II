class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def get_base(self):
        return self.__base
    
    def get_altura(self):
        return self.__altura
    
    def set_base(self, nueva_base):
        if nueva_base > 0:
            self.__base = nueva_base
        else:
            print("La base debe ser mayor que 0")

    def set_altura(self, nueva_altura):
        if nueva_altura > 0:
            self.__altura = nueva_altura
        else:
            print("La altura debe ser mayor que 0")

    def calcular_area(self):
        return self.__base * self.__altura
    
    def calcular_perimetro(self):
        return 2 * (self.__base + self.__altura)
    
rectangulo = Rectangulo(4, 5)
print("Area del rectangulo: ", rectangulo.calcular_area())
print("Perimetro del rectangulo: ", rectangulo.calcular_perimetro())