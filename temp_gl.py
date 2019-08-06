import pygame


def get_2d(x, y, z, w, h, p):
    bx = -z / p * w / 2
    by = -z / p * h / 2
    render_x = bx + (1 + z / p) * x
    render_y = by + (1 + z / p) * y
    return render_x, render_y


def get_attribute(vertices, attributes, start, length, stride):
    for i in range(start, len(vertices) - 1, stride):
        temp = []
        for j in range(length):
            temp.append(vertices[i+j])
        attributes.append(temp)


def draw_elements(size, attributes, elements, screen, start, num):
    for s in range(start, num*size, size):
        # element = []
        # for i in range(size):
        #     element.append(tuple(attributes[elements[s+i]]))
        element = [tuple(attributes[elements[s+i]]) for i in range(size)]
        pixels = [get_2d(*e, screen.get_width(), screen.get_height(), 2000) for e in element]
        pygame.draw.aalines(screen, (255, 255, 255), True, pixels)
