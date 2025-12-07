import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Variables globales para el rango de la vista ortográfica
X_MIN, X_MAX = -5.0, 5.0
Y_MIN, Y_MAX = -5.0, 5.0

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glPointSize(5)  # Tamaño de los puntos
    glLineWidth(1.5) # Ancho de línea para mayor visibilidad
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Usar las variables globales para la vista ortográfica
    gluOrtho2D(X_MIN, X_MAX, Y_MIN, Y_MAX)

# Función para dibujar las marcas y números en los ejes
def dibujar_marcas():
    tick_size = 0.1  # Tamaño de la marca de tick
    label_offset = 0.2  # Desplazamiento para los números
    
    # Color para las marcas de los ejes (gris claro)
    glColor3f(0.7, 0.7, 0.7) 
    
    # Dibujar marcas en el Eje X
    glBegin(GL_LINES)
    # Rango de -4 a 4, con paso de 1
    for x in range(int(X_MIN) + 1, int(X_MAX)): 
        if x != 0:
            # Marcas verticales
            glVertex2f(x, -tick_size)
            glVertex2f(x, tick_size)
    glEnd()

    # Dibujar números en el Eje X
    for x in range(int(X_MIN) + 1, int(X_MAX)):
        if x != 0:
            # Convierte el número a cadena y luego a bytes para GLUT
            label = str(x).encode('ascii') 
            # Posiciona el texto
            glRasterPos2f(x - label_offset, -label_offset * 2.5) 
            # Dibuja el texto
            for char in label:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, char)

    # Dibujar marcas en el Eje Y
    glBegin(GL_LINES)
    # Rango de -4 a 4, con paso de 1
    for y in range(int(Y_MIN) + 1, int(Y_MAX)): 
        if y != 0:
            # Marcas horizontales
            glVertex2f(-tick_size, y)
            glVertex2f(tick_size, y)
    glEnd()
    
    # Dibujar números en el Eje Y
    for y in range(int(Y_MIN) + 1, int(Y_MAX)):
        if y != 0:
            label = str(y).encode('ascii')
            # Posiciona el texto
            glRasterPos2f(label_offset * 1.5, y - label_offset)
            # Dibuja el texto
            for char in label:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, char)

def cartesiano():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Dibujar Ejes X e Y
    glBegin(GL_LINES)  
    glColor3f(1.0, 1.0, 1.0) # Color blanco para los ejes
    glVertex2f(-4.5, 0.0)
    glVertex2f(4.5, 0.0)
    glVertex2f(0.0, -4.5)
    glVertex2f(0.0, 4.5)
    glEnd()
    
    # Llama a la nueva función para dibujar las marcas y coordenadas
    dibujar_marcas()
    
    # Dibujar la función y = cos(x)
    glColor3f(0.2, 0.8, 1.0) # Color azul claro vibrante
    glLineWidth(2.5) # Aumentar el ancho para la curva
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-4.0, 4.0, 200):
        y = np.cos(x)
        glVertex2f(x, y)
    glEnd()

    glFlush() # Asegura que todos los comandos se ejecuten

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    # Cambiar el título de la ventana para reflejar la función cos(x)
    glutCreateWindow(b"Grafico de y = cos(x)") 
    inicializar()
    glutDisplayFunc(cartesiano)
    glutMainLoop()

if __name__=="__main__":
    main()
