#define PI 3.14159265359
#define TWO_PI 6.28318530718

vec2 N22(vec2 p){
    vec3 a = fract(p.xyx * vec3(123.34, 234.34, 345.65));
    a += dot(a, a + 34.45);
    return fract(vec2(a.x*a.y, a.y*a.z));
}

float manhatan_dist(vec2 p){
    return abs(p.x) + abs(p.y);
}

void main()
{
    float time = iGlobalTime * 1.0;
    vec2 uv = gl_FragCoord.xy / iResolution.xy * vec2(iResolution.x/iResolution.y, 1.0);
    uv -= vec2(.5);

    float m = 0.;
    float t = time * .8;

    float minDist = 100.;
    int cellIndex = 0;
    vec3 col = vec3(0);

    // Voronoi noise is a type of procedural noise that generates a pattern of cells, where each cell is associated with a specific value.
    // In Voronoi noise, each cell is defined as the region of space closest to a set of randomly placed points or "seeds". The value associated with each cell is typically based on the distance between the cell and its nearest seed point.
    // One interesting property of Voronoi noise is that it tends to create sharp, jagged edges between adjacent cells, which can be useful for creating textures that resemble natural patterns like cracked earth or rock formations. However, this can also make Voronoi noise more difficult to use in certain contexts, since the sharp edges can create noticeable artifacts when animated or viewed at certain scales.
    //In computer graphics, Voronoi noise is often used in combination with other types of noise, such as Perlin or Simplex noise, to create more complex and interesting procedural patterns. Voronoi noise can also be combined with other techniques, such as displacement mapping or procedural texturing, to create more detailed and realistic textures.

    // naive voronoi
    // for(int i = 1; i < 50; i++)
    // {
    //     vec2 n = N22(vec2(i));
    //     vec2 p = sin(n * t);
    //     float d = length(uv - p);
    //     m += smoothstep(.02, .01, d);
    //     if (minDist > d){
    //         minDist = d;
    //         cellIndex = i;
    //     }
    // }
    uv += vec2(.5);

    uv *= 3.;
    vec2 gv = fract(uv) - .5;
    vec2 id = floor(uv);
    vec2 cid = vec2(0);

    for (float y = -1.; y <= 1.; y++){
        for (float x = -1.; x <= 1.; x++){
            vec2 offset = vec2(x, y);
            vec2 n = N22(id + offset);
            vec2 p = offset + sin(n * t) * .5;
            float ed = length(p - gv);
            float md = manhatan_dist(p - gv);
            float d = mix(ed, md, sin(t) * 0.5 + 0.5);
            if (minDist > d)
            {
                minDist = d;
                cid = id + offset;
            }
        }
    }

    col = vec3(minDist);
    col.rg = cid * .1;
    
    // Output to screen
    gl_FragColor  = vec4(col,1.0);
}