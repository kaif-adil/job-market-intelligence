import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def parse_salary(df):
    df = df.copy()
    
    df['normalized_salary'] = pd.to_numeric(df['normalized_salary'], errors='coerce')
    
    before = df['normalized_salary'].notna().sum()
    df.loc[df['normalized_salary'] < 10000, 'normalized_salary'] = None
    df.loc[df['normalized_salary'] > 1000000, 'normalized_salary'] = None
    after = df['normalized_salary'].notna().sum()
    
    logging.info(f"Salary rows before cleaning: {before:,}")
    logging.info(f"Salary rows after cleaning: {after:,}")
    logging.info(f"Removed {before - after:,} unrealistic salary values")
    
    return df