class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def AplicarAumento(self):
        if self.cargo == "Gerente":
            porcentaje = 0.10
        elif self.cargo == "Supervisor":
            porcentaje = 0.07
        elif self.cargo == "Operario":
            porcentaje = 0.05
        else:
            porcentaje = 0.0

        nuevoSalario = self.salario * (1 + porcentaje)
        return nuevoSalario

empleado1 = Empleado("Carlos", "Gerente", 2000)
empleado2 = Empleado("Maria", "Supervisor", 2000)
empleado3 = Empleado("Ana", "Interna", 800)
empleado4 = Empleado("Roberto", "Operario", 1600)

for emp in (empleado1, empleado2, empleado3, empleado4):
    nuevo = emp.AplicarAumento()
    print(f"{emp.nombre} {emp.cargo}: salario nuevo {nuevo:2f}")