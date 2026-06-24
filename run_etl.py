import pandas as pd
import logging
from etl.raw_loader import load_raw
from etl.cleaner import clean
from etl.salary_parser import parse_salary
from etl.skill_extractor import extract_skills

logging.basicConfig(level=logging.INFO, format='%(message)s')

def run():
    # Step 1 - Load
    df = load_raw('data/raw/postings.csv')
    
    # Step 2 - Clean
    df = clean(df)
    
    # Step 3 - Parse salaries
    df = parse_salary(df)
    
    # Step 4 - Extract skills
    logging.info("Extracting skills from job descriptions (this takes a few minutes)...")
    df['skills'] = df['description'].apply(extract_skills)
    
    # Step 5 - Build skills dataframe
    skill_rows = []
    for _, row in df.iterrows():
        for skill_name, skill_category in row['skills']:
            skill_rows.append({
                'job_id': row['job_id'],
                'skill_name': skill_name,
                'skill_category': skill_category
            })
    
    skills_df = pd.DataFrame(skill_rows)
    logging.info(f"Total skill records: {len(skills_df):,}")
    
    # Step 6 - Save to parquet
    df.drop(columns=['skills']).to_parquet('data/processed/jobs.parquet', index=False)
    skills_df.to_parquet('data/processed/skills.parquet', index=False)
    
    logging.info("ETL complete.")
    logging.info(f"Jobs saved: {len(df):,}")
    logging.info(f"Skill records saved: {len(skills_df):,}")

if __name__ == '__main__':
    run()