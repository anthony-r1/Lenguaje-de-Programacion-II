from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1) # color blanco
    glRasterPos2f(-0.2, 0) # posición del texto
    for ch in "Hola Mundo":
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(ch)) # type: ignore
    glFlush()
    glRasterPos2f(-0.2, -0.3)
    for ch in "Universidad Nacional del Altiplano":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch)) # type: ignore
    glFlush()
    glRasterPos2f(-0.2, 0.3)
    for ch in "Anthony":
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(ch)) # type: ignore
    glFlush()
    
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400, 200)
glutCreateWindow(b"PyOpenGL - Hola mundo")
glClearColor(0, 0, 0, 1) # fondo negro
glutDisplayFunc(display)
glutMainLoop()
