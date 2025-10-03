class Estadistica:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.numeros = []

    def calcular_promedio(self):
        suma = 0
        for i in range(1, self.cantidad + 1):
            numero = float(input(f"Ingrese el numero {i}: "))
            self.numeros.append(numero)
            suma += numero
        return suma / self.cantidad

    def calcular_varianza(self):
        if not self.numeros or self.cantidad == 0:
            return 0
            
        prom = sum(self.numeros) / self.cantidad
        suma_dif = 0
        for numero in self.numeros:
            suma_dif += (numero - prom) ** 2
        return suma_dif / self.cantidad

    def calcular_varianza2(self):
        if not self.numeros or self.cantidad == 0:
            return 0
            
        suma = sum(self.numeros)
        suma_cuad = 0
        for numero in self.numeros:
            suma_cuad += numero ** 2
            
        return (suma_cuad - (suma ** 2) / self.cantidad) / self.cantidad

    def calcular_desviacion_estandar(self):
        if self.cantidad <= 1:
            return 0
            
        prom = sum(self.numeros) / self.cantidad
        suma_dif = 0
        for numero in self.numeros:
            suma_dif += (numero - prom) ** 2
            
        varianza_muestral = suma_dif / (self.cantidad - 1)
        return varianza_muestral ** 0.5

    def calcular_desviacion_estandar2(self):
        if self.cantidad <= 1:
            return 0
            
        suma = sum(self.numeros)
        suma_cuad = 0
        for numero in self.numeros:
            suma_cuad += numero ** 2
            
        varianza_muestral = (suma_cuad - (suma ** 2) / self.cantidad) / (self.cantidad - 1)
        return varianza_muestral ** 0.5

def main():
    try:
        cantidad = int(input("Ingrese la cantidad de numeros a procesar: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return

        estadistica = Estadistica(cantidad)
        
        # Corrección: Se utiliza la variable 'estadistica' que contiene la instancia.
        promedio = estadistica.calcular_promedio()
        
        varianza1 = estadistica.calcular_varianza()
        varianza2 = estadistica.calcular_varianza2()
        desviacion1 = estadistica.calcular_desviacion_estandar()
        desviacion2 = estadistica.calcular_desviacion_estandar2()

        print("\nLos calculos estadisticos son:")
        print(f"El promedio es: {promedio}")
        print(f"La varianza POBLACIONAL (metodo 1) es: {varianza1}")
        print(f"La varianza POBLACIONAL (metodo 2) es: {varianza2}")
        print(f"La desviacion estandar MUESTRAL (metodo 1) es: {desviacion1}")
        print(f"La desviacion estandar MUESTRAL (metodo 2) es: {desviacion2}")
        
    except ValueError:
        print("Error: Por favor ingrese solo números enteros para la cantidad y números válidos para los datos.")

if __name__ == "__main__":
    main()