from pyspark.sql import SparkSession
from pyspark import SparkConf

spark = SparkSession \
    .builder \
    .appName("app-gcs-json") \
    .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", "/Users/luanmorenomaciel/Credentials/silver-charmer-243611-9552f50e9d25.json") \
    .getOrCreate()

print(SparkConf().getAll())
spark.sparkContext.setLogLevel("INFO")

df_users = spark.read.json("gs://owshq-landing-zone/users/*.json")
df_users.show()