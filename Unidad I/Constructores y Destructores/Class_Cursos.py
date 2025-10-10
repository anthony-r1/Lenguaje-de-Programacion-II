import gc
class Cursos:
    def __init__(self,nombre,codigo,profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        print(f"Curso {self.nombre} registrado | código: {self.codigo} | profesor: {self.profesor}")

    def mostrar_info(self):
        return f"Curso: {self.nombre}, Código: {self.codigo}, Profesor: {self.profesor}"
    
    def __del__(self):
        print(f"El curso {self.nombre} ha sido eliminado")

alumnos_datos = [("SISTEMAS DE GESTION DE BASE DE DATOS I", "EST304", "TITO LIPA JOSE PANFILO"),
            ("LENGUAJES DE PROGRAMACION II", "EST305", "COYLA IDME LEONEL"),
            ("PROGRAMACION NUMERICA", "EST207", "TORRES CRUZ FRED"),
            ("ANALISIS Y DISEÑO DE SISTEMAS DE INFORMACION", "EST308", "ROSSEL BERNEDO LUIS ALBERTH"),
            ("INFERENCIA ESTADISTICA", "EST306", "ROQUE CLAROS ROBERTO ELVIS"),
            ("MODELOS DISCRETOS", "EST307", "VARGAS VALVERDE CONFESOR MILAN  ")
            ]

registros = []

for datos in alumnos_datos:
    curso = Cursos(*datos) 
    curso.mostrar_info()
    registros.append(curso)

registros.clear()
del curso
gc.collect()
print("Todos los cursos han sido eliminados")