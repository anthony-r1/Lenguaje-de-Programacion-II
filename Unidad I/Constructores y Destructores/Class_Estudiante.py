import gc
class estudiante:
    def __init__(self,nombre,edad,carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        print(f"Estudiante {self.nombre} registrado | edad: {self.edad} | carrera: {self.carrera}")

    def mostrar_info(self):
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}"
    
    def __del__(self):
        print(f"El estudiante {self.nombre} ha sido eliminado")

datos_estudiantes = [("Juan Perez", 20, "Ingeniería"),
            ("Maria Gomez", 22, "Educacion Primaria"),
            ("Luis Rodriguez", 21, "Medicina"),
            ("Ana Martinez", 23, "Derecho"),
            ("Carlos Sanchez", 24, "Arquitectura"),]

grupo_estudiantes = []

for datos in datos_estudiantes:
    estudiante_instancia = estudiante(*datos)
    estudiante_instancia.mostrar_info()
    grupo_estudiantes.append(estudiante_instancia)

grupo_estudiantes.clear()
del estudiante_instancia
gc.collect()
print("Todos los estudiantes han sido eliminados")