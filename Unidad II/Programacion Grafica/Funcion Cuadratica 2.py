from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Rango de la vista ortográfica
VIEW_MIN, VIEW_MAX = -3.0, 3.0

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glPointSize(5)
    glLineWidth(1.5)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(VIEW_MIN, VIEW_MAX, VIEW_MIN, VIEW_MAX, -1.0, 1.0) 

# Función para dibujar las marcas y números en los ejes
def dibujar_marcas():
    tick_size = 0.08
    label_offset = 0.15
    
    glColor3f(0.7, 0.7, 0.7) 
    
    # Dibujar marcas y números en el Eje X
    glBegin(GL_LINES)
    for coord in np.arange(int(VIEW_MIN) + 1, int(VIEW_MAX)): 
        if coord != 0:
            glVertex2f(coord, -tick_size)
            glVertex2f(coord, tick_size)
    glEnd()

    for coord in np.arange(int(VIEW_MIN) + 1, int(VIEW_MAX)):
        if coord != 0:
            label = str(coord).encode('ascii') 
            glRasterPos2f(coord - label_offset, -label_offset * 3.0) 
            for char in label:
                glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, char)

    # Dibujar marcas y números en el Eje Y
    glBegin(GL_LINES)
    for coord in np.arange(int(VIEW_MIN) + 1, int(VIEW_MAX)): 
        if coord != 0:
            glVertex2f(-tick_size, coord)
            glVertex2f(tick_size, coord)
    glEnd()
    
    for coord in np.arange(int(VIEW_MIN) + 1, int(VIEW_MAX)):
        if coord != 0:
            label = str(coord).encode('ascii')
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
    
    # Dibujar las marcas y coordenadas
    dibujar_marcas()
    
    ## 📈 Generación de Curva Suave (y = x^2)
    
    # 1. Definir el rango de X y el número de puntos
    # Usamos np.linspace para generar 200 puntos uniformemente espaciados entre -1.5 y 1.5
    num_puntos = 200
    rango_x = np.linspace(-1.5, 1.5, num_puntos) 
    
    # 2. Calcular los valores de Y para la función y = x^2
    # El uso de NumPy permite calcular Y para todos los X a la vez (vectorización)
    rango_y = rango_x**2 

    # 3. Dibujar la curva
    glLineWidth(3.0)
    glColor3f(0.0, 0.8, 1.0) # Color azul brillante
    glBegin(GL_LINE_STRIP)
    
    # Iteramos sobre los 200 pares (x, y) y los dibujamos
    for x, y in zip(rango_x, rango_y):
        glVertex2f(x, y)
        
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Grafico de Parabola Suave (y = x^2)")
    inicializar()
    glutDisplayFunc(cartesiano)
    glutMainLoop()

if __name__=="__main__":
    main()
