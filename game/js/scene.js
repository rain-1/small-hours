// Canvas renderer: background, figures, animated weather/steam, hover brackets, fx.
const W = 640, H = 360;

export class SceneView {
  constructor(canvas) {
    this.c = canvas;
    this.g = canvas.getContext("2d");
    this.g.imageSmoothingEnabled = false;
    this.images = new Map();
    this.scene = null;       // scene config
    this.bg = null;
    this.figures = [];       // [{id, img, x, y, w, h, label}]
    this.hotspots = [];      // [{id, x, y, w, h, label, kind}]
    this.hover = null;
    this.rain = [];
    this.splashes = [];
    this.steam = [];
    this.tint = null;        // css colour with alpha
    this.flash = 0;
    this.flicker = 0;
    this.t = 0;
    for (let i = 0; i < 140; i++) this.rain.push(this._drop(true));
  }

  img(path) {
    if (this.images.has(path)) return this.images.get(path);
    const im = new Image();
    const p = new Promise(res => { im.onload = () => res(im); im.onerror = () => res(null); });
    im.src = path;
    this.images.set(path, p);
    return p;
  }

  async set(scene, bgName, figures, hotspots, occluders = null) {
    this.occluders = occluders;
    this.scene = scene;
    this.bg = await this.img(`art/${bgName}.png`);
    const figs = [];
    for (const f of figures) {
      const im = await this.img(`art/figures/${f.sprite}.png`);
      if (!im) continue;
      figs.push({ ...f, img: im, w: im.width, h: im.height, x: Math.round(f.x - im.width / 2), y: Math.round(f.y - im.height) });
    }
    this.figures = figs;
    this.hotspots = hotspots;
    this.steam = [];
    this.hover = null;
  }

  _drop(init) {
    return { x: Math.random() * (W + 80) - 40, y: init ? Math.random() * H : -10 - Math.random() * 40,
             v: 5 + Math.random() * 3.5, l: 5 + Math.random() * 7, a: 0.12 + Math.random() * 0.28 };
  }

  hit(x, y) {
    for (let i = this.figures.length - 1; i >= 0; i--) {
      const f = this.figures[i];
      if (x >= f.x && x < f.x + f.w && y >= f.y && y < f.y + f.h) {
        // alpha test so empty sprite corners don't block hotspots
        const a = this._alphaAt(f, x - f.x, y - f.y);
        if (a > 0) return { type: "figure", ...f };
      }
    }
    const hs = this.hotspots.filter(h => x >= h.x && x < h.x + h.w && y >= h.y && y < h.y + h.h)
      .sort((a, b) => a.w * a.h - b.w * b.h);
    return hs.length ? { type: "hotspot", ...hs[0] } : null;
  }

  _alphaAt(f, x, y) {
    if (!f._alpha) {
      const cv = document.createElement("canvas");
      cv.width = f.w; cv.height = f.h;
      const g = cv.getContext("2d");
      g.drawImage(f.img, 0, 0);
      f._alpha = g.getImageData(0, 0, f.w, f.h).data;
    }
    // be generous: check a small neighbourhood
    for (let dy = -2; dy <= 2; dy++) for (let dx = -2; dx <= 2; dx++) {
      const xx = Math.floor(x) + dx, yy = Math.floor(y) + dy;
      if (xx < 0 || yy < 0 || xx >= f.w || yy >= f.h) continue;
      if (f._alpha[(yy * f.w + xx) * 4 + 3] > 0) return 1;
    }
    return 0;
  }

  tick(dt) {
    this.t += dt;
    const s = this.scene || {};
    if (s.steam) {
      for (const [sx, sy, rate = 1] of s.steam) {
        if (Math.random() < 0.08 * rate) this.steam.push({ x: sx + (Math.random() - 0.5) * 8, y: sy, r: 2 + Math.random() * 3, life: 0, max: 2.2 + Math.random() * 1.5, dx: (Math.random() - 0.5) * 6 });
      }
    }
    for (const p of this.steam) { p.life += dt; p.y -= dt * 14; p.x += p.dx * dt; p.r += dt * 5; }
    this.steam = this.steam.filter(p => p.life < p.max);
    if (s.rain) {
      for (const d of this.rain) {
        d.y += d.v * dt * 60; d.x -= d.v * 0.18 * dt * 60;
        const ground = s.ground || 300;
        if (d.y > ground + Math.random() * (H - ground)) {
          if (Math.random() < 0.35) this.splashes.push({ x: d.x, y: d.y, life: 0 });
          Object.assign(d, this._drop(false));
        }
      }
      for (const sp of this.splashes) sp.life += dt;
      this.splashes = this.splashes.filter(sp => sp.life < 0.25);
    }
    this.flash = Math.max(0, this.flash - dt * 2.5);
    if (this.flicker > 0) this.flicker = Math.max(0, this.flicker - dt);
  }

