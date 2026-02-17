# Relocation Recon Updates — February 16, 2026

## Summary

Added **4 new cities** to the Relocation Recon project and integrated **3 previously created but unlisted cities**. All cities were thoroughly researched with real, current data specific to Josh & Candace's priorities.

---

## New Cities Added

### 1. **Savannah, GA**
- **Key insight:** Majority-Black city (52%) with strong African American community
- **Major concerns:** Crime elevated but improving (down 20% in 2024); Georgia politics conservative
- **Best for:** Diversity (#1 priority) and affordability
- **Verdict:** High diversity score (8/10) but safety concerns (5/10)

### 2. **Boise, ID**
- **Key insight:** Extremely safe, beautiful outdoor access, affordable
- **Major concerns:** ⚠️ Only 2% Black population; Idaho politics very conservative
- **Best for:** Safety, outdoor recreation, cost of living
- **Verdict:** DEALBREAKER on diversity (3/10) despite excellent safety (8/10)

### 3. **Bend, OR**
- **Key insight:** 300 days of sunshine, world-class outdoor recreation, stunning scenery
- **Major concerns:** ⚠️ Only 0.7% Black (332 people out of 105k); very expensive for size
- **Best for:** Outdoor enthusiasts, sunshine lovers
- **Verdict:** DEALBREAKER on diversity (2/10); perfect scenery (10/10) not enough

### 4. **Boulder, CO**
- **Key insight:** Highly educated, progressive, spectacular mountain access
- **Major concerns:** Very expensive (45% above national), crime rising, only 1.5% Black
- **Best for:** Educated progressive culture, outdoor access, walkability
- **Verdict:** Low diversity (4/10), declining safety (6/10), minimal savings vs LA (4/10 COL)

---

## Previously Unlisted Cities Integrated

These cities had JSON files but weren't in index.json:

1. **Minneapolis, MN** — Progressive lakes city, harsh winters, post-2020 crime concerns
2. **Pittsburgh, PA** — Affordable rust belt gem, least diverse option, cloudy weather
3. **Portland, ME** — Coastal New England, extremely safe, very white (Maine's whitest state)

---

## Research Methodology

Each city was researched using current (2024-2025) data:

- **Demographics:** Census data, diversity statistics, Black population percentages
- **Crime:** FBI crime data, local police reports, violent crime rates per 100k
- **Cost of Living:** Multiple rent aggregators (Apartments.com, RentCafe, Zillow)
- **Climate:** Weather averages, snowfall, sunny days from USClimateData & Weather Spark
- **Walkability:** WalkScore.com neighborhood data
- **Neighborhoods:** Local real estate sites, Reddit discussions, community forums
- **Racial Climate:** Reddit experiences, news articles, community reports

---

## Honest Assessments for Josh & Candace

All city profiles include:

✅ **Truthful diversity scores** — no sugar-coating Idaho/Oregon whiteness  
✅ **Safety ratings** — compared to Candace's San Diego baseline  
✅ **"Why for them" neighborhood notes** — speaking directly to their interracial couple situation  
✅ **Political context** — state vs city politics, conservative laws (ID abortion bans, etc.)  
✅ **Real concerns flagged** — ⚠️ warnings for dealbreakers  

---

## Technical Updates

### Data Files
- Created 4 new JSON files in `data/cities/`:
  - `savannah-ga.json`
  - `boise-id.json`
  - `bend-or.json`
  - `boulder-co.json`

### Index Updated
- `data/cities/index.json` now includes all 13 cities (alphabetically)

### Site Rebuilt
- Created `build-site.js` script to regenerate `site/index.html` from JSON files
- Site now displays all 13 cities with full data
- Updated subtitle to reflect "13 cities" instead of "six cities"

---

## City Rankings (Weighted Score)

Using the priority framework (diversity=9, safety=8, politics=7, COL=6, walk=5, scenery=4, seasons=3, culture=2):

**Top tier for Josh & Candace:**
1. Raleigh-Durham, NC — Best balance of all priorities
2. Denver, CO — Strong on most metrics, improving diversity
3. Richmond, VA — Affordable, moderate, diverse

**Middle tier (tradeoffs):**
4. Savannah, GA — High diversity but safety concerns
5. Charlotte, NC — Growing fast, moderate diversity
6. Nashville, TN — Culture strong but political concerns
7. Asheville, NC — Beautiful but very white
8. Minneapolis, MN — Affordable but brutal winter + crime concerns

**Lower tier (significant concerns):**
9. Boulder, CO — Too expensive, low diversity, rising crime
10. Pittsburgh, PA — Least diverse, cloudy, smaller
11. Portland, ME — Tiny, extremely white, far from family

**DEALBREAKERS (for Candace):**
12. Boise, ID — Only 2% Black despite great safety
13. Bend, OR — Only 0.7% Black despite perfect outdoors

---

## Files Modified

1. `data/cities/savannah-ga.json` (new)
2. `data/cities/boise-id.json` (new)
3. `data/cities/bend-or.json` (new)
4. `data/cities/boulder-co.json` (new)
5. `data/cities/index.json` (updated)
6. `site/index.html` (rebuilt)
7. `build-site.js` (new script)

---

## Next Steps (Not Done)

- [ ] Git setup / GitHub integration — per instructions, left for later
- [ ] Review data accuracy — human verification of stats
- [ ] Additional cities? (Austin, Portland OR, Seattle, etc.)
- [ ] Mobile responsive testing
- [ ] Share with Josh & Candace for feedback

---

## Key Takeaways

**Cities that meet diversity + safety baseline:**
- Savannah, GA (if safety concerns are manageable)
- Raleigh-Durham, NC
- Richmond, VA
- Charlotte, NC

**Cities Josh would love (but Candace would face isolation):**
- Boise, ID (outdoors paradise, extremely white)
- Bend, OR (even whiter, even more outdoorsy)
- Boulder, CO (expensive, declining safety, very white)

**Honest verdict:**
The Mountain West cities (Boise, Bend, Boulder) fail the #1 priority (diversity) despite excelling at Josh's preferences (outdoor access, scenery, walkability). The data supports focusing on Southeast/Mid-Atlantic cities where substantial Black communities exist.

---

*Research completed: February 16, 2026*  
*All data current as of 2024-2025*
