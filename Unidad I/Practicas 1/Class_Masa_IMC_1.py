class Masa:
    def __init__(self, nombre, peso, altura):
        self.__nombre = nombre
        self.__peso = peso
        self.__altura = altura
    
    def calcular_imc(self):
        imc = self.__peso / (self.__altura ** 2)
        return imc
    
    def obtener_categoria(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= imc < 24.9:
            return "Normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidad grado I"
        elif 35 <= imc < 39.9:
            return "Obesidad grado II"
        else:
            return "Obesidad grado III (Mórbida)"
nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
persona = Masa(nombre, peso, altura)
print("Nombre:", persona._Masa__nombre)
print("Peso:", persona._Masa__peso)
print("Altura:", persona._Masa__altura)
print("IMC:", persona.calcular_imc())
print("Categoría:", persona.obtener_categoria())