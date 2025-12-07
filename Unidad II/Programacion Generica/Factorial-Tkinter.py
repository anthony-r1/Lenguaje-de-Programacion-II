import tkinter as tk
from tkinter import messagebox # Se mantiene por si quieres usarlo, pero no es necesario para el error en la etiqueta
from typing import TypeVar, Generic

T = TypeVar('T', int, float)

class CalculadoraFactorial(Generic[T]):
    def __init__(self, numero: T):
        self.numero = numero

    def calcular_factorial(self) -> int:
        n = int(self.numero)
        if n < 0:
            # Ahora, solo lanza la excepción. El manejo del error es tarea de la función de la interfaz.
            raise ValueError("El factorial no está definido para números negativos.")
        
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
            
        return resultado

# --- Implementación de Tkinter Modificada ---

def calcular_y_mostrar_factorial():
    """Obtiene el número, calcula el factorial y actualiza la etiqueta de resultado/error."""
    try:
        # Obtener y validar el número
        numero_str = entry_numero.get()
        n = int(numero_str)
        
        # Crear una instancia y calcular
        calculadora = CalculadoraFactorial(n)
        resultado_factorial = calculadora.calcular_factorial()
        
        # **Éxito: Muestra el resultado**
        label_resultado.config(text=f"El Factorial de {n} es: {resultado_factorial}", fg="green")
        
    except ValueError as e:
        # **Error 1: Muestra el error de ValueError en la etiqueta**
        # Esto atrapa tanto entradas no numéricas (por int()) como números negativos (por raise ValueError)
        label_resultado.config(text=f"Error: {str(e)}", fg="red")
        
    except Exception as e:
        # **Error 2: Muestra cualquier otro error inesperado**
        label_resultado.config(text="Error inesperado. Verifique la entrada.", fg="red")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Factorial")
ventana.geometry("400x200") 

# Crear widgets
label_instruccion = tk.Label(ventana, text="Ingrese un número entero:")
label_instruccion.pack(pady=10) 

entry_numero = tk.Entry(ventana, width=30)
entry_numero.pack(pady=5)

boton_calcular = tk.Button(ventana, text="Calcular Factorial", command=calcular_y_mostrar_factorial)
boton_calcular.pack(pady=10)

# Label para el resultado/error. Inicialmente en negro.
label_resultado = tk.Label(ventana, text="Esperando número...", fg="black")
label_resultado.pack(pady=10)

# Iniciar el bucle principal
ventana.mainloop()
