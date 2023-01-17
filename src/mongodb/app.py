import pymongo
from pyspark.sql import SparkSession
from pyspark import SparkConf

spark = SparkSession \
    .builder \
    .appName("app-mongodb-collection") \
    .config("spark.mongodb.connection.uri","mongodb+srv://admin:admin@mongodb-owshq-dev.ozne0pz.mongodb.net/?retryWrites=true&w=majority") \
    .getOrCreate()

print(SparkConf().getAll())
spark.sparkContext.setLogLevel("INFO")

df_payments = spark.read.format("mongodb") \
    .option("database", "owshq") \
    .option("collection", "payments") \
    .load()

df_payments.show()