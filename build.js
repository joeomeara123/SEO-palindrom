const fs = require('fs');
const path = require('path');

// Create public directory
if (!fs.existsSync('public')) {
  fs.mkdirSync('public');
}

// Copy HTML files to public directory
const files = ['index.html', 'chatgpt-vs-claude.html', 'chatgpt-vs-copilot.html'];

files.forEach(file => {
  if (fs.existsSync(file)) {
    fs.copyFileSync(file, path.join('public', file));
    console.log(`Copied ${file} to public/`);
  }
});

console.log('Build completed successfully!');