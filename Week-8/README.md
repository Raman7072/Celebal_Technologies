# Task 02

dbutils.fs.cp("file:/<local-file-path>", "dbfs:/<destination-path>")

## 1.Load the dataset into a DataFrame
```
file_path = "dbfs:/<destination-path>"
df = spark.read.json(file_path)
```
## 2.Flatten the JSON fields
```
from pyspark.sql.functions import col, explode
from pyspark.sql.types import StructType, StructField, StringType, ArrayType

def flatten(df):
    flat_cols = [col for col in df.columns if isinstance(df.schema[col].dataType, (StringType, IntegerType, FloatType, DoubleType))]
    nested_cols = [col for col in df.columns if isinstance(df.schema[col].dataType, (StructType, ArrayType))]
    
    flat_df = df.select(*flat_cols, *[col(nested_col + "." + field.name).alias(nested_col + "_" + field.name) for nested_col in nested_cols for field in df.schema[nested_col].dataType.fields])
    
    for nested_col in nested_cols:
        if isinstance(df.schema[nested_col].dataType, ArrayType):
            flat_df = flat_df.withColumn(nested_col, explode(nested_col))
            flat_df = flatten(flat_df)
    
    return flat_df

flat_df = flatten(df)
```

## 3.Write the flattened DataFrame as an external Parquet table
```
external_table_path = "dbfs:/<external-table-path>"

flat_df.write.mode("overwrite").parquet(external_table_path)

spark.sql(f"""
CREATE TABLE IF NOT EXISTS flattened_table
USING PARQUET
LOCATION '{external_table_path}'
""")
```
