from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

escala = 1

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo gris oscuro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Aplicar escalado
    
    glScalef(escala, escala, 1.0)
    
    # glColor3f(0.0, 1.0, 0.0)  # Color amarillo
    glBegin(GL_TRIANGLES)  
    glColor3f(1.0, 0.0, 0.0); glVertex2f(0.0, 0.5)    # Vértice superior
    glColor3f(0.0, 1.0, 0.0); glVertex2f(-0.5, -0.5)  # Vértice inferior izquierdo
    glColor3f(0.0, 0.0, 1.0); glVertex2f(0.5, -0.5)   # Vértice inferior derecho
    glEnd()

    glFlush()
    
def keyboard(key, x, y):
    global escala
    if key == b'+':
        escala += 0.1
    elif key == b'-':
        escala -= 0.1
    glutPostRedisplay()
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Escala con teclado")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__=="__main__":
    main()
