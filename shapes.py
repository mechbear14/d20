from math import sqrt
from OpenGL.GL import *
from ctypes import c_float, c_void_p
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
            vs = [glm.vec3(*self.vertices[b*3: b*3+3]) for b in base_ids]
            normal = glm.cross(glm.vec3(vs[0] - vs[1]), glm.vec3(vs[0] - vs[2]))
            for v in vs:
                self.vertex_buffer += Vertex(v, normal).export()
        # print(self.vertex_buffer)

    def make(self):
        vertex_buf = (GLfloat * len(self.vertex_buffer))(*self.vertex_buffer)
        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, sizeof(vertex_buf), vertex_buf, GL_STATIC_DRAW)
        # glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(c_float), None)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(c_float), c_void_p(0))
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(c_float), c_void_p(3*sizeof(c_float)))
        glEnableVertexAttribArray(1)
