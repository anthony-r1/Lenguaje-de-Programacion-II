import tkinter as tk
from tkinter import messagebox

class Estadistica:
    """Clase para manejar los cálculos estadísticos."""
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.numeros = []

    # Las funciones de cálculo se mantienen igual
    def calcular_promedio(self):
        if not self.numeros or self.cantidad == 0:
            return 0
        return sum(self.numeros) / self.cantidad

    def calcular_varianza(self):
        if not self.numeros or self.cantidad == 0:
            return 0
            
        prom = self.calcular_promedio()
        suma_dif = sum([(numero - prom) ** 2 for numero in self.numeros])
        return suma_dif / self.cantidad

    def calcular_varianza2(self):
        if not self.numeros or self.cantidad == 0:
            return 0
            
        suma = sum(self.numeros)
        suma_cuad = sum([numero ** 2 for numero in self.numeros])
            
        return (suma_cuad - (suma ** 2) / self.cantidad) / self.cantidad

    def calcular_desviacion_estandar(self):
        if self.cantidad <= 1:
            return 0
            
        prom = self.calcular_promedio()
        suma_dif = sum([(numero - prom) ** 2 for numero in self.numeros])
            
        varianza_muestral = suma_dif / (self.cantidad - 1)
        return varianza_muestral ** 0.5

    def calcular_desviacion_estandar2(self):
        if self.cantidad <= 1:
            return 0
            
        suma = sum(self.numeros)
        suma_cuad = sum([numero ** 2 for numero in self.numeros])
            
        varianza_muestral = (suma_cuad - (suma ** 2) / self.cantidad) / (self.cantidad - 1)
        return varianza_muestral ** 0.5


class InterfazEstadistica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Estadística")
        self.geometry("450x550")
        
        # Variables de estado
        self.cantidad_var = tk.StringVar()
        self.numero_actual_var = tk.StringVar()
        self.resultados_text = tk.StringVar(value="Esperando datos...")
        self.numeros_ingresados = []
        self.cantidad = 0
        self.indice_actual = 0
        
        self.estadistica = None
        
        # Configuración de la interfaz (Etapas)
        self.crear_widgets_cantidad()

## --- Creación de Widgets --- ##

    def crear_widgets_cantidad(self):
        """Paso 1: Solicitar la cantidad de números."""
        
        # Limpiar widgets anteriores
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Paso 1: Ingrese la cantidad de números:", font=('Arial', 12)).pack(pady=10)
        
        tk.Entry(self, textvariable=self.cantidad_var, width=15, justify='center').pack(pady=5)
        
        tk.Button(self, text="Continuar", command=self.procesar_cantidad, bg='lightblue').pack(pady=10)

## --- Funciones de Lógica --- ##

    def procesar_cantidad(self):
        """Valida la cantidad y pasa a la etapa de ingreso de números."""
        try:
            cantidad = int(self.cantidad_var.get())
            if cantidad <= 0:
                messagebox.showerror("Error de entrada", "La cantidad debe ser un número positivo.")
                return

            self.cantidad = cantidad
            self.numeros_ingresados = []
            self.indice_actual = 1
            self.estadistica = Estadistica(cantidad)
            
            # Pasar a la siguiente etapa de la GUI
            self.crear_widgets_numeros()
            
        except ValueError:
            messagebox.showerror("Error de entrada", "Por favor, ingrese un número entero válido para la cantidad.")

    def crear_widgets_numeros(self):
        """Paso 2: Solicitar la entrada de cada número."""
        
        # Limpiar widgets anteriores
        for widget in self.winfo_children():
            widget.destroy()
            
        tk.Label(self, text="Paso 2: Ingrese los números", font=('Arial', 12, 'bold')).pack(pady=10)
        
        self.label_instruccion = tk.Label(self, text=f"Ingrese el número {self.indice_actual} de {self.cantidad}:", font=('Arial', 11))
        self.label_instruccion.pack(pady=5)
        
        self.entry_numero = tk.Entry(self, textvariable=self.numero_actual_var, width=15, justify='center')
        self.entry_numero.pack(pady=5)
        self.entry_numero.focus_set() # Pone el cursor en la caja de texto

        tk.Button(self, text="Ingresar Número", command=self.ingresar_numero, bg='lightgreen').pack(pady=10)

    def ingresar_numero(self):
        """Procesa el número ingresado."""
        try:
            numero = float(self.numero_actual_var.get())
            self.numeros_ingresados.append(numero)
            self.numero_actual_var.set("") # Limpiar la caja de texto
            
            if self.indice_actual < self.cantidad:
                self.indice_actual += 1
                self.label_instruccion.config(text=f"Ingrese el número {self.indice_actual} de {self.cantidad}:")
                self.entry_numero.focus_set()
            else:
                # Todos los números han sido ingresados
                self.estadistica.numeros = self.numeros_ingresados
                self.mostrar_resultados()
                
        except ValueError:
            messagebox.showerror("Error de entrada", "Por favor, ingrese un número válido (entero o decimal).")

    def mostrar_resultados(self):
        """Paso 3: Muestra todos los cálculos estadísticos."""
        
        # Limpiar widgets anteriores
        for widget in self.winfo_children():
            widget.destroy()
            
        self.resultados_text.set("Calculando...")

        # Realizar todos los cálculos
        promedio = self.estadistica.calcular_promedio()
        varianza1 = self.estadistica.calcular_varianza()
        varianza2 = self.estadistica.calcular_varianza2()
        desviacion1 = self.estadistica.calcular_desviacion_estandar()
        desviacion2 = self.estadistica.calcular_desviacion_estandar2()

        # Construir el texto de resultados
        resultado = f"""
        Resultados Estadísticos:
        
        Promedio: {promedio:.4f}

        Varianza POBLACIONAL (M1): {varianza1:.4f}
        Varianza POBLACIONAL (M2): {varianza2:.4f}

        Desv. Estándar MUESTRAL (M1): {desviacion1:.4f}
        Desv. Estándar MUESTRAL (M2): {desviacion2:.4f}
        
        Números ingresados: {self.numeros_ingresados}
        """
        
        self.resultados_text.set(resultado)
        
        tk.Label(self, text="Resultados", font=('Arial', 14, 'bold'), fg='blue').pack(pady=10)
        
        tk.Label(self, textvariable=self.resultados_text, justify=tk.LEFT, font=('Courier', 10)).pack(padx=20, pady=10)
        
        tk.Button(self, text="Reiniciar", command=self.crear_widgets_cantidad, bg='salmon').pack(pady=20)


if __name__ == "__main__":
    app = InterfazEstadistica()
    app.mainloop()