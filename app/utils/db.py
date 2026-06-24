import duckdb

def get_connection():
    conn = duckdb.connect()
    conn.execute("CREATE VIEW jobs AS SELECT * FROM 'data/processed/jobs.parquet'")
    conn.execute("CREATE VIEW skills AS SELECT * FROM 'data/processed/skills.parquet'")
    return conn