import pandas as pd
import pyarrow.parquet as pq
import sqlite3

# Connect to your database
conn = sqlite3.connect('your_database.db')

# Query the data
df = pd.read_sql_query("SELECT * FROM your_table", conn)

# Save to CSV
df.to_csv('output.csv', index=False)

# Save to Parquet
df.to_parquet('output.parquet')
