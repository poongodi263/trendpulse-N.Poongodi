import pandas as pd
import matplotlib.pyplot as plt
import glob
csv_file = sorted(glob.glob('data/trends_*.csv'))[-1]
df = pd.read_csv(csv_file)
df['category'].value_counts().plot(kind='bar')
plt.title('Trending Stories per Category')
plt.savefig('trends_category.png')
plt.show()
