
from google_play_scraper import reviews, Sort
import pandas as pd
import os
from config import APP_IDS, BANKS, REVIEWS_PER_BANK, COUNTRY, LANGUAGE, RAW_DATA_PATH

def scrape_bank_reviews(bank_name, app_id):
    print(f"Scraping {bank_name}...")
    result, _ = reviews(
        app_id,
        lang=LANGUAGE,
        country=COUNTRY,
        sort=Sort.NEWEST,
        count=REVIEWS_PER_BANK
    )
    df = pd.DataFrame(result)
    df['bank'] = bank_name
    df['source'] = 'Google Play'
    return df

if __name__ == "__main__":
    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    all_dfs = []

    for bank in BANKS:
        df = scrape_bank_reviews(bank, APP_IDS[bank])
        filename = f"{RAW_DATA_PATH}/{bank}_reviews.csv"
        df.to_csv(filename, index=False)
        print(f"Saved {len(df)} reviews → {filename}")
        all_dfs.append(df)

    combined = pd.concat(all_dfs, ignore_index=True)
    print(f"\nTotal reviews collected: {len(combined)}")