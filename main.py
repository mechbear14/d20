import pygame
import sys
from shapes import D20

screen = pygame.display.set_mode((960, 540))
pygame.draw.rect(screen, (0, 0, 0), (0, 0, 960, 540))
dice = D20(100, 100, 0, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    dice.render(screen)
    pygame.display.flip()
