class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            print("El precio no puede ser negativo.")
        else:
            self._precio = valor

    def aplicar_descuento(self, porcentaje):
        if 0 < porcentaje <= 100:
            descuento = self._precio * (porcentaje / 100)
            self._precio -= descuento
        else:
            print("Porcentaje inválido.")

p = Producto("Laptop", 1000)
p.precio = -50 
print(f"Precio actual: {p.precio}")

p.aplicar_descuento(10) 
print(f"Precio con descuento: {p.precio}")

p.aplicar_descuento(200) 
