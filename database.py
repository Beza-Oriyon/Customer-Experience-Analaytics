
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

Base = declarative_base()

class BankReview(Base):
    __tablename__ = 'reviews'
    id              = Column(Integer, primary_key=True)
    review          = Column(Text)
    rating          = Column(Integer)
    date            = Column(Date)
    bank            = Column(String(50))
    source          = Column(String(50))
    sentiment_label = Column(String(20))
    sentiment_score = Column(Float)
    theme           = Column(String(100))


DB_URL = "postgresql://postgres:beza123@localhost:5432/postgres"

engine = create_engine(DB_URL)
Base.metadata.create_all(engine)

def load_to_postgres():
    df = pd.read_csv("data/processed/reviews_with_sentiment_and_themes.csv")
    df['date'] = pd.to_datetime(df['date']).dt.date
    df.to_sql('reviews', engine, if_exists='replace', index=False)
    print(f"Loaded {len(df)} rows into PostgreSQL table 'reviews'")

if __name__ == "__main__":
    load_to_postgres()