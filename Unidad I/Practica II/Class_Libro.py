class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        print("Objeto Libro creado")

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")

titulo = input("Ingrese el título del libro: ")
autor = input("Ingrese el autor del libro: ")

libro = Libro(titulo, autor)
libro.mostrar_informacion()

del libro
try:
    print(libro)
except NameError:
    print("Objeto libro destruido")
