#version 330

uniform mat4 m_proj;
uniform mat4 m_view;

in vec3 in_vert;
in vec3 in_color;

out vec3 frag_color;  // Output color to fragment shader

void main() {
    gl_Position = m_proj * m_view * vec4(in_vert, 1.0);
    frag_color = in_color;
}
