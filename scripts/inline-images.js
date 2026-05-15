// Run after generating carousel HTML files to inline local images as base64.
// This ensures html2canvas can render all slides when opened from file://
//
// Usage: node scripts/inline-images.js output/Carousels/YYYY-MM-DD/
//        node scripts/inline-images.js  (defaults to today's date folder)

const fs = require('fs');
const path = require('path');

const today = new Date().toISOString().slice(0, 10);
const targetDir = process.argv[2] || `output/Carousels/${today}`;

const images = [
  {
    file: 'docs/Assets/Black cat paw pointing right 1.png',
    pattern: /src="[^"]*Black%20cat%20paw%20pointing%20right%201\.png"/g
  },
  {
    file: 'docs/Assets/Frame 427320199Bloggo Rounded Corners logo.png',
    pattern: /src="[^"]*Frame%20427320199Bloggo%20Rounded%20Corners%20logo\.png"/g
  }
];

// Build data URLs once
const dataUrls = images.map(img => ({
  pattern: img.pattern,
  dataUrl: 'data:image/png;base64,' + fs.readFileSync(img.file).toString('base64')
}));

const files = fs.readdirSync(targetDir)
  .filter(f => f.endsWith('.html'))
  .map(f => path.join(targetDir, f));

let updated = 0;
files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  const orig = content;
  dataUrls.forEach(({ pattern, dataUrl }) => {
    content = content.replace(pattern, `src="${dataUrl}"`);
  });
  if (content !== orig) {
    fs.writeFileSync(f, content, 'utf8');
    updated++;
    console.log('Inlined:', path.basename(f));
  }
});
console.log(`Done — ${updated}/${files.length} files updated in ${targetDir}`);
