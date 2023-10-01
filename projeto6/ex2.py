from OpenGL.GL import *
from OpenGL.GLUT import *
import math

thetaX = 0.0
thetaY = 0.0
angle = 0.0  # Ângulo de rotação
rotation_enabled = False  # Variável para controlar a animação

def haste():
    glBegin(GL_QUADS)
    
    glColor3f(1.0, 0.0, 0.0)  # Cor vermelha
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)

    glColor3f(0.0, 1.0, 0.0)  # Cor verde
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)

    glColor3f(0.0, 0.0, 1.0)  # Cor azul
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)

    glColor3f(1.0, 1.0, 0.0)  # Cor amarela
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)

    glColor3f(1.0, 0.0, 1.0)  # Cor magenta
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    glColor3f(0.0, 1.0, 1.0)  # Cor ciano
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)

    glEnd()
    
def draw_catavento():
    glBegin(GL_TRIANGLES)

    glColor3f(1.0, 0.0, 0.0)  # Vermelho
    glVertex3f(0.0, 0.5, 0.0)
    glVertex3f(-0.05, 0.0, -0.05)
    glVertex3f(0.05, 0.0, -0.05)

    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex3f(0.0, 0.5, 0.0)
    glVertex3f(0.05, 0.0, -0.05)
    glVertex3f(0.05, 0.0, 0.05)

    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(0.0, 0.5, 0.0)
    glVertex3f(0.05, 0.0, 0.05)
    glVertex3f(-0.05, 0.0, 0.05)

    glColor3f(1.0, 1.0, 0.0)  # Amarelo
    glVertex3f(0.0, 0.5, 0.0)
    glVertex3f(-0.05, 0.0, 0.05)
    glVertex3f(-0.05, 0.0, -0.05)

    glEnd()

def draw_star():
    for i in range(4):
        glPushMatrix()
        glRotatef(90.0 * i, 0.0, 0.0, 1.0)
        glTranslatef(0.0, 0.0, 0.0)
        draw_catavento()
        glPopMatrix()

def desenha():
    global angle, rotation_enabled
    glClearColor(0, 0, 0, 0) 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glPushMatrix()
    glRotatef(thetaX, 1.0, 0.0, 0.0)
    glRotatef(thetaY, 0.0, 1.0, 0.0)
    if rotation_enabled:
        glRotatef(angle, 0.0, 0.0, 1.0)  # Rotação em torno do eixo vertical
        angle += 1.0  # Incrementa o ângulo de rotação
        if angle >= 360.0:
            angle = 0.0
    glTranslatef(0.0, 0.0, 0.0)
    draw_star()
    glPopMatrix()

    glutPostRedisplay()

    glPushMatrix()
    glRotatef(thetaX, 1.0, 0.0, 0.0)
    glRotatef(thetaY, 0.0, 1.0, 0.0)
    glTranslatef(0.0, -0.3, 0.0)
    glScalef(0.04, 0.7, 0.04)
    haste()
    glPopMatrix()

    glFlush()

def tecladoEspecial(tecla, x, y):
    global thetaX, thetaY, rotation_enabled
    if tecla == GLUT_KEY_RIGHT:
        thetaY += 2
    elif tecla == GLUT_KEY_LEFT:
        thetaY -= 2
    elif tecla == GLUT_KEY_UP:
        thetaX += 2
    elif tecla == GLUT_KEY_DOWN:
        thetaX -= 2
    glutPostRedisplay()

def teclado(tecla, x, y):
    global rotation_enabled
    if tecla == b'a':
        rotation_enabled = not rotation_enabled  # Inverte o estado da animação
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"Catavento - press 'a'")
    glutDisplayFunc(desenha)
    glutSpecialFunc(tecladoEspecial)
    glutKeyboardFunc(teclado)
    glutMainLoop()

if __name__ == "__main__":
    main()