import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Configuração inicial da câmera
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

glutInit()

petalas = 6

circle_radius = 0.3  # Raio do miolo da flor
scale_factor = 1.2   
# Ângulo de rotação para distribuir as petalas
angle_step = 360.0 / petalas
current_rotation_angle = 0
rotation_speed = 1.0 

# Função para desenhar um círculo
def draw_circle():
    glBegin(GL_POLYGON)
    num_segments = 50 
    for i in range(num_segments):
        theta = 2.0 * math.pi * float(i) / float(num_segments)
        x = circle_radius * math.cos(theta)
        y = circle_radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

# Função para atribuir entradas do teclado
def handle_keyboard_events():
    global current_rotation_angle
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        current_rotation_angle += rotation_speed
    elif keys[pygame.K_RIGHT]:
        current_rotation_angle -= rotation_speed

# Função principal
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        handle_keyboard_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glColor3f(1, 1, 0) 
        draw_circle()  

        glColor3f(1.0, 0.4, 0.4)

        for i in range(petalas):
            glPushMatrix()
            angle = i * angle_step + current_rotation_angle
            x = circle_radius * scale_factor * 2.0 * math.cos(math.radians(angle))
            y = circle_radius * scale_factor * 2.0 * math.sin(math.radians(angle))
            glTranslatef(x, y, 0.0)  # Translade para a posição desejada
            draw_circle() 
            glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

main()


