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

# projection = glm.perspective(glm.radians(45), 960 / 540, 0.1, 2000)
# view = Camera(glm.vec3(0, 0, 0.5), glm.vec3(0, 0, -100), glm.vec3(0, 1, 0)).look_at
# model = glm.translate(glm.mat4(1.0), dice.location)

projection = view = model = glm.mat4(1.0)

# lamp = Lamp(glm.vec3(0, 0.5, 1), glm.vec3(0.0, 1.0, 1.0))

# dice = D20(0, 0, -2, 0.2)
# dice.compile()
# perspective = glm.perspective(glm.radians(45), 960 / 540, 0.1, 2000)
# camera = Camera(glm.vec3(0, 0, 0.5), glm.vec3(0, 0, -100), glm.vec3(0, 1, 0))
# view = camera.get_matrix()
# model = glm.translate(glm.mat4(1.0), dice.location)
# lamp = Lamp(glm.vec3(0, 0.5, 1), glm.vec3(0.0, 1.0, 1.0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    # dice.render(model, view, perspective, lamp.colour)
    dice_shader.use()
    glBindVertexArray(dice.vao)
    dice_shader.set_mat4("world", model)
    dice_shader.set_mat4("view", view)
    dice_shader.set_mat4("projection", projection)
    dice_shader.set_vec3("aColour", glm.vec3(0.0, 1.0, 0.0))
    dice_shader.set_vec3("lightColour", glm.vec3(1.0, 1.0, 1.0))
    glDrawArrays(GL_TRIANGLES, 0, 60)
    pygame.display.flip()
