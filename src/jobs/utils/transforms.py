from pyspark.sql.functions import *


def get_greatest_rank(df):

    df_transformed = df.select(
        greatest("compliment_cool", "compliment_cute", "compliment_funny", "compliment_hot").alias("highest_rate")
    )

    return df_transformed


def get_rate(df):

    df_transformed = df.withColumn(
        "rank",
        when(col("useful") >= 500, lit("high")).otherwise(lit("low"))
    )

    return df_transformed