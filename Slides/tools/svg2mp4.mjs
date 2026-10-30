// Render an animated (SMIL) SVG asset to a same-name MP4 twin for PPTX.
// usage: node tools/svg2mp4.mjs assets/x.svg [seconds=6] [fps=30]   (needs ffmpeg on PATH)
// Frames are taken with pauseAnimations()+setCurrentTime(), so the loop is exact; 2x scale like svg2png.
import { chromium } from 'file:///C:/Users/KEI/AppData/Roaming/npm/node_modules/@playwright/cli/node_modules/playwright/index.mjs';
import fs from 'fs'; import os from 'os'; import path from 'path'; import { pathToFileURL } from 'url';
import { execFileSync } from 'child_process';
const src = path.resolve(process.argv[2]);
const secs = +(process.argv[3] || 6), fps = +(process.argv[4] || 30);
const m = fs.readFileSync(src, 'utf8').match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);
const [w, h] = [+m[1], +m[2]];
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'svg2mp4-'));
const b = await chromium.launch({ channel: 'chrome' });
const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
await p.goto(pathToFileURL(src).href);
await p.evaluate(() => { document.documentElement.style.background = '#000'; document.documentElement.pauseAnimations(); });
await p.waitForTimeout(400);
const n = Math.round(secs * fps);
for (let i = 0; i < n; i++) {
  await p.evaluate(t => document.documentElement.setCurrentTime(t), i / fps);
  await p.screenshot({ path: path.join(tmp, `f${String(i).padStart(4, '0')}.png`) });
}
await b.close();
const out = src.replace(/\.svg$/, '.mp4');
execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(fps), '-i', path.join(tmp, 'f%04d.png'),
  '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-movflags', '+faststart', out]);
fs.rmSync(tmp, { recursive: true, force: true });
console.log('mp4', out, `${n} frames`);
