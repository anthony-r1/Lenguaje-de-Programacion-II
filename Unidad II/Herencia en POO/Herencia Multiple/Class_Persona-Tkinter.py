import tkinter as tk
from tkinter import ttk, messagebox
import uuid

# ==================================
# Definición de las Clases de Modelo 
# ==================================

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad} años"

class Trabajador:
    def __init__(self, profesion, salario):
        self.profesion = profesion
        self.salario = salario
    def trabajar(self):
        return f"Profesión: {self.profesion}, Salario: S/.{self.salario:,.2f} al mes"

class Estudiante:
    def __init__(self, carrera, universidad):
        self.carrera = carrera
        self.universidad = universidad
    def estudiar(self):
        return f"Carrera: {self.carrera}, Universidad: {self.universidad}"

class PersonaMultirol(Persona, Trabajador, Estudiante):
    def __init__(self, nombre, edad, profesion, salario, carrera, universidad):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, profesion, salario)
        Estudiante.__init__(self, carrera, universidad)
        self.id = uuid.uuid4() 

    def obtener_info_completa(self):
        return (
            f"=========== Info de {self.nombre} (ID: {str(self.id)[:8]}) ===========\n"
            f"{self.presentarse()}\n"
            f"{self.trabajar()}\n"
            f"{self.estudiar()}\n"
            "================================================="
        )

# ========================================
# Clase de la Aplicación Tkinter 
# ========================================

