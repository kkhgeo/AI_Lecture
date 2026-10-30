// Context lecture (21hrs-style deck) — bake pass, adapted from Sidewave_Style/bake.mjs (run before make_pptx.py)
//   npm i playwright   (uses the system Chrome: channel "chrome")
//   node bake.mjs
// Produces:
//   previews/html-slide-N.png     rendered HTML slides
//   assets/pptx_bg_slideN.png     plate + scrims only: every [data-tx] text, [data-ui] shape, [data-icon], [data-img],
//                                 [data-logo], table[data-table] hidden (world plate + scrims only)
//   assets/ui/icon-*.png          [data-icon] glyphs rendered on transparent background
//   pptx_layout.json              rects + runs / fills / borders of every editable element (read by make_pptx.py)
//   USAvionix_Template_16x9.pdf   print export
import { chromium } from 'file:///C:/Users/KEI/AppData/Roaming/npm/node_modules/@playwright/cli/node_modules/playwright/index.mjs';
import fs from 'fs';
import path from 'path';
import { pathToFileURL } from 'url';

const BASE = process.cwd();
const HTML = path.join(BASE, process.argv[2] || 'lecture_context.html');  // node bake.mjs [deck.html]

const browser = await chromium.launch({ channel: 'chrome' });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.goto(pathToFileURL(HTML).href + '?bake=1', { waitUntil: 'load' });  // ?bake disables the glyph-scramble
await page.evaluate(() => document.fonts.ready);
await page.addStyleTag({ content: '.slide-counter{display:none!important}' });
const n = await page.evaluate(() => document.querySelectorAll('.slide').length);

