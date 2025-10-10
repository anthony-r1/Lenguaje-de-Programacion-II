class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.departamentos = []

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

dep1 = Departamento("Ingenieria Estadistica e Informatica")
dep2 = Departamento("Ciencias de la Salud")

uni = Universidad("Universidad Nacional del Altiplano")

uni.agregar_departamento(dep1)
uni.agregar_departamento(dep2)

for dept in uni.departamentos:
    print(dept.nombre)