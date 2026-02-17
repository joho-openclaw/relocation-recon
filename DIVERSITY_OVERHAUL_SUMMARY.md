# Diversity Climate Overhaul - Completed

## Summary

Completed comprehensive research-based overhaul of diversity climate scoring for all 13 cities in the Relocation Recon project. Replaced demographic-heavy scores with lived-experience analysis.

## Task 1: Photo Gallery Removal ✅

- **Removed** `photos` array from all 13 city JSON files
- **Removed** photo gallery HTML/CSS/JS from `site/index.html`:
  - CSS styles for `.photo-gallery`, `.photo-scroll`, `.photo-item`
  - JavaScript rendering code in `showDetail()` function

## Task 2: Diversity Climate Rescoring ✅

Conducted web research for all 13 cities covering:
1. **Hate crime statistics** (FBI data, local reports)
2. **Interracial couple experiences** (Reddit, forums, news)
3. **Anti-discrimination protections** (city/state laws)
4. **Police/racial profiling** (DOJ reports, local data)
5. **Integration vs segregation** (neighborhood patterns)
6. **General reputation** (Reddit, news articles)
7. **Sundown town history** (historical context)

### Updated Scores (1-10 scale)

| City | Old Score | New Score | Change | Key Finding |
|------|-----------|-----------|--------|-------------|
| **Raleigh-Durham, NC** | 6 | **7** | +1 | ✅ Genuinely welcoming, diverse, interracial couples common |
| **Charlotte, NC** | 6 | **7** | +1 | ✅ "Next Black southern hub," 35% Black, real diversity |
| **Nashville, TN** | 6 | **7** | +1 | ✅ Substantial Black community, interracial couples "aplenty" |
| **Denver, CO** | 5 | **6** | +1 | Passive racism but integrated, lots of mixed couples |
| **Richmond, VA** | 5 | **6** | +1 | Reckoning with Confederate past, 47% Black |
| **Boulder, CO** | 6 | **5** | -1 | ⚠️ Performative progressivism, Black student held at gunpoint for picking up trash |
| **Minneapolis, MN** | 6 | **5** | -1 | ⚠️ George Floyd, systemic police racism, but socially welcoming |
| **Pittsburgh, PA** | 6 | **5** | -1 | ⚠️ Over-policing, police violence against Black residents |
| **Portland, ME** | 6 | **5** | -1 | Whitest state, covert racism, friendly but isolating |
| **Savannah, GA** | 6 | **5** | -1 | 54% Black but deeply segregated, slow to change |
| **Asheville, NC** | 4 | **4** | = | Police profiling, displacement history, progressive but white |
| **Boise, ID** | 3 | **4** | +1 | Boise city relatively safe, but Idaho state has Aryan Nations history |
| **Bend, OR** | 4 | **3** | -1 | ⚠️ SEVERE: Murder of Barry Washington, sundown town history nearby, hate crimes surging |

### Scoring Philosophy

**High Scores (7-8):** Genuinely diverse cities where interracial couples are common and Black residents have community. Police issues may exist but not extreme.

**Mid Scores (5-6):** Mixed picture—either very white but friendly, or diverse but with serious police issues. Livable but not ideal.

**Low Scores (3-4):** Serious red flags—active racism, hate crimes, police violence, or extreme isolation due to whiteness.

### Top 3 Recommendations for Josh & Candace

1. **Raleigh-Durham, NC (Score: 7)** - Research Triangle universities create genuine diversity, interracial couples very common, Durham especially welcoming
2. **Charlotte, NC (Score: 7)** - Becoming "next Black southern hub," 35% Black, interracial couples unremarkable (but watch police)
3. **Nashville, TN (Score: 7)** - Substantial Black community (28%), Civil Rights history, "interracial couples aplenty," systemic racism exists but not overt

### Bottom 3 to Avoid

1. **Bend, OR (Score: 3)** - Murder of Barry Washington, Oregon's Black exclusion history, hate crimes surging, sundown towns nearby
2. **Asheville, NC (Score: 4)** - Police profiling documented, displacement history, only 7.7% Black and declining
3. **Boise, ID (Score: 4)** - Boise city OK but Idaho state has Aryan Nations legacy, hate crimes rising 21%

## Git Commits

1. **Site submodule commit:** `f67241c` - "Remove photo gallery feature"
2. **Main repo commit:** `518bb78` - "Overhaul diversity climate scoring with lived-experience data; remove photo gallery"

Both commits pushed to `origin/main` successfully.

## Research Notes

- **Best sources:** Reddit (lived experience), DOJ/FBI hate crime data, local news investigations
- **Most concerning findings:** 
  - Bend, OR: Murder of Barry Washington, nearby sundown towns with lynching history into 1970s
  - Minneapolis: George Floyd + DOJ pattern-of-practice finding against police
  - Asheville: Police profiling despite progressive politics
  - Boulder: Black student held at gunpoint by 8 cops for picking up trash at his own dorm
  
- **Most positive findings:**
  - Raleigh-Durham: "Very accepted and common," universities create real diversity
  - Charlotte: Becoming Black southern hub, interracial couples unremarkable
  - Denver: "Lots of interracial couples and mixed kids running around"

## Updated Fields

For each city, updated:
- `scores.diversity_climate` (1-10)
- `diversity.summary` (focus on lived experience, specific incidents, Reddit quotes)
- `diversity.diversity_index` (kept demographics but contextualized)
- `diversity.notable` (most important finding for interracial couple)

---

**Completed:** February 16, 2026, 11:01 PST  
**Research time:** ~90 minutes  
**Cities researched:** 13  
**Web searches:** ~45  
**Commits:** 2  
**Files modified:** 14 (13 city JSONs + site/index.html)
