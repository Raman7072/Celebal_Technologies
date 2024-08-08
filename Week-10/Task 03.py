from pyspark.sql.functions import expr, col
from pyspark.sql.types import IntegerType, StringType

# Define Event-Hub connection in detail
event_hub_conf = {
    'eventhubs.connectionString': 'EVENT_HUB_CONNECTION_STRING'
}

# Read the stream from the Event-Hub
event_stream = (spark.readStream
                .format('eventhubs')
                .options(**event_hub_conf)
                .load())

# Convert the binary body to an integer
numbers_stream = event_stream.selectExpr("CAST(body AS STRING) AS number")

# Convert the string to an integer
numbers_stream = numbers_stream.withColumn("number", col("number").cast(IntegerType()))

# Add 'Risk' Column on the bases of the value
numbers_with_risk = numbers_stream.withColumn('Risk', expr("CASE WHEN number > 80 THEN 'High' ELSE 'Low' END"))

# Show the streaming Data in the console
query = (numbers_with_risk.writeStream
         .outputMode("append")
         .format("console")
         .start())

query.awaitTermination()
