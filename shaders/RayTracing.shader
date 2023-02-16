float iSphere(in vec3 ro, in vec3 rd, in vec4 center)
{
    ro -= center.xyz;
    // 球的方程 (ro + t*rd)^2 = r^2
    float r = center.w;
    float b = 2.0 * dot(ro, rd);
    float c = dot(ro, ro) - r * r;
    float delta = b * b - 4.0 * c;
    if (delta < 0.0) return -1.0;
    float t = (-b - sqrt(delta))/2.0;
    return t;
}

// 计算法线
vec3 nSphere(in vec3 pos, in vec4 sphere)
{
    return (pos-sphere.xyz)/sphere.w;
}

float iPlane(in vec3 ro, in vec3 rd)
{
    // 平面方程 y = 0 = ro.y + t * rd.y
    return -ro.y/rd.y;
}

vec3 nPlane(in vec3 pos)
{
    return vec3(0.0, 1.0, 0.0);
}

vec4 sphere1 = vec4(0, 1.0, 0, 1);
float intersect(in vec3 ro, in vec3 rd, out float resT)
{
    resT = 1000.0;
    float id = -1.0;
    float tsphere = iSphere(ro, rd, sphere1);
    float tplane = iPlane(ro, rd);
    if (tsphere > 0.0)
    {
        id = 1.0;
        resT = tsphere;
    }
    if (tplane > 0.0 && tplane < resT)
    {
        id = 2.0;
        resT = tplane;
    }
    return id;
}

void main()
{
    float time = iGlobalTime * 1.0;
    // Normalized pixel coordinates (from 0 to 1)
    vec2 uv = gl_FragCoord.xy/iResolution.xy * vec2(iResolution.x/iResolution.y, 1.0);
    // 让球运动
    sphere1 += vec4(1.0, 0.0, -2.0, 0.0);
    sphere1.x += 0.5 * cos(time);
    sphere1.z += 0.5 * sin(time);
    // 定义光源
    vec3 light = vec3(0.577703);

    // 1.生成光线
    vec3 ro = vec3(0, 1.0, 3.0); // 视点
    vec3 rd = vec3(uv*2.0-vec2(1.0), -1.0);// 看向z轴负方向。
    rd = normalize(rd);
    // 2.计算相交
    float t;
    float id = intersect(ro, rd, t);

    vec3 col = vec3(0.0); // 未击中任何物体
    if (id > 0.5 && id < 1.5)
    {// 击中球
        vec3 pos = ro + t*rd;
        vec3 nor = nSphere(pos, sphere1);
        float diffuse = clamp(dot(nor, light), 0.0, 1.0);
        float ao = 0.5 + 0.5 * nor.y;
        col = vec3(0.9, 0.8, 0.6) * diffuse * ao + vec3(0.1, 0.2, 0.4) * ao;
    }
    else if (id > 1.5)
    {// 击中平面
        vec3 pos = ro + t*rd;
        // vec3 nor = nPlane(pos);
        // float diffuse = clamp(dot(nor, light), 0.0, 1.0);
        // col = vec3(1.0, 0.8, 0.6) * diffuse + ambient * vec3(0.5, 0.6, 0.7);
        float ambient = smoothstep(0.0, 1.0 * sphere1.w, length(pos.xz - sphere1.xz));
        col = vec3(ambient * 0.7);
    }

    col = sqrt(col);

    // Output to screen
    gl_FragColor  = vec4(col,1.0);
}