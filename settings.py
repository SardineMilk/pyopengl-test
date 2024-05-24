import glm
import math


# Window
WINDOW_SIZE = glm.vec2(1600, 900)

# Camera
ASPECT_RATIO = WINDOW_SIZE.x / WINDOW_SIZE.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG) # Vertical fov
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)
NEAR = 0.1 # Near clipping plane
FAR = 2000.0
PITCH_CLAMP = glm.radians(89)

# Player
PLAYER_SPEED = 10
PLAYER_ROTATION_SPEED = 0.1

# Chunk
CHUNK_SIZE = 16
CHUNK_MID = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE ** 2
CHUNK_VOLUME = CHUNK_SIZE ** 3

