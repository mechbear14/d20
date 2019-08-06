import pygame
from pygame.locals import *
from OpenGL.GL import *
import sys
from shapes import D20
from objects import Camera, Lamp
import glm

pygame.init()
screen = pygame.display.set_mode((960, 540), flags=DOUBLEBUF | OPENGL)
# pygame.draw.rect(screen, (0, 0, 0), (0, 0, 960, 540))
dice = D20(0, 0, -2, 0.2)
dice.compile()
perspective = glm.perspective(glm.radians(45), 960 / 540, 0.1, 2000)
camera = Camera(glm.vec3(0, 0, 0.5), glm.vec3(0, 0, -100), glm.vec3(0, 1, 0))
view = camera.get_matrix()
model = glm.translate(glm.mat4(1.0), dice.location)
lamp = Lamp(glm.vec3(0, 0.5, 1), glm.vec3(0.0, 1.0, 1.0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    dice.render(model, view, perspective, lamp.colour)
    pygame.display.flip()
