import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

COLUMNS_TO_KEEP = [
    'job_id',
    'company_name', 
    'title',
    'description',
    'normalized_salary',
    'pay_period',
    'location',
    'company_id',
    'formatted_work_type',
    'formatted_experience_level',
    'listed_time',
    'views'
]
def load_raw(path):
    logging.info(f"Loading raw data from {path}")
    df = pd.read_csv(path,dtype=str,usecols=COLUMNS_TO_KEEP)
    logging.info(f"Loaded {len(df):,} rows")
    logging.info(df.isnull().sum())
    return df

if __name__ == "__main__":
    df = load_raw("data/raw/postings.csv")
    print(df.iloc[0])


