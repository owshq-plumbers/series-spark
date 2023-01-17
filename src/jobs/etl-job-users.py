# import session
from pyspark.sql import SparkSession
from pyspark import SparkConf

from utils.input import read_parquet_files
from utils.transforms import get_greatest_rank, get_rate
from utils.output import write_into_parquet


# main definitions & calls
def main():
    spark = SparkSession.builder.appName("etl-job-users").getOrCreate()

    # configs
    print(spark)
    print(SparkConf().getAll())
    spark.sparkContext.setLogLevel("INFO")

    # extract {E}
    users_filepath = "/Users/luanmorenomaciel/GitHub/series-spark/docs/files/parquet/users"
    df_users = read_parquet_files(spark=spark, filename=users_filepath)
    df_users.show()

    # transform {T}
    df_rank = get_greatest_rank(df=df_users)
    df_rank.show()
    df_users_transformed = get_rate(df=df_users)

    # load {L}
    write_into_parquet(df=df_users_transformed, mode="overwrite", location="/Users/luanmorenomaciel/GitHub/series-spark/docs/files/output/users")


# entry point for pyspark etl app
if __name__ == '__main__':
    main()