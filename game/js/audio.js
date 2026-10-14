// Web Audio manager: crossfaded music + ambience beds, one-shot SFX, UI blips.
const BASE = "audio/";

export class Audio {
  constructor() {
    this.ctx = null;
    this.buffers = new Map();
    this.loading = new Map();
    this.music = null;   // {name, src, gain}
    this.amb = null;
    this.vol = { music: 0.7, sfx: 0.8 };
  }

  init() {
    if (this.ctx) return;
    const AC = window.AudioContext || window.webkitAudioContext;
    this.ctx = new AC();
    this.master = this.ctx.createGain();
    this.master.connect(this.ctx.destination);
    this.musicBus = this.ctx.createGain();
    this.sfxBus = this.ctx.createGain();
    this.musicBus.connect(this.master);
    this.sfxBus.connect(this.master);
    this.setVolumes(this.vol);
  }

  setVolumes(v) {
    Object.assign(this.vol, v);
    if (!this.ctx) return;
    this.musicBus.gain.value = this.vol.music;
    this.sfxBus.gain.value = this.vol.sfx;
  }

  async load(path) {
    if (this.buffers.has(path)) return this.buffers.get(path);
    if (this.loading.has(path)) return this.loading.get(path);
    const p = fetch(BASE + path)
      .then(r => (r.ok ? r.arrayBuffer() : Promise.reject(r.status)))
      .then(ab => new Promise((res, rej) => this.ctx.decodeAudioData(ab, res, rej)))
      .then(buf => { this.buffers.set(path, buf); return buf; })
      .catch(() => { this.buffers.set(path, null); return null; });
    this.loading.set(path, p);
    return p;
  }

  preload(paths) { if (this.ctx) paths.forEach(p => this.load(p)); }

  async _bed(slot, path, bus, level, fade) {
    const cur = this[slot];
    if (cur && cur.path === path) return;
    const t = this.ctx.currentTime;
    if (cur) {
      cur.gain.gain.cancelScheduledValues(t);
      cur.gain.gain.setValueAtTime(cur.gain.gain.value, t);
      cur.gain.gain.linearRampToValueAtTime(0, t + fade);
      cur.src.stop(t + fade + 0.1);
    }
    this[slot] = null;
    if (!path) return;
    const token = Symbol();
    this[slot + "Token"] = token;
    const buf = await this.load(path);
    if (!buf || this[slot + "Token"] !== token) return;
    const src = this.ctx.createBufferSource();
    src.buffer = buf;
    src.loop = true;
    // skip mp3 encoder padding at the loop seam
    src.loopStart = Math.min(0.05, buf.duration / 4);
    src.loopEnd = buf.duration - 0.03;
    const gain = this.ctx.createGain();
    gain.gain.value = 0;
    src.connect(gain).connect(bus);
    const now = this.ctx.currentTime;
    src.start(now, 0.05);
    gain.gain.linearRampToValueAtTime(level, now + fade);
    this[slot] = { path, src, gain };
  }

  playMusic(name, { fade = 2.0, loop = true } = {}) {
    if (!this.ctx) return;
    const path = name && name !== "none" ? `music/${name}.mp3` : null;
    this._bed("music", path, this.musicBus, 0.9, fade).then(() => {
      if (this.music && !loop) this.music.src.loop = false;
    });
  }

  playAmb(name, { fade = 1.5 } = {}) {
    if (!this.ctx) return;
    const path = name && name !== "none" ? `sfx/${name}.mp3` : null;
    this._bed("amb", path, this.sfxBus, 0.75, fade);
  }

  duckMusic(level = 0.35, time = 0.6) {
    if (!this.music) return;
    const g = this.music.gain.gain, t = this.ctx.currentTime;
    g.cancelScheduledValues(t); g.setValueAtTime(g.value, t); g.linearRampToValueAtTime(level, t + time);
  }

  async sfx(name, { vol = 1, rate = 1, dir = "sfx" } = {}) {
    if (!this.ctx) return;
    const buf = await this.load(`${dir}/${name}.mp3`);
    if (!buf) return;
    const src = this.ctx.createBufferSource();
    src.buffer = buf;
    src.playbackRate.value = rate;
    const g = this.ctx.createGain();
    g.gain.value = vol;
    src.connect(g).connect(this.sfxBus);
    src.start();
  }

  ui(name, vol = 0.5, rate = 1) { this.sfx(name, { vol, rate, dir: "ui" }); }

  // Synthesised fallback blip so typing still has a voice if ui/blip.mp3 is missing.
  blip(pitch = 1) {
    if (!this.ctx) return;
    const buf = this.buffers.get("ui/blip.mp3");
    if (buf) {
      const src = this.ctx.createBufferSource();
      src.buffer = buf;
      src.playbackRate.value = pitch * (0.94 + Math.random() * 0.12);
      const g = this.ctx.createGain();
      g.gain.value = 0.22;
      src.connect(g).connect(this.sfxBus);
      src.start();
      return;
    }
    const o = this.ctx.createOscillator(), g = this.ctx.createGain(), t = this.ctx.currentTime;
    o.type = "triangle";
    o.frequency.value = 520 * pitch * (0.95 + Math.random() * 0.1);
    g.gain.setValueAtTime(0.0001, t);
    g.gain.exponentialRampToValueAtTime(0.05, t + 0.005);
    g.gain.exponentialRampToValueAtTime(0.0001, t + 0.05);
    o.connect(g).connect(this.sfxBus);
    o.start(t); o.stop(t + 0.06);
  }
}