const extract = () => {
  const slide = document.querySelector('.slide.active');
  const S = slide.getBoundingClientRect();
  const R = el => { const r = el.getBoundingClientRect(); return { x: r.left - S.left, y: r.top - S.top, w: r.width, h: r.height }; };
  const RR = el => { const r = el.getBoundingClientRect(), cx = r.left + r.width / 2 - S.left, cy = r.top + r.height / 2 - S.top;
    return { x: cx - el.offsetWidth / 2, y: cy - el.offsetHeight / 2, w: el.offsetWidth, h: el.offsetHeight }; };
  const rot = el => parseFloat(el.dataset.rot || 0);
  const style = el => { const c = getComputedStyle(el); return {
    family: c.fontFamily.split(',')[0].replace(/"/g, '').trim(), weight: +c.fontWeight, size: parseFloat(c.fontSize),
    color: c.color, ls: c.letterSpacing === 'normal' ? 0 : parseFloat(c.letterSpacing), upper: c.textTransform === 'uppercase',
    strokeW: parseFloat(c.webkitTextStrokeWidth) || 0, strokeColor: c.webkitTextStrokeColor }; };
  const runsOf = root => {
    const out = [];
    const walk = node => {
      for (const ch of node.childNodes) {
        if (ch.nodeType === 3) {
          const t = ch.textContent.replace(/\s+/g, ' ');
          if (!t.trim() && !out.length) continue;
          const st = style(ch.parentElement);
          out.push({ text: st.upper ? t.toUpperCase() : t, ...st, mark: !!ch.parentElement.closest('mark') });
        } else if (ch.nodeType === 1) {
          if (ch.tagName === 'BR') out.push({ text: '\v', ...style(ch.parentElement), mark: false });
          else if (ch.tagName !== 'svg') walk(ch);
        }
      }
    };
    walk(root);
    if (out.length) { out[0].text = out[0].text.replace(/^\s+/, ''); out[out.length - 1].text = out[out.length - 1].text.replace(/\s+$/, ''); }
    return out.filter(r => r.text);
  };
  const texts = [...slide.querySelectorAll('[data-tx]')].map(el => {
    const c = getComputedStyle(el);
    const lh = c.lineHeight === 'normal' ? parseFloat(c.fontSize) * 1.2 : parseFloat(c.lineHeight);
    // text box = the laid-out glyph run (excludes padding); width falls back to the content box for wrapped blocks
    const rg = document.createRange(); rg.selectNodeContents(el);
    const rr = rg.getBoundingClientRect();
    const pl = parseFloat(c.paddingLeft) || 0, pr = parseFloat(c.paddingRight) || 0;
    const contentW = el.clientWidth ? el.clientWidth - pl - pr : rr.width;
    // Range rects are font content areas, not line boxes (Anton's is 1.5em). Rebuild line boxes:
    // count distinct lines from the fragments, centre the first line box on the first fragment.
    const frags = [...rg.getClientRects()].filter(f => f.width > 0 && f.height > 0);
    const tops = []; for (const f of frags) { const cy = (f.top + f.bottom) / 2; if (!tops.some(t => Math.abs(t - cy) < lh / 2)) tops.push(cy); }
    const nLines = Math.max(1, tops.length);
    const lineTop = frags.length ? Math.min(...tops) - lh / 2 : rr.top;
    const multi = nLines > 1;
    const w = multi ? Math.max(rr.width, contentW) : rr.width;
    const rect = el.dataset.rot ? RR(el) : { x: rr.left - S.left, y: lineTop - S.top, w, h: nLines * lh };
    // align: element's own text-align, but inline spans inherit a flex parent's placement → derive from rect vs parent
    let align = c.textAlign === 'right' || c.textAlign === 'end' ? 'right' : c.textAlign === 'center' ? 'center' : 'left';
    if (el.parentElement.classList.contains('pill') || el.parentElement.classList.contains('status-chip')) align = 'center';
    if (el.parentElement.classList.contains('ptab')) align = 'center';
    return { rect, lh, align, rot: rot(el), lines: el.dataset.rot ? 1 : nLines, runs: runsOf(el) };
  });
  const imgs = [...slide.querySelectorAll('[data-img]')].map(el => ({ rect: R(el), src: el.getAttribute('src') }));
  const logos = [...slide.querySelectorAll('[data-logo]')].map(el => ({ rect: R(el) }));
  const tables = [...slide.querySelectorAll('table[data-table]')].map(t => ({
    rect: R(t),
    colW: [...t.rows[0].cells].map(c => c.getBoundingClientRect().width),
    rowH: [...t.rows].map(r => r.getBoundingClientRect().height),
    cells: [...t.rows].map(r => [...r.cells].map(c => ({ runs: runsOf(c), padL: parseFloat(getComputedStyle(c).paddingLeft), padR: parseFloat(getComputedStyle(c).paddingRight) }))),
    border: { top: getComputedStyle(t).borderTopColor, row: getComputedStyle(t.rows[1].cells[0]).borderBottomColor },
  }));
  const ui = [...slide.querySelectorAll('[data-ui]')].map(el => {
    const c = getComputedStyle(el);
    const side = k => ({ w: parseFloat(c[`border${k}Width`]) || 0, color: c[`border${k}Color`] });
    return { rect: el.dataset.rot ? RR(el) : R(el), rot: rot(el), bg: c.backgroundColor, radius: parseFloat(c.borderTopLeftRadius) || 0,
      border: { top: side('Top'), right: side('Right'), bottom: side('Bottom'), left: side('Left') } };
  });
  const icons = [...slide.querySelectorAll('[data-icon]')].map(el => ({ rect: R(el), name: el.dataset.icon }));
  const notes = [...slide.querySelectorAll('.notes li')].map(li => li.textContent.trim()).join(String.fromCharCode(10));
  return { texts, imgs, logos, tables, ui, icons, notes };
};

const layout = [];
fs.mkdirSync(path.join(BASE, 'previews'), { recursive: true });
for (let i = 0; i < n; i++) {
  await page.evaluate(k => window.__show(k), i);
  await page.waitForTimeout(250);
  await page.screenshot({ path: path.join(BASE, 'previews', `html-slide-${i + 1}.png`) });
  layout.push(await page.evaluate(extract));
  const tag = await page.addStyleTag({ content: `
    [data-tx],[data-tx] *{color:transparent!important;-webkit-text-fill-color:transparent!important;-webkit-text-stroke-color:transparent!important}
    mark{background:transparent!important}
    [data-img],[data-logo],[data-ui],[data-icon],table[data-table]{visibility:hidden!important}` });
  await page.screenshot({ path: path.join(BASE, 'assets', `pptx_bg_slide${i + 1}.png`) });
  await tag.evaluate(t => t.remove());
}
fs.writeFileSync(path.join(BASE, 'pptx_layout.json'), JSON.stringify(layout, null, 1));

// icon glyphs: same Phosphor paths as the HTML <symbol>s, colour taken from the rendered element
const iconSpecs = await page.evaluate(() => {
  const out = {};
  for (const el of document.querySelectorAll('[data-icon]')) {
    const name = el.dataset.icon;
    if (out[name]) continue;
    const sym = document.getElementById(name);
    const c = getComputedStyle(el);
    out[name] = { viewBox: sym.getAttribute('viewBox'), inner: sym.innerHTML, style: `fill:${c.fill};stroke:${c.stroke};stroke-width:${c.strokeWidth}` };
  }
  return out;
});
fs.mkdirSync(path.join(BASE, 'assets', 'ui'), { recursive: true });
const ip = await browser.newPage({ viewport: { width: 256, height: 256 } });
for (const [name, spec] of Object.entries(iconSpecs)) {
  await ip.setContent(`<html><body style="margin:0;background:transparent"><svg id="g" xmlns="http://www.w3.org/2000/svg" viewBox="${spec.viewBox}" width="256" height="256" style="display:block;${spec.style}">${spec.inner}</svg></body></html>`);
  await (await ip.$('#g')).screenshot({ path: path.join(BASE, 'assets', 'ui', `icon-${name}.png`), omitBackground: true });
}
await ip.close();

await page.emulateMedia({ media: 'print' });
await page.pdf({ path: path.join(BASE, path.basename(HTML, '.html') + '_16x9.pdf'), width: '1920px', height: '1080px', printBackground: true, preferCSSPageSize: true });
await browser.close();
console.log('baked', n, 'slides');
