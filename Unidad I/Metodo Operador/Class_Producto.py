class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def __str__(self):
        return f"{self.nombre} - S/.{self.precio:.2f} Stock: {self.stock}"

    def __eq__(self, otra):
        return self.nombre == otra.nombre

    def __gt__(self, otra):
        return self.precio > otra.precio

    def __add__(self, otra):
        return self.precio + otra.precio

producto1 = Producto("Arroz", 3.50,20)
producto2 = Producto("Arroz",3.50,15)
producto3 = Producto("Azucar", 4.00,10)

print(producto1)
print(producto2)
print(producto3)

print(producto1 == producto2)
print(producto2 == producto3)
print(producto1 + producto2)
print(producto1 + producto3)
