import pygame
from pygame.locals import *
from OpenGL.GL import *
import sys
from shapes import D20

pygame.init()
screen = pygame.display.set_mode((600, 600), flags=DOUBLEBUF | OPENGL)
# pygame.draw.rect(screen, (0, 0, 0), (0, 0, 960, 540))
dice = D20(0, 0, 0, 0.5)
dice.compile()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    dice.rotate(pygame.time.get_ticks() * 0.05)
    dice.render()
    pygame.display.flip()
