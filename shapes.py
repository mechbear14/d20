from math import sqrt
from OpenGL.GL import *
from ctypes import c_float
import glm


class D20:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

        l = r / sqrt(5)
        self.vertices = [2, 1, 0, 2, -1, 0, -2, -1, 0, -2, 1, 0,
                         1, 0, 2, 1, 0, -2, -1, 0, -2, -1, 0, 2,
                         0, 2, 1, 0, 2, -1, 0, -2, -1, 0, -2, 1]
        for i in range(len(self.vertices)):
            self.vertices[i] *= l
            if i % 3 == 0:
                self.vertices[i] += x
            elif i % 3 == 1:
                self.vertices[i] += y
            elif i % 3 == 2:
                self.vertices[i] += z

        self.elements = [1, 10, 9, 1, 9, 5, 1, 5, 2, 1, 2, 6, 1, 6, 10,
                         3, 8, 4, 3, 12, 8, 3, 11, 12, 3, 7, 11, 3, 4, 7,
                         10, 4, 9, 4, 8, 9, 9, 8, 5, 5, 8, 12, 2, 5, 12,
                         2, 12, 11, 11, 6, 2, 7, 6, 11, 10, 6, 7, 4, 10, 7]
        for t in range(len(self.elements)):
            self.elements[t] -= 1

        self.program = None
        self.vao = None
        self.rot = 0

        # self.attributes = []
        # get_attribute(self.vertices, self.attributes, 0, 3, 3)

    def compile(self):
        vert = """#version 430 core
        layout (location = 0) in vec3 aPos;
        uniform mat4 rotation;
        
        void main(){
            gl_Position = rotation * vec4(aPos, 1.0);
        }
        """
        frag = """#version 430 core
        out vec4 Colour;
        
        void main(){
            Colour = vec4(0.0, 0.2, 0.0, 1.0);
        }
        """
        vs = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(vs, vert)
        glCompileShader(vs)
        print(glGetShaderInfoLog(vs))
        fs = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(fs, frag)
        glCompileShader(fs)
        print(glGetShaderInfoLog(fs))
        self.program = glCreateProgram()
        glAttachShader(self.program, vs)
        glAttachShader(self.program, fs)
        glLinkProgram(self.program)
        print(glGetProgramInfoLog(self.program))

        vertex_buf = (GLfloat * len(self.vertices))(*self.vertices)
        element_buf = (GLuint * len(self.elements))(*self.elements)
        self.vao = glGenVertexArrays(1)
        vbo = glGenBuffers(1)
        ebo = glGenBuffers(1)
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, sizeof(vertex_buf), vertex_buf, GL_STATIC_DRAW)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(element_buf), element_buf, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3*sizeof(c_float), None)
        glEnableVertexAttribArray(0)

    # def render(self, screen):
        # draw_elements(3, self.attributes, self.elements, screen, 0, floor(len(self.elements) / 3))
    def render(self):
        rotation = glGetUniformLocation(self.program, "rotation")
        unit = glm.mat4(1.0)
        rotation_mat = glm.rotate(unit, glm.radians(self.rot), glm.vec3(1.0, 0.0, 0.0))
        glUseProgram(self.program)
        glBindVertexArray(self.vao)
        glUniformMatrix4fv(rotation, 1, GL_FALSE, glm.value_ptr(rotation_mat))
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glDrawElements(GL_TRIANGLES, len(self.elements), GL_UNSIGNED_INT, None)

    def rotate(self, a):
        self.rot = a
