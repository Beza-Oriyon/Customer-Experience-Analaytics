# preprocessing.py  
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords', quiet=True)

stop_words = set(stopwords.words('english'))

def clean_text(text):
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)           # remove punctuation & numbers
    text = re.sub(r'\s+', ' ', text).strip()          # remove extra spaces
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

def preprocess_and_save():
    df = pd.read_csv("data/processed/cleaned_reviews.csv")  # ← 
    print(f"Raw reviews: {len(df)}")
    
    # Deep cleaning
    df['review'] = df['review'].astype(str)
    df['review_cleaned'] = df['review'].apply(clean_text)
    df = df[df['review_cleaned'].str.len() > 10]      # remove very short reviews
    df = df.drop_duplicates(subset=['review_cleaned'])
    
    # Final columns
    df = df[['review_cleaned', 'rating', 'date', 'bank']].rename(columns={'review_cleaned': 'review'})
    df.to_csv("data/processed/cleaned_reviews.csv", index=False)
    print(f"After deep cleaning → {len(df)} high-quality reviews saved")

if __name__ == "__main__":
    preprocess_and_save()