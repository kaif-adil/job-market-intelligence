import logging 
import re

logging.basicConfig(level=logging.INFO, format='%(message)s')

SKILLS = {
    # Languages
    'python': ('Python', 'Language'),
    'sql': ('SQL', 'Language'),
    'r': ('R', 'Language'),
    'java': ('Java', 'Language'),
    'scala': ('Scala', 'Language'),
    'javascript': ('JavaScript', 'Language'),
    'c++': ('C++', 'Language'),
    

    # Frameworks & Libraries
    'pandas': ('Pandas', 'Framework'),
    'numpy': ('NumPy', 'Framework'),
    'tensorflow': ('TensorFlow', 'Framework'),
    'pytorch': ('PyTorch', 'Framework'),
    'spark': ('Spark', 'Framework'),
    'kafka': ('Kafka', 'Framework'),
    'airflow': ('Airflow', 'Framework'),
    'dbt': ('dbt', 'Framework'),

    # Cloud
    'aws': ('AWS', 'Cloud'),
    'amazon web services': ('AWS', 'Cloud'),
    'gcp': ('GCP', 'Cloud'),
    'google cloud': ('GCP', 'Cloud'),
    'azure': ('Azure', 'Cloud'),

    # Databases
    'postgresql': ('PostgreSQL', 'Database'),
    'mysql': ('MySQL', 'Database'),
    'mongodb': ('MongoDB', 'Database'),
    'snowflake': ('Snowflake', 'Database'),
    'redshift': ('Redshift', 'Database'),
    'bigquery': ('BigQuery', 'Database'),
    'elasticsearch': ('Elasticsearch', 'Database'),

    # Tools
    'tableau': ('Tableau', 'Tool'),
    'power bi': ('Power BI', 'Tool'),
    'looker': ('Looker', 'Tool'),
    'excel': ('Excel', 'Tool'),
    'git': ('Git', 'Tool'),
    'docker': ('Docker', 'Tool'),
    'kubernetes': ('Kubernetes', 'Tool'),
    'jupyter': ('Jupyter', 'Tool'),

    # Concepts
    'machine learning': ('Machine Learning', 'Concept'),
    'deep learning': ('Deep Learning', 'Concept'),
    'statistics': ('Statistics', 'Concept'),
    'a/b testing': ('A/B Testing', 'Concept'),
    'etl': ('ETL', 'Concept'),
    'data warehousing': ('Data Warehousing', 'Concept'),
    'nlp': ('NLP', 'Concept'),
    'api': ('API', 'Concept'),
}

def extract_skills(description : str)->list:
    if not description:
        return []
    description = description.lower()
    found_skills = []
    for keyword, value in SKILLS.items():
        if re.search(r'\b' + re.escape(keyword) + r'\b', description):
            found_skills.append(value)
    return found_skills

if __name__ == "__main__":
    from etl.raw_loader import load_raw
    from etl.cleaner import clean
    df = load_raw("data/raw/postings.csv")
    df_cleaned = clean(df)
    python_jobs = df_cleaned[df_cleaned['description'].str.lower().str.contains('python')]
    description = python_jobs['description'].iloc[0]
    print("Job title:", python_jobs['title'].iloc[0])
    print("Skills found:", extract_skills(description))
