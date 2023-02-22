#define PI 3.14159265359
#define TWO_PI 6.28318530718

float N21(vec2 p){
    return fract(sin(p.x * 100. + p.y * 6547.) * 5647.);
}

float SmoothNoise(vec2 p){
    vec2 lv = fract(p);
    lv = lv*lv*(3.-2.*lv); // 直线->平滑S型曲线
    vec2 id = floor(p);

    float bl = N21(id);
    float br = N21(id + vec2(1, 0));
    float b = mix(bl, br, lv.x);
    
    float tl = N21(id + vec2(0, 1));
    float tr = N21(id + vec2(1, 1));
    float t = mix(tl, tr, lv.x);

    return mix(b, t, lv.y);
}

float SmoothNoise2(vec2 p){
    float c = SmoothNoise(p * 4.);
    c += SmoothNoise(p * 8.) * 0.5;    
    c += SmoothNoise(p * 16.) * 0.25;    
    c += SmoothNoise(p * 32.) * 0.125;    
    c += SmoothNoise(p * 65.) * 0.0625; 
    c /= 2.;
    return c;
}

void main()
{
    float time = iGlobalTime * 1.0;
    vec2 uv = gl_FragCoord.xy / iResolution.xy * vec2(iResolution.x/iResolution.y, 1.0);

    // uv += time * 0.1;
    float c = SmoothNoise2(uv);
    vec3 col = vec3(0.);
    col = vec3(c);

    // Output to screen
    gl_FragColor  = vec4(col,1.0);
}
