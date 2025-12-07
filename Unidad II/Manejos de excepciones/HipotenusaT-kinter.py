import tkinter as tk
import math

def calcular_hipotenusa(cateto_a, cateto_b):
    """Calcula la hipotenusa usando el teorema de Pitágoras."""
    return math.sqrt(cateto_a**2 + cateto_b**2)

def calcular_y_mostrar():
    """
    Función que se ejecuta al presionar el botón.
    Maneja el cálculo y muestra el resultado o el error en la etiqueta.
    """
    try:
        # 1. Obtener los valores de los campos de entrada
        # Se usa .get() para recuperar el texto del Entry
        cateto_a = float(entrada_a.get())
        cateto_b = float(entrada_b.get())

        # 2. Validar que los valores sean positivos
        if cateto_a <= 0 or cateto_b <= 0:
            # Si hay error, actualiza la etiqueta con el mensaje de error y color rojo
            resultado_var.set("Error: Los catetos deben ser números positivos.")
            etiqueta_resultado.config(fg="red")
            return # Detiene la ejecución de la función

        # 3. Calcular la hipotenusa
        hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)

        # 4. Mostrar el resultado (éxito)
        resultado_var.set(f"La hipotenusa es: {hipotenusa:.2f}")
        etiqueta_resultado.config(fg="green") # Color para éxito (opcional)

    except ValueError:
        # Maneja errores si el usuario no ingresó un número válido (ej: texto vacío o letras)
        resultado_var.set("Error: Ingrese valores numéricos válidos en ambos campos.")
        etiqueta_resultado.config(fg="red")

    except Exception as e:
        # Maneja cualquier otro problema inesperado
        resultado_var.set(f"Error inesperado: {e}")
        etiqueta_resultado.config(fg="red")


# --- Configuración de la ventana principal ---

ventana = tk.Tk()
ventana.title("Calculadora de Hipotenusa")
ventana.geometry("350x200")

# --- Variables de control ---

resultado_var = tk.StringVar()
resultado_var.set("Ingrese los valores de los catetos.")

# --- Widgets ---

# 1. Cateto A
tk.Label(ventana, text="Cateto A:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entrada_a = tk.Entry(ventana, width=20)
entrada_a.grid(row=0, column=1, padx=10, pady=5)

# 2. Cateto B
tk.Label(ventana, text="Cateto B:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entrada_b = tk.Entry(ventana, width=20)
entrada_b.grid(row=1, column=1, padx=10, pady=5)

# 3. Botón de Cálculo
boton_calcular = tk.Button(ventana, text="Calcular Hipotenusa", command=calcular_y_mostrar, bg="#007bff", fg="white")
boton_calcular.grid(row=2, column=0, columnspan=2, pady=10)

# 4. Etiqueta de Resultado (Ahora muestra Éxito o Error)
# Se guarda la referencia en una variable para poder cambiar su color
etiqueta_resultado = tk.Label(ventana, textvariable=resultado_var, font=("Helvetica", 10, "bold"), fg="black")
etiqueta_resultado.grid(row=3, column=0, columnspan=2, pady=5)

# 5. Configuración de centrado
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# Iniciar el bucle principal
ventana.mainloop()
