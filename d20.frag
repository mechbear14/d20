#version 430 core

out vec4 Colour;

uniform vec3 aColour;
uniform vec3 lightColour;

void main(){
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColour;
    vec3 ambientColour = ambient * aColour;
    Colour = vec4(ambientColour, 1.0);
}