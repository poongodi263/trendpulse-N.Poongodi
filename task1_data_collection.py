import requests
import json
import os
from datetime import datetime
import time

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty"

CATEGORIES = {
    "tech": ["tech", "software", "ai", "apple", "google", "microsoft", "startup", "coding", "programming", "computer"],
    "world news": ["world", "government", "war", "election", "country", "politics", "ukraine", "russia"],
    "sports": ["sports", "football", "cricket", "nba", "soccer", "olympic", "match", "game"],
    "science": ["science", "research", "study", "nasa", "space", "physics", "climate", "scientists"],
    "entertainment": ["movie", "film", "music", "netflix", "hollywood", "entertainment", "show", "celebrity"]
}

def get_category(title):
    title_lower = title.lower()
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in title_lower:
                return cat
    return None

def main():
    print("Fetching top story IDs...")
    res = requests.get(TOP_STORIES_URL)
    top_ids = res.json()[:500]
    collected = {cat: [] for cat in CATEGORIES}
    counts = {cat: 0 for cat in CATEGORIES}
    for story_id in top_ids:
        if all(c >= 25 for c in counts.values()):
            break
        try:
            r = requests.get(ITEM_URL.format(story_id))
            data = r.json()
            if not data or 'title' not in data: continue
            title = data.get('title', '')
            category = get_category(title)
            if category and counts[category] < 25:
                story = {
                    "post_id": data.get('id'),
                    "title": title,
                    "category": category,
                    "score": data.get('score', 0),
                    "num_comments": data.get('descendants', 0),
                    "author": data.get('by', ''),
                    "collected_at": datetime.now().isoformat()
                }
                collected[category].append(story)
                counts[category] += 1
        except: pass
        time.sleep(0.1)
    all_stories = []
    for cat_stories in collected.values():
        all_stories.extend(cat_stories)
    os.makedirs('data', exist_ok=True)
    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_stories, f, indent=2)
    print(f"Saved {len(all_stories)} stories to {filename}")

if __name__ == "__main__":
    main()


Rendu project um ready saare! Copy panni save pannina pothum, full-a odum! Edhavadhu file la error vantha sollunga, udane sari pannidaren!
