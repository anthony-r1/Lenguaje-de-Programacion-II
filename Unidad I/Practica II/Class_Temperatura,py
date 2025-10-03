class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
        print("Objeto Temperatura creado")

    def a_fahrenheit(self):
        fahrenheit = (self.celsius * 9/5) + 32
        return fahrenheit
    def mostrar_temperatura(self):
        print(f"Temperatura en Celsius: {self.celsius}°C")
        print(f"Temperatura en Fahrenheit: {self.a_fahrenheit()}°F")
cel = float(input("Ingrese grados Celsius: "))
temp = Temperatura(cel)
temp.mostrar_temperatura()

del temp
try:
    print(temp)
except NameError:
    print("Objeto temperatura destruido")
    