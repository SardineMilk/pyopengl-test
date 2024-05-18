import numpy
def generate_voxel_mesh():
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

    vertex_data = get_data(vertices, indices)
    

    tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
    tex_coord_indices = [
        (0, 2, 3), (0, 1, 2),
        (0, 2, 3), (0, 1, 2),
        (0, 1, 2), (2, 3, 0),
        (2, 3, 0), (2, 0, 1),
        (0, 2, 3), (0, 1, 2),
        (3, 1, 2), (3, 0, 1),
    ]

    voxel_data = []
    for i in range(len(indices)):
        for j in range(3):
            vertex = vertices[indices[i][j]]
            tex_coord = tex_coord_vertices[tex_coord_indices[i][j]]
            vertex_data = list(vertex) + list(tex_coord)
            voxel_data += vertex_data

    #tex_coord_data = get_data(tex_coord_vertices, tex_coord_indices)
    #voxel_data = numpy.hstack([vertex_data, tex_coord_data])
    return numpy.array(voxel_data, dtype="f4")


def get_data(vertices, indices):
    data = [vertices[ind] for triangle in indices for ind in triangle]
    return numpy.array(data, dtype='float16')

