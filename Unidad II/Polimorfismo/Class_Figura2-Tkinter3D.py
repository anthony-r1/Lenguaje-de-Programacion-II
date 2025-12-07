import tkinter as tk
import math
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d.art3d import Poly3DCollection # Para las caras de polígonos
import numpy as np

# --- 1. CLASES DE FIGURAS 3D (Polimorfismo para Volumen) ---
class Figura:
    def area(self):
        raise NotImplementedError
    def volumen(self):
        raise NotImplementedError
    def get_params(self):
        raise NotImplementedError

class Cubo(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado**2
    def volumen(self):
        return self.lado**3
    def get_params(self):
        return {'lado': self.lado}

class Cilindro(Figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
    def area(self):
        return math.pi * (self.radio**2)
    def volumen(self):
        return math.pi * (self.radio**2) * self.altura
    def get_params(self):
        return {'radio': self.radio, 'altura': self.altura}

class PrismaTriangular(Figura):
    def __init__(self, base_tri, altura_tri, profundidad):
        self.base_tri = base_tri
        self.altura_tri = altura_tri
        self.profundidad = profundidad
    def area(self):
        return (self.base_tri * self.altura_tri) / 2
    def volumen(self):
        return self.area() * self.profundidad
    def get_params(self):
        return {'base': self.base_tri, 'altura': self.altura_tri, 'profundidad': self.profundidad}
# ---------------------------------------------

# --- 2. CLASE PRINCIPAL DE LA APLICACIÓN TKINTER ---

class AreaCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora y Graficador 3D de Volúmenes")
        master.geometry("800x700")
        master.resizable(False, False)

        self.lado_var = tk.DoubleVar()
        self.radio_var = tk.DoubleVar()
        self.base_var = tk.DoubleVar()
        self.altura_var = tk.DoubleVar()
        self.profundidad_var = tk.DoubleVar()

        style = ttk.Style()
        style.configure("TFrame", background="#f5f5f5")
        style.configure("TLabel", background="#f5f5f5", font=("Arial", 10))
        
        main_frame = ttk.Frame(master, padding="15")
        main_frame.pack(fill='both', expand=True)

        control_frame = ttk.Frame(main_frame, padding="5")
        control_frame.pack(pady=5)

        ttk.Label(control_frame, text="Figura 3D:", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=10)

        opciones_figuras = ["Cubo", "Cilindro", "Prisma Triangular"]
        self.combo_figuras = ttk.Combobox(control_frame, values=opciones_figuras, state="readonly", width=20)
        self.combo_figuras.set("Seleccione una...")
        self.combo_figuras.bind("<<ComboboxSelected>>", self.show_inputs) 
        self.combo_figuras.pack(side=tk.LEFT, padx=10)

        self.input_frame = ttk.Frame(main_frame, padding="10", relief=tk.GROOVE)
        self.input_frame.pack(pady=10)

        self.calculate_button = ttk.Button(main_frame, text="Calcular y Graficar Volumen (3D)", command=self.calcular_y_graficar_volumen, state=tk.DISABLED)
        self.calculate_button.pack(pady=10)
        
        self.resultado_label = ttk.Label(main_frame, text="Esperando parámetros...", font=("Arial", 11, "bold"), foreground="#007bff")
        self.resultado_label.pack(pady=5)

        # Configuración del Matplotlib Frame y Canvas
        self.fig = plt.figure(figsize=(6, 5))
        # Es importante crear el subplot 3D en el inicio
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=main_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

        self.clear_input_frame()
        self.ax.set_axis_off() # Ocultar ejes al inicio
        self.canvas.draw() # Dibujar un canvas vacío al inicio para evitar errores de render

    def clear_input_frame(self):
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.calculate_button.config(state=tk.DISABLED)
        self.resultado_label.config(text="Esperando parámetros...")
        
        # Limpiar y reiniciar los ejes 3D
        self.ax.clear()
        self.ax.set_axis_off()
        self.ax.set_title("Gráfico 3D de la Figura")
        self.canvas.draw()

    def create_input_field(self, parent, label_text, entry_var, row, column):
        ttk.Label(parent, text=label_text).grid(row=row, column=column, padx=5, pady=5, sticky='w')
        entry = ttk.Entry(parent, textvariable=entry_var, width=10)
        entry.grid(row=row, column=column + 1, padx=5, pady=5, sticky='e')
        entry_var.set(1.0)
        return entry

    def show_inputs(self, event):
        self.clear_input_frame()
        figura_seleccionada = self.combo_figuras.get()
        self.calculate_button.config(state=tk.NORMAL) 

        if figura_seleccionada == "Cubo":
            self.create_input_field(self.input_frame, "Lado:", self.lado_var, 0, 0)
            
        elif figura_seleccionada == "Cilindro":
            self.create_input_field(self.input_frame, "Radio:", self.radio_var, 0, 0)
            self.create_input_field(self.input_frame, "Altura:", self.altura_var, 1, 0)
            
        elif figura_seleccionada == "Prisma Triangular":
            self.create_input_field(self.input_frame, "Base Triángulo:", self.base_var, 0, 0)
            self.create_input_field(self.input_frame, "Altura Triángulo:", self.altura_var, 1, 0)
            self.create_input_field(self.input_frame, "Profundidad (Z):", self.profundidad_var, 2, 0)

    def get_input_values(self, figura_tipo):
        try:
            if figura_tipo == "Cubo":
                lado = self.lado_var.get()
                if lado <= 0: raise ValueError("El lado debe ser positivo.")
                return {'lado': lado}
            
            elif figura_tipo == "Cilindro":
                radio = self.radio_var.get()
                altura = self.altura_var.get()
                if radio <= 0 or altura <= 0: raise ValueError("Radio y altura deben ser positivos.")
                return {'radio': radio, 'altura': altura}
            
            elif figura_tipo == "Prisma Triangular":
                base = self.base_var.get()
                altura = self.altura_var.get()
                profundidad = self.profundidad_var.get()
                if base <= 0 or altura <= 0 or profundidad <= 0: raise ValueError("Todos los valores deben ser positivos.")
                return {'base_tri': base, 'altura_tri': altura, 'profundidad': profundidad}
            
            return None
        except tk.TclError:
            raise ValueError("Por favor, ingrese un número válido en todos los campos.")


    def calcular_y_graficar_volumen(self):
        figura_seleccionada = self.combo_figuras.get()

        try:
            params = self.get_input_values(figura_seleccionada)
            if not params: return

            if figura_seleccionada == "Cubo":
                figura_obj = Cubo(params['lado'])
            elif figura_seleccionada == "Cilindro":
                figura_obj = Cilindro(params['radio'], params['altura'])
            elif figura_seleccionada == "Prisma Triangular":
                figura_obj = PrismaTriangular(params['base_tri'], params['altura_tri'], params['profundidad'])
            else:
                return

            resultado_volumen = figura_obj.volumen()
            self.resultado_label.config(text=f"El Volumen del {figura_seleccionada} es: {resultado_volumen:,.2f}", foreground="#007bff")
            self.dibujar_figura_3d(figura_obj, figura_seleccionada)

        except ValueError as e:
            messagebox.showerror("Error de Entrada", str(e))
            self.resultado_label.config(text="Error: Revise los parámetros.", foreground="red")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    # --- Métodos de Dibujo 3D (Matplotlib) ---

    def _setup_3d_axes(self, limits):
        self.ax.clear()
        self.ax.set_axis_on() # Mostrar ejes de nuevo
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        
        max_limit_val = max(limits) * 1.2 # Añadir un poco de padding
        min_limit_val = -max_limit_val
        
        self.ax.set_xlim(min_limit_val, max_limit_val)
        self.ax.set_ylim(min_limit_val, max_limit_val)
        self.ax.set_zlim(min_limit_val, max_limit_val)
        
        self.ax.set_box_aspect([1, 1, 1]) # Proporciones iguales
        self.ax.set_title("Gráfico 3D de la Figura") # Título genérico o específico después


    def dibujar_figura_3d(self, figura_obj, figura_tipo):
        if figura_tipo == "Cubo":
            self._draw_cubo(figura_obj)
        elif figura_tipo == "Cilindro":
            self._draw_cilindro(figura_obj)
        elif figura_tipo == "Prisma Triangular":
            self._draw_prisma_triangular(figura_obj)
            
        self.canvas.draw()


    def _draw_cubo(self, figura_obj):
        l = figura_obj.lado / 2 # Mitad del lado para centrar
        limits = [figura_obj.lado, figura_obj.lado, figura_obj.lado] # Usamos el lado para los límites
        self._setup_3d_axes(limits)
        
        # 8 Vértices del cubo
        v = np.array([
            [-l, -l, -l], [l, -l, -l], [l, l, -l], [-l, l, -l],
            [-l, -l, l], [l, -l, l], [l, l, l], [-l, l, l]
        ])

        # Las 6 caras del cubo, cada una definida por 4 vértices (índices en 'v')
        faces = [
            [v[0], v[1], v[2], v[3]], # Bottom
            [v[4], v[5], v[6], v[7]], # Top
            [v[0], v[1], v[5], v[4]], # Front
            [v[2], v[3], v[7], v[6]], # Back
            [v[1], v[2], v[6], v[5]], # Right
            [v[3], v[0], v[4], v[7]]  # Left
        ]
        
        collection = Poly3DCollection(faces, linewidths=1, edgecolors='b', alpha=.5)
        collection.set_facecolor('#add8e6') # Color azul claro
        self.ax.add_collection3d(collection)
        
        self.ax.set_title(f"Cubo (Lado={figura_obj.lado})")


    def _draw_cilindro(self, figura_obj):
        r = figura_obj.radio
        h = figura_obj.altura
        limits = [r * 2, r * 2, h] # Ancho, profundidad, altura
        self._setup_3d_axes(limits)

        # Superficie lateral del cilindro
        z = np.linspace(-h/2, h/2, 50)
        theta = np.linspace(0, 2 * np.pi, 50)
        theta_grid, z_grid = np.meshgrid(theta, z)
        
        x_grid = r * np.cos(theta_grid)
        y_grid = r * np.sin(theta_grid)
        
        self.ax.plot_surface(x_grid, y_grid, z_grid, color='r', alpha=0.6, rstride=5, cstride=5)
        
        # Tapas (discos)
        # Dibujar discos superiores e inferiores como Poly3DCollection
        disk_points = np.array([[r * math.cos(t), r * math.sin(t), h/2] for t in np.linspace(0, 2 * np.pi, 30)])
        self.ax.add_collection3d(Poly3DCollection([disk_points], facecolors='#ffcccb', linewidths=0, alpha=0.8))

        disk_points_bottom = np.array([[r * math.cos(t), r * math.sin(t), -h/2] for t in np.linspace(0, 2 * np.pi, 30)])
        self.ax.add_collection3d(Poly3DCollection([disk_points_bottom], facecolors='#ffcccb', linewidths=0, alpha=0.8))

        self.ax.set_title(f"Cilindro (R={figura_obj.radio}, H={figura_obj.altura})")

    def _draw_prisma_triangular(self, figura_obj):
        b = figura_obj.base_tri
        h_tri = figura_obj.altura_tri
        d = figura_obj.profundidad # Usar directamente para z-axis
        
        limits = [b, h_tri, d]
        self._setup_3d_axes(limits)

        # 6 Vértices del prisma triangular (centrado en (0,0,0) en XY, y en Z)
        # Base triangular inferior (z = -d/2)
        v1 = (-b/2, -h_tri/2, -d/2)
        v2 = (b/2, -h_tri/2, -d/2)
        v3 = (0, h_tri/2, -d/2)

        # Base triangular superior (z = d/2)
        v4 = (-b/2, -h_tri/2, d/2)
        v5 = (b/2, -h_tri/2, d/2)
        v6 = (0, h_tri/2, d/2)
        
        v = np.array([v1, v2, v3, v4, v5, v6])

        # 5 Caras del prisma (2 triángulos, 3 rectángulos)
        faces = [
            [v[0],v[1],v[2]],  # Base inferior
            [v[3],v[4],v[5]],  # Base superior
            [v[0],v[1],v[4],v[3]], # Cara lateral 1
            [v[1],v[2],v[5],v[4]], # Cara lateral 2
            [v[2],v[0],v[3],v[5]]  # Cara lateral 3
        ]
        
        collection = Poly3DCollection(faces, linewidths=1, edgecolors='g', alpha=.5)
        collection.set_facecolor('#90ee90') # Color verde claro
        self.ax.add_collection3d(collection)
        
        self.ax.set_title(f"Prisma Triangular (B={b}, H_tri={h_tri}, P={d})")

def main():
    root = tk.Tk()
    app = AreaCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()