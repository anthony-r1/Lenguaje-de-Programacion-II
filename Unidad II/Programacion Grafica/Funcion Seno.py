import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math # Necesario para usar math.pi

# Variables globales para el rango de la vista ortográfica
X_MIN, X_MAX = -5.0, 5.0
Y_MIN, Y_MAX = -5.0, 5.0

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glPointSize(5)
    glLineWidth(1.5) # Ancho de línea para los ejes
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(X_MIN, X_MAX, Y_MIN, Y_MAX)

## Función para dibujar las marcas y números en los ejes
def dibujar_marcas():
    tick_size = 0.1
    label_offset = 0.25 
    
    # Color para las marcas de los ejes y números (gris claro)
    glColor3f(0.7, 0.7, 0.7) 
    
    # 1. Marcas y Números Enteros en los Ejes (del -4 al 4)
    
    # Eje X
    glBegin(GL_LINES)
    for x in range(int(X_MIN) + 1, int(X_MAX)): 
        if x != 0:
            glVertex2f(x, -tick_size)
            glVertex2f(x, tick_size)
    glEnd()

    for x in range(int(X_MIN) + 1, int(X_MAX)):
        if x != 0:
            label = str(x).encode('ascii') 
            glRasterPos2f(x - label_offset, -label_offset * 2.0) 
            for char in label:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, char)

    # Eje Y
    glBegin(GL_LINES)
    for y in range(int(Y_MIN) + 1, int(Y_MAX)): 
        if y != 0:
            glVertex2f(-tick_size, y)
            glVertex2f(tick_size, y)
    glEnd()
    
    for y in range(int(Y_MIN) + 1, int(Y_MAX)):
        if y != 0:
            label = str(y).encode('ascii')
            glRasterPos2f(label_offset * 1.5, y - label_offset)
            for char in label:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, char)

    # 2. Marcas de Pi (Importante para funciones trigonométricas)
    
    pi_marks = [math.pi, 2 * math.pi, -math.pi, -2 * math.pi]
    pi_labels = [b'$\pi$', b'$2\pi$', b'$-\pi$', b'$-2\pi$'] # Etiquetas con simbolos

    glColor3f(1.0, 0.5, 0.0) # Color Naranja para las marcas de Pi
    
    for x_coord, label in zip(pi_marks, pi_labels):
        if X_MIN < x_coord < X_MAX:
            # Dibujar marcas en X
            glBegin(GL_LINES)
            glVertex2f(x_coord, -tick_size * 2) # Marca más larga
            glVertex2f(x_coord, tick_size * 2)
            glEnd()
            
            # Dibujar etiqueta de Pi
            glRasterPos2f(x_coord - label_offset, -label_offset * 4.5) 
            for char in label:
                # Usar una fuente diferente o una función para simbolos sería ideal,
                # pero nos limitamos a caracteres simples para mantenerlo en GLUT
                if char == ord(b'$'): continue # Ignorar los simbolos de delimitación
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, char)


def cartesiano():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Dibujar Ejes X e Y (Blancos)
    glBegin(GL_LINES)  
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(-4.5, 0.0)
    glVertex2f(4.5, 0.0)
    glVertex2f(0.0, -4.5)
    glVertex2f(0.0, 4.5)
    glEnd()
    
    # Llama a la función para dibujar las marcas y coordenadas
    dibujar_marcas()
    
    ## 📈 Dibujar la Curva (y = sin(x)) Suave
    glLineWidth(3.0) # Línea más gruesa para la curva
    glColor3f(0.2, 0.8, 1.0) # Color azul vibrante
    
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-4.0, 4.0, 200):
        y = np.sin(x) # Función Seno
        glVertex2f(x, y)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    # Título más descriptivo
    glutCreateWindow(b"Grafico de Funcion Seno (y = sin(x))") 
    inicializar()
    glutDisplayFunc(cartesiano)
    glutMainLoop()

if __name__=="__main__":
    main()
