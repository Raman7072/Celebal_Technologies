import pandas as pd
import pyodbc
from sqlalchemy import create_engine

# Load customer dataset
customer_data = pd.read_csv('customers.csv')

# Mark duplicate customers based on Name and Address
customer_data['is_duplicate'] = customer_data.duplicated(subset=['Name', 'Address'], keep=False)

# Assign a Master ID to each group of matching customers
customer_data['Master_ID'] = customer_data.groupby(['Name', 'Address']).ngroup()

# Database connection details
server = 'your_server.database.windows.net'
database = 'your_database'
username = 'your_username'
password = 'your_password'
driver = '{ODBC Driver 17 for SQL Server}'

# Create connection string
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
engine = create_engine(connection_string)

# Write the enriched dataset to Azure SQL
customer_data.to_sql('Customer_Enriched', engine, if_exists='replace', index=False)
