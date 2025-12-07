class Vehiculo:
    def acelerar(self):
        print("El vehículo está acelerando.")

class Volador:
    def volar(self):
        print("El objeto está volando.")

class Avion(Vehiculo, Volador):
    pass

mi_avion = Avion()
mi_avion.acelerar()
mi_avion.volar()
