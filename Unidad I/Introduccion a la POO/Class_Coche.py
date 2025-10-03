class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} {self.color} encendio.")
 
    def acelerar(self):
        print(f"El coche {self.marca} {self.modelo} {self.color} acelero.")

    def frenar(self):
        print(f"El coche {self.marca} {self.modelo} {self.color} freno.")

mi_coche = Coche("Toyota", "Corolla", "Negro")

mi_coche.arrancar()
mi_coche.acelerar()
mi_coche.frenar()