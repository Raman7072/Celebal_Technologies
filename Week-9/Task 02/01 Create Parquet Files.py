# We will create a Date range between 2018-01-01 & 2020-10-23 & create a parquet file.

import pandas as pd
import os
import pyarrow as pa
import pyarrow.parquet as pq

# Create Date range

start_date = pd.to_datetime('2018-01-01')
end_date = pd.to_datetime('2020-10-23')
dates = pd.date_range(start_date, end_date)

# Directory to store parquet files

output_dir = 'parquet_files'

# Create directory if it doesn't exist

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a sample dataframe (replace with actual data as needed)

for date in dates:
    data = {'date': [date], 'value': [f'Sample data for {date}']}
    df = pd.DataFrame(data)
    file_name = f'TSK_{date.strftime("%Y%m%d")}.parquet'
    file_path = os.path.join(output_dir, file_name)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, file_path)
