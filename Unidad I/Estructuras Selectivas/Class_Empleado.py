class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    def AplicarAumento(self):
        if self.cargo == "Gerente":
            porcentaje = 0.10
        elif self.cargo == "Supervisor":
            porcentaje = 0.07
        elif self.cargo == "Operario":
            porcentaje = 0.05
        else:
            porcentaje = 0.00

        nuevoSalario = self.salario * (1 + porcentaje)
        return nuevoSalario

Empleado1 = Empleado("Juan", "Gerente", 2000)
Empleado2 = Empleado("Ana", "Supervisor", 1500)
Empleado3 = Empleado("Luis", "Interno", 1000)
Empleado4 = Empleado("Maria", "Operario", 1200)

for empleado in [Empleado1, Empleado2, Empleado3, Empleado4]:
    nuevoSalario = empleado.AplicarAumento()
    print(f"El nuevo salario de {empleado.nombre} ({empleado.apellido}) es: {nuevoSalario:.2f}")