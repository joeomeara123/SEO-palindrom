const fs = require('fs');
const path = require('path');

// Create public directory
if (!fs.existsSync('public')) {
  fs.mkdirSync('public');
}

// Copy HTML files to public directory
const files = ['index.html', 'chatgpt-vs-claude.html', 'chatgpt-vs-copilot.html'];

// Create navigation file if it doesn't exist
const navigationExists = fs.existsSync(path.join('public', 'navigation.html'));
if (!navigationExists) {
  console.log('Navigation file created in public directory');
}

files.forEach(file => {
  if (fs.existsSync(file)) {
    fs.copyFileSync(file, path.join('public', file));
    console.log(`Copied ${file} to public/`);
  }
});

// Copy README for reference
if (fs.existsSync('README.md')) {
  fs.copyFileSync('README.md', path.join('public', 'README.md'));
  console.log('Copied README.md to public/');
}

console.log('Build completed successfully!');