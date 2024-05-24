import numpy
from settings import *

vertices = [
    (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1),
    (0, 1, 0), (0, 0, 0), (1, 0, 0), (1, 1, 0)
]
indices = [
    (0, 2, 3), (0, 1, 2),
    (1, 7, 2), (1, 6, 7),
    (6, 5, 4), (4, 7, 6),
    (3, 4, 5), (3, 5, 0),
    (3, 7, 4), (3, 2, 7),
    (0, 6, 1), (0, 5, 6)
]
normals = [
    (0.0, 0.0, 1.0),
    (0.0, 0.0, 1.0),
    (1.0, 0.0, 0.0),
    (1.0, 0.0, 0.0),
    (0.0, 0.0, -1.0),
    (0.0, 0.0, -1.0),
    (-1.0, 0.0, 0.0),
    (-1.0, 0.0, 0.0),
    (0.0, -1.0, 0.0),
    (0.0, -1.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 1.0, 0.0)
]

tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
tex_coord_indices = [
    (0, 2, 3), (0, 1, 2),
    (0, 2, 3), (0, 1, 2),
    (0, 1, 2), (2, 3, 0),
    (2, 3, 0), (2, 0, 1),
    (0, 2, 3), (0, 1, 2),
    (3, 1, 2), (3, 0, 1),
]

def generate_voxel_mesh(position, surrounding_voxels):
    voxel_data = []
    for i in range(len(indices)):
        if surrounding_voxels[i//2] == 0:
            for j in range(3):
                vertex = glm.vec3(vertices[indices[i][j]])
                vertex = vertex + position

                tex_coord = tex_coord_vertices[tex_coord_indices[i][j]]

                vertex_data = list(vertex) + list(tex_coord)
                voxel_data += vertex_data

    return voxel_data

