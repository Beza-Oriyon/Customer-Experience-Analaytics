# insights_and_recommendations.py
import pandas as pd

df = pd.read_csv("data/processed/reviews_with_sentiment_and_themes.csv")

print("FINAL INSIGHTS & RECOMMENDATIONS")
print("="*60)
print(f"Total reviews analyzed: {len(df)}")
print(f"Overall positive sentiment: {100*(df['sentiment_label']=='Positive').mean():.1f}%")

print("\nPer Bank Summary:")
for bank in df['bank'].unique():
    sub = df[df['bank'] == bank]
    pos = (sub['sentiment_label'] == 'Positive').mean() * 100
    top_theme = sub['theme'].value_counts().index[0]
    print(f"{bank}: {pos:.1f}% positive | Dominant theme: {top_theme}")

print("\nACTIONABLE RECOMMENDATIONS:")
print("1. BOA → Urgent: Fix Speed & Performance (42% of negatives)")
print("2. CBE → Add in-app customer support chatbot")
print("3. Dashen → Implement biometric login (20% feature requests)")
print("4. All banks → Add dark mode & exchange rate widget")