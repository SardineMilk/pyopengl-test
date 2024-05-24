from settings import *
from cube_mesh import *
import numpy

# Parallel arrays
loaded_chunks_pos = [(0, 0, 0), 
                     (0, 1, 0),
                     (1, 0, 0),
                     (0, 0, 1),]
loaded_chunks_data = [numpy.ones([CHUNK_SIZE, CHUNK_SIZE, CHUNK_SIZE], dtype=int), 
                      numpy.ones([CHUNK_SIZE, CHUNK_SIZE, CHUNK_SIZE], dtype=int),
                      numpy.ones([CHUNK_SIZE, CHUNK_SIZE, CHUNK_SIZE], dtype=int), 
                      numpy.ones([CHUNK_SIZE, CHUNK_SIZE, CHUNK_SIZE], dtype=int),]


def generate_chunk_mesh(chunk_pos, chunk_data):
    chunk_pos = glm.vec3(chunk_pos)
    chunk_mesh = []

    for relative_x in range(CHUNK_SIZE):
        for relative_y in range(CHUNK_SIZE):
            for relative_z in range(CHUNK_SIZE):
                world_pos = glm.vec3(chunk_pos.x*CHUNK_SIZE + relative_x, 
                             chunk_pos.y*CHUNK_SIZE + relative_y, 
                             chunk_pos.z*CHUNK_SIZE + relative_z )

                surrounding_voxels = [
                    get_voxel_data(world_pos+glm.vec3(0.0, 0.0, 1.0)),
                    get_voxel_data(world_pos+glm.vec3(1.0, 0.0, 0.0)),
                    get_voxel_data(world_pos+glm.vec3(0.0, 0.0, -1.0)),
                    get_voxel_data(world_pos+glm.vec3(-1.0, 0.0, 0.0)),
                    get_voxel_data(world_pos+glm.vec3(0.0, 1.0, 0.0)),
                    get_voxel_data(world_pos+glm.vec3(0.0, -1.0, 0.0))
                ]

                voxel_mesh = generate_voxel_mesh(world_pos, surrounding_voxels)
                chunk_mesh.extend(voxel_mesh)
    
    return chunk_mesh


def generate_world_mesh():
    world_mesh = []

    for i in range(len(loaded_chunks_pos)):
        chunk_pos = loaded_chunks_pos[i]
        chunk_data = loaded_chunks_data[i]
        
        world_mesh.extend(generate_chunk_mesh(chunk_pos, chunk_data))

    return numpy.array(world_mesh, dtype="f4")


def get_voxel_data(world_pos):
    chunk_pos, local_pos = world_to_local(world_pos)

    if chunk_pos not in loaded_chunks_pos:
        return 0

    chunk_index = loaded_chunks_pos.index(chunk_pos)
    chunk_data = loaded_chunks_data[chunk_index]

    voxel_type = chunk_data[int(local_pos.x), int(local_pos.y), int(local_pos.z)]

    return voxel_type



def set_voxel_data(world_pos, voxel_type):
    chunk_pos, local_pos = world_to_local(world_pos)

    if chunk_pos in loaded_chunks_pos:
        chunk_index = loaded_chunks_pos.index(chunk_pos)
        print(loaded_chunks_data[chunk_index][int(local_pos.x), int(local_pos.y), int(local_pos.z)])
        loaded_chunks_data[chunk_index][int(local_pos.x), int(local_pos.y), int(local_pos.z)] = voxel_type
        print(loaded_chunks_data[chunk_index][int(local_pos.x), int(local_pos.y), int(local_pos.z)])




def world_to_local(world_pos):
    world_pos = glm.vec3(world_pos)
    chunk_pos = world_pos // CHUNK_SIZE
    local_pos = world_pos % CHUNK_SIZE

    return chunk_pos, local_pos


def load_chunk(chunk_pos):
    pass
