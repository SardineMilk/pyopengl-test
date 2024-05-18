from settings import *
from camera import Camera
from cube_mesh import *

import pygame
import moderngl
import numpy
import sys
import glm
import random
from PIL import Image

"""
import profiler
profiler.profiler().start(True)
"""
class VoxelEngine:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((1600, 900), flags=pygame.OPENGL | pygame.DOUBLEBUF) 
        self.context = moderngl.create_context()

        self.context.enable(flags=moderngl.DEPTH_TEST | moderngl.CULL_FACE | moderngl.BLEND)
        self.context.gc_mode = "auto"  # Enable garbage collection

        # Read the shader code
        with open("vertex_shader.glsl", "r") as file:
            self.vertex_shader = file.read()
        with open("fragment_shader.glsl", "r") as file:
            self.fragment_shader = file.read()

        # Compile shaders
        self.shader_program = self.context.program(vertex_shader=self.vertex_shader, fragment_shader=self.fragment_shader)

        self.vertex_array = generate_voxel_mesh()
                
        # Load an image using PIL
        image = Image.open('cobblestone.png')
        img_data = image.convert('RGBA').tobytes()
        width, height = image.size

        # Create a texture
        self.texture = self.context.texture((width, height), 4, data=img_data)
        self.texture.use()

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

        self.vertex_buffer = self.context.buffer(self.vertex_array)  # Call each time mesh changes
    
        vertex_object = self.context.vertex_array(self.shader_program, self.vertex_buffer, "in_vert", "in_texture_coord")

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

if __name__ == "__main__":
    main = VoxelEngine()
    main.run()