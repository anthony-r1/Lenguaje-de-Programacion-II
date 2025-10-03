class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:")
            for i, tarea in enumerate(self.tareas, start=1):
                print(f"{i}.- {tarea}")

def main():
    gestor = GestorTareas()
    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            tarea = input("Ingrese la descripción de la tarea: ")
            gestor.agregar_tarea(tarea)
        elif opcion == '2':
            gestor.mostrar_tareas()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()