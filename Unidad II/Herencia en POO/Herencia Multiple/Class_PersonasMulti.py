class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años")

class Trabajador:
    def __init__(self, profesion, salario):
        self.profesion = profesion
        self.salario = salario

    def trabajar(self):
        print(f"Estoy trabajando como {self.profesion} y gano ${self.salario}")

class Estudiante:
    def __init__(self, carrera, universidad):
        self.carrera = carrera
        self.universidad = universidad

    def estudiar(self):
        print(f"Estudio {self.carrera} en la {self.universidad}")

class PersonaMultirol(Persona, Trabajador, Estudiante):
    def __init__(self, nombre, edad, profesion, salario, carrera, universidad):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, profesion, salario)
        Estudiante.__init__(self, carrera, universidad)

    def mostrar_informacion(self):
        print("==== INFORMACIÓN DE LA PERSONA ====")
        self.presentarse()
        self.trabajar()
        self.estudiar()
        
def main():
    persona1 = PersonaMultirol(nombre = "Juanita", edad = 25,
                               profesion = "Desarrollador de software",
                               salario = 2500,
                               carrera = "Ingeniería Estadística e Informática",
                               universidad = "Universidad Nacional del Altiplano")
    persona1.mostrar_informacion()

if __name__=="__main__":
    main()
        
