from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glPointSize(5)
    glLineWidth(4.0) # Grosor de línea
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Rango de vista adaptado para centrar las letras (de -0.5 a 0.5)
    glOrtho(-0.5, 0.5, -0.5, 0.5, -1.0, 1.0) 

def dibujar_una_rgb():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # --- Definición de colores RGB ---
    COLOR_ROJO = (1.0, 0.0, 0.0)      # Para la U
    COLOR_VERDE = (0.0, 1.0, 0.0)     # Para la N
    COLOR_AZUL = (0.0, 0.0, 1.0)      # Para la A (Contorno y Centro)
    
    # 1. Letra 'U' (Columna Izquierda, adaptada de tu código) -> ROJO
    glBegin(GL_LINE_STRIP)  
    glColor3f(*COLOR_ROJO) 
    glVertex2f(-0.4, 0.2)
    glVertex2f(-0.4, -0.2)
    glVertex2f(-0.2, -0.2)
    glVertex2f(-0.2, 0.2)
    glEnd()
    
    # 2. Letra 'N' (Columna Central, adaptada de tu código) -> VERDE
    glBegin(GL_LINE_STRIP)  
    glColor3f(*COLOR_VERDE) 
    glVertex2f(-0.1,-0.2)
    glVertex2f(-0.1, 0.2)
    glVertex2f(0.1, -0.2)
    glVertex2f(0.1, 0.2)
    glEnd()
    
    # 3. Letra 'A' (Columna Derecha, Contorno) -> AZUL
    glBegin(GL_LINE_STRIP)  
    glColor3f(*COLOR_AZUL) 
    # El contorno de la A lo adapto para que sea una figura abierta (similar a tu código original)
    glVertex2f(0.2,-0.2)  # Base izquierda
    glVertex2f(0.2, 0.2)  # Pico izquierdo
    glVertex2f(0.4, 0.2)  # Pico derecho
    glVertex2f(0.4, -0.2) # Base derecha
    glEnd()
    
    # 4. Letra 'A' (Línea Horizontal Central) -> AZUL (Cambiado de Amarillo)
    glBegin(GL_LINES)  # Usamos GL_LINES para una línea simple
    glColor3f(*COLOR_AZUL) 
    glVertex2f(0.2, 0.0)
    glVertex2f(0.4, 0.0)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Dibujo Multicolor: U N A")
    inicializar()
    glutDisplayFunc(dibujar_una_rgb) 
    glutMainLoop()

if __name__=="__main__":
    main()
