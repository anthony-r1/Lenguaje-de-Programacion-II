from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

angulo = 0.0
escala = 1
posx = 0
posy = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo gris oscuro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def display():
    global angulo
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Aplicar rotación
    
    glTranslatef(posx, posy, 0)
    
    # Aplicar escalado
    
    glScalef(escala, escala, 1.0)
    
    # Aplicar rotación
    
    glRotate(angulo, 0.0, 0.0, 1.0)
    
    # glColor3f(0.0, 1.0, 0.0)  # Color amarillo
    glBegin(GL_TRIANGLES)  
    glColor3f(1.0, 0.0, 0.0); glVertex2f(0.0, 0.5)    # Vértice superior
    glColor3f(0.0, 1.0, 0.0); glVertex2f(-0.5, -0.5)  # Vértice inferior izquierdo
    glColor3f(0.0, 0.0, 1.0); glVertex2f(0.5, -0.5)   # Vértice inferior derecho
    glEnd()

    glFlush()
    
def special_keys(key, x, y):
    global angulo
    if key == GLUT_KEY_LEFT: # Flecha izquierda
        angulo += 5
    elif key == GLUT_KEY_RIGHT:
        angulo -= 5
    glutPostRedisplay() # Redibujar la escena
    
def keyboard(key, x, y):
    global posx, posy, escala
    paso = 0.05
    if key == b'w':
        posy += paso
    elif key == b's':
        posy -= paso
    elif key == b'a':
        posx -= paso
    elif key == b'd':
        posx += paso
    elif key == b'+':
        escala += 0.1
    elif key == b'-':
        escala -= 0.1
    glutPostRedisplay()
    
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Rotacion con teclado")
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(special_keys)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__=="__main__":
    main()
