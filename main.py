import pygame
from pygame.locals import *
from OpenGL.GL import *
import sys
from shapes import D20
from objects import Shader, ShaderProgram, Camera, Lamp
import glm

pygame.init()
screen = pygame.display.set_mode((960, 540), flags=DOUBLEBUF | OPENGL)

dice = D20(glm.vec3(0, 0, -2), 0.5)
dice.make()
dice_shader = ShaderProgram()
dice_shader.add_shader(Shader("d20.vert", GL_VERTEX_SHADER))
dice_shader.add_shader(Shader("d20.frag", GL_FRAGMENT_SHADER))
dice_shader.make()

projection = glm.perspective(glm.radians(45), 960 / 540, 0.1, 2000)
camera = Camera(glm.vec3(0, 0, 0.5), glm.vec3(0, 0, -100), glm.vec3(0, 1, 0))
view = camera.look_at
model = glm.translate(glm.mat4(1.0), dice.location)

light = Lamp(glm.vec3(0.0, 0.0, 1.0), glm.vec3(1.0, 1.0, 1.0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    dice_shader.use()
    glBindVertexArray(dice.vao)
    dice_shader.set_mat4("world", model)
    dice_shader.set_mat4("view", view)
    dice_shader.set_mat4("projection", projection)
    dice_shader.set_mat4("rotation", glm.rotate(glm.mat4(1.0), glm.radians(pygame.time.get_ticks() * 0.1), glm.vec3(1.0, 1.0, 0.0)))
    dice_shader.set_vec3("aColour", glm.vec3(0.0, 0.5, 0.0))
    dice_shader.set_vec3("lightColour", light.colour)
    dice_shader.set_vec3("lightLocation", light.location)
    dice_shader.set_vec3("cameraLocation", camera.location)
    glDrawArrays(GL_TRIANGLES, 0, 60)
    pygame.display.flip()
