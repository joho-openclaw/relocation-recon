# Relocation Recon — Static Site

A sleek, modern static website for researching relocation cities. Built with pure HTML, CSS, and JavaScript.

## Features

- **Dark mode interface** with subtle gradients and smooth animations
- **City overview** — grid of city cards with weighted scores
- **Detailed city profiles** — click any city to see full analysis with radar charts
- **Comparison table** — side-by-side scoring across all 8 dimensions
- **Weighted scoring** — based on priority framework (diversity > safety > politics > COL > walkability > scenery > seasons > culture)
- **Mobile responsive** — works beautifully on all screen sizes

## Structure

- `index.html` — Single-file app with embedded CSS and JavaScript
- All city data is inlined from JSON files (no external dependencies except Chart.js CDN)

## Tech Stack

- Pure HTML/CSS/JS (no build tools, no frameworks)
- [Inter font](https://fonts.google.com/specimen/Inter) from Google Fonts
- [Chart.js](https://www.chartjs.org/) for radar charts (loaded from CDN)

## Viewing the Site

Simply open `index.html` in any modern web browser. No server required!

### Options:

1. **Local file:** Double-click `index.html`
2. **Simple server:** `python3 -m http.server 8000` then open `http://localhost:8000`
3. **OpenClaw Canvas:** Deploy to OpenClaw canvas for preview
4. **GitHub Pages:** Push to GitHub and enable Pages for sharing

## Priority Framework

The weighted scoring system reflects these priorities:

1. **Diversity Climate** (weight: 9) — Welcoming to interracial couples
2. **Safety** (weight: 8) — Physical safety, low crime
3. **Political Moderation** (weight: 7) — Not extreme in either direction
4. **Cost of Living** (weight: 6) — Lower than SoCal
5. **Walkability** (weight: 5) — Safe, walkable neighborhoods
6. **Scenic Beauty** (weight: 4) — Mountains, natural backdrop
7. **Seasons** (weight: 3) — Real seasons, snow okay
8. **Culture** (weight: 2) — Place with identity and character

## Cities Analyzed

- Asheville, NC
- Charlotte, NC
- Denver, CO
- Nashville, TN
- Raleigh-Durham, NC
- Richmond, VA

---

Built with ❤️ for Josh & Candace's relocation research
