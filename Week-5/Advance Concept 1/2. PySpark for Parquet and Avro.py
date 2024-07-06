from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName('DataExport').getOrCreate()

# Load data from the database
df = spark.read.format("jdbc").options(
    url="jdbc:mysql://your_database_url",
    driver="com.mysql.cj.jdbc.Driver",
    dbtable="your_table",
    user="your_username",
    password="your_password"
).load()

# Save to Parquet
df.write.parquet('output.parquet')

# Save to Avro
df.write.format("avro").save('output.avro')
