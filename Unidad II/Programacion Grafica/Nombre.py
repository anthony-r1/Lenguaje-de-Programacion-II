from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def inicializar():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glPointSize(5)
    glLineWidth(2.5)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)

def dibujar_anthony_corregido():
    glClear(GL_COLOR_BUFFER_BIT)
    
    base_x_start = -0.76 
    current_x = base_x_start

    COLOR_R = (1.0, 0.0, 0.0, 1.0)
    COLOR_G = (0.0, 1.0, 0.0, 1.0)
    COLOR_B = (0.0, 0.0, 1.0, 1.0)
    
    ESPACIADO_BASE = 0.20

    # A
    glColor4f(*COLOR_R)
    glBegin(GL_LINE_STRIP)
    glVertex2f(current_x + 0.0, -0.15)
    glVertex2f(current_x + 0.06, 0.15)
    glVertex2f(current_x + 0.12, -0.15)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(current_x + 0.03, 0.0)
    glVertex2f(current_x + 0.09, 0.0)
    glEnd()
    current_x += ESPACIADO_BASE 

    # N
    glColor4f(*COLOR_G)
    glBegin(GL_LINE_STRIP)
    glVertex2f(current_x + 0.0, -0.15)
    glVertex2f(current_x + 0.0, 0.15)
    glVertex2f(current_x + 0.12, -0.15)
    glVertex2f(current_x + 0.12, 0.15)
    glEnd()
    current_x += 0.22 
    
    # T
    glColor4f(*COLOR_B)
    glBegin(GL_LINE_STRIP)
    glVertex2f(current_x - 0.06, 0.15)
    glVertex2f(current_x + 0.06, 0.15)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(current_x, 0.15)
    glVertex2f(current_x, -0.15)
    glEnd()
    current_x += ESPACIADO_BASE 

    # H
    glColor4f(*COLOR_R)
    glBegin(GL_LINE_STRIP)
    glVertex2f(current_x + 0.0, -0.15)
    glVertex2f(current_x + 0.0, 0.15)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2f(current_x + 0.12, -0.15)
    glVertex2f(current_x + 0.12, 0.15)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(current_x + 0.0, 0.0)
    glVertex2f(current_x + 0.12, 0.0)
    glEnd()
    current_x += ESPACIADO_BASE 

    # O
    glColor4f(*COLOR_G)
    glBegin(GL_LINE_LOOP)
    glVertex2f(current_x + 0.0, -0.15)
    glVertex2f(current_x + 0.0, 0.15)
    glVertex2f(current_x + 0.12, 0.15)
    glVertex2f(current_x + 0.12, -0.15)
    glEnd()
    current_x += ESPACIADO_BASE 

    # N
    glColor4f(*COLOR_B)
    glBegin(GL_LINE_STRIP)
    glVertex2f(current_x + 0.0, -0.15)
    glVertex2f(current_x + 0.0, 0.15)
    glVertex2f(current_x + 0.12, -0.15)
    glVertex2f(current_x + 0.12, 0.15)
    glEnd()
    current_x += ESPACIADO_BASE 
    
    # Y
    glColor4f(*COLOR_R)
    glBegin(GL_LINE_STRIP)
    glVertex2f(current_x + 0.0, 0.15)
    glVertex2f(current_x + 0.06, 0.0)
    glVertex2f(current_x + 0.12, 0.15)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(current_x + 0.06, 0.0)
    glVertex2f(current_x + 0.06, -0.15)
    glEnd()
    
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(850, 400)
    glutCreateWindow(b"ANTHONY Espaciado Perfecto")
    inicializar()
    glutDisplayFunc(dibujar_anthony_corregido)
    glutMainLoop()

if __name__ == "__main__":
    main()
