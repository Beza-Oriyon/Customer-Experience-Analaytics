def test_final_file_exists():
    import os
    assert os.path.exists("data/processed/reviews_with_sentiment_and_themes.csv")

def test_sentiment_column():
    import pandas as pd
    df = pd.read_csv("data/processed/reviews_with_sentiment_and_themes.csv")
    assert 'sentiment_label' in df.columns
    assert df['sentiment_label'].isin(['Positive', 'Negative']).any()