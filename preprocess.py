
import pandas as pd
import os
from config import RAW_DATA_PATH, BANKS, FINAL_OUTPUT, PROCESSED_DATA_PATH

def load_and_clean():
    dfs = []
    for bank in BANKS:
        path = f"{RAW_DATA_PATH}/{bank}_reviews.csv"
        if os.path.exists(path):
            df = pd.read_csv(path)
            dfs.append(df)

    data = pd.concat(dfs, ignore_index=True)

    # Clean
    data = data[['content', 'score', 'at', 'bank', 'source']]
    data.rename(columns={'content': 'review', 'score': 'rating', 'at': 'date'}, inplace=True)
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    data.drop_duplicates(subset=['review', 'date'], inplace=True)
    data.dropna(subset=['review', 'rating'], inplace=True)

    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    data.to_csv(FINAL_OUTPUT, index=False)
    print(f"Cleaned data saved → {FINAL_OUTPUT}")
    print(f"Final reviews: {len(data)} | Missing: {data.isna().mean().mean()*100:.2f}%")
def main():
    load_and_clean()
    
if __name__ == "__main__":
    load_and_clean()