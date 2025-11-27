# config.py
APP_IDS = {
    'CBE': 'com.combanketh.mobilebanking',
    'BOA': 'com.boa.boaMobileBanking',
    'Dashen': 'com.cr2.amolelight'
}

BANKS = ['CBE', 'BOA', 'Dashen']
REVIEWS_PER_BANK = 600
COUNTRY = 'et'
LANGUAGE = 'en'

# Folders
RAW_DATA_PATH = 'data/raw'
PROCESSED_DATA_PATH = 'data/processed'
FINAL_OUTPUT = f'{PROCESSED_DATA_PATH}/cleaned_reviews.csv'