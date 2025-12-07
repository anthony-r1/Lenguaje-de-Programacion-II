import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Rango de la vista ortográfica
VIEW_MIN, VIEW_MAX = -3.0, 3.0

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glPointSize(5)
    glLineWidth(1.5) # Ancho de línea para los ejes
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(VIEW_MIN, VIEW_MAX, VIEW_MIN, VIEW_MAX)

## Función para dibujar las marcas y números en los ejes
def dibujar_marcas():
    tick_size = 0.08  # Tamaño de la marca de tick
    label_offset = 0.15  # Desplazamiento para posicionar los números
    
    # Color para las marcas de los ejes y números (gris claro)
    glColor3f(0.7, 0.7, 0.7) 
    
    # Dibujar marcas y números en el Eje X (de -2 a 2)
    glBegin(GL_LINES)
    # Iterar de -2 a 2
    for coord in np.arange(int(VIEW_MIN) + 1, int(VIEW_MAX)): 
        if coord != 0:
            # Marcas verticales (ticks)
            glVertex2f(coord, -tick_size)
            glVertex2f(coord, tick_size)
    glEnd()

    for coord in np.arange(int(VIEW_MIN) + 1, int(VIEW_MAX)):
        if coord != 0:
            label = str(coord).encode('ascii') 
            # Posiciona el texto debajo del eje
            glRasterPos2f(coord - label_offset, -label_offset * 3.0) 
            for char in label:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, char)

    # Dibujar marcas y números en el Eje Y (de -2 a 2)
    glBegin(GL_LINES)
    for coord in np.arange(int(VIEW_MIN) + 1, int(VIEW_MAX)): 
        if coord != 0:
            # Marcas horizontales (ticks)
            glVertex2f(-tick_size, coord)
            glVertex2f(tick_size, coord)
    glEnd()
    
    for coord in np.arange(int(VIEW_MIN) + 1, int(VIEW_MAX)):
        if coord != 0:
            label = str(coord).encode('ascii')
            # Posiciona el texto a la izquierda del eje
            glRasterPos2f(label_offset * 1.5, coord - label_offset)
            for char in label:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, char)

def cartesiano():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Dibujar Ejes X e Y (Blancos)
    glBegin(GL_LINES)  
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(-2.5, 0.0)
    glVertex2f(2.5, 0.0)
    glVertex2f(0.0, -2.5)
    glVertex2f(0.0, 2.5)
    glEnd()
    
    # Llama a la nueva función para dibujar las marcas y coordenadas
    dibujar_marcas()
    
    ## 📈 Dibujar la Curva (y = x^3) Suave
    glLineWidth(3.0) # Línea más gruesa para la curva
    glColor3f(0.8, 0.2, 1.0) # Color morado vibrante para la curva
    
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-1.5, 1.5, 200):
        y = x ** 3
        glVertex2f(x, y)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    # Título más descriptivo
    glutCreateWindow(b"Grafico de Funcion Cubica (y = x^3)") 
    inicializar()
    glutDisplayFunc(cartesiano)
    glutMainLoop()

if __name__=="__main__":
    main()
