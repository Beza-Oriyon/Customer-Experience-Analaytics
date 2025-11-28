import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import re

# Load English model (will download ~500MB first time)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spacy model...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Simple keyword → theme mapping (you can improve this later)
THEME_RULES = {
    # Login / Access
    "login|password|otp|pin|forgot|blocked|account locked|sign in": "Login & Access Issues",
    # Speed / Performance
    "slow|delay|loading|wait|hang|freeze|crash|bug": "Speed & Performance",
    # Transfer / Payment
    "transfer|send money|payment|transaction|failed|charge|fee": "Transfer & Payment",
    # UI / Design
    "interface|design|beautiful|ugly|easy|hard|confusing|nice ui|good app": "UI/UX & Design",
    # Customer Support
    "support|call center|agent|help|customer service|branch": "Customer Support",
    # Features
    "fingerprint|face id|dark mode|budget|exchange rate|qr|cardless": "Feature Request"
}

def extract_theme(text):
    if pd.isna(text):
        return "Other"
    text_lower = text.lower()
    for pattern, theme in THEME_RULES.items():
        if re.search(pattern, text_lower):
            return theme
    return "General Feedback"

def add_themes(df):
    print("Assigning themes to reviews...")
    df['theme'] = df['review'].apply(extract_theme)
    return df