# task2_pipeline.py   ← REPLACE EVERYTHING WITH THIS
import pandas as pd
from sentiment import add_sentiment   # ← fixed import
from themes import add_themes         # ← fixed import

INPUT_FILE = "data/processed/cleaned_reviews.csv"
OUTPUT_FILE = "data/processed/reviews_with_sentiment_and_themes.csv"

# Load data
df = pd.read_csv(INPUT_FILE)
print(f"Loaded {len(df)} reviews")

# Run sentiment + themes
df = add_sentiment(df)
df = add_themes(df)

# Save final result
df.to_csv(OUTPUT_FILE, index=False)
print(f"\nTASK 2 100% COMPLETED!")
print(f"Final file → {OUTPUT_FILE}")
print("\nPreview:")
print(df[['bank', 'rating', 'sentiment_label', 'sentiment_score', 'theme']].head(10))