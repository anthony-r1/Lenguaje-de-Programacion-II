import tkinter as tk
from tkinter import ttk
import math
import random
from typing import TypeVar, Generic, Union

# ==========================================
# 1. LÓGICA MATEMÁTICA (Tus clases)
# ==========================================

T = TypeVar('T', int, float)

class FiguraGeometrica(Generic[T]):
    def area(self) -> float:
        raise NotImplementedError
    def perimetro(self) -> float:
        raise NotImplementedError

class Rectangulo(FiguraGeometrica[T]):
    def __init__(self, base: T, altura: T):
        self.base = base
        self.altura = altura
    def area(self) -> T:
        return self.base * self.altura
    def perimetro(self) -> T:
        return 2 * (self.base + self.altura)

class Circulo(FiguraGeometrica[T]):
    def __init__(self, radio: T):
        self.radio = radio
    def area(self) -> float:
        if self.radio < 0: raise ValueError("Radio negativo")
        return math.pi * (self.radio ** 2)
    def perimetro(self) -> float:
        if self.radio < 0: raise ValueError("Radio negativo")
        return 2 * math.pi * self.radio

# ==========================================
# 2. INTERFAZ GRÁFICA "PRIMARIA"
# ==========================================

class GeometriaVisualGUI:
    def __init__(self, master):
        self.master = master
        master.title("🎨 Geometría Divertida")
        master.geometry("600x550")
        master.configure(bg='#FFF8E1') # Fondo crema suave

        # Variables
        self.base_var = tk.StringVar()
        self.altura_var = tk.StringVar()
        self.radio_var = tk.StringVar()
        self.resultado_var = tk.StringVar(value="¡Elige una figura y a pintar!")

        # Paleta de colores "Primaria"
        self.colores = ['#FF6B6B', '#4ECDC4', '#FFD166', '#06D6A0', '#118AB2', '#EF476F', '#9D4EDD']

        # --- Título ---
        lbl_titulo = tk.Label(master, text="✨ Aprendiendo Figuras ✨", 
                              font=('Comic Sans MS', 16, 'bold'), 
                              bg='#FFF8E1', fg='#FF6B6B')
        lbl_titulo.pack(pady=10)

        # --- Pestañas ---
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(pady=5, padx=20, expand=False, fill='x')

        # Pestaña Rectángulo
        self.frame_rect = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.frame_rect, text=' 🟦 Rectángulo ')
        self.setup_rectangulo_tab()

        # Pestaña Círculo
        self.frame_circ = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.frame_circ, text=' 🔴 Círculo ')
        self.setup_circulo_tab()

        # --- Área de Dibujo (CANVAS) ---
        # Aquí es donde ocurre la magia visual
        self.canvas_frame = tk.Frame(master, bg='white', bd=5, relief="ridge")
        self.canvas_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        self.canvas = tk.Canvas(self.canvas_frame, bg="white", highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        # --- Etiqueta de Resultado ---
        self.lbl_resultado = tk.Label(master, textvariable=self.resultado_var,
                                      font=('Verdana', 10, 'bold'), 
                                      bg='#FFF8E1', fg='#333')
        self.lbl_resultado.pack(pady=10)

    def setup_rectangulo_tab(self):
        # Entradas
        f_inputs = tk.Frame(self.frame_rect)
        f_inputs.pack()
        
        tk.Label(f_inputs, text="Base:").grid(row=0, column=0, padx=5)
        tk.Entry(f_inputs, textvariable=self.base_var, width=10).grid(row=0, column=1, padx=5)
        
        tk.Label(f_inputs, text="Altura:").grid(row=0, column=2, padx=5)
        tk.Entry(f_inputs, textvariable=self.altura_var, width=10).grid(row=0, column=3, padx=5)

        # Botones
        tk.Button(self.frame_rect, text="🎨 Calcular y Dibujar", bg="#4ECDC4", fg="white", font=('Arial', 10, 'bold'),
                  command=lambda: self.procesar_rectangulo()).pack(pady=10)

    def setup_circulo_tab(self):
        # Entradas
        f_inputs = tk.Frame(self.frame_circ)
        f_inputs.pack()
        
        tk.Label(f_inputs, text="Radio:").grid(row=0, column=0, padx=5)
        tk.Entry(f_inputs, textvariable=self.radio_var, width=10).grid(row=0, column=1, padx=5)

        # Botones
        tk.Button(self.frame_circ, text="🎨 Calcular y Dibujar", bg="#FF6B6B", fg="white", font=('Arial', 10, 'bold'),
                  command=lambda: self.procesar_circulo()).pack(pady=10)

    # --- Lógica de Dibujo Inteligente ---
    def dibujar_figura(self, tipo, dimension_1, dimension_2=0):
        self.canvas.delete("all") # Borrar dibujo anterior
        
        # Obtener tamaño actual del canvas
        w_canvas = self.canvas.winfo_width()
        h_canvas = self.canvas.winfo_height()
        cx, cy = w_canvas / 2, h_canvas / 2 # Centro
        
        color_relleno = random.choice(self.colores) # Color sorpresa

        if tipo == "rect":
            base, altura = dimension_1, dimension_2
            
            # Algoritmo de escalado:
            # Calculamos qué tan grande es la figura respecto al canvas
            # y creamos un factor de zoom para que siempre quepa
            margen = 40
            factor_w = (w_canvas - margen) / base if base > 0 else 1
            factor_h = (h_canvas - margen) / altura if altura > 0 else 1
            zoom = min(factor_w, factor_h) # Usamos el menor para que quepa todo
            
            # Dimensiones visuales
            viz_w = base * zoom
            viz_h = altura * zoom
            
            # Dibujar Rectángulo centrado
            self.canvas.create_rectangle(cx - viz_w/2, cy - viz_h/2,
                                         cx + viz_w/2, cy + viz_h/2,
                                         fill=color_relleno, outline="black", width=3)
            
            # Poner texto de medidas
            self.canvas.create_text(cx, cy + viz_h/2 + 15, text=f"Base: {base}", fill="blue")
            self.canvas.create_text(cx + viz_w/2 + 10, cy, text=f"Alt: {altura}", fill="blue", anchor="w")

        elif tipo == "circ":
            radio = dimension_1
            diametro = radio * 2
            
            # Escalado
            margen = 40
            zoom = (min(w_canvas, h_canvas) - margen) / diametro if diametro > 0 else 1
            
            viz_r = radio * zoom
            
            # Dibujar Círculo centrado
            self.canvas.create_oval(cx - viz_r, cy - viz_r,
                                    cx + viz_r, cy + viz_r,
                                    fill=color_relleno, outline="black", width=3)
            
            # Texto
            self.canvas.create_text(cx, cy, text=f"r={radio}", fill="white", font=('Arial', 10, 'bold'))

    # --- Procesamiento ---
    def obtener_float(self, val):
        try:
            return float(val)
        except:
            return None

    def procesar_rectangulo(self):
        b = self.obtener_float(self.base_var.get())
        h = self.obtener_float(self.altura_var.get())
        
        if b and h and b > 0 and h > 0:
            rect = Rectangulo(b, h)
            area = rect.area()
            perim = rect.perimetro()
            
            self.resultado_var.set(f"Área: {area:.2f}  |  Perímetro: {perim:.2f}")
            self.lbl_resultado.config(fg="green")
            self.dibujar_figura("rect", b, h)
        else:
            self.resultado_var.set("❌ Ingresa números válidos mayores a 0")
            self.lbl_resultado.config(fg="red")

    def procesar_circulo(self):
        r = self.obtener_float(self.radio_var.get())
        
        if r and r > 0:
            circ = Circulo(r)
            area = circ.area()
            perim = circ.perimetro()
            
            self.resultado_var.set(f"Área: {area:.2f}  |  Perímetro: {perim:.2f}")
            self.lbl_resultado.config(fg="green")
            self.dibujar_figura("circ", r)
        else:
            self.resultado_var.set("❌ Ingresa un radio válido mayor a 0")
            self.lbl_resultado.config(fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeometriaVisualGUI(root)
    root.mainloop()
