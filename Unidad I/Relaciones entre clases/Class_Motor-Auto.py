class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def enceder(self):
        return f"El motor {self.tipo} está encendido."
    
class Auto:
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor("V8")

    def arrancar(self):
        print(f"El auto {self.marca} está arrancando.")
        self.motor.enceder()

mi_auto = Auto("Toyota supra")
mi_auto.arrancar()