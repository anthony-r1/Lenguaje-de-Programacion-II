class Motor:
    def encender(self):
        print(" El motor ha arrancado correctamente.")

class Auto:
    def __init__(self):
        self.motor = Motor() 

    def arrancar(self):
        print("Girando la llave del auto...")
        self.motor.encender()
        print("¡Auto listo para avanzar!")

mi_auto = Auto()
mi_auto.arrancar()
