#Pandas is used for small data

import pandas as pd
import sqlite3
source_conn = sqlite3.connect('source_database.db')
destination_conn = sqlite3.connect('destination_database.db')

# Get list of all tables

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", source_conn)
for table_name in tables['name']:
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", source_conn)
    df.to_sql(table_name, destination_conn, if_exists='replace', index=False)
