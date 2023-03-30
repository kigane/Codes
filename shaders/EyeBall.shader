#define PI 3.14159265359
#define TWO_PI 6.28318530718

const mat2 m = mat2( 0.80,  0.60, -0.60,  0.80 );

float hash( float n )
{
    return fract(sin(n)*43.7585453);
}

float noise( in vec2 x )
{
    vec2 p = floor(x);
    vec2 f = fract(x);

    f = f*f*(3.0-2.0*f);

    float n = p.x + p.y*57.0;

    return mix(mix( hash(n+  0.0), hash(n+  1.0),f.x),
               mix( hash(n+ 57.0), hash(n+ 58.0),f.x),f.y);
}

float fbm( vec2 p )
{
    float f = 0.0;

    f += 0.50000*noise( p ); p = m*p*2.02;
    f += 0.25000*noise( p ); p = m*p*2.03;
    f += 0.12500*noise( p ); p = m*p*2.01;
    f += 0.06250*noise( p ); p = m*p*2.04;
    f += 0.03125*noise( p );

    return f/0.984375;
}

void main()
{
    float time = iGlobalTime * 1.0;
    vec2 uv = gl_FragCoord.xy / iResolution.xy * vec2(iResolution.x/iResolution.y, 1.0);
    vec2 p = uv * 2. - 1.;

    float bg = smoothstep(-0.25, 0.25, p.x);
    p.x -= 0.75;

    float r = length(p);
    float a = atan(p.y, p.x);
    
    vec3 col = vec3(1.);

    float ss = 0.5 + 0.5*sin(2.*time);
    float anim = 1. + 0.1*ss*clamp(1. - r, 0., 1.);
    r *= anim;

    if (r < 0.8)
    {
        col = vec3(0.2, 0.3, 0.4);

        // 噪音底色
        float f = fbm(p * 5.);
        col = mix(col, vec3(0.2, 0.5, 0.4), f);
        // 加一点黄色瞳仁
        f = 1. - smoothstep(0.25, 0.5, r);
        col = mix(col, vec3(0.9, 0.6, 0.2), f);
        // 加一点噪音扭曲
        a += 0.5*fbm(p);
        // 白色瞳丝
        f = fbm(vec2(6.*r, 20.*a));
        f = smoothstep(0.33, 1.0, f);
        col = mix(col, vec3(1.), f);
        // 黑色瞳丝
        f = fbm(vec2(8.*r, 17.*a));
        f = smoothstep(0.4, 0.9, f);
        col *= 1. - 0.5*f;
        // 边缘
        f = smoothstep(0.6, 0.8, r);
        col *= 1. - 0.5 * f;
        // 黑色瞳孔
        f = smoothstep(0.2, 0.25, r);
        col *= f;
        // 添加高光
        f = 1. - smoothstep(0.0, 0.2, length(p - vec2(0.2, 0.2)));
        col += f * vec3(1., 0.9, 0.8) * 0.9;
        // 平滑
        f = smoothstep(0.77, 0.8, r);
        col = mix(col, vec3(1), f);
    }

    // Output to screen
    gl_FragColor  = vec4(col * bg,1.0);
}