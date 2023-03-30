#define PI 3.14159265359
#define TWO_PI 6.28318530718

float HexDist(vec2 uv)
{
    uv = abs(uv);
    float d = dot(uv, normalize(vec2(1, 1.732)));
    d = max(d, uv.x);
    return d;
}

vec4 HexCoord(vec2 uv)
{
    vec2 gv;
    vec2 r = vec2(1.0, 1.732);
    vec2 h = 0.5 * r;
    vec2 a = mod(uv, r) - h;
    vec2 b = mod(uv - h, r) - h;

    if (length(a) < length(b))
        gv = a;
    else
        gv = b;

    // 将gv转换为极坐标
    float x = atan(gv.y, gv.x);
    float y = 0.5 - HexDist(gv);
    
    // 区分每个格子
    vec2 id = uv - gv;
    return vec4(x, y, id);
}

void main()
{
    float time = iGlobalTime * 1.0;
    vec2 uv = gl_FragCoord.xy / iResolution.xy * vec2(iResolution.x/iResolution.y, 1.0);
    uv -= vec2(0.5);
    vec3 col = vec3(0);

    uv *= 5.0;

    // float d = HexDist(abs(uv));
    // d = sin(d*10. + iTime);

    vec4 hc = HexCoord(uv);
    // col = vec3(hc.y);
    // col = vec3(0.5*(hc.x/TWO_PI + 1.));
    // col.rg = hc.zw * 0.1;

    col = vec3(smoothstep(0.05, 0.1, hc.y*sin(hc.z * hc.w + iTime)));

    // Output to screen
    gl_FragColor  = vec4(col,1.0);
}