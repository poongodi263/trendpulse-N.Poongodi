import json
import pandas as pd
import glob
import os
from datetime import datetime

files = glob.glob('data/trends_*.json')
latest_file = sorted(files)[-1]
with open(latest_file, 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)
df = df.drop_duplicates(subset=['post_id'])
df['title'] = df['title'].astype(str).str.strip()
df['score'] = pd.to_numeric(df['score'], errors='coerce').fillna(0).astype(int)
df['num_comments'] = pd.to_numeric(df['num_comments'], errors='coerce').fillna(0).astype(int)
df['category'] = df['category'].str.lower().str.strip()
df['collected_at'] = pd.to_datetime(df['collected_at'])
csv_file = f"data/trends_{datetime.now().strftime('%Y%m%d')}.csv"
df.to_csv(csv_file, index=False)
print(f"Cleaned data saved to {csv_file}")
