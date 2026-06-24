import pandas as pd
import logging
from etl.raw_loader import load_raw

logging.basicConfig(level=logging.INFO, format='%(message)s')

def clean(df):
    df = df.copy()
    before = len(df)
    df = df.dropna(subset=['description'])
    after = len(df)
    logging.info(f"Dropped {before - after:,} rows with missing descriptions")

    before = len(df)
    df = df.drop_duplicates(subset=['job_id'])
    after = len(df)
    logging.info(f"Dropped {before - after:,} duplicate rows based on job_id")

    df['listed_time'] = pd.to_datetime(pd.to_numeric(df['listed_time'], errors='coerce') ,unit='ms', errors='coerce')

    df['title'] = df['title'].str.strip().str.title()

    df['has_salary'] = df['normalized_salary'].notna()

    logging.info(f"final count: {len(df):,}")
    return df

if __name__ == "__main__":
    df = load_raw("data/raw/postings.csv")
    df_cleaned = clean(df)
    print(df_cleaned.iloc[0])