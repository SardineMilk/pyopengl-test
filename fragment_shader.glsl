#version 330

uniform sampler2D Texture;
in vec2 texture_coord;

out vec4 fragColor;

void main() {
    fragColor = texture(Texture, texture_coord);
    //fragColor = vec4(texture_coord, 1.0, 1.0);
}