  draw() {
    const g = this.g;
    g.clearRect(0, 0, W, H);
    if (this.bg) g.drawImage(this.bg, 0, 0);
    const s = this.scene || {};
    // neon breathing: a faint additive pulse on the whole frame
    for (const f of this.figures) g.drawImage(f.img, f.x, f.y);
    // occluders: repaint foreground bits of the background over figures (e.g. the shop counter)
    if (this.bg && this.occluders) for (const [x, y, w, h] of this.occluders) g.drawImage(this.bg, x, y, w, h, x, y, w, h);
    // steam
    for (const p of this.steam) {
      const k = p.life / p.max;
      g.fillStyle = `rgba(246,231,200,${0.16 * (1 - k) * Math.min(1, p.life * 3)})`;
      const r = Math.round(p.r);
      // chunky pixel puff
      g.fillRect(Math.round(p.x - r), Math.round(p.y - r / 2), r * 2, r);
      g.fillRect(Math.round(p.x - r / 2), Math.round(p.y - r), r, r * 2);
    }
    if (s.rain) {
      g.strokeStyle = "rgba(190,220,255,1)";
      g.lineWidth = 1;
      for (const d of this.rain) {
        g.globalAlpha = d.a;
        g.beginPath();
        g.moveTo(Math.round(d.x) + 0.5, Math.round(d.y));
        g.lineTo(Math.round(d.x + d.l * 0.18) + 0.5, Math.round(d.y - d.l));
        g.stroke();
      }
      g.globalAlpha = 0.5;
      g.fillStyle = "rgba(200,230,255,1)";
      for (const sp of this.splashes) {
        const r = Math.round(1 + sp.life * 10);
        g.fillRect(Math.round(sp.x) - r, Math.round(sp.y), 1, 1);
        g.fillRect(Math.round(sp.x) + r, Math.round(sp.y), 1, 1);
      }
      g.globalAlpha = 1;
    }
    if (this.tint) { g.fillStyle = this.tint; g.fillRect(0, 0, W, H); }
    if (this.flicker > 0) {
      const on = Math.sin(this.t * 40) > 0.2 || Math.random() < 0.2;
      g.fillStyle = `rgba(5,4,12,${on ? 0.25 : 0.82})`;
      g.fillRect(0, 0, W, H);
    }
    if (this.debug) {
      g.strokeStyle = "#0f0"; g.lineWidth = 1; g.font = "7px monospace"; g.fillStyle = "#0f0";
      for (const h of this.hotspots) { g.strokeRect(h.x + 0.5, h.y + 0.5, h.w, h.h); g.fillText(h.id, h.x + 2, h.y + 8); }
      g.strokeStyle = "#f0f";
      for (const f of this.figures) g.strokeRect(f.x + 0.5, f.y + 0.5, f.w, f.h);
    }
    if (this.flash > 0) { g.fillStyle = `rgba(230,240,255,${this.flash * 0.5})`; g.fillRect(0, 0, W, H); }
    // hover brackets
    const h = this.hover;
    if (h) {
      const x = Math.round(h.x), y = Math.round(h.y), w = Math.round(h.w), hh = Math.round(h.h);
      const k = 4 + Math.round(Math.sin(this.t * 5) * 1);
      g.fillStyle = h.kind === "talk" ? "#ff5fa2" : h.kind === "go" ? "#4ff0e6" : "#ffb347";
      const br = (bx, by, sx, sy) => { g.fillRect(bx, by, k * sx || 1, 1); g.fillRect(bx, by, 1, k * sy || 1); };
      g.fillRect(x - 1, y - 1, k, 1); g.fillRect(x - 1, y - 1, 1, k);
      g.fillRect(x + w - k + 1, y - 1, k, 1); g.fillRect(x + w, y - 1, 1, k);
      g.fillRect(x - 1, y + hh, k, 1); g.fillRect(x - 1, y + hh - k + 1, 1, k);
      g.fillRect(x + w - k + 1, y + hh, k, 1); g.fillRect(x + w, y + hh - k + 1, 1, k);
    }
  }
}
