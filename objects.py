import glm


class Camera:
    def __init__(self, location, target, up):
        self.location = location
        self.target = target
        self.right = glm.normalize(glm.cross(target, up))
        self.up = glm.normalize(glm.cross(self.right, target))

    def get_matrix(self):
        return glm.lookAt(self.location, self.target, self.up)


class Lamp:
    def __init__(self, location, colour):
        self.location = location
        self.colour = colour
