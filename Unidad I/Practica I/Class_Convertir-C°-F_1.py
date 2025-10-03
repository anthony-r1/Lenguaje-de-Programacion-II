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
        celsius = (self.__fahr - 32) * 5 / 9
        return round(celsius, 2)

    def con_fa(self):
        fahre = (self.__cel * 9 / 5) + 32
        return round(fahre, 2)

fahr = float(input("Ingrese grados Fahrenheit: "))
cel = float(input("Ingrese grados Celsius: "))

conversor = Convertir(fahr, cel)

print(f"{conversor.get_fahr()} °F equivalen a {conversor.con_cel()} °C")
print(f"{conversor.get_cel()} °C equivalen a {conversor.con_fa()} °F")