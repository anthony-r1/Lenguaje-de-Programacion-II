from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import sys

class Cube3D:
    def __init__(self):
        self.angle_x = 0
        self.angle_y = 0
        self.textures = [] 
        self.filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg"]
        self.init_window()

    def init_window(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(600, 600)
        glutCreateWindow(b"Cubo 3D con Imagenes - Anthony") 

        self.load_textures() 
        self.init_configuration()

        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutSpecialFunc(self.keyboard_special)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1, 1, 50)
        glMatrixMode(GL_MODELVIEW)

        glutMainLoop()

    def load_textures(self):
        glEnable(GL_TEXTURE_2D)
        
        for name in self.filenames:
            try:
                img = Image.open(name)
                # Convertimos y aseguramos que los datos sean bytes crudos
                img = img.convert("RGB")
                img_data = img.tobytes("raw", "RGB", 0, -1)
                width, height = img.size
                
                tex_id = glGenTextures(1)
                glBindTexture(GL_TEXTURE_2D, tex_id)
                
                # --- CORRECCIÓN DEL ERROR ---
                # Esto evita el crash si el ancho de la imagen no es múltiplo de 4
                glPixelStorei(GL_UNPACK_ALIGNMENT, 1) 
                # ----------------------------

                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
                
                glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
                
                self.textures.append(tex_id)
                print(f"Imagen cargada: {name}")
            except Exception as e:
                print(f"Error cargando {name}: {e}")
                sys.exit()

    def init_configuration(self):
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.2, 0.3, 0.4, 1.0)
        glColor3f(1.0, 1.0, 1.0) 

    def draw_textured_cube(self):
        size = 0.75 
        
        # FRONTAL (1.jpg)
        if len(self.textures) > 0: glBindTexture(GL_TEXTURE_2D, self.textures[0])
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0); glVertex3f(-size, -size,  size)
        glTexCoord2f(1.0, 0.0); glVertex3f( size, -size,  size)
        glTexCoord2f(1.0, 1.0); glVertex3f( size,  size,  size)
        glTexCoord2f(0.0, 1.0); glVertex3f(-size,  size,  size)
        glEnd()

        # TRASERA (2.jpg)
        if len(self.textures) > 1: glBindTexture(GL_TEXTURE_2D, self.textures[1])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 0.0); glVertex3f(-size, -size, -size)
        glTexCoord2f(1.0, 1.0); glVertex3f(-size,  size, -size)
        glTexCoord2f(0.0, 1.0); glVertex3f( size,  size, -size)
        glTexCoord2f(0.0, 0.0); glVertex3f( size, -size, -size)
        glEnd()

        # SUPERIOR (3.jpg)
        if len(self.textures) > 2: glBindTexture(GL_TEXTURE_2D, self.textures[2])
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0); glVertex3f(-size,  size, -size)
        glTexCoord2f(0.0, 0.0); glVertex3f(-size,  size,  size)
        glTexCoord2f(1.0, 0.0); glVertex3f( size,  size,  size)
        glTexCoord2f(1.0, 1.0); glVertex3f( size,  size, -size)
        glEnd()

        # INFERIOR (4.jpg)
        if len(self.textures) > 3: glBindTexture(GL_TEXTURE_2D, self.textures[3])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0); glVertex3f(-size, -size, -size)
        glTexCoord2f(0.0, 1.0); glVertex3f( size, -size, -size)
        glTexCoord2f(0.0, 0.0); glVertex3f( size, -size,  size)
        glTexCoord2f(1.0, 0.0); glVertex3f(-size, -size,  size)
        glEnd()

        # DERECHA (5.jpg)
        if len(self.textures) > 4: glBindTexture(GL_TEXTURE_2D, self.textures[4])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 0.0); glVertex3f( size, -size, -size)
        glTexCoord2f(1.0, 1.0); glVertex3f( size,  size, -size)
        glTexCoord2f(0.0, 1.0); glVertex3f( size,  size,  size)
        glTexCoord2f(0.0, 0.0); glVertex3f( size, -size,  size)
        glEnd()

        # IZQUIERDA (6.jpg)
        if len(self.textures) > 5: glBindTexture(GL_TEXTURE_2D, self.textures[5])
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0); glVertex3f(-size, -size, -size)
        glTexCoord2f(1.0, 0.0); glVertex3f(-size, -size,  size)
        glTexCoord2f(1.0, 1.0); glVertex3f(-size,  size,  size)
        glTexCoord2f(0.0, 1.0); glVertex3f(-size,  size, -size)
        glEnd()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0) 
        
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0)

        self.draw_textured_cube()

        glutSwapBuffers()

    def keyboard_special(self, key, x, y):
        if key == GLUT_KEY_RIGHT:
            self.angle_y += 5
        elif key == GLUT_KEY_LEFT:
            self.angle_y -= 5
        elif key == GLUT_KEY_UP:
            self.angle_x -= 5
        elif key == GLUT_KEY_DOWN:
            self.angle_x += 5
        glutPostRedisplay()

if __name__ == "__main__":
    Cube3D()
