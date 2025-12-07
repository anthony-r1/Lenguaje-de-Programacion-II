from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Cube3D: # Cambié el nombre de la clase para ser más descriptivo
    def __init__(self):
        self.angle_x = 0
        self.angle_y = 0
        self.init_window()

    def init_window(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(600, 600)
        # Título de la ventana actualizado para reflejar el cubo
        glutCreateWindow(b"Cubo 3D con rotacion e iluminacion") 

        self.init_lighting()

        glEnable(GL_DEPTH_TEST)
        glClearColor(0.2, 0.3, 0.4, 1.0) # Fondo azul oscuro

        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutSpecialFunc(self.keyboard_special)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1, 1, 50) # Proyección en perspectiva
        glMatrixMode(GL_MODELVIEW)

        glutMainLoop()

    def init_lighting(self):
        # Habilita la iluminación, la luz 0 y la normalización de vectores
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_NORMALIZE)

        # Parámetros de la luz (Light0)
        light_position = [5.0, 5.0, 5.0, 1.0] # Luz direccional/puntual
        light_ambient = [0.2, 0.2, 0.2, 1.0]
        light_diffuse = [0.8, 0.8, 0.8, 1.0]
        light_specular = [1.0, 1.0, 1.0, 1.0]

        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

        # Material del objeto (color Naranja con brillo)
        mat_ambient = [1.0, 0.5, 0.0, 1.0]
        mat_diffuse = [1.0, 0.5, 0.0, 1.0]
        mat_specular = [1.0, 1.0, 1.0, 1.0]
        mat_shininess = [50.0]

        glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
        glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity() # Carga la matriz identidad

        # Posiciona la cámara y el cubo
        glTranslatef(0.0, 0.0, -5.0) 
        
        # Aplicar rotación según los ángulos controlados por teclado
        glRotatef(self.angle_x, 1, 0, 0) # Rotación alrededor del eje X
        glRotatef(self.angle_y, 0, 1, 0) # Rotación alrededor del eje Y

        # Dibuja el cubo sólido con lado de 1.5 unidades
        glutSolidCube(1.5)

        glutSwapBuffers() # Intercambia los buffers para mostrar la escena

    def keyboard_special(self, key, x, y):
        # Controla la rotación del cubo usando las flechas
        if key == GLUT_KEY_RIGHT:
            self.angle_y += 5
        elif key == GLUT_KEY_LEFT:
            self.angle_y -= 5
        elif key == GLUT_KEY_UP:
            self.angle_x -= 5
        elif key == GLUT_KEY_DOWN:
            self.angle_x += 5
        glutPostRedisplay() # Indica que la ventana necesita ser redibujada

if __name__ == "__main__":
    Cube3D()
