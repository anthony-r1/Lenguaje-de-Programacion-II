class Hipotenusa:
    def __init__(self, cat1, cat2):
        self.cat1 = cat1
        self.cat2 = cat2
    
    def cal_hipotenusa(self):
        hipotenusa = (self.cat1**2 + self.cat2**2) ** 0.5
        return hipotenusa
    
    def mostrar_info(self):
        print(f"El primer cateto del triangulo es: {self.cat1}")
        print(f"El segundo cateto del triangulo es: {self.cat2}")
        print(f"La hipotenusa del triangulo es: {self.cal_hipotenusa():.2f}")

hip_famoso = Hipotenusa(3, 4)

hip_famoso.mostrar_info()