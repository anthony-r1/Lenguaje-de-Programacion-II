import tkinter as tk
from tkinter import ttk # Importamos ttk para widgets más modernos
from typing import TypeVar, Generic, Union

# Definición del Tipo Genérico
T = TypeVar('T', int, float)

# Clase Calculadora (sin cambios)
class Calculadora(Generic[T]):
    """Una clase genérica para realizar operaciones aritméticas básicas."""
    def __init__(self, a: T, b: T):
        self.a = a
        self.b = b

    def sumar(self) -> T:
        return self.a + self.b

    def restar(self) -> T:
        return self.a - self.b

    def multiplicar(self) -> T:
        return self.a * self.b

    def dividir(self) -> float:
        if self.b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return self.a / self.b

# Clase principal de la Aplicación Tkinter
class CalculadoraGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Genérica Moderna")
        master.geometry("450x250")
        master.configure(bg='#f0f0f0')

        # Variables de control
        self.a_var = tk.StringVar()
        self.b_var = tk.StringVar()
        self.resultado_var = tk.StringVar(value="Resultado / Errores aquí")
        
        # Usaremos un Frame principal para el padding
        main_frame = ttk.Frame(master, padding="10 10 10 10")
        main_frame.pack(fill='both', expand=True)

        # --- Entrada de Datos ---
        
        # Frame para las entradas
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=0, column=0, columnspan=2, pady=10, sticky='ew')
        
        # Número A
        ttk.Label(input_frame, text="Número A:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        ttk.Entry(input_frame, textvariable=self.a_var, width=15).grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        # Número B
        ttk.Label(input_frame, text="Número B:").grid(row=0, column=2, padx=5, pady=5, sticky='w')
        ttk.Entry(input_frame, textvariable=self.b_var, width=15).grid(row=0, column=3, padx=5, pady=5, sticky='ew')

        # Configurar la expansión de las entradas
        input_frame.grid_columnconfigure(1, weight=1)
        input_frame.grid_columnconfigure(3, weight=1)

        # --- Botones de Operación en una Fila ---
        
        # Frame para los botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Botones de Operación 
        ttk.Button(button_frame, text="Suma (+)", command=lambda: self.ejecutar_operacion(Calculadora.sumar)).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(button_frame, text="Resta (-)", command=lambda: self.ejecutar_operacion(Calculadora.restar)).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(button_frame, text="Multiplicación (x)", command=lambda: self.ejecutar_operacion(Calculadora.multiplicar)).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(button_frame, text="División (/)", command=lambda: self.ejecutar_operacion(Calculadora.dividir)).grid(row=0, column=3, padx=5, pady=5)
        
        # --- Área de Resultado/Error ---
        
        ttk.Label(main_frame, text="Resultados y Mensajes:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        
        # CORRECCIÓN: Usamos ttk.Label en lugar de tk.Label para que el 'padding' sea válido
        self.resultado_label = ttk.Label(main_frame, 
                                        textvariable=self.resultado_var, 
                                        wraplength=400, 
                                        justify=tk.LEFT, 
                                        background='#ffffff', # Opción de color para ttk
                                        foreground='black',   # Opción de color para ttk
                                        borderwidth=2, 
                                        relief="groove", 
                                        padding="8 8 8 8")
        self.resultado_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='ew')
        
        # Configurar la expansión
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

    def obtener_valores(self) -> Union[tuple[int, int], tuple[float, float], None]:
        """Intenta obtener y convertir los valores de entrada, manejando posibles errores."""
        try:
            val_a_str = self.a_var.get().strip()
            val_b_str = self.b_var.get().strip()
            
            # Intentar primero con números enteros
            try:
                a = int(val_a_str)
                b = int(val_b_str)
                return a, b
            except ValueError:
                # Si falla, intentar con números flotantes
                a = float(val_a_str)
                b = float(val_b_str)
                return a, b

        except ValueError:
            # Mostrar error si la conversión a int o float falla
            self.resultado_var.set("❌ Error de entrada: Ambos valores deben ser números válidos (enteros o decimales).")
            self.resultado_label.config(foreground='red') # Usamos foreground para ttk.Label
            return None

    def ejecutar_operacion(self, operacion):
        """Ejecuta la operación de la calculadora y muestra el resultado o error."""
        self.resultado_label.config(foreground='black')
        valores = self.obtener_valores()

        if valores is not None:
            a, b = valores
            try:
                # Crear una instancia de Calculadora
                calc = Calculadora(a, b)
                
                # Ejecutar la operación
                resultado = operacion(calc)

                # Mostrar el resultado con un emoji
                self.resultado_var.set(f"✅ Resultado: {resultado}")
                self.resultado_label.config(foreground='green')

            except ZeroDivisionError as e:
                # Mostrar error de división por cero
                self.resultado_var.set(f"⚠️ Error aritmético: {e}")
                self.resultado_label.config(foreground='darkorange')
            
            except Exception as e:
                # Mostrar cualquier otro error inesperado
                self.resultado_var.set(f"❌ Error inesperado: {e}")
                self.resultado_label.config(foreground='red')

# --- Ejecución de la Aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()
