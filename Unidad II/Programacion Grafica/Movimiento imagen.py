from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

posx = 0
posy = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo gris oscuro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Aplicar rotación
    
    glTranslatef(posx, posy, 0)
    
    # glColor3f(0.0, 1.0, 0.0)  # Color amarillo
    glBegin(GL_TRIANGLES)  
    glColor3f(1.0, 0.0, 0.0); glVertex2f(0.0, 0.5)    # Vértice superior
    glColor3f(0.0, 1.0, 0.0); glVertex2f(-0.5, -0.5)  # Vértice inferior izquierdo
    glColor3f(0.0, 0.0, 1.0); glVertex2f(0.5, -0.5)   # Vértice inferior derecho
    glEnd()

    glFlush()
    
def keyboard(key, x, y):
    global posx, posy
    paso = 0.05
    if key == GLUT_KEY_UP:
        posy += paso
    elif key == GLUT_KEY_DOWN:
        posy -= paso
    elif key == GLUT_KEY_LEFT:
        posx -= paso
    elif key == GLUT_KEY_RIGHT:
        posx += paso
    glutPostRedisplay()
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Traslacion con teclado")
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(keyboard)
    glutMainLoop()

if __name__=="__main__":
    main()
