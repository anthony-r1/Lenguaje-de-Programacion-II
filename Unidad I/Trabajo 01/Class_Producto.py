class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio if precio > 0 else 1.0
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("Error: El precio debe ser mayor a 0455.")
    
    def mostrar_producto(self):
        print(f"Producto: {self.__nombre}")
        print(f"Precio: S/. {self.__precio:.2f}")

if __name__ == "__main__":
    producto1 = Producto("Laptop", 2500.00)
    producto1.mostrar_producto()
    producto1.precio = 3000.00
    producto1.mostrar_producto()
    producto1.precio = -500