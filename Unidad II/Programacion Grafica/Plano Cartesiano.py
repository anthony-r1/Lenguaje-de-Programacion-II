import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Rango de la vista ortográfica
VIEW_MIN, VIEW_MAX = -3.0, 3.0

def texto(x, y, string, font=GLUT_BITMAP_HELVETICA_12): # type: ignore
    """Función auxiliar para escribir texto en (x, y)"""
    glRasterPos2f(x, y)
    for ch in string.encode('ascii'): # Convertir a bytes para GLUT
        glutBitmapCharacter(font, ch)

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glPointSize(5)
    glLineWidth(2.0) # Líneas más gruesas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(VIEW_MIN, VIEW_MAX, VIEW_MIN, VIEW_MAX)

def cartesiano():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # --- Ejes Principales (Blancos) ---
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-2.9, 0.0) # Eje X más largo
    glVertex2f(2.9, 0.0)
    glVertex2f(0.0, -2.9) # Eje Y más largo
    glVertex2f(0.0, 2.9)
    glEnd()

    # --- Marcas y Coordenadas Estéticas (Gris Claro) ---
    tick_size = 0.08
    glColor3f(0.7, 0.7, 0.7) 

    # Rango de -2 a 2
    for val in range(-2, 3):
        if val != 0:
            # Marcas y números del eje X
            glBegin(GL_LINES)
            glVertex2f(val, -tick_size)
            glVertex2f(val, tick_size)
            glEnd()
            texto(val - 0.15, -0.4, str(val)) # Etiqueta debajo

            # Marcas y números del eje Y
            glBegin(GL_LINES)
            glVertex2f(-tick_size, val)
            glVertex2f(tick_size, val)
            glEnd()
            texto(-0.4, val - 0.1, str(val)) # Etiqueta a la izquierda

    # --- Dibujar la Función Cúbica y = x^3 ---
    glColor3f(0.8, 0.2, 1.0) # Color Morado Vibrante
    glLineWidth(3.5) # Línea aún más gruesa para la curva
    glBegin(GL_LINE_STRIP)
    
    # Generamos puntos en un rango más amplio (-1.5 a 1.5) para que la curva sea visible y suave
    for x in np.linspace(-1.5, 1.5, 300):
        y = x ** 3 # Función cúbica
        glVertex2f(x, y)
    glEnd()

    # --- Título y Etiquetas (Amarillo) ---
    glColor3f(1.0, 1.0, 0.0)
    texto(-2.9, 2.7, "Grafico: y = x^3 (Funcion Cubica)", GLUT_BITMAP_HELVETICA_18) # type: ignore

    # Etiquetas de Ejes
    texto(2.7, -0.4, "X")
    texto(-0.4, 2.7, "Y")

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Plano cartesiano con texto - y = x^3")
    inicializar()
    glutDisplayFunc(cartesiano)
    glutMainLoop()

if __name__ == "__main__":
    main()
