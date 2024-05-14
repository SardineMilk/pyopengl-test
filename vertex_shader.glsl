#version 330

in vec3 in_vert;
in vec3 in_color;

out vec3 frag_color;  // Output color to fragment shader

void main() {
    gl_Position = vec4(in_vert.x, in_vert.y, 0.0, 1.0);
    frag_color = in_color;
}
