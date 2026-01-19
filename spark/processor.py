from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col, current_timestamp

spark = SparkSession.builder.appName("CryptoRealTime").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

raw_stream = spark.readStream.format("socket").option("host", "producer").option("port", 9999).load()

parsed_stream = raw_stream.withColumn("timestamp_api", split(col("value"), ",")[0]).withColumn("price_usd", split(col("value"), ",")[1])
processed_stream = parsed_stream.withColumn("processing_time", current_timestamp())

print("Démarrage ecriture HDFS sur port 8020...")

query_hdfs = processed_stream.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("path", "hdfs://namenode:8020/data/crypto/") \
    .option("checkpointLocation", "hdfs://namenode:8020/checkpoints/crypto/") \
    .start()

query_hdfs.awaitTermination()
