#version 330

uniform mat4 m_proj;
uniform mat4 m_view;

in vec3 in_vert;
in vec2 in_texture_coord;

out vec2 texture_coord;

void main() {
    texture_coord = in_texture_coord;
    gl_Position = m_proj * m_view * vec4(in_vert, 1.0);
}
