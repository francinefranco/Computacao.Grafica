import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, -3.0, -10) 

glutInit()

# Variáveis para o ângulo de rotação dos bracos e pernas
arm_rotation = 0.0
leg_rotation = 0.0

def draw_rectangle(width, height):
    half_width = width / 2
    half_height = height / 2

    glBegin(GL_QUADS)
    glVertex3f(-half_width, -half_height, 0.0)  
    glVertex3f(half_width, -half_height, 0.0)  
    glVertex3f(half_width, half_height, 0.0)   
    glVertex3f(-half_width, half_height, 0.0)   
    glEnd()

# Função para desenhar o robô
def draw_robot():
    glColor3f(0.0, 0.0, 1.0) 
    glPushMatrix()
    glTranslatef(0.0, 0.25, 0.0)  # Posição da cabeça
    draw_rectangle(0.15, 0.15)  # Tamanho da cabeça (quadrado)
    glPopMatrix()

    glColor3f(1.0, 1.0, 0.0) 
    glPushMatrix()
    glTranslatef(0.0, 0.16, 0.0)  # Posição do pescoço
    draw_rectangle(0.02, 0.025)  # Tamanho do pescoço (retângulo)
    glPopMatrix()

    glColor3f(0.0, 0.0, 1.0) 
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)  # Posição do tronco
    draw_rectangle(0.1, 0.3)  # Tamanho do tronco (retângulo)
    glPopMatrix()

    glColor3f(1.0, 0.0, 0.0)  
    glPushMatrix()
    glTranslatef(-0.03, -0.07, 0.0)  # Posição da perna esquerda
    glTranslatef(0.0, -0.09, 0.0)  # Ajuste para o ponto fixo de rotação
    glRotatef(leg_rotation, 0.0, 0.0, 1.0)  # Rotação da perna esquerda
    glTranslatef(0.0, -0.09, 0.0)  # Ajuste para restaurar a posição do ponto fixo de rotação
    draw_rectangle(0.04, 0.18)  # Tamanho da perna (retângulo)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.03, -0.07, 0.0)  # Posição da perna direita
    glTranslatef(0.0, -0.09, 0.0)  # Ajuste para o ponto fixo de rotação
    glRotatef(-leg_rotation, 0.0, 0.0, 1.0)  # Rotação da perna direita
    glTranslatef(0.0, -0.09, 0.0)  # Ajuste para restaurar a posição do ponto fixo de rotação
    draw_rectangle(0.04, 0.18)  # Tamanho da perna (retângulo)
    glPopMatrix()

    glColor3f(1.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(-0.075, 0.22, 0.0)  # Posição do braço esquerdo
    glTranslatef(0.0, -0.075, 0.0)  # Ajuste para o ponto fixo de rotação
    glRotatef(arm_rotation, 0.0, 0.0, 1.0)  # Rotação do braço esquerdo
    glTranslatef(0.0, -0.075, 0.0)  # Ajuste para restaurar a posição do ponto fixo de rotação
    draw_rectangle(0.03, 0.15)  # Tamanho do braço (retângulo)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.075, 0.22, 0.0)  # Posição do braço direito
    glTranslatef(0.0, -0.075, 0.0)  # Ajuste para o ponto fixo de rotação
    glRotatef(-arm_rotation, 0.0, 0.0, 1.0)  # Rotação do braço direito
    glTranslatef(0.0, -0.075, 0.0)  # Ajuste para restaurar a posição do ponto fixo de rotação
    draw_rectangle(0.03, 0.15)  # Tamanho do braço (retângulo)
    glPopMatrix()

# Função para atribuir entradas do teclado
def handle_keyboard_events():
    global arm_rotation, leg_rotation

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        arm_rotation += 1.0
        leg_rotation += 1.0
    elif keys[pygame.K_RIGHT]:
        arm_rotation -= 1.0
        leg_rotation -= 1.0

# Função principal
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        handle_keyboard_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        draw_robot()

        pygame.display.flip()
        pygame.time.wait(10)

main()
