#!/usr/bin/env python3
import json
import os

# Define score updates
score_updates = {
    "asheville-nc.json": 10,
    "savannah-ga.json": 10,
    "nashville-tn.json": 10,
    "charlotte-nc.json": 8,
    "raleigh-durham-nc.json": 8,
    "richmond-va.json": 8,
    "denver-co.json": 7,
    "pittsburgh-pa.json": 5,
    "boulder-co.json": 5,
    "bend-or.json": 5,
    "portland-me.json": 6,
    "minneapolis-mn.json": 3,
    "boise-id.json": 4
}

# Summary updates
summary_updates = {
    "savannah-ga.json": "Warm-weather paradise: mild winters that rarely freeze, hot summers (90s with humidity). No snow—maybe a dusting once a decade. If you love warmth and want to avoid harsh cold, this delivers. Spring (March-May) and fall (Oct-Nov) are beautiful. Over 200 sunny days annually.",
    
    "nashville-tn.json": "Mild winters with just occasional snow/ice, hot summers. If you want seasonal variety without brutal cold, Nashville delivers—real fall colors and spring blooms, but winter is manageable. Humidity is significant. Spring tornadoes are rare but real.",
    
    "charlotte-nc.json": "Four seasons with mild winters—occasional snow melts quickly. Hot, humid summers balanced by beautiful spring and fall. If you like seasonal change without harsh cold, Charlotte works well. More humidity than Denver, less dramatic weather.",
    
    "raleigh-durham-nc.json": "Four seasons with mild winters and just a few inches of snow per year. Hot, humid summers balanced by beautiful spring and fall. If you want seasonal variety without extreme cold, the Triangle delivers. Similar to Charlotte but slightly cooler.",
    
    "richmond-va.json": "Four distinct seasons with manageable winters—some snow but not brutal. Hot, humid summers balanced by beautiful spring (cherry blossoms) and fall. More seasonal variation than Charlotte, less extreme than Denver. Good for those who want real seasons without harsh cold.",
    
    "denver-co.json": "300 days of sunshine and four seasons—but 60 inches of snow means real winter. Snow melts quickly thanks to sun, but November-April brings consistent cold. Summers are hot and dry with cool evenings. Great if you want seasons and sun, but winter is genuine.",
    
    "pittsburgh-pa.json": "Four true seasons with cold, snowy winters—42 inches of snow is real winter, not mild. Hot, humid summers. Beautiful spring and stunning fall colors. Cloudy/gray days are common (only 160 sunny days). This is proper Northeast weather. Not ideal for warm-weather preference.",
    
    "boulder-co.json": "300+ sunny days but 89 inches of snow annually—this is cold, real winter despite the sunshine. Foothills location means more snow than Denver. Summers are warm (not hot) with cool nights. Beautiful spring and fall, but winter is genuine and long. Not ideal for warm-weather preference. Altitude is 5,430 feet—adjustment period likely.",
    
    "bend-or.json": "300+ days of sunshine but cold winters—highs in the 80s, lows down to 24°F. Dry, beautiful summers but winter is real (22 inches of snow). Oregon's 'sunny side' but still cold compared to mild climates. Cold nights year-round (desert). Better for those who prioritize sun over warmth.",
    
    "portland-me.json": "Four true seasons with real New England winter—61 inches of snow and cold temps. Beautiful mild summers and stunning fall colors, but winter is genuine. Ocean moderates temperatures slightly but this is still cold. Gray days common. Not for warm-weather preference.",
    
    "minneapolis-mn.json": "Four EXTREME seasons—winters are brutally cold with sub-zero temps and 54 inches of snow. This is genuinely harsh winter, not mild. Summers are warm and beautiful, fall is gorgeous, but winter dominates much of the year. If warm weather is a priority, Minneapolis is a dealbreaker.",
    
    "boise-id.json": "Four true seasons with dry, sunny weather—but winter is genuinely cold (lows around 24°F, 20 inches of snow). Hot summers (90s) are dry and bearable. Over 200 sunny days, but the cold is real. High desert climate with big temperature swings. Better than Minneapolis but still cold for warm-weather preference."
}

base_path = "data/cities"

for filename, new_score in score_updates.items():
    filepath = os.path.join(base_path, filename)
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    # Update score
    data['scores']['climate'] = new_score
    
    # Update summary if available
    if filename in summary_updates:
        data['climate']['summary'] = summary_updates[filename]
    
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')  # Add trailing newline

print("All climate scores and summaries updated successfully!")
