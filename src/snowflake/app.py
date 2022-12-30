import os
from pyspark.sql import SparkSession
from pyspark import SparkConf

spark = SparkSession \
    .builder \
    .appName("app-snowflake") \
    .getOrCreate()

print(SparkConf().getAll())
spark.sparkContext.setLogLevel("INFO")

SNOWFLAKE_OPTIONS = {
    'sfURL': os.environ.get("SNOWFLAKE_URL", "vg65446.us-central1.gcp.snowflakecomputing.com"),
    'sfAccount': os.environ.get("SNOWFLAKE_ACCOUNT", "vg65446"),
    'sfUser': os.environ.get("SNOWFLAKE_USER", "LUANMACIEL"),
    'sfPassword': os.environ.get("SNOWFLAKE_PASSWORD", "Q1w2e3r4!"),
    'sfDatabase': os.environ.get("SNOWFLAKE_DATABASE", "PYTHIANDB"),
    'sfSchema': os.environ.get("SNOWFLAKE_SCHEMA", "PUBLIC"),
    'sfWarehouse': os.environ.get("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
    'sfRole':  os.environ.get("SNOWFLAKE_ROLE", "accountadmin")
    }

# query pushdown {}
df_subscription = spark.read.format("snowflake") \
    .options(**SNOWFLAKE_OPTIONS) \
    .option('dbtable', "Subscription") \
    .load()

df_subscription.show()