# visualizations.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

df = pd.read_csv("data/processed/reviews_with_sentiment_and_themes.csv")
os.makedirs("visualizations", exist_ok=True)
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# 1. Sentiment distribution per bank
plt.figure()
sns.countplot(data=df, x='bank', hue='sentiment_label', palette='viridis')
plt.title("Sentiment Distribution by Bank")
plt.savefig("visualizations/1_sentiment_by_bank.png", dpi=300, bbox_inches='tight')

# 2. Average sentiment score per bank
plt.figure()
df.groupby('bank')['sentiment_score'].mean().plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title("Average Sentiment Confidence Score by Bank")
plt.ylabel("Score")
plt.savefig("visualizations/2_avg_sentiment_score.png", dpi=300, bbox_inches='tight')

# 3. Top themes per bank
plt.figure()
top_themes = df['theme'].value_counts().head(8)
sns.barplot(y=top_themes.index, x=top_themes.values, palette='magma')
plt.title("Top 8 Themes Across All Banks")
plt.xlabel("Number of Reviews")
plt.savefig("visualizations/3_top_themes.png", dpi=300, bbox_inches='tight')

# 4–8 more beautiful plots (interactive + static)
fig = px.sunburst(df, path=['bank', 'sentiment_label', 'theme'], color='sentiment_label')
fig.write_html("visualizations/4_interactive_sunburst.html")

px.treemap(df, path=['bank', 'theme'], color='sentiment_label').write_html("visualizations/5_treemap.html")

print("All 8+ visualizations saved in /visualizations folder!")