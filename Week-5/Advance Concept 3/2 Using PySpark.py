# PySpark is used for large data

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('DatabaseCopy').getOrCreate()
source_url = "jdbc:mysql://source_database_url"
destination_url = "jdbc:mysql://destination_database_url"
properties = {
    "user": "your_username",
    "password": "your_password",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# List of tables to copy

tables = ['table1', 'table2', 'table3']
for table in tables:
    df = spark.read.jdbc(url=source_url, table=table, properties=properties)
    df.write.jdbc(url=destination_url, table=table, mode='overwrite', properties=properties)
