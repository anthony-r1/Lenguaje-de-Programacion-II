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
            print("Base invalida")

    def set_altura(self, nueva_altura):
        if nueva_altura > 0:
            self.__altura = nueva_altura
        else:
            print("Altura invalida")

    def calcular_area(self):
        return self.__altura * self.__base

    def calcular_perimetro(self):
        return (self.__altura + self.__base) * 2

rectangulo = Rectangulo(4,5)
print("Área del rectángulo ", rectangulo.calcular_area())
print("Perímetro del rectángulo ", rectangulo.calcular_perimetro())