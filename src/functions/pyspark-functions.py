""""
https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html
https://towardsdatascience.com/selecting-multiple-columns-in-pyspark-d1aac072fcc0
"""

from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.functions import *

spark = SparkSession \
    .builder \
    .appName("py-functions") \
    .getOrCreate()

print(SparkConf().getAll())
spark.sparkContext.setLogLevel("ERROR")

loc_users = "/Users/luanmorenomaciel/GitHub/series-spark/docs/files/json/users.json"
loc_business = "/Users/luanmorenomaciel/GitHub/series-spark/docs/files/json/business.json"
df_users = spark.read.json(loc_users)
df_business = spark.read.json(loc_business)

df_users.printSchema()
print(df_users.show())

#-----------------#
# functions
#-----------------#

# select
df_users.select("user_id", "name", "average_stars", "review_count", "fans", "yelping_since").show()
df_users.select(col("user_id"), col("name")).show()

# lit = add literal or constant
# withColumn = add new column to df or manipulate
# when
df_users.select(lit(1).alias("valid_row")).show()
df_users.withColumn("rank", when(col("useful") >= 500, lit("high")).otherwise(lit("low"))).show()

# monotonically_increasing_id = generated id
df_users.select(monotonically_increasing_id().alias("event"), "name").show(2)

# greatest = greatest value of the list
df_users.select(
    "name",
    "compliment_cool",
    "compliment_cute",
    "compliment_funny",
    "compliment_hot",
    greatest("compliment_cool", "compliment_cute", "compliment_funny", "compliment_hot").alias("highest_rate")
).show()

# expr = expression string into the column that it represents {sql-like expressions}
df_users.select(expr("CASE WHEN useful >= 500 THEN 'high' " + " ELSE 'low' END").alias("score")).show()

# round = given value to scale decimal places
df_users.select(col("average_stars"), round("average_stars", 0)).show()

# current_date & current timestamp = current date & timestamp
df_users.select(current_date(), current_timestamp()).show()

# year = retrieve year
df_users.select(year(current_timestamp())).alias("year").show()

# pyspark.sql.DataFrame.transform() {3.0} & pyspark.sql.functions.transform() = applying a transformation to each element
from pyspark.sql.functions import upper


def verify_rank(df):
    return df_users.withColumn("rank", when(col("useful") >= 500, lit("high")).otherwise(lit("low")))


df_users.transform(verify_rank).show()

# avg = returns the average of the values in a group
df_users.select(avg("average_stars")).show()
