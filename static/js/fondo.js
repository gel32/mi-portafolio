/* =========================================================
   Fondo de partículas de luz (WebGL)
   ---------------------------------------------------------
   Un campo 3D de puntos luminosos detrás del contenido.
   - La "cámara" rota suavemente siguiendo al mouse (parallax).
   - Cada punto deriva lentamente por su cuenta.
   - Al hacer scroll, el campo se estira un poco en vertical.
   - Los colores se leen de las variables CSS (:root), así el
     fondo siempre coincide con la paleta del sitio.
   - Respeta prefers-reduced-motion (dibuja un cuadro estático)
     y se pausa solo cuando la pestaña no está visible.
   Si el navegador no soporta WebGL, el canvas queda vacío y
   se ven los halos de fondo definidos en CSS.
   ========================================================= */
(function () {
    'use strict';

    var canvas = document.getElementById('fondo-particulas');
    if (!canvas) return;

    // Canvas transparente con alfa premultiplicado: el color acumulado se suma
    // tal cual sobre el fondo de la página (efecto de luz aditiva).
    var opts = { alpha: true, antialias: false, premultipliedAlpha: true };
    var gl = canvas.getContext('webgl', opts) || canvas.getContext('experimental-webgl', opts);
    if (!gl) return;

    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var finePointer  = window.matchMedia('(pointer: fine)').matches;
    var isSmall      = window.innerWidth < 760;

    /* ---------- Colores desde las variables CSS ---------- */
    function cssColor(name, fallback) {
        var v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
        var m = /^#([0-9a-f]{6})$/i.exec(v) ? v : fallback;
        var n = parseInt(m.slice(1), 16);
        return [((n >> 16) & 255) / 255, ((n >> 8) & 255) / 255, (n & 255) / 255];
    }
    var COL_BASE   = cssColor('--text-muted',   '#94a3b8');  // gris pizarra (mayoría)
    var COL_ACCENT = cssColor('--accent',       '#60a5fa');  // azul de acento
    var COL_ALT    = cssColor('--accent-alt',   '#818cf8');  // índigo
    var COL_CORE   = cssColor('--accent-hover', '#93c5fd');  // núcleos brillantes

    /* ---------- Partículas ---------- */
    var N = isSmall ? 2600 : 6000;
    var pos = new Float32Array(N * 3);   // posición 3D
    var rnd = new Float32Array(N * 4);   // 4 aleatorios por punto (fase, velocidad, tamaño, tipo)

    function gauss() {
        var u = 0, v = 0;
        while (!u) u = Math.random();
        while (!v) v = Math.random();
        return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
    }

    for (var i = 0; i < N; i++) {
        var x, y, z;
        if (i % 5 === 0) {
            // 20 %: pequeñas "nebulosas" (cúmulos) para dar profundidad
            var c = (i / 5) % 6;
            var cx = [-4.2, 3.8, -1.2, 4.6, -3.4, 1.6][c];
            var cy = [ 1.8, 1.2, -1.9, -1.6, -0.4, 2.4][c];
            x = cx + gauss() * 0.7;
            y = cy + gauss() * 0.5;
            z = gauss() * 0.9;
        } else {
            // 80 %: campo disperso que cubre toda la pantalla
            x = (Math.random() * 2 - 1) * 7.5;
            y = (Math.random() * 2 - 1) * 4.2;
            z = (Math.random() * 2 - 1) * 3.0;
        }
        pos[i * 3] = x; pos[i * 3 + 1] = y; pos[i * 3 + 2] = z;
        rnd[i * 4]     = Math.random();
        rnd[i * 4 + 1] = Math.random();
        rnd[i * 4 + 2] = Math.random();
        rnd[i * 4 + 3] = Math.random();
    }

    /* ---------- Shaders ---------- */
    var VS = [
        'attribute vec3 aPos;',
        'attribute vec4 aR;',
        'uniform float uT, uAspect, uF, uCam, uPix, uVel;',
        'uniform vec2 uRot;',
        'uniform vec3 uBase, uAccent, uAlt, uCore;',
        'varying vec3 vCol;',
        'varying float vA;',
        'void main() {',
        '  vec3 p = aPos;',
        // deriva suave e independiente de cada punto
        '  p += 0.28 * vec3(sin(uT * (0.18 + aR.y * 0.25) + aR.z * 6.2831),',
        '                   cos(uT * (0.15 + aR.x * 0.25) + aR.w * 6.2831),',
        '                   sin(uT * 0.12 + aR.x * 6.2831));',
        // estiramiento vertical según la velocidad del scroll
        '  p.y += uVel * (aR.w - 0.5) * 0.9;',
        // rotación de cámara (eje Y con el mouse X, eje X con el mouse Y)
        '  float cy = cos(uRot.x), sy = sin(uRot.x);',
        '  float cx = cos(uRot.y), sx = sin(uRot.y);',
        '  p.xz = mat2(cy, -sy, sy, cy) * p.xz;',
        '  p.yz = mat2(cx, -sx, sx, cx) * p.yz;',
        '  float vz = p.z - uCam;',
        '  gl_Position = vec4(p.x * uF / uAspect, p.y * uF, 0.0, -vz);',
        '  float near = clamp(1.0 - (-vz - 4.0) / 8.0, 0.35, 1.0);',
        '  gl_PointSize = uPix * (2.0 + aR.z * 3.2) * (uF * 4.0 / -vz);',
        // color según el "tipo" de partícula
        '  float k = aR.w;',
        '  vec3 col = uBase; float a = 0.45;',
        '  if (k > 0.62) { col = uAccent; a = 0.65; }',
        '  if (k > 0.86) { col = uAlt;    a = 0.70; }',
        '  if (k > 0.965){ col = uCore;   a = 0.80; }',
        '  vCol = col;',
        '  vA = a * near;',
        '}'
    ].join('\n');

    var FS = [
        'precision mediump float;',
        'varying vec3 vCol;',
        'varying float vA;',
        'void main() {',
        '  float d = length(gl_PointCoord - 0.5);',
        '  float a = 1.0 - smoothstep(0.0, 0.5, d);', // disco suave (bordes en orden válido)
        '  a = a * (0.55 + 0.45 * a);',               // núcleo más brillante
        '  gl_FragColor = vec4(vCol, a * vA);',
        '}'
    ].join('\n');

    function compile(type, src) {
        var s = gl.createShader(type);
        gl.shaderSource(s, src);
        gl.compileShader(s);
        if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
            console.warn('fondo.js:', gl.getShaderInfoLog(s));
            return null;
        }
        return s;
    }
    var vs = compile(gl.VERTEX_SHADER, VS);
    var fs = compile(gl.FRAGMENT_SHADER, FS);
    if (!vs || !fs) return;

    var prog = gl.createProgram();
    gl.attachShader(prog, vs);
    gl.attachShader(prog, fs);
    gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) return;
    gl.useProgram(prog);

    function attrib(name, data, size) {
        var buf = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, buf);
        gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW);
        var loc = gl.getAttribLocation(prog, name);
        gl.enableVertexAttribArray(loc);
        gl.vertexAttribPointer(loc, size, gl.FLOAT, false, 0, 0);
    }
    attrib('aPos', pos, 3);
    attrib('aR', rnd, 4);

    var U = {};
    ['uT', 'uAspect', 'uF', 'uCam', 'uPix', 'uVel', 'uRot', 'uBase', 'uAccent', 'uAlt', 'uCore']
        .forEach(function (n) { U[n] = gl.getUniformLocation(prog, n); });

    gl.uniform3fv(U.uBase, COL_BASE);
    gl.uniform3fv(U.uAccent, COL_ACCENT);
    gl.uniform3fv(U.uAlt, COL_ALT);
    gl.uniform3fv(U.uCore, COL_CORE);

    // Mezcla aditiva: donde se cruzan puntos, brillan más.
    // Color: rgb·a (queda premultiplicado). Alfa: se suma sin volver a multiplicar.
    gl.enable(gl.BLEND);
    gl.blendFuncSeparate(gl.SRC_ALPHA, gl.ONE, gl.ONE, gl.ONE);

    var F = 1 / Math.tan((50 * Math.PI / 180) / 2);  // campo de visión de 50°
    var CAM = 7.0;                                    // distancia de la cámara

    /* ---------- Tamaño del canvas ---------- */
    var W = 0, H = 0, dpr = 1;
    function resize() {
        dpr = Math.min(1.75, window.devicePixelRatio || 1);
        W = window.innerWidth;
        H = window.innerHeight;
        canvas.width = Math.round(W * dpr);
        canvas.height = Math.round(H * dpr);
        gl.viewport(0, 0, canvas.width, canvas.height);
    }
    resize();

    /* ---------- Entrada: mouse y scroll ---------- */
    var mx = 0, my = 0;      // objetivo del mouse (-1..1)
    var smx = 0, smy = 0;    // valor suavizado
    if (finePointer) {
        window.addEventListener('pointermove', function (e) {
            mx = (e.clientX / W) * 2 - 1;
            my = (e.clientY / H) * 2 - 1;
        }, { passive: true });
    }

    var lastScroll = window.scrollY, vel = 0;

    /* ---------- Dibujo ---------- */
    var t0 = performance.now();
    function draw(now) {
        var t = reduceMotion ? 0 : (now - t0) / 1000;

        // suavizado (lerp) del mouse: el campo "persigue" al cursor
        smx += (mx - smx) * 0.045;
        smy += (my - smy) * 0.045;

        // velocidad del scroll, suavizada
        var dy = window.scrollY - lastScroll;
        lastScroll = window.scrollY;
        vel += (Math.max(-1, Math.min(1, dy / 40)) - vel) * 0.08;

        // rotación lenta automática + inclinación según el mouse
        var rotY = t * 0.025 + smx * 0.38;
        var rotX = 0.08 + smy * 0.20;

        gl.clearColor(0, 0, 0, 0);
        gl.clear(gl.COLOR_BUFFER_BIT);
        gl.uniform1f(U.uT, t);
        gl.uniform1f(U.uAspect, W / H);
        gl.uniform1f(U.uF, F);
        gl.uniform1f(U.uCam, CAM);
        gl.uniform1f(U.uPix, dpr);
        gl.uniform1f(U.uVel, reduceMotion ? 0 : vel);
        gl.uniform2f(U.uRot, rotY, rotX);
        gl.drawArrays(gl.POINTS, 0, N);
    }

    if (reduceMotion) {
        // Movimiento reducido: un único cuadro estático (se redibuja al redimensionar)
        draw(t0);
        window.addEventListener('resize', function () { resize(); draw(t0); });
        return;
    }

    window.addEventListener('resize', resize);

    // requestAnimationFrame se pausa solo cuando la pestaña no es visible
    function loop(now) {
        draw(now);
        window.requestAnimationFrame(loop);
    }
    window.requestAnimationFrame(loop);
})();
