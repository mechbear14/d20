from math import sqrt
from OpenGL.GL import *
from ctypes import c_float
import glm
from objects import Vertex


class D20:
    def __init__(self, location, size):
        self.location = location
        self.size = size
        self.vbo = None
        self.vao = None

        unit = self.size / sqrt(5)
        self.vertices = [2, 1, 0, 2, -1, 0, -2, -1, 0, -2, 1, 0,
                         1, 0, 2, 1, 0, -2, -1, 0, -2, -1, 0, 2,
                         0, 2, 1, 0, 2, -1, 0, -2, -1, 0, -2, 1]
        for i in range(len(self.vertices)):
            self.vertices[i] *= unit

        self.elements = [1, 10, 9, 1, 9, 5, 1, 5, 2, 1, 2, 6, 1, 6, 10,
                         3, 8, 4, 3, 12, 8, 3, 11, 12, 3, 7, 11, 3, 4, 7,
                         10, 4, 9, 4, 8, 9, 9, 8, 5, 5, 8, 12, 2, 5, 12,
                         2, 12, 11, 11, 6, 2, 7, 6, 11, 10, 6, 7, 4, 10, 7]
        for t in range(len(self.elements)):
            self.elements[t] -= 1

        self.vertex_buffer = []
        for e in range(0, len(self.elements), 3):
            base_ids = self.elements[e: e+3]
            vectors = [glm.vec3(*self.vertices[b*3: b*3+3]) for b in base_ids]
            for v in vectors:
                self.vertex_buffer += Vertex(v).export()
            # v1 = glm.vec3(*self.vertices[e*3: e*3+3])
            # v2 = glm.vec3(*self.vertices[(e+1)*3: (e+1)*3+3])
            # v3 = glm.vec3(*self.vertices[(e+2)*3: (e+2)*3+3])
            # # normal = glm.cross(v1-v2, v1-v3)
            # # self.vertex_buffer += Vertex(v1, normal).export()
            # # self.vertex_buffer += Vertex(v2, normal).export()
            # # self.vertex_buffer += Vertex(v3, normal).export()
            # self.vertex_buffer += Vertex(v1).export()
            # self.vertex_buffer += Vertex(v2).export()
            # self.vertex_buffer += Vertex(v3).export()

    def make(self):
        vertex_buf = (GLfloat * len(self.vertex_buffer))(*self.vertex_buffer)
        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, sizeof(vertex_buf), vertex_buf, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(c_float), None)
        # glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(c_float), None)
        # glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(c_float), 3 * sizeof(c_float))
        glEnableVertexAttribArray(0)

# class D20:
#     def __init__(self, x, y, z, r):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.r = r
#
#         # TODO: Use this first
#         self.location = glm.vec3(x, y, z)
#
#         l = r / sqrt(5)
#         self.vertices = [2, 1, 0, 2, -1, 0, -2, -1, 0, -2, 1, 0,
#                          1, 0, 2, 1, 0, -2, -1, 0, -2, -1, 0, 2,
#                          0, 2, 1, 0, 2, -1, 0, -2, -1, 0, -2, 1]
#         for i in range(len(self.vertices)):
#             self.vertices[i] *= l
#             if i % 3 == 0:
#                 self.vertices[i] += x
#             elif i % 3 == 1:
#                 self.vertices[i] += y
#             elif i % 3 == 2:
#                 self.vertices[i] += z
#
#         self.elements = [1, 10, 9, 1, 9, 5, 1, 5, 2, 1, 2, 6, 1, 6, 10,
#                          3, 8, 4, 3, 12, 8, 3, 11, 12, 3, 7, 11, 3, 4, 7,
#                          10, 4, 9, 4, 8, 9, 9, 8, 5, 5, 8, 12, 2, 5, 12,
#                          2, 12, 11, 11, 6, 2, 7, 6, 11, 10, 6, 7, 4, 10, 7]
#         for t in range(len(self.elements)):
#             self.elements[t] -= 1
#
#         self.program = None
#         self.vao = None
#         self.rot = 0
#
#         # self.attributes = []
#         # get_attribute(self.vertices, self.attributes, 0, 3, 3)
#
#     def compile(self):
#         vert = """#version 430 core
#         layout (location = 0) in vec3 aPos;
#
#         uniform mat4 world;
#         uniform mat4 view;
#         uniform mat4 projection;
#
#         void main(){
#             gl_Position = projection * view * world * vec4(aPos, 1.0);
#         }
#         """
#         frag = """#version 430 core
#         out vec4 Colour;
#
#         uniform vec3 aColour;
#         uniform vec3 lightColour;
#
#         void main(){
#             float ambientStrength = 0.1;
#             vec3 ambient = ambientStrength * lightColour;
#             vec3 ambientColour = ambient * aColour;
#             Colour = vec4(ambientColour, 1.0);
#         }
#         """
#         vs = glCreateShader(GL_VERTEX_SHADER)
#         glShaderSource(vs, vert)
#         glCompileShader(vs)
#         print(glGetShaderInfoLog(vs))
#         fs = glCreateShader(GL_FRAGMENT_SHADER)
#         glShaderSource(fs, frag)
#         glCompileShader(fs)
#         print(glGetShaderInfoLog(fs))
#         self.program = glCreateProgram()
#         glAttachShader(self.program, vs)
#         glAttachShader(self.program, fs)
#         glLinkProgram(self.program)
#         print(glGetProgramInfoLog(self.program))
#
#         vertex_buf = (GLfloat * len(self.vertices))(*self.vertices)
#         element_buf = (GLuint * len(self.elements))(*self.elements)
#         self.vao = glGenVertexArrays(1)
#         vbo = glGenBuffers(1)
#         ebo = glGenBuffers(1)
#         glBindVertexArray(self.vao)
#         glBindBuffer(GL_ARRAY_BUFFER, vbo)
#         glBufferData(GL_ARRAY_BUFFER, sizeof(vertex_buf), vertex_buf, GL_STATIC_DRAW)
#         glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
#         glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(element_buf), element_buf, GL_STATIC_DRAW)
#         glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3*sizeof(c_float), None)
#         glEnableVertexAttribArray(0)
#
#     # def render(self, screen):
#         # draw_elements(3, self.attributes, self.elements, screen, 0, floor(len(self.elements) / 3))
#     def render(self, world, view, projection, lamp):
#         glUseProgram(self.program)
#         glBindVertexArray(self.vao)
#         world_loc = glGetUniformLocation(self.program, "world")
#         glUniformMatrix4fv(world_loc, 1, GL_FALSE, glm.value_ptr(world))
#         view_loc = glGetUniformLocation(self.program, "view")
#         glUniformMatrix4fv(view_loc, 1, GL_FALSE, glm.value_ptr(view))
#         proj_loc = glGetUniformLocation(self.program, "projection")
#         glUniformMatrix4fv(proj_loc, 1, GL_FALSE, glm.value_ptr(projection))
#         light_colour_loc = glGetUniformLocation(self.program, "lightColour")
#         glUniform3fv(light_colour_loc, 1, glm.value_ptr(lamp))
#         colour_loc = glGetUniformLocation(self.program, "aColour")
#         glUniform3fv(colour_loc, 1, glm.value_ptr(glm.vec3(1.0, 0.5, 0.0)))
#         glDrawElements(GL_TRIANGLES, len(self.elements), GL_UNSIGNED_INT, None)
#
#     def rotate(self, a):
#         self.rot = a
