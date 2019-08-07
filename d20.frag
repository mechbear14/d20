#version 430 core

in vec3 nNormal;
in vec3 fragLocation;
out vec4 Colour;

uniform vec3 aColour;
uniform vec3 lightColour;
uniform vec3 lightLocation;
uniform vec3 cameraLocation;

void main(){
    float ambientStrength = 0.1;
    vec3 ambientColour = ambientStrength * lightColour;

    vec3 normal = normalize(nNormal);
    vec3 lightDirection = normalize(lightLocation - fragLocation);
    float diffuse = max(dot(normal, lightDirection), 0.0);
    vec3 diffuseColour = diffuse * lightColour;

    float specularStrength = 0.9;
    vec3 viewDirection = normalize(cameraLocation - fragLocation);
    vec3 reflectDirection = reflect(-lightDirection, normal);
    float spec = pow(max(dot(viewDirection, reflectDirection), 0.0), 256);
    vec3 specularColour = specularStrength * spec * lightColour;

    vec3 result = (ambientColour + diffuseColour + specularColour) * aColour;
    Colour = vec4(result, 1.0);
}