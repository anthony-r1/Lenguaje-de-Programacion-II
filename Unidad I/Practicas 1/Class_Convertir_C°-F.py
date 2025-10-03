class Convertir:
    def __init__(self, fahr, cel):
        self.__fahr = fahr
        self.__cel = cel

    def get_fahr(self):
        return self.__fahr

    def get_cel(self):
        return self.__cel

    def set_fahr(self, nueva_fahr):
        self.__fahr = nueva_fahr

    def set_cel(self, nueva_cel):
        self.__cel = nueva_cel

    def con_cel(self):
        Celsius = ((self.__fahr - 32) * 5) / 9
        return Celsius

    def con_fa(self):
        Fahre = (self.__cel * (9 / 5)) + 32
        return Fahre

num = Convertir(98.6, 0)
num1 = Convertir(0, 25)
print("Fahrenheit a Celsius ", num.con_cel())
print("Celsius a Fahrenheit ", num1.con_fa())