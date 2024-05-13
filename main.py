import pygame
import moderngl
import numpy

import profiler
profiler.profiler().start(True)


# Read the vertex shader code
with open("vertex_shader.glsl", "r") as file:
    vertex_shader = file.read()

# Read the fragment shader code
with open("fragment_shader.glsl", "r") as file:
    fragment_shader = file.read()


pygame.init()

# Create opengl context
pygame.display.set_mode((1600, 900), flags=pygame.OPENGL | pygame.DOUBLEBUF) 
context = moderngl.create_context()

# Compile shaders
shader_program = context.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

clock = pygame.time.Clock()
frames = 0

vertex_array = numpy.array([
    -0.6, -0.6, 
    0.6, -0.6, 
    0.0, 0.6
    ], dtype='f4')

vertex_buffer = context.buffer(vertex_array)
vertex_object = context.simple_vertex_array(shader_program, vertex_buffer , "in_vert")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    # Render
    context.clear(color=(0.0, 0.5, 0.5))

    shader_program['color'].value = (0.5, 0.0, 0.5, 1.0)

    vertex_object.render(moderngl.TRIANGLES)

    pygame.display.flip()

    clock.tick(255)