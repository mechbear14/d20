from math import sqrt, floor
from temp_gl import *


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

        self.attributes = []
        get_attribute(self.vertices, self.attributes, 0, 3, 3)

    def render(self, screen):
        draw_elements(3, self.attributes, self.elements, screen, 0, floor(len(self.elements) / 3))
