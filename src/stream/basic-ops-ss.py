"""
Apache Spark 3.3.1
Scala 2.12
"""


import pyspark
from delta import *

builder = pyspark.sql.SparkSession.builder \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()
spark.sparkContext.setLogLevel("INFO")

# read file & get schema
device_filepath = "/Users/luanmorenomaciel/GitHub/series-spark/docs/files/device/device_2022_6_7_19_39_24.json"
df_device_sch = spark.read.json(device_filepath)
get_device_sch = df_device_sch.schema
print(get_device_sch)

# read stream
df_device_stream = spark.readStream \
  .schema(get_device_sch) \
  .format("json") \
  .option("header", "true") \
  .load("/Users/luanmorenomaciel/GitHub/series-spark/docs/files/device/*.json") \

# write stream
df_device_stream.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/Users/luanmorenomaciel/GitHub/series-spark/src/stream/checkpoint") \
    .start("/Users/luanmorenomaciel/GitHub/series-spark/src/stream/data/device")

print(df_device_stream.count())