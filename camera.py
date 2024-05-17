from settings import *
import pygame

class Camera:
    def __init__(self, position, yaw, pitch) -> None:
        self.position = glm.vec3(position)
        self.yaw = yaw
        self.pitch = pitch

        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)

        self.m_proj = glm.perspective(V_FOV, ASPECT_RATIO, NEAR, FAR)
        self.m_view = glm.mat4()

    def update(self):
        self.update_vectors()
        self.update_view_matrix()

    def update_view_matrix(self):
        self.m_view = glm.lookAt(self.position, self.position + self.forward, self.up)

    def update_vectors(self):
        # Update the camera vectors based on view direction
        self.forward.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.forward.y = glm.sin(self.pitch)
        self.forward.z = glm.sin(self.yaw) * glm.cos(self.pitch)
        self.forward = glm.normalize(self.forward)

        # Use the cross product to calculate up and right vectors
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def move_camera(self, keys, speed):

        if keys[pygame.K_w]:  # Move forward
            self.move_forward(speed)
        if keys[pygame.K_s]:  # Move backward
            self.move_back(speed)
        if keys[pygame.K_d]:  # Strafe left
            self.move_right(speed)
        if keys[pygame.K_a]:  # Strafe right
            self.move_left(speed)
        if keys[pygame.K_SPACE]:  # Move up
            self.move_up(speed)
        if keys[pygame.K_LSHIFT]:  # Move down
            self.move_down(speed)



    def rotate_pitch(self, delta_y):
        self.pitch -= delta_y * PLAYER_ROTATION_SPEED
        self.pitch = glm.clamp(self.pitch, -PITCH_CLAMP, PITCH_CLAMP)
    
    def rotate_yaw(self, delta_x):
        self.yaw += delta_x * PLAYER_ROTATION_SPEED

    def move_left(self, velocity):
        self.position -= self.right * velocity
    
    def move_right(self, velocity):
        self.position += self.right * velocity

    def move_up(self, velocity):
        self.position += self.up * velocity

    def move_down(self, velocity):
        self.position -= self.up * velocity

    def move_forward(self, velocity):
        self.position += self.forward * velocity

    def move_back(self, velocity):  
        self.position -= self.forward * velocity