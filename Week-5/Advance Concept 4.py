tables_columns = {
    'table1': ['column1', 'column2'],
    'table2': ['column3', 'column4'],
}

for table, columns in tables_columns.items():
    columns_str = ', '.join(columns)
    df = pd.read_sql_query(f"SELECT {columns_str} FROM {table}", source_conn)
    df.to_sql(table, destination_conn, if_exists='replace', index=False)