class AplicacionGUIEditable:
    def __init__(self, root, personas_list):
        self.root = root
        self.personas = {p.nombre: p for p in personas_list}
        self.persona_actual = None  
        
        root.title("Gestor Interactivo de Personas Multirol")
        root.geometry("680x500")
        
        self.vars = {}
        main_frame = ttk.Frame(root, padding="15")
        main_frame.pack(fill='both', expand=True)
        
        self.setup_selector(main_frame)
        self.setup_campos_edicion(main_frame)
        self.setup_botones_y_salida(main_frame)

        main_frame.columnconfigure(1, weight=1)
        
        self.actualizar_selector() 
        if self.personas:
            self.persona_selector.current(0)
            self.cargar_persona_seleccionada(None)
        else:
            self.limpiar_campos()
            self.output_text.set("Sistema listo. Presiona 'Agregar Nueva' para empezar.")

    # ==================== Métodos de Setup ====================

    def setup_selector(self, frame):
        ttk.Label(frame, text="Seleccionar Persona:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky=tk.W, pady=10)
        self.combo_var = tk.StringVar()
        self.persona_selector = ttk.Combobox(
            frame, textvariable=self.combo_var, state="readonly", width=50
        )
        self.persona_selector.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=10)
        self.persona_selector.bind("<<ComboboxSelected>>", self.cargar_persona_seleccionada)

    def setup_campos_edicion(self, frame):
        self.campos_datos = [
            ("Nombre", 'nombre', str),
            ("Edad", 'edad', int),
            ("Profesión", 'profesion', str),
            ("Salario (S/.)", 'salario', float),
            ("Carrera", 'carrera', str),
            ("Universidad", 'universidad', str)
        ]
        
        for i, (label_text, attr_name, data_type) in enumerate(self.campos_datos):
            ttk.Label(frame, text=f"{label_text}:").grid(row=i + 1, column=0, sticky=tk.W, padx=5, pady=5)
            
            var = tk.StringVar(value="")
            
            # 💡 SOLUCIÓN DEL ERROR: Usamos un DICCIONARIO en lugar de una tupla para poder añadir 'entry'
            self.vars[attr_name] = {
                'var': var, 
                'type': data_type, 
                'entry': None 
            }
            
            entry = ttk.Entry(frame, textvariable=var, width=50)
            entry.grid(row=i + 1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
            
            # Guardamos la referencia al widget Entry en el diccionario
            self.vars[attr_name]['entry'] = entry 
            
    def setup_botones_y_salida(self, frame):
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=len(self.campos_datos) + 1, column=0, columnspan=2, pady=10)

        ttk.Button(btn_frame, text="GUARDAR Cambios", command=self.actualizar_y_mostrar).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="AGREGAR Nueva Persona", command=self.agregar_nueva_persona).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="ELIMINAR Persona", command=self.eliminar_persona).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(frame, text="Salida/Mensajes:", font=("Helvetica", 10, "italic")).grid(row=len(self.campos_datos) + 2, column=0, sticky=tk.W, pady=5)
        self.output_text = tk.StringVar(value="")
        self.output_label = ttk.Label(frame, textvariable=self.output_text, justify=tk.LEFT, wraplength=600)
        self.output_label.grid(row=len(self.campos_datos) + 3, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=5)

        ttk.Label(frame, text="Personas ingresadas (Consola):", font=("Helvetica", 10, "italic")).grid(row=len(self.campos_datos) + 4, column=0, sticky=tk.W, pady=5)
        ttk.Button(frame, text="Imprimir Lista Completa", command=self.imprimir_lista_completa).grid(row=len(self.campos_datos) + 4, column=1, sticky=tk.E, padx=5)
    
    # ==================== Métodos de Gestión ====================

    def actualizar_selector(self):
        """Refresca la lista desplegable de personas."""
        nombres = list(self.personas.keys())
        self.persona_selector['values'] = nombres
        return nombres

    def limpiar_campos(self):
        """Limpia todos los campos de entrada."""
        for attr_name in self.vars:
            self.vars[attr_name]['var'].set("") # ⬅️ USAR CLAVE 'var'
        self.persona_actual = None
        self.combo_var.set("") 
        self.output_text.set("Campos limpios. Ingresa datos para una nueva persona.")
        
    def imprimir_lista_completa(self):
        """Imprime la información de todas las personas en la consola."""
        if not self.personas:
            print("\n--- No hay personas ingresadas en la lista. ---")
            self.output_text.set("La lista de personas está vacía.")
            return

        print("\n================== LISTA DE PERSONAS INGRESADAS ==================")
        for persona in self.personas.values():
            print(persona.obtener_info_completa())
        print("==================================================================")
        self.output_text.set(f"Lista de {len(self.personas)} personas impresa en la consola.")
        
    def cargar_persona_seleccionada(self, event):
        """Busca el objeto seleccionado, actualiza los campos y MUESTRA LA HERENCIA."""
        nombre_seleccionado = self.combo_var.get()
        
        self.persona_actual = self.personas.get(nombre_seleccionado)
        
        if self.persona_actual:
            # ⬅️ USAR CLAVE 'var'
            self.vars['nombre']['var'].set(self.persona_actual.nombre)
            self.vars['edad']['var'].set(str(self.persona_actual.edad))
            self.vars['profesion']['var'].set(self.persona_actual.profesion)
            self.vars['salario']['var'].set(f"{self.persona_actual.salario:.2f}") 
            self.vars['carrera']['var'].set(self.persona_actual.carrera)
            self.vars['universidad']['var'].set(self.persona_actual.universidad)
            
            self.output_text.set(f"Persona **{self.persona_actual.nombre}** cargada para edición. Herencia impresa en consola.")
            self.imprimir_herencia()
        else:
            self.limpiar_campos() 
            
    def agregar_nueva_persona(self):
        """Prepara los campos para ingresar una nueva persona."""
        self.limpiar_campos()
        self.output_text.set("Modo **NUEVA PERSONA**. Ingresa los datos y presiona 'GUARDAR Cambios'.")
        
    def eliminar_persona(self):
        """Elimina la persona actualmente seleccionada de la lista."""
        if not self.persona_actual:
            messagebox.showwarning("Advertencia", "Selecciona una persona de la lista desplegable para eliminar.")
            return

        nombre = self.persona_actual.nombre
        confirm = messagebox.askyesno(
            "Confirmar Eliminación", 
            f"¿Estás seguro de que deseas eliminar a {nombre}?"
        )

        if confirm:
            try:
                del self.personas[nombre]
                
                self.limpiar_campos()
                self.actualizar_selector()
                
                if self.personas:
                    primer_nombre = list(self.personas.keys())[0]
                    self.combo_var.set(primer_nombre)
                    self.cargar_persona_seleccionada(None)
                
                self.output_text.set(f"Persona **{nombre}** ha sido eliminada correctamente.")
                self.imprimir_lista_completa() 
                
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar a {nombre}. Error: {e}")

    def actualizar_y_mostrar(self):
        """Guarda los cambios en el objeto actual o crea uno nuevo."""
        
        try:
            datos_nuevos = {}
            for label, attr_name, _ in self.campos_datos:
                
                # ⬅️ USAR CLAVE 'var' y 'type'
                var_str = self.vars[attr_name]['var'].get()
                data_type = self.vars[attr_name]['type']
                
                if not var_str and attr_name != 'salario': 
                    messagebox.showwarning("Advertencia", f"El campo '{label}' no puede estar vacío.")
                    return
                
                if data_type == int:
                    valor = int(var_str)
                elif data_type == float:
                    # Corrección del ValueError: elimina comas de miles
                    cleaned_str = var_str.replace(',', '') 
                    valor = float(cleaned_str)
                else:
                    valor = var_str
                
                datos_nuevos[attr_name] = valor
                
            nombre_nuevo = datos_nuevos['nombre']

            # Determinar si es una ACTUALIZACIÓN o CREACIÓN
            if self.persona_actual and self.persona_actual.nombre == nombre_nuevo:
                # Caso A: ACTUALIZACIÓN
                self.persona_actual.nombre = nombre_nuevo
                self.persona_actual.edad = datos_nuevos['edad']
                self.persona_actual.profesion = datos_nuevos['profesion']
                self.persona_actual.salario = datos_nuevos['salario']
                self.persona_actual.carrera = datos_nuevos['carrera']
                self.persona_actual.universidad = datos_nuevos['universidad']
                
                self.output_text.set(f"¡Datos de **{nombre_nuevo}** actualizados correctamente!")
                
            else:
                # Caso B: CREACIÓN o RENOMBRE
                if nombre_nuevo in self.personas:
                     messagebox.showwarning("Error", f"Ya existe una persona con el nombre '{nombre_nuevo}'.")
                     return
                
                if self.persona_actual: # Si se está renombrando
                    del self.personas[self.persona_actual.nombre]

                nueva_persona = PersonaMultirol(**datos_nuevos)
                self.personas[nombre_nuevo] = nueva_persona
                self.persona_actual = nueva_persona
                
                self.output_text.set(f"¡Nueva persona **{nombre_nuevo}** ha sido agregada y guardada correctamente!")

            # 3. Refrescar la GUI
            self.actualizar_selector()
            self.combo_var.set(nombre_nuevo) 
            
            self.imprimir_lista_completa()
            self.imprimir_herencia()

        except ValueError as e:
            error_msg = f"Error de formato: Asegúrate de que **Edad** sea entero y **Salario** un número válido (ej: 2500.00)."
            messagebox.showerror("Error de Entrada", error_msg)
            self.output_text.set(error_msg)
        except Exception as e:
            error_msg = f"Ocurrió un error inesperado: {e}"
            messagebox.showerror("Error", error_msg)
            self.output_text.set(error_msg)

    # --- Impresión de Herencia ---
    def imprimir_herencia(self):
        if self.persona_actual:
            mro_list = self.persona_actual.__class__.__mro__
            print("\n================== Jerarquía de Herencia (MRO) ==================")
            print(f"Clase Base: {self.persona_actual.__class__.__name__}")
            for i, clase in enumerate(mro_list):
                indent = '  ' * i
                print(f"{indent}--> {clase.__name__}")
            print("=================================================================\n")

# ==================================
# Función Principal
# ==================================

def main():
    personas_iniciales = [
        PersonaMultirol(nombre="Juanita Pérez", edad=23, profesion="Desarrollador de software", salario=2500.00, carrera="Ingeniería de Sistemas", universidad="UNAP"),
        PersonaMultirol(nombre="Carlos López", edad=32, profesion="Gerente de Ventas", salario=4800.50, carrera="Administración de Empresas", universidad="Universidad del Altiplano"),
        PersonaMultirol(nombre="Sofía Mendoza", edad=21, profesion="Becaria de Investigación", salario=1000.00, carrera="Biología", universidad="UNSA"),
    ]

    root = tk.Tk()
    app = AplicacionGUIEditable(root, personas_iniciales)
    root.mainloop()

if __name__ == "__main__":
    main()