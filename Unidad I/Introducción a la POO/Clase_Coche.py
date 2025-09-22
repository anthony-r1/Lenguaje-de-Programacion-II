class Coche:
    def __init__(self, Marca, Modelo, Color):
        self.Marca = Marca
        self.Modelo = Modelo
        self.Color = Color

    def Arranca(self):
        print(f"El coche {self.Marca} {self.Modelo} {self.Color} encendió")

    def Acelera(self):
        print(f"El coche {self.Marca} {self.Modelo} {self.Color} aceleró")

    def Frena(self):
        print(f"El coche {self.Marca} {self.Modelo} {self.Color} frenó")

mi_coche = Coche("Toyota", "Corolla", "Blanco")

mi_coche.Arranca()
mi_coche.Acelera()
mi_coche.Frena()