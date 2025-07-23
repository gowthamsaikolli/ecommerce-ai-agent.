import pandas as pd
from sqlalchemy import create_engine

# 1. Replace with your dataset filenames and desired table names
datasets = [
    ("data/Product-Level Ad Sales and Metrics.csv", "ad_sales"),
    ("data/Product-Level Total Sales and Metrics.csv", "total_sales"),
    ("data/Product-Level Eligibility Table.csv", "eligibility"),
]

# 2. Create SQLite database file in /data folder
engine = create_engine('sqlite:///data/ecommerce.db', echo=True)

for file_path, table_name in datasets:
    # Read CSV into DataFrame
    df = pd.read_csv(file_path)
    # Save DataFrame to SQLite table (replace if exists)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Loaded {file_path} as table '{table_name}'")

print("All data loaded into SQLite database.")
