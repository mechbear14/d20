from OpenGL.GL import *
import glm


class Vertex:
    def __init__(self, location, normal=None, tex_coord=None):
        self.location = location
        self.normal = normal
        self.tex_coord = tex_coord

    def set_normal(self, normal):
        self.normal = normal

    def set_texture(self, tex_coord):
        self.tex_coord = tex_coord

    def export(self):
        v = []
        v += [self.location.x, self.location.y, self.location.z]
        if self.normal is not None:
            v += [self.normal.x, self.normal.y, self.normal.z]
        if self.tex_coord is not None:
            v += [self.tex_coord.x, self.tex_coord.y]
        return v


class Shader:
    def __init__(self, file_path, kind):
        self.file_path = file_path
        self.kind = kind
        self.source = ""
        self.id = None
        try:
            with open(file_path) as file:
                self.source = file.read()
        except FileNotFoundError:
            print("No such file: {}".format(file_path))

    def compile(self):
        self.id = glCreateShader(self.kind)
        glShaderSource(self.id, self.source)
        glCompileShader(self.id)
        print(glGetShaderInfoLog(self.id))


class ShaderProgram:
    def __init__(self):
        self.shaders = []
        self.program = None

    def add_shader(self, shader):
        self.shaders.append(shader)

    def make(self):
        for shader in self.shaders:
            shader.compile()
        self.program = glCreateProgram()
        for shader in self.shaders:
            glAttachShader(self.program, shader.id)
        glLinkProgram(self.program)
        print(glGetProgramInfoLog(self.program))
        for shader in self.shaders:
            glDeleteShader(shader.id)

    def set_mat4(self, prop, mat4):
        loc = glGetUniformLocation(self.program, prop)
        glUniform4fv(loc, 1, glm.value_ptr(mat4))

    def set_vec3(self, prop, vec3):
        loc = glGetUniformLocation(self.program, prop)
        glUniform3fv(loc, 1, glm.value_ptr(vec3))

    def use(self):
        glUseProgram(self.program)


class Camera:
    def __init__(self, location, target, up):
        self.location = location
        self.target = glm.normalize(target)
        self.right = glm.normalize(glm.cross(target, up))
        self.up = glm.normalize(glm.cross(self.right, target))
        self.look_at = glm.lookAt(self.location, self.target, self.up)


class Lamp:
    def __init__(self, location, colour):
        self.location = location
        self.colour = colour

