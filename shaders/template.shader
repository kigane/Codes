#define PI 3.14159265359
#define TWO_PI 6.28318530718

void main()
{
    float time = iGlobalTime * 1.0;
    vec2 uv = gl_FragCoord.xy / iResolution.xy * vec2(iResolution.x/iResolution.y, 1.0);

    float d = length(uv);
    
    vec3 col = vec3(d);

    // Output to screen
    gl_FragColor  = vec4(col,1.0);
}