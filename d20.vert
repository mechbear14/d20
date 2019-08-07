#version 430 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 normal;
out vec3 nNormal;
out vec3 fragLocation;

uniform mat4 world;
uniform mat4 view;
uniform mat4 projection;
uniform mat4 rotation;

void main(){
    fragLocation = vec3(world * rotation * vec4(aPos, 1.0));
    nNormal = vec3(rotation * vec4(normal, 1.0));
    gl_Position = projection * view * vec4(fragLocation, 1.0);
}