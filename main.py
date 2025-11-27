# main.py  ← REPLACE YOUR CURRENT main.py WITH THIS
import subprocess
import sys

print("Starting Task 1: Scraping + Cleaning Reviews\n")

# Run scraper.py
print("Scraping reviews from Google Play...")
subprocess.run([sys.executable, "scraper.py"])

print("\n" + "="*60)
print("Preprocessing and cleaning data...")
print("="*60 + "\n")

# Run preprocess.py
subprocess.run([sys.executable, "preprocess.py"])

print("\nTASK 1 COMPLETED SUCCESSFULLY!")
print("Check: data/processed/cleaned_reviews.csv")