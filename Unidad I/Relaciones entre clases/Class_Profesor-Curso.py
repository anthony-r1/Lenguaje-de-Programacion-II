class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

profesor = Profesor("COYLA IDME LEONEL  ")
curso = Curso("Lenguaje de Programacion II", profesor)
print(f"El curso {curso.nombre} es impartido por el profesor {curso.profesor.nombre}.")