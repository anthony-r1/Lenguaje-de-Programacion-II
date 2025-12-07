import tkinter as tk
import math
from tkinter import ttk, messagebox

# --- 1. CLASES DE FIGURAS (Polimorfismo) ---
# Las clases permanecen igual, manteniendo la lógica central.
class Figura:
    def area(self):
        raise NotImplementedError

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado**2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * (self.radio**2)

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2
# ---------------------------------------------

# --- 2. CLASE PRINCIPAL DE LA APLICACIÓN TKINTER ---

class AreaCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora y Graficador de Áreas Interactivo")
        master.geometry("600x600")
        master.resizable(False, False)

        # Variables de control para las entradas (DoubleVar asegura que sean números)
        self.lado_var = tk.DoubleVar()
        self.radio_var = tk.DoubleVar()
        self.base_var = tk.DoubleVar()
        self.altura_var = tk.DoubleVar()
        
        # Configuración de Estilos
        style = ttk.Style()
        style.configure("TFrame", background="#f5f5f5")
        style.configure("TLabel", background="#f5f5f5", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10, "bold"))
        
        main_frame = ttk.Frame(master, padding="15")
        main_frame.pack(fill='both', expand=True)

        # --- 1. Controles de Selección ---
        control_frame = ttk.Frame(main_frame, padding="5")
        control_frame.pack(pady=5)

        ttk.Label(control_frame, text="Seleccione la Figura:", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=10)

        opciones_figuras = ["Cuadrado", "Círculo", "Triángulo"]
        self.combo_figuras = ttk.Combobox(control_frame, values=opciones_figuras, state="readonly", width=15)
        self.combo_figuras.set("Seleccione una...")
        # Bind: Ejecuta self.show_inputs cada vez que se selecciona un elemento
        self.combo_figuras.bind("<<ComboboxSelected>>", self.show_inputs) 
        self.combo_figuras.pack(side=tk.LEFT, padx=10)

        # --- 2. Frame Dinámico de Entradas ---
        # Este frame contendrá las entradas específicas de cada figura
        self.input_frame = ttk.Frame(main_frame, padding="10", relief=tk.GROOVE)
        self.input_frame.pack(pady=10)

        # --- 3. Botón y Resultado ---
        self.calculate_button = ttk.Button(main_frame, text="Calcular y Graficar", command=self.calcular_y_graficar_area, state=tk.DISABLED)
        self.calculate_button.pack(pady=10)
        
        self.resultado_label = ttk.Label(main_frame, text="Esperando parámetros...", font=("Arial", 11, "bold"), foreground="#007bff")
        self.resultado_label.pack(pady=5)

        # --- 4. Canvas para Dibujar ---
        self.canvas_dibujo = tk.Canvas(main_frame, width=400, height=300, bg="#ffffff", relief=tk.SUNKEN, bd=2)
        self.canvas_dibujo.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

    def clear_input_frame(self):
        """Limpia el frame de entradas y reinicia el estado."""
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.calculate_button.config(state=tk.DISABLED)
        self.resultado_label.config(text="Esperando parámetros...")
        self.canvas_dibujo.delete("all")

    def create_input_field(self, parent, label_text, entry_var, row, column):
        """Crea una etiqueta y un campo de entrada para un parámetro."""
        ttk.Label(parent, text=label_text).grid(row=row, column=column, padx=5, pady=5, sticky='w')
        entry = ttk.Entry(parent, textvariable=entry_var, width=10)
        entry.grid(row=row, column=column + 1, padx=5, pady=5, sticky='e')
        # Limpiar la variable cada vez que se crea el campo
        entry_var.set(0.0)
        return entry

    def show_inputs(self, event):
        """Muestra automáticamente las entradas correctas para la figura seleccionada."""
        self.clear_input_frame()
        figura_seleccionada = self.combo_figuras.get()
        self.calculate_button.config(state=tk.NORMAL) 

        # Configuración de entradas específicas para cada figura
        if figura_seleccionada == "Cuadrado":
            self.create_input_field(self.input_frame, "Lado:", self.lado_var, 0, 0)
            
        elif figura_seleccionada == "Círculo":
            self.create_input_field(self.input_frame, "Radio:", self.radio_var, 0, 0)
            
        elif figura_seleccionada == "Triángulo":
            self.create_input_field(self.input_frame, "Base:", self.base_var, 0, 0)
            self.create_input_field(self.input_frame, "Altura:", self.altura_var, 1, 0)

    def get_input_values(self, figura_tipo):
        """Obtiene y valida los valores de las entradas dinámicas."""
        try:
            if figura_tipo == "Cuadrado":
                lado = self.lado_var.get()
                if lado <= 0: raise ValueError("El lado debe ser un número positivo.")
                return {'lado': lado}
            
            elif figura_tipo == "Círculo":
                radio = self.radio_var.get()
                if radio <= 0: raise ValueError("El radio debe ser un número positivo.")
                return {'radio': radio}
            
            elif figura_tipo == "Triángulo":
                base = self.base_var.get()
                altura = self.altura_var.get()
                if base <= 0 or altura <= 0: raise ValueError("La base y la altura deben ser números positivos.")
                return {'base': base, 'altura': altura}
            
            return None
        except tk.TclError:
            raise ValueError("Por favor, ingrese un número válido en todos los campos.")


    def calcular_y_graficar_area(self):
        """Lógica de cálculo, validación, actualización del resultado y graficación."""
        figura_seleccionada = self.combo_figuras.get()

        try:
            # 1. Obtener y validar valores
            params = self.get_input_values(figura_seleccionada)
            if not params: return

            # 2. Crear la instancia de la figura (Polimorfismo)
            if figura_seleccionada == "Cuadrado":
                figura_obj = Cuadrado(params['lado'])
            elif figura_seleccionada == "Círculo":
                figura_obj = Circulo(params['radio'])
            elif figura_seleccionada == "Triángulo":
                figura_obj = Triangulo(params['base'], params['altura'])
            else:
                return

            # 3. Calcular área y dibujar
            resultado_area = figura_obj.area()
            self.resultado_label.config(text=f"El Área del {figura_seleccionada} es: {resultado_area:,.2f}", foreground="#007bff")
            self.dibujar_figura(figura_obj, figura_seleccionada)

        except ValueError as e:
            messagebox.showerror("Error de Entrada", str(e))
            self.resultado_label.config(text="Error: Revise los parámetros.", foreground="red")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def dibujar_figura(self, figura_obj, figura_tipo):
        """Dibuja la figura con colores en el Canvas."""
        canvas = self.canvas_dibujo
        canvas.delete("all")
        
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        center_x = canvas_width / 2
        center_y = canvas_height / 2
        max_visual_dim = min(canvas_width, canvas_height) * 0.7 
        
        if figura_tipo == "Cuadrado":
            lado = figura_obj.lado
            scale_factor = max_visual_dim / lado if lado > 0 else 0
            visual_lado = min(lado * scale_factor, max_visual_dim)
            
            x1 = center_x - visual_lado / 2
            y1 = center_y - visual_lado / 2
            x2 = center_x + visual_lado / 2
            y2 = center_y + visual_lado / 2
            
            # Color: Azul
            canvas.create_rectangle(x1, y1, x2, y2, outline="#007bff", width=3, fill="#add8e6")
            
        elif figura_tipo == "Círculo":
            radio = figura_obj.radio
            scale_factor = max_visual_dim / (radio * 2) if radio > 0 else 0
            visual_radio = min(radio * scale_factor, max_visual_dim / 2)
            
            x1 = center_x - visual_radio
            y1 = center_y - visual_radio
            x2 = center_x + visual_radio
            y2 = center_y + visual_radio
            
            # Color: Rojo
            canvas.create_oval(x1, y1, x2, y2, outline="#ff0000", width=3, fill="#ffcccb")
            
        elif figura_tipo == "Triángulo":
            base = figura_obj.base
            altura = figura_obj.altura
            
            max_dim = max(base, altura)
            scale_factor = max_visual_dim / max_dim if max_dim > 0 else 0
            
            # Ajuste visual para que la figura no sea demasiado grande/pequeña
            visual_base = base * scale_factor * 0.5 
            visual_altura = altura * scale_factor * 0.5 

            # Coordenadas: Base centrada
            p1_x = center_x - visual_base / 2
            p1_y = center_y + visual_altura / 2
            p2_x = center_x + visual_base / 2
            p2_y = center_y + visual_altura / 2
            p3_x = center_x
            p3_y = center_y - visual_altura / 2
            
            # Color: Verde
            canvas.create_polygon(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, outline="#28a745", width=3, fill="#90ee90")


def main():
    root = tk.Tk()
    app = AreaCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()