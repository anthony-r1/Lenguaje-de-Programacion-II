class Persona:
    def __init__(self, Nombre, Edad):
        self.Nombre = Nombre
        self.Edad = Edad

    def Es_mayor_de_edad(self):
        if self.Edad > 18:
            return "Es mayor de edad"
        else:
            return "No es mayor de edad"

ejemplo = Persona("Maria", 25)
res = ejemplo.Es_mayor_de_edad()

print(ejemplo.Nombre, res)