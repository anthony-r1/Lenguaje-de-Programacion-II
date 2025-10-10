class Estudiante:
    def __init__(self, nombre, dni, codigo_estudiante):
        self.nombre = nombre
        self.dni = dni
        self.codigo_estudiante = codigo_estudiante
        self.cursos = []

    def inscribir_curso(self, curso):
        self.cursos.append(curso)
        curso.agregar_estudiante(self)

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}, DNI: {self.dni}, Código: {self.codigo_estudiante}")
        print("Cursos inscritos:")
        for curso in self.cursos:
            print(f"- {curso.nombre_curso} ")

class Profesor:
    def __init__(self, nombre, dni, departamento):
        self.nombre = nombre
        self.dni = dni
        self.departamento = departamento
    
    def mostrar_info(self):
        print(f"Profesor: {self.nombre} | DNI: {self.dni} | Depto: {self.departamento}")

class Curso:
    def __init__(self, nombre_curso, profesor):
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.codigo_curso = nombre_curso[:3].upper()
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)

    def mostrar_info(self):
        print(f"Curso: {self.nombre_curso}")
        print(f"Profesor: {self.profesor.nombre}")
        print("Estudiantes inscritos:")
        for estudiante in self.estudiantes:
            print(f"- {estudiante.nombre} ({estudiante.codigo_estudiante})")

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_info(self):
        for curso in self.cursos:
            curso.mostrar_info()

prof1 = Profesor("Ing. Coyla Leonel", "01323043", "Programación")
prof2 = Profesor("Ing. Tito Jose", "02839212", "Programación")
prof3 = Profesor("Dr. Valvede Confesor", "02839312", "Estadística")
prof4 = Profesor("Ing. Torres Fred", "03987412", "Programación")
prof5 = Profesor("Ing. Roque Elvis", "94847311", "Estadística")
prof6 = Profesor("Ing. Rossel Luis", "83474711", "Programación")

curso1 = Curso("Lenguajes de Programación II", prof1)
curso2 = Curso("Sistema de gestión de base de datos", prof2)
curso3 = Curso("Modelos discretos", prof3)
curso4 = Curso("Programación numérica", prof4)
curso5 = Curso("Inferencia estadística", prof5)
curso6 = Curso("Análisis y diseños de sistemas de información", prof6)

est1 = Estudiante("Juan Perez", "12345678", "245678")
est2 = Estudiante("Maria Gomez", "87654321", "245679")

univ = Universidad("Universidad Nacional del Altiplano")
univ.agregar_curso(curso1)
univ.agregar_curso(curso2)

est1.inscribir_curso(curso1)
est1.inscribir_curso(curso2)
est1.inscribir_curso(curso3)
est1.inscribir_curso(curso4)
est1.inscribir_curso(curso5)
est1.inscribir_curso(curso6)

est2.inscribir_curso(curso1)
est2.inscribir_curso(curso2)
est2.inscribir_curso(curso3)
est2.inscribir_curso(curso4)
est2.inscribir_curso(curso5)
est2.inscribir_curso(curso6)

print(univ.nombre)
univ.mostrar_info()
est1.mostrar_info()
est2.mostrar_info()