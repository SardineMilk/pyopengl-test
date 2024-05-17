from settings import *
from camera import Camera

import pygame
import moderngl
import numpy
import sys
import glm
import random

"""
import profiler
profiler.profiler().start(True)
"""
class VoxelEngine:
    def __init__(self):
        # Initialise pygame
        pygame.init()
        # Create opengl context
        pygame.display.set_mode((1600, 900), flags=pygame.OPENGL | pygame.DOUBLEBUF) 
        self.context = moderngl.create_context()

        self.context.enable(flags=moderngl.DEPTH_TEST | moderngl.CULL_FACE | moderngl.BLEND)
        self.context.gc_mode = "auto"

        # Read the shader code
        with open("vertex_shader.glsl", "r") as file:
            self.vertex_shader = file.read()
        with open("fragment_shader.glsl", "r") as file:
            self.fragment_shader = file.read()

        # Compile shaders
        self.shader_program = self.context.program(vertex_shader=self.vertex_shader, fragment_shader=self.fragment_shader)

        self.vertex_array = generate_tris()
        self.vertex_buffer = self.context.buffer(self.vertex_array)  # Call each time mesh changes
        self.camera = Camera((0, 2, 0), 0, 0)

        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        self.running = True

    def update(self):
        self.delta = self.clock.tick()
        self.fps = glm.clamp(self.clock.get_fps(), 1, 9999)
        self.time = pygame.time.get_ticks() * 0.001
        
        self.keys = pygame.key.get_pressed()

        mouse_dx, mouse_dy = pygame.mouse.get_rel()
        self.camera.rotate_yaw(mouse_dx)
        self.camera.rotate_pitch(mouse_dy)

        self.camera.move_camera(self.keys, PLAYER_SPEED/self.fps)
        self.camera.update()


    def render(self):
        self.context.clear(color=(0.0, 0.5, 0.5))
    
        self.shader_program["m_proj"].write(self.camera.m_proj)
        self.shader_program["m_view"].write(self.camera.m_view)
        vertex_object = self.context.simple_vertex_array(self.shader_program, self.vertex_buffer , "in_vert", "in_color")  # Call each frame / camera update

        vertex_object.render(moderngl.TRIANGLES)
        pygame.display.flip()
    


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(255)
        pygame.quit()
        sys.exit()

def generate_tris():
    # This is very temporary and will be replaced
    num_triangles = 1000
    vertex_array = []
    for i in range(0, num_triangles):
        vertex_data = []  # x, y, z, r, g, b * 3
        for j in range(0, 100):
            vertex = [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)]
            color = [random.random(), random.random(), random.random()]

            vertex_data += vertex
            vertex_data += color
        
        vertex_array += vertex_data

    vertex_array = numpy.array(vertex_array, dtype="f4")
    return vertex_array

if __name__ == "__main__":
    main = VoxelEngine()
    main.run()