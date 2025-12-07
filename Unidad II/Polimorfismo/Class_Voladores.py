class Pajaro:
    def volar(self):
        print("El pajaro vuela")

class Avion:
    def volar(self):
        print("El avión vuela")

def hacer_volar(obj):
    obj.volar()

hacer_volar(Pajaro())
hacer_volar(Avion())
