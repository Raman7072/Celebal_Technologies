# write a function in Databricks that reads the parquet files from ADLS based on a date range and returns a single DataFrame.

from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder.getOrCreate()

def read_parquets_from_adls(start_date, end_date, account_name, container_name):
	
    # Generate the list of dates
	
    dates = pd.date_range(start_date, end_date)
    year_months = set(date.strftime('%Y%m') for date in dates)
    
    # Read parquet files from each relevant folder
	
    dataframes = []
    for year_month in year_months:
        folder_path = f'abfss://{container_name}@{account_name}.dfs.core.windows.net/{year_month}/*'
        df = spark.read.parquet(folder_path)
        df = df.filter((df.date >= start_date) & (df.date <= end_date))
        dataframes.append(df)
    
    # Combine dataframes
	
    combined_df = dataframes[0]
    for df in dataframes[1:]:
        combined_df = combined_df.union(df)
    
    return combined_df

# Example usage:

start_date = '2019-01-01'
end_date = '2019-02-01'
account_name = 'your_adls_account'
container_name = 'your_container'
df = read_parquets_from_adls(start_date, end_date, account_name, container_name)
df.show()
