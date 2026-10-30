// Render an SVG asset to a same-name PNG twin at 2x (for PPTX). usage: node tools/svg2png.mjs assets/x.svg
import { chromium } from 'file:///C:/Users/KEI/AppData/Roaming/npm/node_modules/@playwright/cli/node_modules/playwright/index.mjs';
import fs from 'fs'; import path from 'path'; import { pathToFileURL } from 'url';
const src = path.resolve(process.argv[2]);
const m = fs.readFileSync(src, 'utf8').match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);
const [w, h] = [+m[1], +m[2]];
const b = await chromium.launch({ channel: 'chrome' });
const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
await p.goto(pathToFileURL(src).href);  // file:// page can load the SVG directly (setContent's about:blank cannot)
await p.evaluate(() => { document.documentElement.style.background = '#000'; });
await p.waitForTimeout(400);
await p.screenshot({ path: src.replace(/\.svg$/, '.png'), omitBackground: false });
await b.close(); console.log('png', src.replace(/\.svg$/, '.png'));
