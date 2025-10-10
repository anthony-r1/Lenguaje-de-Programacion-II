import gc
class Producto:
    def __init__(self,nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        print(f"Producto {self.nombre} registrado | precio: {self.precio} | cantidad: {self.cantidad}")

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"

    def __del__(self):
        print(f"El producto {self.nombre} ha sido eliminado")

productos_datos = [
    ("Laptop", 1200, 5),
    ("Smartphone", 800, 10),
    ("Tablet", 600, 7),
    ("Monitor", 300, 3)
]

inventario = []

for datos in productos_datos:
    producto = Producto(*datos)
    producto.mostrar_info()
    inventario.append(producto)

inventario.clear()
del producto
gc.collect()
print("Todos los productos han sido eliminados")