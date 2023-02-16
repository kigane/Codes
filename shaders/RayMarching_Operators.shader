#define PI 3.14159265359
#define TWO_PI 6.28318530718
#define MAX_STEPS 100
#define MAX_DIST 100.0
#define SURF_DIST 0.01
#define iTime iGlobalTime

float smin(float a, float b, float k)
{
    float h = clamp(0.5 + 0.5 * (b-a)/k, 0.0, 1.0);
    return mix(b, a, h) - k * h * (1.0 - h);
}

mat2 rotate2d(float a)
{
    float c = cos(a);
    float s = sin(a);
    return mat2(c, -s, s, c);
}

// line->capsule
float sdCapsule(vec3 p, vec3 a, vec3 b, float r)
{
    vec3 ab = b - a;
    vec3 ap = p - a;
    float t = dot(ap, ab) / dot(ab, ab);
    t = clamp(t, 0.0, 1.0); // 限制|ap| cos(theta) 超出ab的部分
    float d = length(p - (a + t*ab)) - r;
    return d;
}

// capsule->cylinder
float sdCylinder(vec3 p, vec3 a, vec3 b, float r)
{
    vec3 ab = b - a;
    vec3 ap = p - a;
    float t = dot(ap, ab) / dot(ab, ab);
    // t = clamp(t, 0.0, 1.0); 
    float x = length(p - (a + t*ab)) - r; // p 到 ab 所在直线的距离
    // 将ab上的点的t值变为负数。ab外的点的t值为正数。
    float y = (abs(t - 0.5) - 0.5) * length(ab);
    float exterior = length(max(vec2(x, y), 0.0));
    float interior = min(max(x, y), 0.0);
    return exterior + interior;
}

// 大圆+以大圆上点为圆心的小圆->torus
float sdTorus(vec3 p, vec2 r, vec3 pos)
{
    p -= pos;
    // 以原点为中心。
    float x = length(p.xz) - r.x;
    return length(vec2(x, p.y)) - r.y;
}

float sdBox(vec3 p, vec3 size)
{
    return length(max(abs(p) - size, 0.0));
}

float GetDist(vec3 p)
{
    // 球
    vec4 sph = vec4(3.0, 1.0, 6.0, 1.0);

    vec3 sp = p;
    sp -= vec3(0, 1, 0);
    sp *= vec3(1, 4, 1); // 缩放。 距离场拉伸会产生瑕疵
    float sph_dist = length(sp - sph.xyz) - sph.w;
    float sph_dist1 = length(p - vec3(1, 1, 6)) - 0.5;
    float sph_dist2 = length(p - vec3(0.5, 1, 6)) - 0.5;
    // 与立方体重合
    float sph_dist3 = length(p - vec3(-1.5, 1, 6)) - 2.0;
    // float sph_dist3 = length(p - vec3(-1.5, 1, 6)) - 1.0; // 有瑕疵

    // 平面
    float pla_dist = p.y;

    // 立方体
    vec3 bp = p;
    bp -= vec3(-1.5, 1.0, 6.0); // 平移
    bp.xz *= rotate2d(iTime); // 旋转
    float box_dist = sdBox(bp, vec3(1.0));

    // 最终距离
    float dist = min(pla_dist, sph_dist / 4.); // 恢复距离场。除以scale向量的最大值。
    // dist = min(dist, box_dist);

    // substraction
    // dist = min(dist, max(-sph_dist1, sph_dist2));

    // intersection
    // dist = min(dist, max(sph_dist1, sph_dist2));

    // Union
    // dist = min(dist, min(sph_dist1, sph_dist2));

    // Blend
    dist = min(dist, smin(sph_dist1, sph_dist2, 0.2));

    dist = min(dist, mix(sph_dist3, box_dist, 0.5 + 0.5 * sin(iTime)));

    return dist;
}

float RayMarching(vec3 ro, vec3 rd)
{
    float t = 0.0;

    for (int i = 0; i < MAX_STEPS; i++)
    {
        vec3 p = ro + t * rd;
        float dist = GetDist(p);
        t += dist;
        if (dist < SURF_DIST || t > MAX_DIST) break;
    }

    return t;
}

vec3 GetNormal(vec3 p)
{// 类似2维法线求法，在交点附近找两个极近的交点作差。
    float d = GetDist(p);
    vec2 e = vec2(0.01, 0);
    vec3 n = d - vec3( // delta_x, delta_y, delta_z
    GetDist(p - e.xyy),
    GetDist(p - e.yxy),
    GetDist(p - e.yyx)
    );
    return normalize(n);
}

float GetLight(vec3 p)
{
    vec3 lightPos = vec3(-1.0, 7.0, 4.0);
    // lightPos.xz += vec2(2.0*cos(iTime), 2.0*sin(iTime));
    vec3 l = normalize(lightPos - p);
    vec3 n = GetNormal(p);
    float diffuse = clamp(dot(l, n), 0.0, 1.0);

    // 制造阴影
    // 从p点出发会先检测到自己，并且距离小于SURF_DIST
    // 因此需要让p点先沿法线移动足够的距离，才能得到正确的结果。
    // float d = RayMarching(p, l); 
    float d = RayMarching(p + n * SURF_DIST * 2.0, l);
    if (d < length(p - lightPos)) diffuse *= 0.1;
    return 0.4 + 0.6 * diffuse;
}

void main()
{
    vec2 uv = gl_FragCoord.xy / iResolution.xy * vec2(iResolution.x/iResolution.y, 1.0);

    uv -= vec2(0.5);

    vec3 ro = vec3(0.0, 2.0, -2.0) + vec3(cos(iTime), 0, sin(iTime));
    vec3 rd = normalize(vec3(uv, 1.0));

    vec3 col = vec3(0);

    float t = RayMarching(ro, rd);
    vec3 p = ro + t * rd;
    float diffuse = GetLight(p);
    col = vec3(diffuse);
    // col = GetNormal(p);

    // Output to screen
    gl_FragColor  = vec4(col,1.0);
}