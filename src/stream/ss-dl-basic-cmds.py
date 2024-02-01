"""
### Description
Exactly-Once Processing with Apache Spark Structured Streaming and Delta Lake

### Version
pyspark --version
3.5.0

### Execute
spark-submit --packages io.delta:delta-spark_2.12:3.1.0 /Users/luanmoreno/GitHub/series-spark/src/stream/ss-dl-basic-cmds.py

### Links
https://spark.apache.org/docs/latest/api/python/reference/pyspark.ss/index.html
https://spark.apache.org/docs/3.1.3/api/python/reference/pyspark.ss.html
"""

import pyspark
from delta import *

builder = pyspark.sql.SparkSession.builder.appName("ss-dl-basic-cmds") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

device_sch = spark.read.json("/Users/luanmoreno/GitHub/series-spark/docs/files/device/device_2022_6_7_19_39_24.json").schema

df_devices = spark.readStream \
    .schema(device_sch) \
    .format("json") \
    .option("header", "true") \
    .load("/Users/luanmoreno/GitHub/series-spark/docs/files/device/*.json")


df_devices \
  .writeStream \
  .format("delta") \
  .outputMode("append") \
  .option("checkpointLocation", "/Users/luanmoreno/GitHub/series-spark/docs/checkpoint") \
  .start("/Users/luanmoreno/GitHub/series-spark/docs/files/output/devices")