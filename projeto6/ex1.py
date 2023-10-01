from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Variáveis para a rotação
head_rotation = 0.0
hair_rotation_left = 0.0
hair_rotation_right = 0.0

# Variáveis de controle das animações
head_animation_active = False
hair_animation_active = False

# Função de inicialização
def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Palhaco - press 'a' 's'")

    glClearColor(0.0, 0.0, 0.0, 1.0) 
    glEnable(GL_DEPTH_TEST) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

# Função para desenhar o rosto do palhaço
def draw_clown_face():
    # Desenha a cabeça
    glColor3f(1.0, 0.9, 0.6) 
    glutSolidSphere(1.0, 100, 100)

    # Desenha o nariz
    glColor3f(1.0, 0.0, 0.0) 
    glTranslatef(0.0, 0.2, 1.0) 
    glutSolidSphere(0.2, 100, 100)

    # Desenha os olhos
    glColor3f(0.0, 0.0, 0.0) 
    glTranslatef(-0.2, 0.3, -0.1) 
    glutSolidSphere(0.1, 100, 100)

    glTranslatef(0.4, 0.0, 0.0)  # Posição do olho direito em relação ao olho esquerdo
    glutSolidSphere(0.1, 100, 100)

    # Desenha os cabelos
    glColor3f(0.0, 1.0, 0.0) 

    glPushMatrix()
    glTranslatef(0.75, 0.0, -0.7)  
    glRotatef(hair_rotation_right, 0.0, 0.0, 1.0)  # Rotação do cabelo direito
    glScalef(0.5, 0.5, 0.5) 
    glutSolidOctahedron()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.1, 0.0, -0.6) 
    glRotatef(hair_rotation_left, 0.0, 0.0, 1.0)  # Rotação do cabelo esquerdo
    glScalef(0.5, 0.5, 0.5) 
    glutSolidOctahedron()
    glPopMatrix()

    # Desenha o chapéu
    glColor3f(0.0, 0.0, 1.0)  
    glTranslatef(-0.2, 0.25, -0.9)  # Posição da base do chapéu em relação ao rosto
    glRotatef(270, 1, 0, 0) 
    glutSolidCone(0.7, 1.4, 100, 100)

# Função para tratar eventos de teclado
def handle_keyboard_events(key, x, y):
    global head_rotation, hair_rotation_left, hair_rotation_right, head_animation_active, hair_animation_active

    if key == b'a':
        # Se a tecla 'a' for pressionada, inicia ou interrompe a animação da cabeça
        head_animation_active = not head_animation_active

    if key == b's':
        # Se a tecla 's' for pressionada, inicia ou interrompe a animação do cabelo
        hair_animation_active = not hair_animation_active

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -5.0)  
    glRotatef(head_rotation, 0.0, 1.0, 0.0) 

    draw_clown_face()

    glutSwapBuffers()

def update(value):
    global head_rotation, hair_rotation_left, hair_rotation_right

    if head_animation_active:
        head_rotation += 1.0

    if hair_animation_active:
        hair_rotation_left += 1.0
        hair_rotation_right += 1.0

    glutPostRedisplay() 
    glutTimerFunc(10, update, 0) 

# Função principal
def main():
    init()
    glutDisplayFunc(display)
    glutTimerFunc(10, update, 0)  
    glutKeyboardFunc(handle_keyboard_events)  
    glutMainLoop()

if __name__ == "__main__":
    main()
