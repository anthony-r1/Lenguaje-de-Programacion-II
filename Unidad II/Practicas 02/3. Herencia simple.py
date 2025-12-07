class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_pago(self):
        return self.salario_base

class EmpleadoTiempoCompleto(Empleado):
    def calcular_pago(self):
        return self.salario_base * 1.10

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, tarifa_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_base = 0
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_pago(self):
        return self.tarifa_hora * self.horas_trabajadas

empleados = [
    EmpleadoTiempoCompleto("Luis", 2000),
    EmpleadoPorHoras("Ana", 20, 80)
]

for emp in empleados:
    print(f"{emp.nombre}: Pago total = {emp.calcular_pago()}")
