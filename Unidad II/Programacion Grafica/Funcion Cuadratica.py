from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np # Importamos numpy para el rango de iteración

# Rango de la vista ortográfica
VIEW_MIN, VIEW_MAX = -3.0, 3.0

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glPointSize(5)  # Tamaño de los puntos
    glLineWidth(1.5) # Ancho de línea para los ejes
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Usamos glOrtho para una vista 2D (ignora el tercer par Z)
    glOrtho(VIEW_MIN, VIEW_MAX, VIEW_MIN, VIEW_MAX, -1.0, 1.0) 

# Función para dibujar las marcas y números en los ejes
def dibujar_marcas():
    tick_size = 0.08  # Tamaño de la marca de tick
    label_offset = 0.15  # Desplazamiento para posicionar los números
    
    # Color para las marcas de los ejes y números (gris claro)
    glColor3f(0.7, 0.7, 0.7) 
    
    # Rango de iteración para las marcas: desde -2 hasta 2 (excluyendo 0)
    # np.arange(start, stop, step) es útil aquí
    
    # Dibujar marcas en el Eje X
    glBegin(GL_LINES)
    for coord in np.arange(int(VIEW_MIN) + 1, int(VIEW_MAX)): 
        if coord != 0:
            # Marcas verticales (ticks)
            glVertex2f(coord, -tick_size)
            glVertex2f(coord, tick_size)
    glEnd()

    # Dibujar números en el Eje X
    for coord in np.arange(int(VIEW_MIN) + 1, int(VIEW_MAX)):
        if coord != 0:
            label = str(coord).encode('ascii') 
            # Posiciona el texto debajo del eje
            glRasterPos2f(coord - label_offset, -label_offset * 3.0) 
            for char in label:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, char)

    # Dibujar marcas en el Eje Y
    glBegin(GL_LINES)
    for coord in np.arange(int(VIEW_MIN) + 1, int(VIEW_MAX)): 
        if coord != 0:
            # Marcas horizontales (ticks)
            glVertex2f(-tick_size, coord)
            glVertex2f(tick_size, coord)
    glEnd()
    
    # Dibujar números en el Eje Y
    for coord in np.arange(int(VIEW_MIN) + 1, int(VIEW_MAX)):
        if coord != 0:
            label = str(coord).encode('ascii')
            # Posiciona el texto a la izquierda del eje
            glRasterPos2f(label_offset * 1.5, coord - label_offset)
            for char in label:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, char)

def cartesiano():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Dibujar Ejes X e Y
    glBegin(GL_LINES)  
    glColor3f(1.0, 1.0, 1.0) # Ejes Blancos
    glVertex2f(-2.5, 0.0)
    glVertex2f(2.5, 0.0)
    glVertex2f(0.0, -2.5)
    glVertex2f(0.0, 2.5)
    glEnd()
    
    # Llama a la nueva función para dibujar las marcas y coordenadas
    dibujar_marcas()
    
    # Dibujar la función cuadrática (Parábola)
    glLineWidth(3.0) # Línea más gruesa para la curva
    glBegin(GL_LINE_STRIP)
    glColor3f(0.0, 0.8, 1.0) # Color azul brillante para la curva
    glVertex2f(-1.5, 2.25)
    glVertex2f(-1.0, 1.0)
    glVertex2f(-0.5, 0.25)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.5, 0.25)
    glVertex2f(1.0, 1.0)
    glVertex2f(1.5, 2.25)
    glEnd()

    glFlush() # Asegura que todos los comandos se ejecuten

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Grafico de Parabola (y = x^2)")
    inicializar()
    glutDisplayFunc(cartesiano)
    glutMainLoop()

if __name__=="__main__":
    main()
