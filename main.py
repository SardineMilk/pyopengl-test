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

# Read the vertex shader code
with open("vertex_shader.glsl", "r") as file:
    vertex_shader = file.read()

# Read the fragment shader code
with open("fragment_shader.glsl", "r") as file:
    fragment_shader = file.read()

# Initialise pygame
pygame.init()

# Create opengl context
pygame.display.set_mode((1600, 900), flags=pygame.OPENGL | pygame.DOUBLEBUF) 
context = moderngl.create_context()

context.enable(flags=moderngl.DEPTH_TEST | moderngl.CULL_FACE | moderngl.BLEND)
context.gc_mode = "auto"

# Compile shaders
shader_program = context.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

clock = pygame.time.Clock()
frames = 0

num_triangles = 10

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


"""
# Test triangle
vertex_array = numpy.array([
    -0.5, -0.5, 1.0,   
    1.0, 0.0, 0.0,

    0.5, -0.5, 1.0,
    0.0, 1.0, 0.0,

    0.0, 0.5, 1.0,
    0.0 ,0.0, 1.0,     
    ], dtype="f4")
"""

vertex_buffer = context.buffer(vertex_array)  # Call each time mesh changes

camera = Camera((0, 0, 0), 0, 0)

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    delta = clock.tick()
    time = pygame.time.get_ticks() * 0.001

    mouse_dx, mouse_dy = pygame.mouse.get_rel()
    camera.rotate_yaw(mouse_dx)
    camera.rotate_pitch(mouse_dy)

    keys = pygame.key.get_pressed()
    
    camera.move_camera(keys, PLAYER_SPEED)
    camera.update()

    # Render
    context.clear(color=(0.0, 0.5, 0.5))
    
    shader_program["m_proj"].write(camera.m_proj)
    shader_program["m_view"].write(camera.m_view)
    vertex_object = context.simple_vertex_array(shader_program, vertex_buffer , "in_vert", "in_color")  # Call each frame / camera update

    vertex_object.render(moderngl.TRIANGLES, vertices=num_triangles*3)

    pygame.display.flip()
    clock.tick(255)