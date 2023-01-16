""""
Pandas
https://pandas.pydata.org/

Pandas API on {Spark}
https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/index.html

* PySpark
* Koalas
* PySpark.Pandas

Databricks Notebook
https://adb-2090585310411504.4.azuredatabricks.net/?o=2090585310411504#notebook/1215094018680562
"""

# import & set configs
from pyspark.sql import SparkSession
builder = SparkSession.builder.appName("etl-yelp-pandas-json")
builder = builder.config("spark.sql.execution.arrow.pyspark.enabled", "true")
builder.getOrCreate()
print(builder)

# pandas
# import pandas as pd

# pandas api on spark
import pyspark.pandas as pd

# loc files {local}
loc_users = "/Users/luanmorenomaciel/GitHub/series-spark/docs/files/json/users.json"
loc_business = "/Users/luanmorenomaciel/GitHub/series-spark/docs/files/json/business.json"
loc_reviews = "/Users/luanmorenomaciel/GitHub/series-spark/docs/files/json/reviews.json"

# read files
pd_users = pd.read_json(loc_users, lines=True)
pd_business = pd.read_json(loc_business, lines=True)
pd_reviews = pd.read_json(loc_reviews, lines=True)

# get df info
pd_users.info()
pd_business.info()
pd_reviews.info()

# describe ds
print(pd_users.describe())

# top results
print(pd_users.head())

# display amount
# print(pd_users.sample(n=10))

# amount of rows
print(len(pd_users.index))

# columns and number of columns
print(pd_users.columns)
print(len(pd_users.columns))

# extract specific range
print(pd_users.loc[0:3])

# pick specific column
print(pd_users.loc[0:1,['name', 'average_stars']])

# unique values
print(pd_business['state'].unique())

# filter
# https://towardsdatascience.com/data-engineering-pandas-101-d8bf5d68750c
# print(pd_users[pd_users.average_stars > 4].sort_values(average_stars))

# https://pandas.pydata.org/docs/user_guide/10min.html
