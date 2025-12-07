class Catetoa:
    def __init__(self, cateto_a):
        self.cateto_a = cateto_a

class Catetob:
    def __init__(self, cateto_b):
        self.cateto_b = cateto_b

class Hipotenusa(Catetoa, Catetob):
    def __init__(self, cateto_a, cateto_b):
        Catetoa.__init__(self, cateto_a)
        Catetob.__init__(self, cateto_b)

    def calcular_hipotenusa(self):
        if (self.cateto_a < 0) or (self.cateto_b < 0):
            raise ValueError("Los catetos deben ser mayors que 0")
        return (self.cateto_a ** 2 + self.cateto_b ** 2) ** 0.5

    def mostrar_resultado(self):
        hipotenusa = self.calcular_hipotenusa()
        return f"La hipotenusa es : {hipotenusa}"

def leer_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("Por favor, ingrese un valor positivo")
                continue
            return valor
        except ValorError:
            print("Entrada invalida, ingrese un número valido")

catetoa = leer_float("Ingrese el cateto a: ")
catetob = leer_float("Ingrese el cateto b: ")

triangulo = Hipotenusa(cateto_a = catetoa, cateto_b = catetob)
print(triangulo.mostrar_resultado())

