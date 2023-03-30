#define PI 3.14159265359
#define TWO_PI 6.28318530718

void main()
{
    float time = iGlobalTime * 1.0;
    vec2 uv = gl_FragCoord.xy / iResolution.xy;
    uv.x *= iResolution.x/iResolution.y;
    uv -= vec2(.5);
    uv = clamp(uv, -0.5, .5);

    uv *= 3.;

    vec3 col = vec3(0);
    float d = length(uv);
    float m = .02/d; // 更像光源
    // col += m;

    float rays = max(0., 1. - abs(uv.x * uv.y * 1000.));
    col += rays;

    // Output to screen
    gl_FragColor  = vec4(col, 1.0);
}