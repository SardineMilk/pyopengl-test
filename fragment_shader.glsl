#version 330

uniform sampler2D Texture;
in vec2 texture_coord;

out vec4 fragColor;

void main() {
    fragColor = texture(Texture, texture_coord);
}
