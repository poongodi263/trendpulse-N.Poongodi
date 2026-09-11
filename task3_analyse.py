import pandas as pd
import glob
csv_file = sorted(glob.glob('data/trends_*.csv'))[-1]
df = pd.read_csv(csv_file)
print(df.groupby('category')['score'].mean())
print(df.sort_values('num_comments', ascending=False).head())
