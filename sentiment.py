
from transformers import pipeline
import pandas as pd
from tqdm import tqdm

# Load DistilBERT model (automatically downloads the first time)
print("Loading sentiment analysis model (DistilBERT)...")
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    device=-1  # -1 = CPU, change to 0 if you have GPU
)

def add_sentiment(df):
    """Adds sentiment_label and sentiment_score columns"""
    labels = []
    scores = []
    
    print("Analyzing sentiment for all reviews (this takes 2–4 minutes)...")
    for text in tqdm(df['review'], desc="Sentiment"):
        if pd.isna(text) or text.strip() == "":
            labels.append("Neutral")
            scores.append(0.0)
            continue
            
        result = sentiment_pipeline(text[:512])[0]  # model limit
        label = "Positive" if result['label'] == "POSITIVE" else "Negative"
        labels.append(label)
        scores.append(round(result['score'], 4))
    
    df['sentiment_label'] = labels
    df['sentiment_score'] = scores
    return df