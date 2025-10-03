class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        return self.__nombre
    
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa")
        return self.__edad
    
persona = Persona("Juan", 30)
print("Nombre:", persona.get_nombre())
print("Edad:", persona.get_edad())
print(persona.get_nombre(), "tiene", persona.get_edad(), "años")

persona.set_nombre("Pedro")
persona.set_edad(35)

print("Nuevo nombre:", persona.get_nombre())
print("Nueva edad:", persona.get_edad())
print(persona.get_nombre(), "tiene", persona.get_edad(), "años")
