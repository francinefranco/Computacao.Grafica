import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Configuração inicial da câmera
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

glutInit()

# Variáveis para a posição das rodas
wheel_left_x = -0.75
wheel_right_x = 0.75

# Variáveis para a rotação das rodas
wheel_left_rotation = 0.0
wheel_right_rotation = 0.0

# Velocidade de movimento e rotação das rodas
movement_speed = 0.05
rotation_speed = 2.0

# Função para desenhar a lataria do carro (retangulo)
def draw_rectangle(width, height, x_center):
    glBegin(GL_QUADS)
    glVertex3f(x_center - width / 2, -height / 2, 0.0) 
    glVertex3f(x_center + width / 2, -height / 2, 0.0)  
    glVertex3f(x_center + width / 2, height / 2, 0.0)  
    glVertex3f(x_center - width / 2, height / 2, 0.0)  
    glEnd()

# Função para desenhar uma roda (quadrado)
def draw_wheel(size, rotation_angle, x_position):
    glPushMatrix()
    glTranslatef(x_position, -1.5 * size, 0.0)  # Posição da roda
    glRotatef(rotation_angle, 0.0, 0.0, 1.0)  # Rotação da roda
    glBegin(GL_QUADS)
    glVertex2f(-size / 2, -size / 2) 
    glVertex2f(size / 2, -size / 2)
    glVertex2f(size / 2, size / 2)  
    glVertex2f(-size / 2, size / 2)  
    glEnd()
    glPopMatrix()

# Função para atribuir entradas do teclado
def handle_keyboard_events():
    global wheel_left_x, wheel_right_x, wheel_left_rotation, wheel_right_rotation

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        wheel_left_x -= movement_speed
        wheel_right_x -= movement_speed
        wheel_left_rotation += rotation_speed
        wheel_right_rotation += rotation_speed
    elif keys[pygame.K_RIGHT]:
        wheel_left_x += movement_speed
        wheel_right_x += movement_speed
        wheel_left_rotation -= rotation_speed
        wheel_right_rotation -= rotation_speed

# Função principal
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        handle_keyboard_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glColor3f(0.0, 0.0, 1.0)

        glPushMatrix()
        x_center = (wheel_left_x + wheel_right_x) / 2 
        glTranslatef(x_center, 0.0, 0.0) 
        draw_rectangle(2.0, 1.0, 0.0)  
        glPopMatrix()

        glColor3f(0.0, 1.0, 0.0) 

        # Roda esquerda
        glPushMatrix()
        draw_wheel(0.35, wheel_left_rotation, wheel_left_x)  # Tamanho, rotação e posição da roda esquerda
        glPopMatrix()

        # Roda direita
        glPushMatrix()
        draw_wheel(0.35, wheel_right_rotation, wheel_right_x)  # Tamanho, rotação e posição da roda direita
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

main()
