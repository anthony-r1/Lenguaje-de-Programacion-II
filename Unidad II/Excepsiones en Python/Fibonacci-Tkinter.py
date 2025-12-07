import tkinter as tk
from tkinter import scrolledtext
import math

# --- Funciones de Lógica ---

def generar_fibonacci(n, output_widget):
    """
    Genera la serie de Fibonacci y muestra los resultados en el widget de salida.
    """
    # Limpiar y preparar el área de texto
    output_widget.config(state=tk.NORMAL) # Habilitar escritura temporalmente
    output_widget.delete('1.0', tk.END) # Borrar todo el contenido
    output_widget.config(foreground="black") # Resetear color a negro para resultados

    if n <= 0:
        # Aunque ya está validado, este es el mensaje de seguridad de la función.
        output_widget.insert(tk.END, "Error: La cantidad de términos debe ser un número positivo mayor que cero.")
        output_widget.config(foreground="red")
        output_widget.config(state=tk.DISABLED)
        return

    a = 0
    b = 1
    
    output_widget.insert(tk.END, "Serie de Fibonacci:\n")
    
    # Mostrar 0 y 1
    output_widget.insert(tk.END, f"{a}\n")
    if n > 1:
        output_widget.insert(tk.END, f"{b}\n")

    # Generar el resto de los términos
    for i in range(3, n + 1):
        siguiente_termino = a + b
        output_widget.insert(tk.END, f"{siguiente_termino}\n")
        
        a = b
        b = siguiente_termino
        
    output_widget.config(state=tk.DISABLED) # Deshabilitar la edición por el usuario

def ejecutar_generacion():
    """
    Función que se ejecuta al presionar el botón. Maneja la validación y llama a la generación.
    Todos los errores se redirigen al área_resultado con color rojo.
    """
    
    # Resetear el color del texto a rojo para posibles errores
    area_resultado.config(state=tk.NORMAL)
    area_resultado.delete('1.0', tk.END)
    area_resultado.config(foreground="red")
    
    try:
        n_terminos_str = entrada_n.get()
        
        if not n_terminos_str:
            raise ValueError("Por favor, ingrese un valor en el campo.")
            
        n_terminos_float = float(n_terminos_str)
        
        # Validar que sea un entero positivo
        if n_terminos_float != int(n_terminos_float) or n_terminos_float <= 0:
            raise ValueError("Debe ingresar un **número entero positivo** (ej: 10).")
            
        n_terminos = int(n_terminos_float)
        
        # Si todo es correcto, llama a la función de generación (que usa color negro/normal)
        generar_fibonacci(n_terminos, area_resultado)

    except ValueError as ve:
        # Mostrar errores de validación directamente en el ScrolledText
        area_resultado.insert(tk.END, f"Error de Entrada: {str(ve)}")
        area_resultado.config(state=tk.DISABLED)
        
    except Exception as e:
        # Maneja cualquier otro problema inesperado
        area_resultado.insert(tk.END, f"Error Inesperado: Ocurrió un problema - {e}")
        area_resultado.config(state=tk.DISABLED)


# --- Configuración de la Ventana Principal ---

ventana = tk.Tk()
ventana.title("Generador de Serie de Fibonacci")
ventana.geometry("350x450")

# --- Widgets ---

# Entrada N
tk.Label(ventana, text="Cantidad de términos (N):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entrada_n = tk.Entry(ventana, width=20)
entrada_n.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Botón de Generación
boton_generar = tk.Button(ventana, text="Generar Fibonacci", command=ejecutar_generacion, bg="#4CAF50", fg="white")
boton_generar.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew", padx=10)

# Etiqueta de Resultado
tk.Label(ventana, text="Resultado:").grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 0), sticky="w")

# Área de Texto con Scroll (mostrará tanto resultados como errores)
# Nota: La propiedad 'foreground' se modifica en las funciones para cambiar el color del texto.
area_resultado = scrolledtext.ScrolledText(ventana, width=40, height=15, wrap=tk.WORD, state=tk.DISABLED)
area_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="nsew")
area_resultado.config(foreground="black") # Color inicial del texto

# Configuración de Layout para Redimensionamiento
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(3, weight=1)

# Iniciar el bucle principal
ventana.mainloop()
