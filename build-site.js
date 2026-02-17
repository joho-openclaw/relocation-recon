#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

// Read the index to get list of cities
const index = JSON.parse(fs.readFileSync('data/cities/index.json', 'utf8'));

// Load all city data
const cities = index.map(slug => {
  const cityPath = `data/cities/${slug}.json`;
  return JSON.parse(fs.readFileSync(cityPath, 'utf8'));
});

// Read the HTML template parts
const htmlContent = fs.readFileSync('site/index.html', 'utf8');

// Find where cities array starts and ends
const citiesStart = htmlContent.indexOf('const cities = [');
const citiesArrayStart = htmlContent.indexOf('[', citiesStart);
const citiesArrayEnd = htmlContent.indexOf('];', citiesStart) + 2;

// Extract header and footer
const header = htmlContent.substring(0, citiesArrayStart);
const footer = htmlContent.substring(citiesArrayEnd);

// Build new cities array
const citiesJson = '[\n' + 
  cities.map(city => '            ' + JSON.stringify(city, null, 2).split('\n').join('\n            ')).join(',\n') + 
  '\n        ]';

// Combine
const newHtml = header + citiesJson + footer;

// Update subtitle to reflect number of cities
const updatedHtml = newHtml.replace(
  /A data-driven exploration of \w+ cities/,
  `A data-driven exploration of ${cities.length} cities`
);

// Write back
fs.writeFileSync('site/index.html', updatedHtml, 'utf8');

console.log(`✓ Built site with ${cities.length} cities:`);
cities.forEach(c => console.log(`  - ${c.name}`));
