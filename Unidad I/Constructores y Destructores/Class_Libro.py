import gc
class Libro:
    def __init__(self,titulo,autor,anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f"Libro '{self.titulo}' registrado | Autor: {self.autor} | Año: {self.anio}")

    def mostrar_info(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"

    def __del__(self):
        print(f"El libro '{self.titulo}' ha sido eliminado")

libro_datos = [("Cien Años de Soledad", "Gabriel García Márquez", 1967),
            ("Don Quijote de la Mancha", "Miguel de Cervantes", 1605),
            ("La Sombra del Viento", "Carlos Ruiz Zafón", 2001),
            ("1984", "George Orwell", 1949),]

biblioteca = []

for datos in libro_datos:
    libro = Libro(*datos)
    libro.mostrar_info()
    biblioteca.append(libro)

biblioteca.clear()
del libro
gc.collect()
print("Todos los libros han sido eliminados")