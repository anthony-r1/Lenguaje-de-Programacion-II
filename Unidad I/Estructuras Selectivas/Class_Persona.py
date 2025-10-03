class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def EsMayorDeEdad(self):
        if self.edad >= 18:
            return "Es mayor de edad"
        else:
            return "No es mayor de edad"
        
ejemplo = Persona("Carlos", 20)
res = ejemplo.EsMayorDeEdad()

print(f"{ejemplo.nombre} tiene {ejemplo.edad} años. {res}")
    